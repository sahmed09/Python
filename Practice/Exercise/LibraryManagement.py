class Library:
    def __init__(self, lists, name):
        self.bookList = lists  # List of books
        self.name = name  # Name of Library
        self.lendDict = {}  # lists of books which has been taken by a user (key->book, value->user)

    def display_books(self):
        print(f"We have following book in our library : {self.name}")
        for book in self.bookList:
            print(book)

    def lend_book(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("Lender Book Database has been updated. You can take the book now.")
        else:
            print(f"Book is already been taken by {self.lendDict[book]}")

    def add_book(self, book):
        self.bookList.append(book)
        print("Book has been successfully added to the book list.")

    def return_book(self, book):
        self.lendDict.pop(book)
        print("Book returned successfully.")


if __name__ == '__main__':
    shihab = Library(['python', 'c for everyone', 'java', 'machine learning', 'c++ beginners'], "ProPlanet")
    choice = {'1': 'Display Books', '2': 'Lend Book', '3': 'Add a Book', '4': 'Return Book'}
    while True:
        print(f"Welcome to the {shihab.name} Library. Enter your choice to continue.")

        for key, value in choice.items():
            print(key, "for", value)

        user_choice = input("Enter your choice: ")

        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option according the list")
            continue

        else:
            user_choice = int(user_choice)
            if user_choice == 1:
                shihab.display_books()

            elif user_choice == 2:
                book = input("Enter the name of the book you want to lend: ").lower()
                user = input("Enter your name: ")
                shihab.lend_book(user, book)

            elif user_choice == 3:
                book = input("Enter the name of the book you want to add: ").lower()
                shihab.add_book(book)

            elif user_choice == 4:
                book = input("Enter the name of the book you want to return: ").lower()
                shihab.return_book(book)

            else:
                print("Not a valid option")

            print("Press q to Quit or c to Continue!!")
            choice_again = ""

            while choice_again != "c" and choice_again != "q":
                choice_again = input().lower()
                if choice_again == "q":
                    exit()

                elif choice_again == "c":
                    continue
