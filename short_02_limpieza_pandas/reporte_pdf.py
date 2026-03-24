

# ============================================
# Reporte PDF - Limpieza de Datos con Pandas
# ============================================
import os
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch

def df_a_tabla(df):
    data = [list(df.columns)]
    for row in df.itertuples(index=False):
        data.append(["NaN" if str(v) == "nan" else str(v).replace(".0", "") for v in row])
    return data

def generar_pdf(df_sucio, df_limpio):

    ruta = os.path.join(os.path.dirname(__file__), "limpieza_datos.pdf")  #buenas practicas
    doc = SimpleDocTemplate(ruta, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Título
    story.append(Paragraph("MateIncognita — Limpieza de Datos con Pandas", styles["Title"]))
    story.append(Spacer(1, 12))

    # Tabla Sucia
    story.append(Paragraph("Tabla Sucia:", styles["Heading2"]))
    story.append(Spacer(1, 6))
    tabla_sucia = Table(df_a_tabla(df_sucio), colWidths=[2*inch]*3)
    tabla_sucia.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
        ("GRID",       (0,0), (-1,-1), 0.5, colors.black),
        ("ALIGN",      (0,0), (-1,-1), "CENTER"),
        ("PADDING",    (0,0), (-1,-1), 6),
    ]))
    story.append(tabla_sucia)
    story.append(Spacer(1, 20))

    # Tabla Limpia
    story.append(Paragraph("Tabla Limpia:", styles["Heading2"]))
    story.append(Spacer(1, 6))
    tabla_limpia = Table(df_a_tabla(df_limpio), colWidths=[2*inch]*3)
    tabla_limpia.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR",  (0,0), (-1,0), colors.white),
        ("GRID",       (0,0), (-1,-1), 0.5, colors.black),
        ("ALIGN",      (0,0), (-1,-1), "CENTER"),
        ("PADDING",    (0,0), (-1,-1), 6),
    ]))
    story.append(tabla_limpia)

    doc.build(story)
    print("PDF generado en:", ruta)