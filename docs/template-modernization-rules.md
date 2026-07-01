# Reglas para modernizar plantillas Impress desde código fuente

Estas reglas existen para evitar que una plantilla se vea bien solo en las diapositivas incluidas, pero falle cuando el usuario cree una diapositiva nueva desde LibreOffice Impress.

## Principio general

Una plantilla no está terminada solo porque las diapositivas base se ven bien.

También debe cumplir esto:

- al crear una nueva diapositiva desde un layout existente;
- al duplicar una diapositiva;
- al cambiar el layout de una diapositiva;
- al escribir títulos o texto reales en los placeholders;

la presentación debe seguir funcionando visualmente.

## Regla principal

Si la plantilla tiene dos o más layouts o páginas maestras, cualquier diapositiva nueva creada a partir de ellas debe colocar el texto en la zona correcta y con un tamaño razonable.

En otras palabras:

- no basta con mover cajas en la diapositiva visible;
- hay que alinear `master-page`, `presentation-page-layout`, `content.xml` y estilos de placeholder.

## Reglas obligatorias

### 1. El master y el layout deben coincidir

Si en `content.xml` una diapositiva usa `presentation:class="subtitle"`, el `master-page` correspondiente no debe estar definido como si fuera `title` o `outline`.

Cada layout debe ser consistente en:

- `styles.xml`:
  - `style:master-page`
  - `style:presentation-page-layout`
  - estilos `presentation`
- `content.xml`:
  - `draw:page`
  - `draw:frame`
  - `presentation:class`

## 2. Los placeholders deben ser reales, no decorativos

Los elementos donde el usuario escribirá texto deben seguir siendo placeholders válidos.

No conviene reemplazarlos por cajas visuales normales si el usuario necesita:

- insertar título;
- insertar subtítulo;
- insertar contenido;
- crear una nueva diapositiva usando el mismo layout.

## 3. El texto debe caber al crear una diapositiva nueva

Cuando el usuario crea una diapositiva nueva con un layout existente:

- el texto no debe salir cortado;
- no debe aparecer fuera del bloque visual;
- no debe quedar descentrado si el layout es centrado;
- no debe solaparse con rectángulos, bandas o adornos.

Para eso conviene revisar:

- `draw:fit-to-size="shrink-to-fit"` cuando aplique;
- `draw:auto-grow-height`;
- `draw:textarea-horizontal-align`;
- `draw:textarea-vertical-align`;
- `fo:font-size`;
- el tamaño real de la caja `svg:width` y `svg:height`.

## 4. Cada layout debe tener una intención clara

No crear layouts ambiguos.

Cada uno debe responder a un uso concreto, por ejemplo:

- portada;
- título + contenido;
- sección;
- comparación;
- cierre.

Si un layout es de sección, no debe comportarse como uno de contenido largo.

## 5. La miniatura debe coincidir con la plantilla real

`Thumbnails/thumbnail.png` no debe mostrar un diseño viejo o diferente.

Si la plantilla cambia visualmente:

- la miniatura debe regenerarse;
- la galería de LibreOffice no debe inducir a error.

## 6. No guardar documentación dentro de la plantilla

Archivos como:

- `README.md`
- `IMPLEMENTATION.md`
- notas temporales

no deben quedar dentro de la carpeta de una plantilla si se va a empaquetar como `.otp`.

La documentación del trabajo debe ir en `docs/`.

## 7. El paquete `.otp` debe seguir las reglas ODF

Al empaquetar:

- `mimetype` debe ser la primera entrada;
- `mimetype` debe ir sin compresión;
- no deben entrar archivos ajenos;
- `content.xml`, `styles.xml`, `meta.xml`, `settings.xml` y `META-INF/manifest.xml` deben existir.

## 8. El patrón visual debe ser visible

Una plantilla demasiado sutil puede parecer vacía aunque técnicamente funcione.

Cada plantilla modernizada debe tener al menos uno de estos elementos visibles:

- barra de acento;
- bloque de color;
- panel lateral;
- banda superior;
- layout de sección claro.

## 9. El pie de página no debe competir con el contenido

Fecha, footer y numeración deben:

- verse discretos;
- mantener contraste suficiente;
- no robar atención al título ni al cuerpo.

## 10. Antes de dar una plantilla por buena, probar estos casos

Pruebas mínimas:

1. abrir la plantilla como `.otp`;
2. crear una presentación nueva basada en ella;
3. escribir un título largo y uno corto;
4. escribir texto en el placeholder de contenido;
5. crear una nueva diapositiva usando cada layout disponible;
6. duplicar una diapositiva;
7. cambiar entre layouts;
8. revisar que el texto siga dentro de las zonas correctas.

## Flujo recomendado de trabajo

1. editar `styles.xml`;
2. editar `content.xml`;
3. validar XML;
4. empaquetar `.otp`;
5. abrir en LibreOffice;
6. probar creación de nuevas diapositivas;
7. corregir masters y placeholders;
8. regenerar `thumbnail.png`.

## Señales de que una plantilla aún no está lista

- la diapositiva original se ve bien, pero una nueva no;
- el layout 3 crea texto fuera del bloque visual;
- un placeholder aparece en una posición distinta al diseño;
- la miniatura muestra otra estética;
- el usuario necesita mover manualmente el texto cada vez.

## Definición de plantilla inteligente

Una plantilla Impress es inteligente cuando:

- su diseño base se ve bien;
- sus layouts tienen intención clara;
- los placeholders están bien definidos;
- una nueva diapositiva creada por el usuario funciona sin corrección manual.
