class vector2D:
    def __init__(self,i,j):
     self.i=i
     self.j=j
    def show(self):
        print(f"the vector is {self.i}i+{self.j}j ")
class vector3D(vector2D):
    def __init__(self,i,j,k):
       super ().__init__(i,j)  #parent ka init call kro taaki i or j ki value set ho jaye
       self.k=k     #child is adding its extra value
    def show(self):
        print(f"the vector is {self.i}i+{self.j}j+{self.k}k")
e=vector2D(1,2)
e.show()
f=vector3D(1,2,3)
f.show()

class animals:
   pass
class pets(animals):
   pass
class dog(pets):
   @staticmethod
   def bark():
      print("BOW BOW!")
d=dog()
d.bark()      

class employee:
   def __init__(self,)
   