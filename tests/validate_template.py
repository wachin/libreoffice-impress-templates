#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
import zipfile


REQUIRED_XML = [
    "content.xml",
    "styles.xml",
    "meta.xml",
    "settings.xml",
    "META-INF/manifest.xml",
]

REQUIRED_PACKAGE_ENTRIES = [
    "mimetype",
    "content.xml",
    "styles.xml",
    "meta.xml",
    "settings.xml",
    "META-INF/manifest.xml",
]

EXPECTED_MIMETYPE = "application/vnd.oasis.opendocument.presentation-template"


def fail(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def info(message: str) -> None:
    print(f"OK: {message}")


def validate_directory(template_dir: Path) -> int:
    if not template_dir.is_dir():
        return fail(f"No existe el directorio {template_dir}")

    for relative in REQUIRED_XML:
        path = template_dir / relative
        if not path.is_file():
            return fail(f"Falta {relative}")
        ET.parse(path)
        info(f"XML valido: {relative}")

    mimetype_path = template_dir / "mimetype"
    if not mimetype_path.is_file():
        return fail("Falta mimetype")

    mimetype = mimetype_path.read_text(encoding="utf-8").strip()
    if mimetype != EXPECTED_MIMETYPE:
        return fail(f"mimetype inesperado: {mimetype}")
    info("mimetype correcto")

    markdown_files = sorted(
        str(path.relative_to(template_dir)) for path in template_dir.rglob("*.md")
    )
    if markdown_files:
        return fail(f"Hay archivos .md dentro de la plantilla: {', '.join(markdown_files)}")
    info("No hay archivos .md dentro de la plantilla")
    return 0


def validate_package(otp_path: Path) -> int:
    if not otp_path.is_file():
        return fail(f"No existe el archivo {otp_path}")

    with zipfile.ZipFile(otp_path, "r") as archive:
        infos = archive.infolist()
        if not infos:
            return fail("El paquete esta vacio")
        if infos[0].filename != "mimetype":
            return fail("La primera entrada no es mimetype")

        names = {info.filename for info in infos}
        for entry in REQUIRED_PACKAGE_ENTRIES:
            if entry not in names:
                return fail(f"Falta {entry} dentro del .otp")
        info("Entradas ODF requeridas presentes en el .otp")

        mimetype_info = infos[0]
        if mimetype_info.compress_type != zipfile.ZIP_STORED:
            return fail("mimetype fue comprimido dentro del .otp")
        info("mimetype va primero y sin compresion en el .otp")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Valida una plantilla Impress descomprimida y, si existe, su archivo .otp"
    )
    parser.add_argument("template_dir", help="Ruta al directorio de la plantilla")
    args = parser.parse_args()

    template_dir = Path(args.template_dir).resolve()

    result = validate_directory(template_dir)
    if result != 0:
        return result

    otp_path = template_dir.parent / f"{template_dir.name}.otp"
    if otp_path.exists():
        result = validate_package(otp_path)
        if result != 0:
            return result
    else:
        print(f"WARN: No existe {otp_path}, se valido solo la carpeta fuente", file=sys.stderr)

    print(f"Plantilla validada: {template_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
