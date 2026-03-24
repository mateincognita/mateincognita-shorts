

# ============================================
# Main - Limpieza de Datos con Pandas
# 

from limpieza import df_sucio, df_limpio
from reporte_pdf import generar_pdf

# Paso 1: Tabla sucia
print("--- Tabla Sucia ---")
print(df_sucio)

# Paso 2 y 3: Tabla limpia
print("\n--- Tabla Limpia ---")
print(df_limpio)

# Paso 4: Generar PDF
generar_pdf(df_sucio, df_limpio)
print("\nListo! Revisa el archivo limpieza_datos.pdf")


