import geopandas as gpd
from shapely.geometry import box
import pandas as pd  
###############################################################################################
# Función para unir capas
def unir_gdfs(lista_gdfs, nombres=None, crs_objetivo=None, reset_index=True):
    """
    Une una lista de GeoDataFrames en uno solo, opcionalmente etiquetando su origen.

    Parámetros:
    -----------
    lista_gdfs : list of gpd.GeoDataFrame
        Lista de GeoDataFrames ya cargados.
    nombres : list of str, opcional
        Lista de nombres identificadores (debe coincidir en longitud con lista_gdfs).
    crs_objetivo : int o str, opcional
        EPSG objetivo. Si se especifica, reproyecta todas las capas.
    reset_index : bool, por defecto True
        Reiniciar el índice del GeoDataFrame final.

    Retorna:
    --------
    gpd.GeoDataFrame
        GeoDataFrame unido con columna de origen si se proporcionan nombres.
    """
    if not lista_gdfs:
        raise ValueError("La lista de GeoDataFrames está vacía.")

    if nombres and len(nombres) != len(lista_gdfs):
        raise ValueError("La lista de nombres no coincide con la cantidad de GeoDataFrames.")

    lista_gdfs_modificados = []

    for i, gdf in enumerate(lista_gdfs):
        gdf_copia = gdf.copy()
        if crs_objetivo:
            gdf_copia = gdf_copia.to_crs(crs_objetivo)
        if nombres:
            gdf_copia["origen"] = nombres[i]
        lista_gdfs_modificados.append(gdf_copia)

    gdf_unido = gpd.GeoDataFrame(pd.concat(lista_gdfs_modificados, ignore_index=reset_index),
                                 crs=lista_gdfs_modificados[0].crs)
    return gdf_unido
    
################################################################################################
# función para generar grilla
def grilla_expansion_urbana(gdf, cell_size=1000):
    """
    Genera una grilla regular de celdas cuadradas sobre la extensión de un GeoDataFrame.

    Parámetros:
    ----------
    gdf : GeoDataFrame, Capa de referencia sobre la cual se generará la grilla.
    cell_size : Tamaño de la celda en unidades del CRS de la capa de entrada. Por defecto 1000 (1 km).

    Retorna:
    -------
    grid : Grilla de celdas cuadradas como GeoDataFrame, con el mismo CRS que la capa de entrada.
    """
    bounds = gdf.total_bounds
    xmin, ymin, xmax, ymax = bounds
    celdas = []
    x = xmin
    while x < xmax:
        y = ymin
        while y < ymax:
            c = box(x, y, x + cell_size, y + cell_size)
            celdas.append(c)
            y += cell_size
        x += cell_size
    grid = gpd.GeoDataFrame(geometry=celdas, crs=gdf.crs)
    return grid