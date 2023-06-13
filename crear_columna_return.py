import pandas as pd

# Leer el archivo CSV y especificar el tipo de datos de la columna 'release_year'
df = pd.read_csv('movies_dataset.csv', dtype={'release_year': str}, low_memory=False)

# Convertir las columnas 'revenue' y 'budget' a tipo numérico
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')

# Crear la columna 'return' calculando el retorno de inversión
df['return'] = df['revenue'].fillna(0) / df['budget'].fillna(0)

# Guardar los cambios en el archivo CSV
df.to_csv('movies_dataset.csv', index=False)
