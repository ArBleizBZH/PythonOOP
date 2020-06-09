class Product():
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self.discount = discount
        
    #create a read only property named selling_price that is calculated by deducting discount from the marked_price. 
    # The instance variable discount represents discount in percent.   
    @property
    def selling_price(self):
        return (self.marked_price - (self.marked_price * (self.discount / 100)))
    
    def display(self):
        print(self.id,  self.marked_price,  self.discount)

    #Suppose after some time, you want to give an additional 2% discount on a product, if its price is above 500. 
    # To incorporate this change, implement discount as a property in your Product class.      
    @property
    def extra_discount(self, xtraDisc = 2):
        if self.selling_price > 500:
            return (self.selling_price - (self.selling_price * (xtraDisc /100)))
        else:
            return self.selling_price


def callProduct():    
    p1 = Product('X879', 400, 6)
    p2 = Product('A234', 100, 5)
    p3 = Product('B987', 990, 4)
    p4 = Product('H456', 800, 6)
    p5 = Product('H456', 2000, 50)
    print(p5.selling_price)
    print(p5.extra_discount)

callProduct()




