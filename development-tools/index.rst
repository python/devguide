import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill

# Crear libro
wb = Workbook()

# === Estilos ===
bold = Font(bold=True)
center = Alignment(horizontal="center", vertical="center")
thin_border = Border(
    left=Side(style="thin"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin")
)
fill_header = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")

# --- Hoja 1: Libro Diario ---
ws1 = wb.active
ws1.title = "Libro Diario"

# Encabezados
headers = ["Fecha", "Cuenta", "Débito", "Crédito"]
ws1.append(headers)

# Aplicar formato a encabezados
for col in range(1, 5):
    cell = ws1.cell(row=1, column=col)
    cell.font = bold
    cell.alignment = center
    cell.fill = fill_header
    cell.border = thin_border

# Transacciones
transacciones = [
    ("01/10/2025", "Caja", 1500, ""),
    ("", "Capital Social", "", 1500),
    ("", "SUMAS IGUALES", 1500, 1500),

    ("02/10/2025", "Bancos", 800, ""),
    ("", "Caja", "", 800),
    ("", "SUMAS IGUALES", 800, 800),

    ("03/10/2025", "Inventario Mercancías", 1200, ""),
    ("", "Proveedores", "", 1200),
    ("", "SUMAS IGUALES", 1200, 1200),

    ("04/10/2025", "Proveedores", 500, ""),
    ("", "Bancos", "", 500),
    ("", "SUMAS IGUALES", 500, 500),

    ("05/10/2025", "Gastos de Administración", 300, ""),
    ("", "Caja", "", 300),
    ("", "SUMAS IGUALES", 300, 300),

    ("", "TOTALES GENERALES", 4300, 4300),
]

for fila in transacciones:
    ws1.append(fila)

# Formato general
for row in ws1.iter_rows(min_row=2, max_row=ws1.max_row, min_col=1, max_col=4):
    for cell in row:
        cell.border = thin_border
        if cell.column in (3, 4):  # Débito y Crédito
            cell.alignment = Alignment(horizontal="right")
        else:
            cell.alignment = Alignment(horizontal="left")

# Ajustar ancho de columnas
col_widths = [12, 30, 15, 15]
for i, width in enumerate(col_widths, 1):
    ws1.column_dimensions[openpyxl.utils.get_column_letter(i)].width = width


# --- Hoja 2: Balance de Prueba ---
ws2 = wb.create_sheet(title="Balance de Prueba")

headers2 = ["Cuenta", "Débito", "Crédito"]
ws2.append(headers2)

for col in range(1, 4):
    cell = ws2.cell(row=1, column=col)
    cell.font = bold
    cell.alignment = center
    cell.fill = fill_header
    cell.border = thin_border

balance = [
    ("Caja", 700, ""),
    ("Bancos", 300, ""),
    ("Inventario Mercancías", 1200, ""),
    ("Proveedores", "", 700),
    ("Gastos de Administración", 300, ""),
    ("Capital Social", "", 1500),
    ("TOTALES", 2500, 2500),
]

for fila in balance:
    ws2.append(fila)

# Formato general hoja 2
for row in ws2.iter_rows(min_row=2, max_row=ws2.max_row, min_col=1, max_col=3):
    for cell in row:
        cell.border = thin_border
        if cell.column in (2, 3):
            cell.alignment = Alignment(horizontal="right")
        else:
            cell.alignment = Alignment(
