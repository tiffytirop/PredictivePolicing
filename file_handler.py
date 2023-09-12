import pandas as pd
import geopandas

class FileHandler:

    def read_csv_file(file_name):
        file=pd.read_csv(file_name)
        return file

    def set_map_geometry(file_name):
        file = geopandas.read_file(file_name)
        file.crs = {'init': 'epsg:4326'}
        file = file.set_geometry('geometry')
        return file








