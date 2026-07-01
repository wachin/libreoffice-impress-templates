# Hoja de ruta de modernizacion: fase 1

Esta fase cubre las tres primeras plantillas seleccionadas para crear una base moderna y coherente:

- `lo5-design-candidates/simple-clear`
- `lo5-design-candidates/simple-dark`
- `lo5-design-candidates/peter-river`

El objetivo no es solo retocar colores. La meta es convertirlas en tres familias reutilizables para 2026.

## Objetivos de la fase

- Pasar todo a una reticula 16:9 consistente.
- Mejorar legibilidad para pantalla y proyector.
- Crear variantes de diapositivas realmente utiles.
- Reducir ruido visual y estilos envejecidos.
- Mantener licencias limpias y metadatos consistentes.

## Entregables por plantilla

Cada plantilla modernizada deberia incluir al menos estas diapositivas maestras o variantes:

- portada;
- agenda o indice;
- separador de seccion;
- contenido a una columna;
- contenido a dos columnas;
- cita o mensaje clave;
- grafico o KPI;
- tabla o comparativa;
- cierre o contacto.

## Cambios comunes a las tres

### Formato y reticula

- Estandarizar a 16:9.
- Definir una zona segura comun para titulos, cuerpo y pie.
- Evitar objetos pegados a los bordes.
- Reservar espacio real para tablas, capturas y graficos.

### Tipografia

- Reemplazar jerarquias debiles por tres niveles claros: titulo, subtitulo, cuerpo.
- Usar tamanos suficientemente grandes para presentaciones en sala.
- Evitar abuso de mayusculas, sombras, contornos o efectos heredados.

### Color

- Definir 1 color principal, 1 secundario y 1 color de acento.
- Asegurar contraste alto entre fondo y texto.
- Limitar el uso de colores saturados a acentos y datos importantes.

### Componentes

- Crear estilos de listas, tablas y cajas destacadas.
- Preparar placeholders para imagen, grafico y numeracion.
- Crear un pie discreto con numero de diapositiva y titulo corto opcional.

### Metadatos y preview

- Revisar `meta.xml` para descripcion, autor, licencia y tags.
- Regenerar `Thumbnails/thumbnail.png` cuando el diseño final quede listo.
- Revisar `Settings/ColorTable.xml` cuando exista para alinear paleta.

## Plantilla 1: `simple-clear`

### Objetivo visual

Convertirla en la plantilla base `minimal-light`.

### Direccion de diseño

- Fondo claro limpio.
- Titulo fuerte y alineacion precisa.
- Acentos discretos, no decorativos.
- Mucho espacio en blanco.

### Cambios concretos

- Rehacer portada con una banda o bloque de acento muy contenido.
- Dar mas presencia al titulo principal con mejor escala.
- Añadir layouts de contenido con alineaciones mas firmes.
- Crear una diapositiva de comparacion y otra para metricas.
- Reducir cualquier borde o detalle que no aporte jerarquia.

### Uso ideal

- presentaciones corporativas;
- propuestas;
- capacitacion;
- documentacion visual.

## Plantilla 2: `simple-dark`

### Objetivo visual

Convertirla en la plantilla base `minimal-dark`.

### Direccion de diseño

- Fondo oscuro neutro, no completamente negro.
- Tipografia clara con acentos frios o cian/azul.
- Sensacion tecnica y sobria.

### Cambios concretos

- Ajustar el color de fondo para proyeccion real, evitando negro puro si degrada la lectura.
- Subir contraste de texto secundario y bullets.
- Diseñar una portada con acento lineal o bloque lateral.
- Crear estilos de graficos y tablas pensados para fondo oscuro.
- Introducir una diapositiva de codigo o datos tecnicos si el proyecto la quiere cubrir.

### Riesgos

- Bajo contraste en proyectores mediocres.
- Exceso de brillo en colores de acento.

### Uso ideal

- charlas tecnicas;
- temas de software;
- dashboards;
- workshops.

## Plantilla 3: `peter-river`

### Objetivo visual

Convertirla en la plantilla base `business-blue`.

### Direccion de diseño

- Azul profesional, no infantil ni demasiado saturado.
- Composicion plana y estructurada.
- Sensacion de producto, estrategia y negocio.

### Cambios concretos

- Limpiar cualquier elemento plano heredado que se vea demasiado generico.
- Refinar la paleta azul con un acento secundario sobrio.
- Crear portada, roadmap, comparativa y pagina final.
- Definir estilos para iconos, datos y bloques de resumen.
- Mejorar reticula para que soporte capturas, mockups y graficos.

### Uso ideal

- presentaciones de producto;
- pitch interno;
- estados de proyecto;
- ventas B2B.

## Orden de ejecucion recomendado

1. `simple-clear`
2. `simple-dark`
3. `peter-river`

Este orden permite cerrar primero la familia mas universal y luego derivar reglas a las otras dos.

## Archivos a tocar en cada plantilla

- `styles.xml`: estilos, pagina maestra, tipografia, fondos.
- `content.xml`: placeholders, cajas, variantes y contenido de ejemplo.
- `Settings/ColorTable.xml`: paleta reutilizable.
- `meta.xml`: descripcion y metadatos.
- `Thumbnails/thumbnail.png`: preview actualizado.

## Criterio de exito

La fase 1 estara bien resuelta si al final existen tres plantillas que:

- se ven contemporaneas sin depender de modas pasajeras;
- funcionan bien tanto en oficina como en proyeccion;
- cubren al menos el 80 por ciento de los casos de uso comunes;
- pueden servir de base para ampliar una coleccion curada.

## Siguiente fase sugerida

Despues de estas tres, continuar con:

1. `bright-blue`
2. `progress`
3. `focus`

Con eso ya se podria publicar una primera coleccion corta tipo `curated-2026`.
