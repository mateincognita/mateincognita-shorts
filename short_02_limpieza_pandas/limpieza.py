
# ============================================
# Limpieza de Datos con Pandas
# ============================================
# Este script muestra cómo limpiar un DataFrame
# con 3 pasos básicos:
#   1. Eliminar duplicados
#   2. Rellenar valores nulos (NaN)
#   3. Corregir tipos de datos
#
# ============================================


import pandas as pd

data = {
    "Nombre": ["Juan", "Juan", "María"],
    "Edad": [None, None, 25],
    "Precio": [150, 150, 200]
}

# Tabla sucia
df_sucio = pd.DataFrame(data)
print("--- Tabla Sucia ---")
print(df_sucio)

# Paso 1: Eliminar duplicados
df_limpio = df_sucio.drop_duplicates()

# Paso 2: Rellenar nulos con 0
df_limpio["Edad"] = df_limpio["Edad"].fillna(0)

# Paso 3: Corregir tipos de datos
df_limpio["Edad"] = df_limpio["Edad"].astype(int)
df_limpio["Precio"] = df_limpio["Precio"].astype(int)

print("\n--- Tabla Limpia ---")
print(df_limpio)