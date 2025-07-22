# Evaluación de Aptitud Territorial para Identificación de Zonas de Expansión Urbana en Municipios Intermedios  

## 1. Objetivo del proyecto

El objetivo de este proyecto es identificar, mediante análisis espacial en Python, las zonas más aptas para la expansión urbana del municipio de interés, considerando criterios ambientales, de accesibilidad y restricciones normativas. La metodología se basa en una evaluación multicriterio espacial que permite priorizar áreas favorables para un crecimiento urbano planificado y sostenible.

## 2. Metodología general

La metodología se implementa en tres notebooks principales:

- `1_data_preparation.ipynb`: carga, proyección, limpieza y generación de capas base.
- `2_suitability_analysis.ipynb`: aplicación de filtros espaciales y normalización de criterios para calcular un índice de idoneidad.
- `3_visualization.ipynb`: generación de mapas finales e interpretación visual de resultados.

Se utilizan librerias como `GeoPandas`, `Rasterio`, `Shapely`, `Matplotlib` y `Contextily`.

## 3. Criterios considerados en el análisis

-  Pendientes del terreno menores al 15%.
-  Cercanía a vías principales (< 1 km).
-  Cercanía a centros poblados (< 1 km).
-  Exclusión de zonas cercanas a cuerpos de agua (< 30 m).
-  Exclusión de zonas con bosque o áreas protegidas.
-  Coberturas del suelo compatibles (pastizales, áreas agrícolas).
-  Exclusión de zonas inestables por riesgo de movimientos en masa.

Cada criterio se normalizó (0 = no apto, 1 = apto) y se combinó en un índice final de idoneidad.

## 4. Estructura del repositorio

├── data/ # Datos originales (shapefiles, raster)
├── docs/
│ ├── references.md # Criterios Técnicos Delimitación de Áreas de Expansión Urbana
├── notebooks/
│ ├── 1_data_preparation.ipynb
│ ├── 2_suitability.ipynb
│ └── 3_visualization.ipynb
├── docs/
│ ├── references.md # Criterios Técnicos Delimitación de Áreas de Expansión Urbana
├── results/
│ ├── maps # Imágenes PNG de las salidas graficas
├── src/
│ ├── analysis_functions.py
│ ├── data_preprocessing.py
│ └── visualization_tools.py
└──README.txt


## 5. Resultados

Se genera un mapa final de idoneidad clasificado en tres niveles:

-  **Alto**: zonas óptimas para expansión urbana inmediata.
-  **Medio**: zonas con potencial condicionado.
-  **Bajo**: zonas no recomendadas por restricciones físicas o normativas.

##  6. Tecnologías y librerías utilizadas

- Python 3.11  
- Jupyter Notebooks  
- GeoPandas  
- Rasterio  
- Shapely  
- Matplotlib  
- Contextily  

##  7. Consideraciones finales

Este proyecto demuestra cómo las técnicas de análisis espacial y la programación en Python pueden apoyar procesos de planeación territorial con criterios técnicos y normativos. La metodología desarrollada es reproducible y adaptable a otros contextos geográficos similares.

##  Relación con los componentes mínimos del proyecto

### Adquisición y preparación de datos
- Carga de datos públicos en formato shapefile (centros poblados, red vial, cuerpos de agua, uso del suelo, coberturas, límites municipales, etc.).
- Proyección y limpieza de datos con geopandas.
- Transformación de DEM para derivar capas de pendiente.

### Análisis de atributos y filtrado
- Filtrado temático de capas para excluir áreas no aptas:
  - Pendientes > 15%
  - Zonas protegidas (bosques, cuerpos de agua)
  - Uso del suelo no compatible
  - Distancia a vías > 1 km
- Selección de subconjuntos clave para el análisis multicriterio.

### Operaciones espaciales
- Generación de buffers alrededor de vías, centros poblados y drenajes.
- Intersección y combinación de capas.
- Cálculo de índice de aptitud mediante álgebra de mapas.
- Derivación de estadísticas de densidad y accesibilidad.

### Visualización y documentación
- Mapas temáticos de entrada y resultados.
- Leyendas personalizadas, porcentajes por clase.
- Documentación clara en notebooks organizados y GitHub.