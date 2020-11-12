import unidecode
class Person:

    values = []
    href = ""
    def __init__(self, faculty_short, faculty):
        self.faculty_short = faculty_short
        self.faculty = faculty
        self.values = []
        self.href = ""


    def addValues(self, value, original_number):
        if isinstance(original_number, str):
            self.values.append(str(original_number)+"=\"" + str(value).replace("\"", "'") + "\"")
        else:
            self.values.append(str(self.values_format[original_number])+"=\"" + str(value).replace("\"", "'").strip() + "\"")
            if str(self.values_format[original_number]) == "name":
                self.href = unidecode.unidecode(self.href + str(value).replace("\"", "'").lower().strip())
            elif str(self.values_format[original_number]) == "surname":
                self.href = unidecode.unidecode(self.href + str(value).replace("\"", "'").lower().strip())


    def addValuesFormated(self, value):
        self.values_format = value


    def formatBeforeSaveToFile(self):
        full_data = "[sc "

        full_data = full_data + " faculty=\"" + self.faculty + "\""
        full_data = full_data + " href=\"" + self.href + "\""
        for temp_data in self.values:
            full_data = full_data + " " + temp_data + "\n"

        full_data = full_data + "]\n"
        return full_data

    def savetoFile(self):
        file_open = open(self.faculty_short + ".txt", 'a')
        file_open.write(str(self.formatBeforeSaveToFile()))

    def __del__(self):
        self.faculty_short = None
        self.faculty = None
        self.values = []
        self.values_format = []
