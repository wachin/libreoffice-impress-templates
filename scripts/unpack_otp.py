#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path
import sys
import zipfile


def unpack_otp(otp_path: Path) -> Path:
    if not otp_path.is_file():
        raise FileNotFoundError(f"No existe el archivo {otp_path}")

    output_dir = otp_path.parent / otp_path.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(otp_path, "r") as archive:
        archive.extractall(output_dir)

    print(f'  * Template "{output_dir.name}" unpacked successfully')
    return output_dir


def find_otp_files(base_dir: Path) -> list[Path]:
    return sorted(path for path in base_dir.iterdir() if path.is_file() and path.suffix == ".otp")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Desempaqueta archivos .otp de LibreOffice Impress"
    )
    parser.add_argument(
        "templates",
        nargs="*",
        help="Archivos .otp a desempaquetar. Si se omiten, se desempaquetan todos los .otp del directorio actual.",
    )
    args = parser.parse_args()

    cwd = Path.cwd()
    targets = [cwd / rel for rel in args.templates] if args.templates else find_otp_files(cwd)

    if not targets:
        print("No se encontraron archivos .otp para desempaquetar.", file=sys.stderr)
        return 1

    for target in targets:
        unpack_otp(target.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
