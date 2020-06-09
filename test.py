
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("I am.", self.name)
    
    def greet(self):
        if self.age < 80:
            print("Hello! How are you doing?")
        else:
            print("Hello, how do you do?")
        self.display()
def callPerson():
    print(id(Person))

    p1 = Person("John", 20)
    p2 = Person("Tim", 40)
    print("p1:")
    print(id(p1))
    print(type(p1))
    print(p1)
    print("p2:")
    print(id(p2))
    print(type(p2))
    print(p2)

    p1.display()
    p1.greet()

    p2.display()
    p2.greet()
#callPerson()

class Bank:
    #sets name and a balance of 0
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance 

    def display(self):
        #display name and balance instance vars
        print(self.name, ' - ', self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount
def callBank():
    acc1 = Bank("John")
    acc1.deposit(100)
    acc1.withdraw(50)
    acc1.display()

    acc2 = Bank("Tim")
    acc2.deposit(10)
    acc2.withdraw(50)
    acc2.display()
#callBank()

class Product:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def display(self):
        print(self._x, self._y)

    @property
    def value(self):
        return self._x

    @value.setter
    def value(self, val):
        self._x = val

    @value.deleter
    def value(self):
        print('value deleted')
def callprods():
    p = Product(12, 24)
    p.display()
    del p.value
    p.display()
#callprods()

class Book:
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self._price = price
        self.copies = copies

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, val):
        print("value: ", val)
        if val > 1000:
            print("The price can't be higher than 1000")
        elif val < 50:
            print("The price can't be less than 50")
        else:
            self._price = val

    def display(self):
        #print(self.isbn, ' ', self.title, ' ', self._price, ' ', self.copies)
        print(self.title)
        print(f'ISBN: {self.isbn}')
        print(f'Price: {self.price}')
        print(f'Copies: {self.copies}')
        print('.' * 50)

    def in_stock(self):
        # if self.copies > 0:
        #     return True
        # else:
        #     return False
        return True if self.copies > 0 else False

    def sell(self):
        if self.in_stock():
            self.copies -= 1
        else:
            print("Sorry the book is out of stock")
def callbooks():
    book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
    book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
    book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,21)
    book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,10)
    
    #book3.sell()
    #book4.sell()

    #booksbyjack = [book.title for book in mybooks if book.author == 'Jack']
    #print(booksbyjack)

    mybooks = [book1, book2, book3, book4]
    for book in mybooks:
        book.display()

    book1.price = 2000
    book2.price = 10
    book3.price = 999
    print("\n")
    mybooks = [book1, book2, book3, book4]
    for book in mybooks:
        book.display()
#callbooks()

class Fraction:
    def __init__(self, nr, dr = 1):
        self.nr = abs(nr)
        self.dr = abs(dr)
        self.__reduce(self.nr, self.dr)
        print(f'My frac reduced is: {self.nr} / {self.dr}')

    @staticmethod
    def hcf(x,y):
        x=abs(x)
        y=abs(y)
        smaller = y if x>y else x
        s = smaller
        while s>0:
            if x%s==0 and y%s==0:
                break
            s-=1
        return s
        #Make it a static method in the Fraction class that you had written in earlier exercise.

    #In your Fraction class, write a private instance method _reduce that reduces a fraction to its lowest terms. 
    # To reduce a Fraction to its lowest terms you have to divide the numerator and denominator by the highest common factor.
    #  Call this method in __init__and also call it on the resultant fraction in methods multiply and add.
    def __reduce(self, nr, dr):
        print(f'nr: {nr} and dr: {dr}')
        high_denom = self.hcf(nr, dr)
        print(f'high_denom: {high_denom}')
        self.nr = int(nr / high_denom)
        self.dr = int(dr / high_denom)
        #print(reduced_Frac.show())
        #return reduced_Frac

    def show(self):
        #print("%s/%s" % (self.nr, self.dr))
        print(f'{self.nr}/{self.dr}')

    def multiply(self, frac):
        print(f'frac is: {frac.nr} / {frac.dr}')
        print(f'self is: {self.nr} / {self.dr}')
        # if type(self) == int:
        #     return Fraction((abs(self) * frac.nr), frac.dr)
        # elif type(frac) == int:
        #     return Fraction((self.nr * abs(frac)), self.dr)
        # else:
        #     return Fraction((self.nr * frac.nr), (self.dr * frac.dr))
        if isinstance(frac, int):
            frac = Fraction(frac)
        nr = self.nr * frac.nr
        dr = self.dr * frac.dr
        result = Fraction(nr, dr)
        print(f'result var: {result.show()}')
        print(f'multiplicaton result: {nr}/{dr}')
        print(f'Reduced multiplicaton result: {result.show()}')
        return Fraction( (self.nr * frac.nr), (self.dr * frac.dr) )

    def add(self, frac):
        # if type(self) == int:
        #     return Fraction(((abs(self) * frac.dr) + frac.nr), frac.dr)
        # elif type(frac) == int:
        #     return Fraction((self.nr + (abs(frac) * self.dr)), self.dr)
        # else:
        #     return Fraction(((self.nr * frac.dr) + (frac.nr * self.dr)), (self.dr * frac.dr))
        if isinstance(frac, int):
            frac = Fraction(frac)
        return Fraction.reduce(((self.nr * frac.dr) + (frac.nr * self.dr)), (self.dr * frac.dr))    

def callFraction():
    #myfrac1 = Fraction(-2,-6)
    myfrac1 = 2
    myfrac2 = Fraction(3,2)
    myfrac2.show()
    #myfrac2 = 2
    #print(frac.nr)
    #print(frac.dr)
    #myfracmult = multiply(myfrac1, myfrac2)
    #myfracmult.show()
    myfracmult1 = Fraction.multiply(myfrac1, myfrac2)
    myfracmult1.show()
#callFraction()
def testfraction():
    f1 = Fraction(2,3)
    f1.show()
    f2 = Fraction(3,4)
    f2.show()
    f3 = f1.multiply(f2)
    f3.show()
    f3 = f1.add(f2)
    f3.show()
    f3 = f1.add(5) 
    f3.show()
    f3 = f1.multiply(5) 
    f3.show()
    """ 
    The output that you should get is given below.
    2/3
    3/4
    6/12
    17/12
    17/3
    10/3
    """
#testfraction()
print(f'Fraction.hcf(210, 235): {Fraction.hcf(210, 235)}')
newfrac = Fraction(4, 16)
newfrac.show()
myfrac = Fraction(312, 984)
myfrac.show()
res = newfrac.multiply(myfrac)
print(f'type of result: {type(res)}')
print(f'newfrac x myfrac: { res.show() }')
print(f'myfrac x newfrac: {myfrac.multiply(newfrac)}')
#print(f'newfrac + myfrac: {newfrac.add(myfrac)}')
#print(f'myfrac + newfrac: {myfrac.add(newfrac)}')



class MyClass:
    a = 5
    def __init__(self, x):
        self.x = x
    
    #Instance method is the best choice when method needs to access instance variables
    def method1(self):
        print(self.x)

    #class method is the best choice when method needs to access class variables
    @classmethod
    def method2(cls):
        print(cls.a)

    #static method is the best choice when the method needs to access neither class nor instance variables
    # it's like a regular method but in the class namespace.
    @staticmethod
    def method3(m, n):
        return m + n






