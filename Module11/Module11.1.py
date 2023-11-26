class Publication:

    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Publication Name: {self.name}")


class Book(Publication):

    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"Book Author: {self.author}")
        print(f"Book Page count: {self.page_count}")


class Magazine(Publication):

    def __init__(self, name, chief_author):
        self.chief_author = chief_author
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"Magazine Chief Author: {self.chief_author}")


magazine1 = Magazine("Donald Duck", "Aki Hyyppä")
book1 = Book("Compartment No. 6", "author Rosa Liksom", 192)

magazine1.print_information()
print()
book1 .print_information()
