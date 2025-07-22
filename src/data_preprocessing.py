import geopandas as gpd
import os

########################################################################################################################################
#Función recorte municipio de interés
def clip_vector(vector, aoi, ruta_salida=None):
    """
    Recorta una capa vectorial usando un polígono (aoi).

    Parámetros:
    - vector: GeoDataFrame a recortar
    - aoi: GeoDataFrame del área de interés
    - ruta_salida: ruta opcional para guardar el resultado

    Retorna:
    - GeoDataFrame recortado
    
    """
    # Asegura el mismo sistema de referencia
    if vector.crs != aoi.crs:
        aoi = aoi.to_crs(vector.crs)
        
    # Recorte
    recorte = gpd.clip(vector, aoi)
    
    # Filtrar solo polígonos
    solo_poligonos = recorte[recorte.geometry.type.isin(['Polygon', 'MultiPolygon'])]

    # Guardar si se solicita
    if ruta_salida:
        os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
        solo_poligonos.to_file(ruta_salida)
        print(f"Archivo guardado en: {ruta_salida}")

    return solo_poligonos

####################################################################################################################
#Función áreas de influencia - Buffer

def buffer_areas_influencia(capa_geografica, distancia_buffer, epsg_proyeccion=None):
    """
    Genera áreas de influencia (buffers) alrededor de una capa vectorial de puntos, líneas o polígonos.

    Parámetros:
    - capa_geografica: GeoDataFrame que contiene la capa de entrada sobre la cual se generarán los buffers.
    - distancia_buffer: Distancia del buffer en metros.
    - epsg_proyeccion: Código EPSG del sistema de coordenadas proyectadas en metros. Si se especifica,
                       la capa será reproyectada antes de calcular el buffer para asegurar que las distancias
                       sean precisas.

    Retorna:
    - GeoDataFrame con geometrías de tipo polígono representando áreas de influencia generadas alrededor de las geometrías originales.
    """
    # verificar sistema o convertir
    if epsg_proyeccion is not None:
        capa_proyectada = capa_geografica.to_crs(epsg=epsg_proyeccion)
    else:
        capa_proyectada = capa_geografica.copy()

    # se hace la copia para no editar el original
    copia_capa = capa_proyectada.copy()

    # iniciarmos la lista para el nuevo bff
    lista_buffers = []

    # Recorrer cada geometría individualmente
    for index, fila in copia_capa.iterrows():
        # Aplicar buffer a cada geometría
        geom = fila.geometry
        buffer_geom = geom.buffer(distancia_buffer)
        lista_buffers.append(buffer_geom)

    # Reemplazar las geometrías en la copia con los buffers generados
    copia_capa['geometry'] = lista_buffers

    return copia_capa



