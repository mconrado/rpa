from openpyxl import Workbook

print("Iniciando o robô...")
print("Lendo dados do arquivo de texto ...")
file_txt = open("gastos.txt", "r", encoding="utf-8")

arquivo = file_txt.read()

lista_dados = arquivo.splitlines()

for i in range(0, len(lista_dados)):
    lista_dados[i] = lista_dados[i].split(",")

wb = Workbook()
ws = wb.active

for row in lista_dados:
    ws.append(row)

wb.save("gastos.xlsx")
