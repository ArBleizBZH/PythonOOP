class Fraction:

    def __init__(self, nr, dr = 1):
        # myreducedvals = self.__reduce(nr, dr) 
        # self.nr = myreducedvals[0]
        # self.dr = myreducedvals[1]
        self.nr = abs(nr)
        self.dr = abs(dr)
        self._reduce()
        
    @staticmethod
    def hcf(x,y):
        x=abs(x)
        y=abs(y)
        smaller = y if x > y else x
        s = smaller
        while s > 0:
            if x%s == 0 and y%s == 0:
                break
            s-=1
        return s
        #Make it a static method in the Fraction class that you had written in earlier exercise.

    #In your Fraction class, write a private instance method _reduce that reduces a fraction to its lowest terms. 
    # To reduce a Fraction to its lowest terms you have to divide the numerator and denominator by the highest common factor.
    #  Call this method in __init__and also call it on the resultant fraction in methods multiply and add.
    # def __reduce(self, nr, dr):
    #     return (abs(int(nr / self.hcf(nr, dr))), abs(int(dr / self.hcf(nr, dr))))
    #### OR for reduce to return an object
    def _reduce(self):
        h = Fraction.hcf(self.nr, self.dr)
        print(f'_reduce() - value of hcf = {h}')
        if h == 0:
            return
        self.nr = int(self.nr / h)
        self.dr = int(self.dr / h)

    def show(self):
        print(f'{self.nr}/{self.dr}') #actual method output

    def add(self, frac):
        print(f'We are adding: {self.nr}/{self.dr} + {frac.nr}/{frac.dr}')
        if isinstance(frac, int):
            frac = Fraction(frac)    
        additionresult = Fraction( ( (self.nr * frac.dr) + (frac.nr * self.dr) ), (self.dr * frac.dr) )
        additionresult._reduce()    
        print(f'Fraction addition result: {additionresult.nr} / {additionresult.dr}')
        return additionresult

    def multiply(self, frac):
        print(f'We are multiplying: {self.nr}/{self.dr} * {frac.nr}/{frac.dr}')
        if isinstance(frac, int):
            frac = Fraction(frac)  
        multipliedresult = Fraction( (self.nr * frac.nr), (self.dr * frac.dr) )
        multipliedresult._reduce()
        print(f'03A- multipliedresult value AFTER reduce: {multipliedresult.nr}/{multipliedresult.dr}')
        return multipliedresult

################ TEST
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n TEST RUN: 12   ")
print(f'__TST__: Creating Fraction Object testfrac1..')
testfrac1 = Fraction(4, 16)
print(f'__TST__: Fraction Object testfrac1 created: {testfrac1.nr} / {testfrac1.dr}')
print(f'__TST__: calling testfrac1.show(): ')
testfrac1.show()

print(f'__TST__: Creating Fraction Object testfrac2....')
testfrac2 = Fraction(6, 9)
print(f'__TST__: Fraction Object testfrac1 created: {testfrac2.nr} / {testfrac2.dr}')
print(f'__TST__: calling testfrac2.show():')
testfrac2.show()

print("\n")  # 1/4 * 2/3 = 1/6
print(f'__TST__: calling testfrac1.multiply(testfrac2)  # 1/4 * 2/3 = 1/6')
testfrac1.multiply(testfrac2)
# 2/3 * 1/4 = 1/6
print(f'__TST__: calling testfrac2.multiply(testfrac1)  # 2/3 * 1/4 = 1/6')
testfrac2.multiply(testfrac1) 

print("\n")  # 1/4 + 2/3 = 1/6
print(f'__TST__: calling testfrac1.add(testfrac2)  # 1/4 + 2/3 = 11/12')
testfrac1.add(testfrac2)
# 2/3 + 1/4 = 1/6
print(f'__TST__: calling testfrac1.add(testfrac2)  # 2/3 + 1/4 = 11/12')
testfrac1.add(testfrac2)




