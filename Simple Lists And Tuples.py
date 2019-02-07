class Chapter():
    def __init__(self, title):
        self.title = title
        self.sections = list()
        self.pages = None

    def add_sections(self, sect):
        self.sections.append(sect)

    def get_sections(self):
        for s in self.sections:
            print(s)
        return "\t\tDone"

    def __str__(self):
        return "{}".format(self.title)

d_type_chap = Chapter('Data Types')
d_type_chap.add_sections('int')
d_type_chap.add_sections('str')
d_type_chap.add_sections('float')
d_type_chap.add_sections('complex')
d_type_chap.add_sections('boolean')

ds_chap = Chapter("Data Structures")
ds_chap.add_sections('list')
ds_chap.add_sections('tuple')

print(d_type_chap.get_sections())
