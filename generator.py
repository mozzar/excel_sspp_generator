import xlrd
import person
import os
#dane konfiguracyjne do wypełnienia
#loc = "kwestionariusz.xlsx"
#original, column_name from input, index in excel
faculty_data = ['faculty']
#nazwa kierunkow na wydzialu typu
faculty_subject_data = 'subject'

loc = input("Podaj nazwę pliku .xlsx wraz z rozszerzeniem: ")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

rows = sheet.nrows #ilosc wierszy
columns = sheet.ncols #ilosc kolumn

#tu zbiera numery kolumn w ktorych sa kierunki wydzialow
columns_faculty_subject_indexes = []

#additional columns to get
additional_columns_size = 0
additional_columns = []
additional_columns_original_name = []
additional_columns_values = []


faculties = []
short_faculties = []


print("Podaj nazwę kolumny z wydziałami (duże litery, polskie znaki mają znaczenie): ")
faculty_data.append(input())
#print(len(faculty_data))


print("Podaj ilość kolumn dodatkowych do pobrania (Odlicz kolumnę wydziałów):");
additional_columns_size = int(input())

for i in range(additional_columns_size):
    additional_columns.append(input("Podaj kolumne dodatkowa nr [%d]:" % i))
    additional_columns_original_name.append(input("Podaj nazwę która będzie pobierana nr [%d]:" % i))


#pobranie wydziałów
for i in range(rows):
    if i == 0:
        for j in range(columns):
            if str(sheet.cell_value(i, j)) == faculty_data[1]:
                faculty_data.append(j)
    elif i != 0 and faculty_data[1] != 0:
        if sheet.cell_value(i, faculty_data[2]) not in faculties:
            faculties.append(sheet.cell_value(i, faculty_data[2]))





#pobranie kierunku
for j in range(columns):
    if "kierunek" in sheet.cell_value(0, j):
        columns_faculty_subject_indexes.append(j)


for i in range(rows):
    for j in range(columns):
        for k in range(additional_columns_size):
            if str(sheet.cell_value(i, j)) == additional_columns[k]:
                additional_columns_values.append(j)

def getShortFaculty(faculty):
    faculty_splitted = faculty.split()
    short_fac = ""
    for temp in faculty_splitted:
        if temp == "Chemicznej":
            short_fac = short_fac + temp[0] + temp[1]
        else:
            short_fac = short_fac + temp[0]
    return short_fac


for i in range(rows):
    if i > 0:
        fac = sheet.cell_value(i, int(faculty_data[2]))
        object = person.Person(getShortFaculty(fac), fac.replace("Wydział", ""))
        object.addValuesFormated(additional_columns_original_name)
        for l in columns_faculty_subject_indexes:
            if sheet.cell_value(i, l) != "":
                object.addValues(str(sheet.cell_value(i, l)).strip(), faculty_subject_data)
        for index, k in enumerate(additional_columns_values):

            object.addValues(sheet.cell_value(i, k), index)
        object.savetoFile()
        del object
    else:
        continue

print("Poszło okej! :D ")