import pandas as pd

# Leer el archivo CSV desanidado con la especificación del tipo de datos y low_memory=False
df = pd.read_csv('movies_dataset.csv', dtype={'popularity': str}, low_memory=False)

# Reemplazar los valores nulos por 0 en las columnas 'revenue' y 'budget'
df['revenue'].fillna(0, inplace=True)
df['budget'].fillna(0, inplace=True)

# Guardar el DataFrame actualizado en el mismo archivo
df.to_csv('movies_dataset.csv', index=False)