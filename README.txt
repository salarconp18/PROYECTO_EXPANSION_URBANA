EVALUACIÓN DE APTITUD TERRITORIAL PARA IDENTIFICACIÓN DE ZONAS DE EXPANSIÓN URBANA PARA MUNICIPIOS INTERMEDIOS

Descripción general del código:
Este código implementa un flujo de trabajo en Python para identificar zonas con potencial de expansión urbana a partir de criterios técnicos, espaciales y ambientales. Utiliza datos geoespaciales públicos y herramientas de análisis geográfico para filtrar, procesar y visualizar áreas aptas para crecimiento urbano planificado.

Relación con los 4 componentes mínimos del proyecto:

1. Adquisición y preparación de datos
- Carga de datos públicos en formato shapefile (centros poblados, red vial, cuerpos de agua, uso del suelo, coberturas, límites municipales, etc.).
- Proyección y limpieza de datos con geopandas.
- Transformación de DEM para derivar capas de pendiente.

2. Análisis de atributos y filtrado
- Filtrado temático de capas para excluir áreas no aptas:
  • Pendientes mayores al 15%
  • Áreas de bosque y protección ambiental
  • Zonas cercanas a cuerpos de agua (<30 m)
  • Zonas alejadas de vías (>1 km)
  • Áreas con uso del suelo incompatible
- Selección de subconjuntos clave para el análisis multicriterio.

3. Operaciones espaciales
- Generación de buffers (áreas de influencia) alrededor de vías, centros poblados y drenajes.
- Intersección y combinación de capas para construir la base de análisis.
- Cálculo de índice de aptitud urbana mediante álgebra de mapas (ponderación de criterios).
- Cálculo de densidad vial y proximidad como indicadores de accesibilidad.

4. Visualización y documentación
- Mapas temáticos de entrada (vías, hidrografía, centros poblados, restricciones).
- Mapas de resultado (zonas de alta, media y baja aptitud para expansión).
- Documentación del proceso en Jupyter Notebooks con uso de librerías: geopandas, rasterio, matplotlib.