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

class Book():
    def __init__(self, isnb):
        self.isbn = isnb
        self.chapters = list()
        self.sections = list()
        
    def add_chapter(self, chap):
        if isinstance(chap, Chapter):
            self.chapters.append(chap)
        else:
            raise TypeError('ChapterError')

    def get_chapters(self):
        for i in self.chapters:
            print(i)
            print("{}".format(i.get_sections()))

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


p_book = Book(123)

p_book.add_chapter(d_type_chap)
p_book.add_chapter(ds_chap)
p_book.get_chapters()


