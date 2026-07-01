# Simple Clear modernization

Este archivo fija los cambios exactos recomendados para convertir `simple-clear` en la familia `minimal-light`.

## Estado actual

- La plantilla es 4:3.
- Tiene 3 layouts base en `content.xml`.
- Usa `Source Sans Pro`, lo cual sigue siendo util.
- El fondo es casi blanco con un gradiente radial muy leve.
- La estructura es suficientemente simple como para modernizarla sin rehacerla completa.

## Cambio ya aplicado

- Se actualizo `Settings/ColorTable.xml` con una paleta mas coherente:
  - neutrales de papel;
  - tintas oscuras;
  - acentos azules y cian;
  - colores de estado.

## Cambios exactos pendientes en `styles.xml`

### 1. Fondo

Ubicacion:

- estilo `SimpleClear-background`
- gradiente `Luz_20_tenue_20_sobre_20_pared_20_blanca`

Cambios:

- mantener fondo claro;
- reducir aun mas el efecto decorativo del gradiente;
- usar fondo casi plano para que no parezca plantilla de 2015.

Valores sugeridos:

- `draw:start-color="#ffffff"`
- `draw:end-color="#f8fafc"`
- `draw:start-intensity="100%"`
- `draw:end-intensity="100%"`

### 2. Titulo principal

Ubicacion:

- estilo `SimpleClear-title`

Cambios:

- usar color `#0f172a`;
- aumentar peso visual;
- bajar un poco la altura total para dejar mas aire.

Objetivo:

- titulo mas editorial;
- mejor contraste;
- menos sensacion de bloque gigante vacio.

### 3. Cuerpo y outline

Ubicacion:

- estilo `SimpleClear-outline1`

Cambios:

- usar color de texto `#334155`;
- bullets de primer nivel en `#2563eb`;
- bullets de segundo nivel en `#94a3b8`;
- reducir niveles visibles a 3 utiles en vez de arrastrar 8-10 niveles irreales.

### 4. Footer, fecha y numeracion

Ubicacion:

- estilos `MP1`, `MP2`, `MP3`
- frames `Mpr1`, `Mpr4`, `Mpr7`

Cambios:

- bajar protagonismo visual;
- usar `#64748b`;
- reducir altura de esas bandas y subirlas ligeramente desde el borde inferior;
- convertirlas en pie discreto, no en tres zonas que compiten con el contenido.

### 5. Layout base

Ubicacion:

- master pages `SimpleClear`, `SimpleClear1`, `SimpleClear2`

Cambios:

- conservar los 3 layouts, pero reinterpretarlos como:
  - portada;
  - titulo + contenido;
  - seccion o cita.

## Cambios exactos pendientes en `content.xml`

### 1. Portada

Pagina:

- `page1`

Cambios:

- mover el titulo mas arriba;
- convertir `subtitle` en subtitulo corto o descriptor;
- reservar un bloque visual de acento delgado a la izquierda o arriba.

Propuesta:

- titulo: `x=2.2cm`, `y=2.0cm`, `w=22.5cm`, `h=5.6cm`
- subtitulo: `x=2.2cm`, `y=8.6cm`, `w=18.0cm`, `h=2.2cm`

### 2. Titulo + contenido

Pagina:

- `page2`

Cambios:

- dejarla como layout principal;
- titulo mas corto en alto;
- outline con mas ancho util;
- preparar espacio para listas o 2 columnas.

Propuesta:

- titulo: `x=1.8cm`, `y=1.4cm`, `w=24.5cm`, `h=2.6cm`
- cuerpo: `x=1.8cm`, `y=4.8cm`, `w=24.5cm`, `h=12.0cm`

### 3. Seccion / cita

Pagina:

- `page3`

Cambios:

- usar el layout casi vacio como separador de seccion;
- centrar mensaje corto con acento visual;
- si se mantiene `subtitle`, renombrarlo mentalmente como bloque de mensaje.

Propuesta:

- bloque principal: `x=2.5cm`, `y=5.4cm`, `w=21.5cm`, `h=6.0cm`

## Paso siguiente recomendado

Antes de editar `styles.xml` y `content.xml`, conviene hacer una de estas dos cosas:

1. abrir la plantilla en LibreOffice y confirmar que `Source Sans Pro` esta disponible;
2. decidir si la conversion a 16:9 se hace ya en `simple-clear` o en una variante nueva.

## Conversion a 16:9

No la apliqué todavía. Hay que tocar las definiciones de `page-layout` en `styles.xml`, no solo mover cajas.

Objetivo recomendado:

- ancho `33.867cm`
- alto `19.05cm`

Si se decide avanzar con eso, el orden correcto es:

1. cambiar `page-layout`;
2. ajustar `master-page`;
3. ajustar `content.xml`;
4. regenerar `thumbnail.png`.
