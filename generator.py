import xlrd

loc = "kwestionariusz.xlsx"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

#print(sheet.cell_value(0,0))
rows = sheet.nrows # 62
columns = sheet.ncols #29
names = []

faculty_column_index = 0;
faculty_column_name = None
surname_column_index = 0;
name_column_index = 0;

faculties = []


print("Podaj nazwę kolumny z wydziałami (duże litery, polskie znaki mają znaczenie): ")
faculty_column_name = input()

#pobranie wydziałów
for i in range(rows):
    if i == 0:
        for j in range(columns):
            if str(sheet.cell_value(i, j)) == faculty_column_name:
                faculty_column_index = j;
    if faculty_column_index != 0 and i != 0:
        if sheet.cell_value(i, faculty_column_index) not in faculties:
            faculties.append(sheet.cell_value(i,faculty_column_index))

'''
for i in range(rows):
    for a in range(columns):
        #first column is labels
        print(str(sheet.cell_value(i, a)) + '  '+str(a) );
        print("\n")
        if str(sheet.cell_value(i, a)) == "Imię":
            name_column_index = a
        elif str(sheet.cell_value(i, a)) == "Nazwisko":
            surname_column_index = a;


          #names.insert(i, )
print("-------------")
print(name_column_index)
'''

for i in range(len(faculties)):
    print(str(faculties[i]) + "\n")