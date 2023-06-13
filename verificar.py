import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('movies_dataset.csv')

# Obtener las columnas del DataFrame
columns = df.columns

# Imprimir las columnas del DataFrame
print(columns)