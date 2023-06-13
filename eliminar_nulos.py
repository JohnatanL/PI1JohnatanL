import pandas as pd

# Leer el archivo CSV y especificar el tipo de datos de 'release_date'
df = pd.read_csv('movies_dataset.csv', dtype={'release_date': str}, low_memory=False)

# Eliminar filas con valores nulos en el campo 'release_date'
df = df.dropna(subset=['release_date'])

# Guardar el DataFrame actualizado en el mismo archivo CSV
df.to_csv('movies_dataset.csv', index=False)

print("Los valores nulos en el campo 'release_date' han sido eliminados.")