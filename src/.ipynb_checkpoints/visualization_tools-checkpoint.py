import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# Función de visualización de mapa categórico de uso actual del suelo
    
def plot_uso_suelo(gdf, municipio, columna='CS_TIPO', titulo='Uso actual del suelo'):
    """
    Genera un mapa temático del uso actual del suelo con categorías predefinidas.

    Parámetros:
    ----------
    gdf :Capa geográfica con información sobre el uso del suelo. 
    municipio : Capa del municipio de interés, utilizada como base para la visualización.
    columna : 'CS_TIPO' Nombre de la columna que contiene los tipos de uso del suelo.
    titulo : Título del mapa que se mostrará sobre la visualización.

    Detalles:
    --------
    La función asigna colores específicos a tres clases de uso del suelo y genera un gráfico que         incluye:
        - el municipio como base,
        - la capa temática coloreada por categoría,
        - una leyenda personalizada ubicada en la esquina superior izquierda.

    Ejemplo de uso:
    --------------
    plot_uso_suelo(uso_suelo, municipio)
    """
    colores_uso = {
        'Urbano': '#f2b0b8',
        'Expansión urbana': '#b0d3f2',
        'Rural': '#d3f8dc',
        }
    
    fig, ax = plt.subplots(figsize=(8, 8)) 
    
    municipio.plot(ax=ax, facecolor='none', edgecolor='black')
    gdf.plot(ax=ax, color=gdf[columna].map(colores_uso), edgecolor='gray', linewidth=0.3)

    legend = [mpatches.Patch(color=color, label=label) for label, color in colores_uso.items()]
    ax.legend(handles=legend, loc='upper left', title='Uso del Suelo', fontsize=8)
    ax.set_title(titulo)
    ax.axis('off')
    plt.show()


# Función de visualización de mapa categórico de coberturas de la tierra
def plot_coberturas(gdf, municipio, columna='nivel_1', titulo='Coberturas de la tierra'):
    """
    Genera un mapa temático de coberturas del suelo con categorías y colores predefinidos.

    Parámetros:
    ----------
    gdf : Capa geográfica que contiene la clasificación de coberturas del suelo. 
    municipio : Capa geográfica del municipio de interés, utilizada como base para la visualización.
    columna : Nombre de la columna que contiene las clases de cobertura'nivel_1'.
    titulo : Título del mapa mostrado en la visualización.

    Detalles:
    --------
    La función utiliza una codificación de colores fija para representar cinco clases de cobertura y genera una figura con:
        - el municipio como base,
        - la capa temática coloreada por categoría,
        - una leyenda personalizada ubicada en la esquina superior izquierda.

    La visualización se muestra directamente mediante `plt.show()`.

    Ejemplo de uso:
    --------------
    plot_coberturas(coberturas_clip, municipio)
    """
    colores_cobertura = {
        '1. Territorios artificializados': '#E4080A',
        '2. Territorios agrícolas': '#FFECA1',
        '3. Bosques y áreas seminaturales': '#7DDA58',
        '4. Áreas húmedas': '#E7DDFF',
        '5. Superficies de agua': '#98F5F9'
    }
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    municipio.plot(ax=ax, facecolor='none', edgecolor='black')
    gdf.plot(ax=ax, color=gdf[columna].map(colores_cobertura), edgecolor='gray', linewidth=0.3)

    legend = [mpatches.Patch(color=color, label=label) for label, color in colores_cobertura.items()]
    ax.legend(handles=legend, loc='upper left', title='Cobertura', fontsize=8)
    ax.set_title(titulo)
    ax.axis('off')
    plt.show()


# Función de visualización de mapa categórico de Amenazas
    
def plot_amenazas(gdf, municipio, columna='Amenaza', titulo='Mapa de Amenaza'):
    """
    Genera un mapa temático de amenaza a partir de un GeoDataFrame clasificado por niveles.

    Parámetros:
    ----------
    gdf : Capa que contiene los datos de amenaza con una columna categórica que indica el nivel de             amenaza.
    municipio : Capa del municipio de interés, utilizada como base para la visualización.
    columna :'Amenaza' Nombre de la columna que contiene la clasificación de niveles de amenaza.
    titulo : Título del mapa para mostrar en la visualización.

    Detalles:
    --------
    La función asigna colores específicos a cinco categorías de amenaza (de 'Muy Baja' a 'Muy Alta') usando un diccionario predefinido, y genera una figura con:
        - el municipio como base,
        - la capa temática coloreada según el nivel de amenaza,
        - una leyenda personalizada ubicada en la esquina superior izquierda.

    Ejemplo de uso:
    --------------
    plot_amenazas(Amenazas, municipio)
    """
    colores_amenaza = {
        '1. Muy Baja': '#006837',
        '2. Baja': '#31a354',
        '3. Media': '#FFDE59',
        '4. Alta': '#FE9900',
        '5. Muy Alta': '#D20103'
    }
    
    fig, ax = plt.subplots(figsize=(8, 8))
        
    municipio.plot(ax=ax, facecolor='none', edgecolor='black')
    gdf.plot(ax=ax, color=gdf[columna].map(colores_amenaza), edgecolor='gray', linewidth=0.3)

    legend = [mpatches.Patch(color=color, label=label) for label, color in colores_amenaza.items()]
    ax.legend(handles=legend, loc='upper left', title='Amenaza', fontsize=8)
    ax.set_title(titulo)
    ax.axis('off')
    plt.show()