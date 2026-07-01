#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path
import sys
import zipfile


def iter_entries(template_dir: Path) -> list[Path]:
    entries: list[Path] = []
    for path in sorted(template_dir.rglob("*")):
        if path.is_dir():
            continue
        if path.name == "mimetype":
            continue
        if path.suffix.lower() == ".md":
            continue
        entries.append(path)
    return entries


def build_otp(template_dir: Path) -> Path:
    if not template_dir.is_dir():
        raise FileNotFoundError(f"No existe el directorio {template_dir}")

    mimetype_path = template_dir / "mimetype"
    if not mimetype_path.is_file():
        raise FileNotFoundError(f"Falta mimetype en {template_dir}")

    output_path = template_dir.parent / f"{template_dir.name}.otp"
    if output_path.exists():
        output_path.unlink()

    with zipfile.ZipFile(output_path, "w") as archive:
        archive.writestr(
            "mimetype",
            mimetype_path.read_bytes(),
            compress_type=zipfile.ZIP_STORED,
        )
        for path in iter_entries(template_dir):
            archive.write(
                path,
                arcname=path.relative_to(template_dir),
                compress_type=zipfile.ZIP_DEFLATED,
            )

    print(f'  * Template "{output_path.name}" built successfully')
    return output_path


def find_template_dirs(base_dir: Path) -> list[Path]:
    return sorted(path for path in base_dir.iterdir() if path.is_dir())


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Reempaqueta directorios de plantillas Impress como archivos .otp"
    )
    parser.add_argument(
        "templates",
        nargs="*",
        help="Directorios de plantilla a empaquetar. Si se omiten, se empaquetan todos los subdirectorios.",
    )
    args = parser.parse_args()

    cwd = Path.cwd()
    targets = [cwd / rel for rel in args.templates] if args.templates else find_template_dirs(cwd)

    if not targets:
        print("No se encontraron directorios para empaquetar.", file=sys.stderr)
        return 1

    for target in targets:
        build_otp(target.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
