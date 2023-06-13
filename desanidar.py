import pandas as pd

# Leer el archivo CSV
df = pd.read_csv(r'C:\Users\ADMIN\OneDrive\Documentos\DataScience\Henry\Proyecto Individual\Dataset\movies_dataset.csv', low_memory=False)

# Crear una lista de columnas anidadas
columnas_anidadas = ['belongs_to_collection', 'genres', 'production_companies', 'production_countries', 'spoken_languages']

# Desanidar las columnas anidadas
for columna in columnas_anidadas:
    if columna in df.columns:
        df_desanidado = pd.json_normalize(df[columna])
        df = pd.concat([df.drop(columna, axis=1), df_desanidado], axis=1)

# Guardar el resultado en un nuevo archivo CSV
df.to_csv('movies_dataset.csv', index=False)