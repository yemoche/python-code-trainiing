class Car:
   """
    This is a car class
   """
   def __init__(self, name, color, model):
       self.nameType = name
       self.colorType = color
       self.modelType = model
   
    #class function definition

   def accel(self):
       print(f'The {self.colorType} {self.nameType} accelerates at 200mph')

   #def __repr__(self):
        #return f'Car({self.name},{self.year_built},{self.model})'

#calling the object properties
c1 = Car('Toyota Venza', 'Yellow','MX1')
c2 = Car('Audi','Blue','AKL1')

#calling the function to obtain the object function
c1.accel()
c2.accel()


'''
print(c1.nameType)
print(c1.colorType)
print(c1.modelType)
print(c2.nameType)
print(c2.colorType)
print(c2.modelType)
'''