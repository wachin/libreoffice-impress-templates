# Empaquetar y probar plantillas Impress

Este repositorio guarda las plantillas como directorios descomprimidos. Para probar una plantilla en LibreOffice hay que volver a empaquetarla como `.otp`.

## Requisitos

- `python3`
- `libreoffice`

En Debian o Ubuntu:

```bash
sudo apt install python3 libreoffice
```

## Importante

No metas archivos de documentacion como `*.md` dentro de la carpeta de una plantilla si luego vas a empaquetarla.

Ejemplo:

- correcto: `docs/simple-clear-modernization.md`
- incorrecto: `lo5-design-candidates/simple-clear/IMPLEMENTATION.md`

El script de empaquetado excluye `*.md`, pero igual conviene mantener la documentacion fuera de las plantillas.

## Empaquetar una plantilla

Desde la raiz del repo:

```bash
cd /home/wachin/Dev2/libreoffice-impress-templates-Dev/libreoffice-impress-templates/lo5-design-candidates
python3 ../scripts/repack_otp.py simple-clear
```

Eso genera:

```text
lo5-design-candidates/simple-clear.otp
```

## Importarla y probarla en LibreOffice Impress

La forma mas fiable de probar una plantilla `.otp` es importarla dentro del gestor de plantillas de LibreOffice Impress y luego crear una presentacion nueva a partir de ella.

Pasos:

1. Abre LibreOffice Impress.
2. Ve a `Archivo > Nuevo > Presentacion`.
3. En la ventana de seleccion, abre `Gestionar`.
4. Crea una categoria nueva si hace falta.
5. Usa `Gestionar > Importar`.
6. Elige la categoria de destino.
7. Importa el archivo `.otp`.
8. Crea una presentacion nueva usando esa plantilla importada.

Ejemplo de archivo:

```text
/home/wachin/Dev2/libreoffice-impress-templates-Dev/libreoffice-impress-templates/lo5-design-candidates/simple-clear.otp
```

Tambien puedes abrir el `.otp` directamente para una revision rapida, pero para comprobar bien el comportamiento de la plantilla conviene usar el flujo de importacion.

## Verificacion rapida del paquete

Antes de abrir la plantilla, puedes revisar que el paquete tenga una estructura ODF razonable:

```bash
unzip -lv /home/wachin/Dev2/libreoffice-impress-templates-Dev/libreoffice-impress-templates/lo5-design-candidates/simple-clear.otp | sed -n '1,40p'
```

Lo importante es:

- `mimetype` debe aparecer como la primera entrada.
- `mimetype` debe estar `Stored`, no comprimido.
- Deben existir `content.xml`, `styles.xml`, `meta.xml`, `settings.xml`, `META-INF/manifest.xml`.

## Validacion automatica minima

Hay un script en `tests/validate_template.py` para comprobar la carpeta fuente y, si ya existe, tambien el `.otp` generado.

Ejemplo:

```bash
python3 tests/validate_template.py lo5-design-candidates/simple-clear
```

Ese script revisa:

- que los XML obligatorios existan;
- que los XML sean parseables;
- que `mimetype` tenga el valor correcto;
- que no haya `*.md` dentro de la carpeta de la plantilla;
- que el `.otp`, si existe, tenga `mimetype` primero y sin compresion.

## Revisar si un XML sigue valido

Si editaste a mano un XML y quieres comprobar que no quedó roto:

```bash
python3 - <<'PY'
import xml.etree.ElementTree as ET
for rel in [
    'lo5-design-candidates/simple-clear/styles.xml',
    'lo5-design-candidates/simple-clear/content.xml',
    'lo5-design-candidates/simple-clear/Settings/ColorTable.xml',
]:
    ET.parse(rel)
    print('OK', rel)
PY
```

## Flujo recomendado de trabajo

1. Editar `styles.xml`, `content.xml`, `meta.xml` o `Settings/ColorTable.xml`.
2. Verificar XML.
3. Reempaquetar con `scripts/repack_otp.py`.
4. Abrir el `.otp` en LibreOffice.
5. Revisar visualmente la portada, contenido, pies y placeholders.
6. Si queda bien, regenerar luego `Thumbnails/thumbnail.png`.

## Desempaquetar una plantilla

Si quieres partir de un `.otp` ya generado:

```bash
cd /home/wachin/Dev2/libreoffice-impress-templates-Dev/libreoffice-impress-templates/lo5-design-candidates
python3 ../scripts/unpack_otp.py simple-clear.otp
```

## Problemas comunes

### LibreOffice dice que el `.otp` está corrupto

Las causas más comunes son:

- `mimetype` no está primero en el ZIP;
- `mimetype` fue comprimido;
- un XML quedó mal formado;
- se metieron archivos ajenos a la plantilla dentro del paquete.

### La plantilla abre pero se ve rara

Suele deberse a:

- tipografías no instaladas;
- placeholders movidos fuera de zona útil;
- cambios excesivos en `styles.xml` sin revisar en LibreOffice.
