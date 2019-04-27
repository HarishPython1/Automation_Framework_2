import xlrd

file_loc="C:\\Users\\QSP\\Desktop\\Automation.xlsx"
wb=xlrd.open_workbook(file_loc)
ws=wb.sheet_by_index(0)
cell_val=ws.cell_value(0,1)
print(cell_val)

print(ws.ncols)#totla col values
print(ws.nrows)#total row values


