# Checklist de revisión para plantillas Impress

Usa esta lista cada vez que se modernice una plantilla desde su código fuente.

## 1. Estructura del template

- `content.xml` abre y valida sin errores XML.
- `styles.xml` abre y valida sin errores XML.
- `meta.xml`, `settings.xml` y `META-INF/manifest.xml` existen.
- `mimetype` existe.
- no hay archivos `.md` ni notas de trabajo dentro de la carpeta de la plantilla.

## 2. Empaquetado `.otp`

- `mimetype` fue empaquetado como primera entrada.
- `mimetype` fue empaquetado sin compresión.
- el archivo `.otp` se genera sin errores.
- LibreOffice abre la plantilla sin pedir reparación.

## 3. Diseño visual base

- la portada se ve intencional y no vacía.
- el layout principal tiene jerarquía visual clara.
- los colores tienen contraste suficiente.
- el pie de página no compite con el contenido.
- la plantilla se ve bien en la proporción esperada, por ejemplo `16:9`.

## 4. Layouts y masters

- cada layout tiene una intención clara.
- el `master-page` coincide con el `presentation-page-layout`.
- los placeholders del master coinciden con los usados en `content.xml`.
- un layout de sección no se comporta como uno de contenido largo.

## 5. Pruebas funcionales en LibreOffice

- crear una presentación nueva desde la plantilla funciona.
- escribir un título corto funciona.
- escribir un título largo sigue cabiendo.
- escribir contenido en la caja principal funciona.
- crear una diapositiva nueva usando cada layout funciona.
- duplicar una diapositiva conserva bien el diseño.
- cambiar el layout de una diapositiva no rompe la composición.

## 6. Prueba específica de plantilla inteligente

- si la plantilla tiene dos o más layouts, una diapositiva nueva creada desde cualquiera de ellos coloca el texto en la zona correcta.
- el texto no sale cortado.
- el texto no queda fuera del bloque visual.
- el texto no se superpone con adornos o bandas de color.
- el usuario no necesita mover manualmente la caja de texto.

## 7. Miniatura y entrega

- `Thumbnails/thumbnail.png` coincide con el diseño actual.
- la documentación del cambio quedó en `docs/`.
- la plantilla final quedó lista para importarse desde LibreOffice Impress.
