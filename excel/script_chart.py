from openpyxl import Workbook
from openpyxl.chart import AreaChart, Reference, series

wb = Workbook()
ws = wb.active

rows = [
    ["Ano", "Lucro", "Custos"],
    [2015, 40, 30],
    [2016, 40, 25],
    [2017, 45, 25],
    [2018, 50, 30],
    [2019, 30, 10],
    [2020, 25, 5],
]

for row in rows:
    ws.append(row)

chart = AreaChart()
chart.title = "Lucros x Custos"
chart.style = 13
chart.x_axis.title = "Ano"
chart.y_axis.title = "Porcentagem"

categorias = Reference(ws, min_col=1, min_row=1, max_row=6)
dados = Reference(ws, min_col=2, min_row=1, max_col=3, max_row=6)

chart.add_data(dados, titles_from_data=False)
chart.set_categories(categorias)

ws.add_chart(chart, "A10")
wb.save(filename="chart.xlsx")
