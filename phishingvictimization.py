import pandas as pd
import numpy as np
import geopandas as gpd

# Path to the relevant geofiles
municipality_shapefile = "data/geo/gemeenten_2021_v3.shp"
provinces_shapefile = "data/geo/provincie.gpkg"

# Path to the relevant files
municipality_names_path = "data/gemeenten2021.csv"
company_establishment_path = "data/Companyestablishment-CBS-2023.csv"
phising_victimization_path = "data/Crimerates-CBS-2023.csv"
digital_skills_path = "data/Digitalskills-CBS-2023.csv"
education_path = "data/Educationlevel-CBS-2023.csv"
GDP_path = "data/GDP-CBS-2023.csv"
education_path = "data/Educationlevel-CBS-2023.csv"
urbanization_path = "data/Urbanization-CBS-2023.csv"
