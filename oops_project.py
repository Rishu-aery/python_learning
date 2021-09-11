class Library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.lendict={}
    def displaybooks(self):
        print('We have following books in our',self.name,'\n')
        for books in self.booklist:
            print(books)
    def lendbook(self,username,book):
        if book not in self.lendict:
            self.lendict.update({book: username})
            print('you can take the book')

        else:
            print('Book is already taken by',self.lendict[book])
    def addbook(self,book):
        self.booklist.append(book)
        print("Book added successfully")
    def returnbook(self,book):
        self.lendict.pop(book)
        print("Book returned successfully")

if __name__ == '__main__':
    student=Library(['Things b/w you and me','Saamvedna','Black suits you'
                     ,'How about a sin tonight'],"Rishabh Library")
    while(True):
        print(f"Welcome to {student.name}")
        print('Press 1 for display books')
        print('Press 2 for lend books')
        print('Press 3 for add books')
        print('Press 4 for return books')
        user_choice=int(input('Enter your choice:\n'))
        if user_choice==1:
            student.displaybooks()
        elif user_choice==2:
            name=input('Enter your name:')
            book=input('Enter the book name you want to lend:')
            student.lendbook(name,book)
        elif user_choice == 3:
            book = input('Enter the book name you want to add:')
            student.addbook(book)
        elif user_choice == 4:
            book = input('Enter the book name you want to return:')
            student.returnbook(book)
        else:
            print('Invalid choice....')
        a = ''
        while(a!='c'and a!='q'):
            a=input("\nPress Q to quit and C to continue:\n")
            if a=='q':
                exit()
            if a=='c':
                continue


