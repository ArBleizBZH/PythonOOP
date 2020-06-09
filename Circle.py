# Write a Circle class with an instance variable named radius and a method named area. 
# Create two more attributes named diameter and circumference and make them behave as read only attributes. 
# Perform data validation on radius, user should not be allowed to assign a negative value to it.
#       For a circle
#       diameter =  2 * radius  
#       circumference =  2 * 3.14 * radius 
#       area =  3.14 * radius * radius

class Circle:
    def __init__(self, radius):
        self.radius = radius
        #self.radius = abs(radius)
        # self._diameter = None
        # self._circumference = None
        
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius > 0:
            self._radius = new_radius
        else:
            raise ValueError("Radius should be positive")

    @property
    def diameter(self):
        return (2 * self._radius)
    
    @diameter.setter
    def diameter(self, val): 
        raise ValueError("Error: diameter can't be changed")

    @property
    def circumference(self):
        return (2 * 3.14 * self._radius)
    
    @circumference.setter
    def circumference(self, val): 
        raise ValueError("Error: circumference can't be changed")

    def area(self):
        return (3.14 * self.radius * self.radius)
        
def callcircle():
    mycircle = Circle(5)
    print(mycircle.area())
    print(mycircle.diameter)
    print(mycircle.circumference)
    #mycircle.diameter = 2
    #mycircle.circumference = 2

callcircle()






