class Library:
    def __init__(self, booklist, name):
        self.booklist = booklist
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our Library: {self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict[book] = user
            print("Lender-Book Database has been updated. You can take the book now")
        else:
            print(f"Book is already in use by {self.lendDict[book]}")

    def addBook(self, book):
        self.booklist.append(book)
        print("Book has been added to your list")

    def returnBook(self, book):
        self.lendDict.pop(book)
        print("Book has been returned")

if __name__ == '__main__':
    dnyanesh = Library(['python', 'c++', 'java', 'machinelearning'], "AI")
    while True:
        print(f"Welcome to the {dnyanesh.name} library. Enter your choice to continue")
        print("1. Display books")
        print("2. Lend books")
        print("3. Add books")
        print("4. Return books")
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
            continue
        else:
            user_choice = int(user_choice)
        if user_choice == 1:
            dnyanesh.displayBooks()
        elif user_choice == 2:
            book = input("Enter the name of book you want to lend: ")
            user = input("Enter Your Name: ")
            dnyanesh.lendBook(user, book)
        elif user_choice == 3:
            book = input("Enter the name of book do you want to add: ")
            dnyanesh.addBook(book)
        elif user_choice == 4:
            book = input('Enter the name of book that you want to return: ')
            dnyanesh.returnBook(book)
        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice = input()
        if user_choice == "q":
            exit()
        if user_choice == "c":
            continue
