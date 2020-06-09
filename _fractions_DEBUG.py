class Fraction:
    # cnt = 0
    # print("\n\n")
    # print(f'{cnt}.  CLASS INIT: Beginning with counter at: {cnt}')

    def __init__(self, nr, dr = 1):        
        # Fraction.cnt += 1
        # print(f'{Fraction.cnt}.  FRACTION INSTANCE INIT: Creating new Fraction Object')
        ## Applying reduce directly to nr and dr
        # Fraction.cnt += 1
        # print(f'{Fraction.cnt}.  FRACTION INSTANCE INIT: calling __reduce() with nr={nr} and dr={dr}')
        myreducedvals = self.__reduce(nr, dr) 
        self.nr = myreducedvals[0]
        self.dr = myreducedvals[1]
        # Fraction.cnt += 1
        # print(f'{Fraction.cnt}.  FRACTION INSTANCE INIT: : {self.nr} / {self.dr} ')
        # print(f'{Fraction.cnt}.  FRACTION INSTANCE INIT: : {type(myreducedvals)} ')
        #print(f'{Fraction.cnt}.  FRACTION INSTANCE INIT: type of myreducedvals: {type(myreducedvals)} is none because __reduce() sets instance object rather than returning values')
        

    #    Fraction.cnt += 1
    #     print(f'{Fraction.cnt}.  FRACTION INSTANCE INIT: Call instance created, with My frac reduced is: {self.nr} / {self.dr}')
    #     #self.nr = abs(nr)
    #     #self.dr = abs(dr)
    #     Fraction.cnt += 1
    #     print(f'{Fraction.cnt}.  FRACTION INSTANCE INIT: the type of self at end of init: {type(self) }')
    #     Fraction.cnt += 1
    #     print(f'{Fraction.cnt}.  FRACTION INSTANCE INIT: the value at fraction instantiation is : {self.nr} / {self.dr}')

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
        Fraction.cnt += 1
        # print(f'{Fraction.cnt}.     __reduce() method: is now Receiving: {nr} / {dr}')

        # Fraction.cnt += 1
        # print(f'{Fraction.cnt}.     __reduce() method: ****frac to reduce is nr: {nr}, and dr: {dr}')
        high_denom = self.hcf(nr, dr)
        # Fraction.cnt += 1
        # print(f'{Fraction.cnt}.     __reduce() method: high_denom: {high_denom}')
        
        #setting nr and dr here ????????? ## OR ##
        # Fraction.cnt += 1
        #print(f'{Fraction.cnt}.     __reduce() method: Setting the Fraction.nr and Fraction.dr values')
        #self.nr = abs(int(nr / high_denom))
        #self.dr = abs(int(dr / high_denom))
        reduced_nr = abs(int(nr / high_denom))
        reduced_dr = abs(int(dr / high_denom))
        # print(f'{Fraction.cnt}.     __reduce() method: returns a tuple (reduced_nr, reduced_dr)' )
        return (reduced_nr, reduced_dr)

        ### OR Returning as nr and dr ??????
        #return 
        #print(reduced_Frac.show())
        #return reduced_Frac

    def show(self):
        # Fraction.cnt += 1
        # print(f'{Fraction.cnt}.            Show() method is starting - display: {type(self) }')
        #print("%s/%s" % (self.nr, self.dr))
        # print(f'{Fraction.cnt}.            Show() method result prints:{self.nr}/{self.dr}')
        print(f'{self.nr}/{self.dr}') #actual method output

    def add(self, frac):
        print(f'We are adding: {self.nr}/{self.dr} + {frac.nr}/{frac.dr}')
        # Fraction.cnt += 1
        # print(f'{Fraction.cnt}.            add() method: is starting with types: {type(self)} * {type(frac)}')
        # print(f'{Fraction.cnt}.            add() method: frac is: {frac.nr} / {frac.dr}')
        # print(f'{Fraction.cnt}.            add() method: self is: {self.nr} / {self.dr}')
        if isinstance(frac, int):
            frac = Fraction(frac)             
        #     return Fraction(((self.nr * frac.dr) + (frac.nr * self.dr)), (self.dr * frac.dr))
        nr = ((self.nr * frac.dr) + (frac.nr * self.dr))
        dr = (self.dr * frac.dr)
        # print(f'{Fraction.cnt}.            multiply() method: after addition we have: {nr} / {dr}')
        reducedadditionrresult = self.__reduce(nr, dr)
        #this obnly requires printing out the result
        print(f'Fraction addition result: {reducedadditionrresult[0]} / {reducedadditionrresult[1]}')

    def multiply(self, frac):
        print(f'We are multiplying: {self.nr}/{self.dr} * {frac.nr}/{frac.dr}')
        # Fraction.cnt += 1
        # print(f'{Fraction.cnt}.            multiply() method: is starting with types: {type(self)} * {type(frac)}')
        # print(f'{Fraction.cnt}.            multiply() method: frac is: {frac.nr} / {frac.dr}')
        # print(f'{Fraction.cnt}.            multiply() method: self is: {self.nr} / {self.dr}')

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
        # print(f'{Fraction.cnt}.            multiply() method: after multiplication wr have: {nr} / {dr}')
        #WE SHOULD JUST reduce the values and print back
        multipliedresult = self.__reduce(nr, dr)
        # print(f'{Fraction.cnt}.            multiply() method: reduced multiplaction result: {multipliedresult[0]} / {multipliedresult[1]}')
        # print(f'{Fraction.cnt}.            multiply() method: TYPE multiplaction result: {type(multipliedresult)}')
        #this obnly requires printing out the result
        print(f'Fraction multiplication result: {multipliedresult[0]} / {multipliedresult[1]}')
        # return multipliedresult

""" 
        ##### OR OPTION B!!!!! RETURN AS A FRACTION OBJECT
        result = Fraction(nr, dr)
        print(f'{Fraction.cnt}.              multiply() method: **** result obj created! print result object instance: {result}')
        result = Fraction(nr, dr)
        print(f'{Fraction.cnt}.              multiply() method: result.show() var: {result.show()}')
        print(f'{Fraction.cnt}.              multiply() method: multiplicaton result: {nr}/{dr}')
        print(f'{Fraction.cnt}.              multiply() method: Reduced multiplicaton result.show(): {result.show()}')
        ###### What should multiply return???????
        print(f'{Fraction.cnt}.              multiply() method: returning the fraction object * result *.show() : {result.show()}' )
        print(f'{result.show()}')
        ### return Fraction( (self.nr * frac.nr), (self.dr * frac.dr) )
 """
################TEST
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n TEST RUN: 6")
print(f'__TST__: Creating Fraction Object testfrac1..')
testfrac1 = Fraction(4, 16)
print(f'__TST__: Fraction Object testfrac1 created and returned')
print(f'__TST__: calling Fraction.show() on testfrac1 ')
testfrac1.show()

print("\n")
print(f'__TST__: Creating Fraction Object testfrac2....')
testfrac2 = Fraction(6, 9)
print(f'__TST__: Fraction Object testfrac2 created and returned')
print(f'__TST__: calling Fraction.show() on testfrac2')
testfrac2.show()

print("\n")  # 1/4 * 2/3 = 1/6
print(f'__TST__: calling testfrac1.multiply(testfrac2)  # 1/4 * 2/3 = 1/6')
testfrac1.multiply(testfrac2)

print("\n")  # 2/3 * 1/4 = 1/6
print(f'__TST__: calling testfrac2.multiply(testfrac1)  # 2/3 * 1/4 = 1/6')
testfrac2.multiply(testfrac1) 

print("\n")  # 1/4 + 2/3 = 1/6
print(f'__TST__: calling testfrac1.add(testfrac2)  # 1/4 + 2/3 = 11/12')
testfrac1.add(testfrac2)

print("\n")  # 2/3 + 1/4 = 1/6
print(f'__TST__: calling testfrac1.add(testfrac2)  # 2/3 + 1/4 = 11/12')
testfrac1.add(testfrac2)




