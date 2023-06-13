import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('movies_desanidado.csv')

# Verificar las columnas actuales
print(df.columns)
