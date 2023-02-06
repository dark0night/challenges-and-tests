
class Line:

    def __init__(self,coor1,coor2):
        self.coordinate1= coor1
        self.coordinate2= coor2
    
    def distance(self,coor1,coor2):
        d = (coor1[0]-coor1[1])^2 + (coor2[0]-coor2[1])^2
        print(√d) 
    
    def slope(self):
        pass


coordinate1 = (3,2)
coordinate2 = (8,10)

 line = Line(coordinate1,coordinate2)