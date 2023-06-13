import pandas as pd

# Leer el archivo CSV y especificar el tipo de datos de 'release_date' como objeto
df = pd.read_csv('movies_dataset.csv', dtype={'release_date': object})

# Convertir la columna 'release_date' al formato deseado 'AAAA-MM-DD'
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce').dt.strftime('%Y-%m-%d')

# Crear la columna 'release_year' con el año de las fechas en 'release_date'
df['release_year'] = pd.to_datetime(df['release_date']).dt.year

# Mostrar las primeras filas del DataFrame con las columnas 'release_date' y 'release_year'
print(df[['release_date', 'release_year']].head())

# Guardar el DataFrame modificado en el archivo 'movies_dataset.csv'
df.to_csv('movies_dataset.csv', index=False)