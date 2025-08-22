from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# Crear el documento en horizontal
output_path = "Ecosistemas_Uruguay_Ordenado_Casillas_Chicas.pdf"
doc = SimpleDocTemplate(output_path, pagesize=landscape(A4))

# Estilos
styles = getSampleStyleSheet()
title_style = styles["Title"]
subtitle_style = styles["Heading2"]

# Datos de la tabla
data = [
    ["Ecosistema", "Características", "Flora", "Fauna"],
    ["Pradera", "Paisaje predominante de Uruguay, suelos fértiles y clima templado.",
     "Pastos, gramíneas, tréboles, cardos.",
     "Ñandúes, mulitas, zorros, venados de campo, aves rapaces."],
    ["Monte Ribereño", "Ubicado a orillas de ríos y arroyos, con suelos húmedos y fértiles.",
     "Sauce criollo, ceibo, sarandí.",
     "Carpincho, lobito de río, aves acuáticas, peces."],
    ["Monte Serrano", "Zonas de sierras y suelos pedregosos, clima variable.",
     "Coronilla, arrayán, molle serrano.",
     "Lagartos, zorros, aves serranas."],
    ["Monte de Quebrada", "Ambientes húmedos y sombríos entre sierras y quebradas.",
     "Laurel, helechos, azahar del monte.",
     "Murciélagos, aves insectívoras, anfibios."],
    ["Palmares", "Regiones donde predomina la palma Butiá.",
     "Butiá, pastos bajos.",
     "Aves frugívoras, zorros, insectos polinizadores."],
    ["Monte de Parque", "Bosques dispersos en praderas con árboles aislados.",
     "Talas, espinillos, algarrobos.",
     "Pájaros carpinteros, zorros, liebres."],
    ["Monte Psamófito", "Ecosistema costero sobre dunas y suelos arenosos.",
     "Espartillo, clavel del aire, gramíneas.",
     "Culebras, aves playeras, insectos."],
    ["Arenales", "Áreas de dunas móviles o fijas en zonas costeras.",
     "Pastos marítimos, gramíneas adaptadas.",
     "Cangrejos, aves costeras, reptiles."],
    ["Humedales o Bañados", "Zonas con acumulación de agua y gran biodiversidad.",
     "Juncos, totoras, camalotes.",
     "Garzas, anfibios, carpinchos, peces."]
]

# Contenido
elements = []
elements.append(Paragraph("Ecosistemas de Uruguay", title_style))
elements.append(Spacer(1, 12))
elements.append(Paragraph("Características, Flora y Fauna", subtitle_style))
elements.append(Spacer(1, 24))

# Tabla con casillas más chicas y texto reducido
table = Table(data, colWidths=[100, 200, 140, 140])
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#4F81BD")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 11),   # Encabezados
    ("FONTSIZE", (0, 1), (-1, -1), 8),   # Texto del cuerpo
    ("TOPPADDING", (0, 1), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 1), (-1, -1), 4),
    ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F9FAFC")),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
]))

elements.append(table)

# Construir PDF
doc.build(elements)
print(f"PDF generado en: {output_path}")
