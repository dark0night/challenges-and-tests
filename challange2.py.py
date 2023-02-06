from math import * 

#problem 1
class Line:

    def __init__(self,coor1,coor2):
        self.coor1= coor1
        self.coor2= coor2
        # print(coordinate1)

    #distance member function
    def distance(self):
        diff1 = self.coor2[0]-self.coor1[0]#x2-x1
        diff2=self.coor2[1]-self.coor1[1]#y2-y1
        d = diff1**2 + diff2**2 #sqr both the values
        r = sqrt(d) 
        print(r)
    
    #slope member function
    def slope(self):
        denomenator = self.coor2[0]-self.coor1[0] #x2-x1
        numerator = self.coor2[1]-self.coor1[1]#y2-y1
        #y=mx+C
        result = numerator/denomenator
        print(result)
        pass

# coordinate are (x1,y1)
# coordinate are (x2,y2)
coordinate1 = (3,2) #point 1
coordinate2 = (8,10) #point 2

#object creation
line = Line(coordinate1,coordinate2)
#calling distance on object line
line.distance()
#calling slope on object line
line.slope()

#problem 2
class Cylinder:
    
    def __init__(self,height,radius):
        self.height = height #creation of attributes
        self.radius = radius

        
    def volume(self):
        volume = 3.14 * self.radius * self.radius * self.height #var for equation
        print(volume) 

    
    def surface_area(self):
        area = 2 * 3.14 * self.radius * self.height + 2 * 3.14 * self.radius*self.radius #var for equation
        print(area) 

#object creation
c = Cylinder(2,3)
#calling volume method on object cylinder
c.volume()
#calling surface area method on object cylinder
c.surface_area()
