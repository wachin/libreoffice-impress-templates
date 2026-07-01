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

### 2. Titulo principal

Ubicacion:

- estilo `SimpleClear-title`

Cambios:

- usar color `#0f172a`;
- aumentar peso visual;
- bajar un poco la altura total para dejar mas aire.

### 3. Cuerpo y outline

Ubicacion:

- estilo `SimpleClear-outline1`

Cambios:

- usar color de texto `#334155`;
- bullets de primer nivel en un azul fuerte;
- bullets secundarios mas suaves;
- reducir la sensacion de lista vieja y apretada.

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

### 2. Titulo + contenido

Pagina:

- `page2`

Cambios:

- dejarla como layout principal;
- titulo mas corto en alto;
- outline con mas ancho util;
- preparar espacio para listas o 2 columnas.

### 3. Seccion / cita

Pagina:

- `page3`

Cambios:

- usar el layout casi vacio como separador de seccion;
- centrar mensaje corto con acento visual;
- si se mantiene `subtitle`, renombrarlo mentalmente como bloque de mensaje.

## Paso siguiente recomendado

Antes de editar mas la plantilla, conviene abrirla y comprobar:

1. si `Source Sans Pro` esta disponible;
2. si la jerarquia nueva funciona bien en pantalla;
3. si la conversion a 16:9 conviene hacerla ya o en una variante nueva.

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
