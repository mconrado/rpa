from openpyxl import load_workbook

dest_arquivo = "book2.xlsx"
wb = load_workbook(filename=dest_arquivo)
ws = wb["Data"]


ws.move_range("A2:Z2", rows=-1)

ws.move_range("F8:F8", cols=2)
ws.move_range("f10:f10", cols=-2)
ws.move_range("C13:E15", cols=-2)

wb.save(filename=dest_arquivo)
