# # Ways of defining a Class in Python
# class Computer:
#     # In a Class we can put in two things behaviours (Methods)
#     # and Attributes (variables)
#     def config(self): # Here we define the configuration of Computer
#         print("i5, 16 GB, 1TB")
# 
# # Since the Variable contains an int datatype
# # So it will be of <class 'int'>
# a = 9
# print(type(a))
# 
# # Obviously just like any other Variable we don't
# # have a type for this variable. So we need to mention
# # that it is an instance of the Class.
# com1 = Computer()
# 
# # Let's Check the type of the Object of Computer
# print(type(com1))

# class Computer: # class is defined
#     def config(self): # while working with instances we use self in the methods
#         print("i5, 16GB, 1TB")
# 
# com1 = Computer() # Initializing com1 as the Object of the Class Computer
# Computer.config(com1)



# class Computer: # Class gets initialized
    
#     def config(self): # Regitering the first method with the Self argument
#         print("i5, 16GB, 1TB")
        

# # Initializing the first Object
# com1 = Computer()

# #Initializing the Second Object
# com2 = Computer()

# # Here we have both the Objects of the Same Class.
# # Now, let' call each of those

# Computer.config(com1)
# Computer.config(com2)

# # Let's See a Different Way of calling a method which is uded generally.
# # In this method we use the Object itself to call the method of the Class.
# com1.config()
# com2.config()



# class Computer: # Class gets initialized

#     def __init__(self): # Constructor/Variable Storage gets initialized
#         print("in init")

#     def config(self): # The First Method with a Self Argument
#         print("i5, 16GB, 1TB")

# # First and Second Object of the Class is Created
# com1 = Computer()
# com2 = Computer()

# # Let's Call the method using the Objects
# # Now, as we know init is called automatically for the number of 
# # objects created. 

# com1.config()
# com2.config()


# class Computer: # Class gets initialized

#     def __init__(self, cpu, ram): # Constructor/Variable Storage gets initialized
#         #Obviously we have values in parameters but need variablees to 
#         # store them
#         self.a = cpu # We do that by writing "self.'variable' = Parameter"
#         self.b = ram

#     def config(self): # The First Method with a Self Argument
#         # Now we print the Details Passed in by the Object. Again we need to access the 
#         # Variables in the Class by Self since they are insatnce Variables
#         print(f"Config is {self.a} and {self.b}")

# # First and Second Object of the Class is Created, and 
# # Each Object has it's own Configuration.

# com1 = Computer('i5', 16) # Datas of the First Object
# com2 = Computer('Ryzen 3', 8) # Datas of the Second Object

# # Let's Call the method using the Objects
# # Now, as we know init is called automatically for the number of 
# # objects created. 

# com1.config()
# com2.config()


# class Computer:
#     pass

# c1 = Computer()
# c2 = Computer()

# print(id(c1))
# print(id(c2))

# class Computer: # Class gets initialized

#     def __init__(self): # Constructor with the instance Variables
#         self.name = "Navin"
#         self.age = 28

# # Objects of Class getting initialized
# c1  = Computer()
# c2  = Computer()

# print(c1.name)
# print(c2.name)

# class Computer: # Class getting initialized

#     def __init__(self): # Constructor with two Self Variables
#         self.name = "Apurba"
#         self.age = 18

#     def update(self): # Updating the Age with self as parameter
#         # Now this Self does an important Job, as soon as you call the method how does
#         # the Method knows which Objects age to Update, it is determined by the Self which
#         # takes the Object as the Parameter as said before. So, if you have 10 Objects pointing 
#         # Out you can work with a Single one by just calling the method with that particular
#         # Object
#         self.age = 30

# c1 = Computer()
# c2 = Computer()
# print("By Default",c1.name, c1.age)

# # After we Update the Value
# c1.name = 'Navin'
# c1.age = 12
# print("After Changing",c1.name, c1.age)

# # Calling the Update Method and getting it restored with the Age Changed
# c1.update()
# print("Calling Update",c1.name, c1.age)


# class Computer: # Class getting initialized

#     def __init__(self): # Constructor with two Self Variables and their default values
#         self.name = "Apurba"
#         self.age = 18
    

#     def compare(self, other): # Making a Compare Method with two variables
#         # Now, important thing is that here the self is getting replaced by the
#         # Object which calls it and other is getting replaced by the Object which is
#         # Passed as an Argument
#         if self.age == other.age: # Comparing age of two Objects and returning results 
#             return True
#         else:
#             return False


# # Initializing the Objects
# c1 = Computer()
# # Updating the Age of c1 as by default both of them has age as 18
# c1.age = 30
# c2 = Computer()

# if c1.compare(c2):
#     print("They Are Same")
# else:
#     print("They Are Different")


# class Computer: # Class getting initialized

#     def __init__(self): # Constructor with two Self Variables and their default values
#         self.name = "Apurba"
#         self.age = 18
    

#     def compare(self, other): # Making a Compare Method with two variables
#         # Now, important thing is that here the self is getting replaced by the
#         # Object which calls it and other is getting replaced by the Object which is
#         # Passed as an Argument
#         if self.age == other.age: # Comparing age of two Objects and returning results 
#             return True
#         else:
#             return False


# # Initializing the Objects
# c1 = Computer()
# # Updating the Age of c1 as by default both of them has age as 18
# c1.age = 30
# c2 = Computer()

# if c1.compare(c2):
#     print("They Are Same")
# else:
#     print("They Are Different")


# class Car: # Class gets Initialized

#     # Defining the Class Variable
#     wheels = 4  # --> Class Variable

#     def __init__(self): # Constructor gets Initialized with two Self Variables

#         # Now Since these Variables are inside the Constructor so they are called Instance 
#         # Variables as they might as well have a Default Value but it changes for each Object
#         # Seperately according to the Object Called and does not affect all the Object's Value

#         self.mil = 10 # It tells the Milage of the Car --> Instance Variable
#         self.com = "BMW" # It tells the Company/Brand of the Car --> Instance Variable
# # Objects getting Initialized
# c1 = Car()
# c2 = Car()

# # Changing the Value for wheels for all the Objects 
# Car.wheels = 5

# # Printing the Values for both the Objects
# print(f"""        Credentials of C1:
# Car Milage: {c1.mil}
# Car Brand: {c1.com}
# Car Wheels: {c2.wheels}
#         Credentials of C2:
# Car Milage: {c2.mil}
# Car Brand: {c2.com}
# Car Wheels: {c2.wheels}""")


# class Student: # class gets Initaliszed

#     # Declearation of Class/Static Variable
#     school = 'CodeSpectrum'

#     def __init__(self, m1, m2, m3): # Constructor gets Initialized with thee self Variables

#         # Instance Variables are stored and decleared as they are working with Objects and can
#         # be changed for each Object without disturbing other Objects.
#         self.m1 = m1  
#         self.m2 = m2
#         self.m3 = m3
    
#     def avg(self): # Local Method for calculating average
#         # This Average Method is an Instance Method as t works with the Objects

#         return (self.m1 + self.m2 + self.m3) / 3 # It is returning the average of all the Values
        

# # Objects getting decleared
# s1 = Student(34, 47, 42)
# s2 = Student(88, 42, 12)



# class Student: # class gets Initaliszed

#     # Declearation of Class/Static Variable
#     school = 'CodeSpectrum'

#     def __init__(self, m1, m2, m3): # Constructor gets Initialized with thee self Variables

#         # Instance Variables are stored and decleared as they are working with Objects and can
#         # be changed for each Object without disturbing other Objects.
#         self.m1 = m1  
#         self.m2 = m2
#         self.m3 = m3
    
#     def get_value(self): # Here we treat it as Accessor/Getter --> It fetches or gets the Value
#         return f"The Value of m1 is: {self.m1}"
    
#     def set_value(self, value): # Here we treat it as Mutators/Setters --> It sets or Mutates Value.
#         self.m1 = value
        

# # Objects getting decleared
# s1 = Student(34, 47, 42)
# s2 = Student(88, 42, 12)

# print("Before Setting",s1.get_value());  s1.set_value(45)
# print("After Setting", s1.get_value())




# class Student: # class gets Initaliszed

#     # Declearation of Class/Static Variable
#     school = 'CodeSpectrum'

#     def __init__(self, m1, m2, m3): # Constructor gets Initialized with thee self Variables

#         # Instance Variables are stored and decleared as they are working with Objects and can
#         # be changed for each Object without disturbing other Objects.
#         self.m1 = m1  
#         self.m2 = m2
#         self.m3 = m3
    
#     @classmethod # Property Decorator, if not decleared it will ask for argument for cls.
#     def info(cls): # We use cls here as we work with Class Variables in this method.
#         return cls.school
        

# # Objects getting decleared
# s1 = Student(34, 47, 42)
# s2 = Student(88, 42, 12)

# # Calling and getting the Clas Variable, here the School Name
# print(f"The School name is: {Student.info()}")


# class Student: # class gets Initaliszed

#     # Declearation of Class/Static Variable
#     school = 'CodeSpectrum'

#     def __init__(self, m1, m2, m3): # Constructor gets Initialized with thee self Variables

#         # Instance Variables are stored and decleared as they are working with Objects and can
#         # be changed for each Object without disturbing other Objects.
#         self.m1 = m1  
#         self.m2 = m2
#         self.m3 = m3
    
#     @classmethod # Property Decorator, if not decleared it will ask for argument for cls.
#     def info(cls): # We use cls here as we work with Class Variables in this method.
#         return cls.school

#     @staticmethod # Property Decorator for the static Method declearation
#     def info2():
#         print("This is StaticMethod in ABC Module")   # Simply Prints the given Statement

# # Objects getting decleared
# s1 = Student(34, 47, 42)
# s2 = Student(88, 42, 12)

# # Calling the StaticMethod
# print(f"The info is that: ", end= " ");Student.info2()



# class Student: # Initializing the Class

#     def __init__(self, name, roll): # Initializing the constructor with two Instance variables
#         self.name = name
#         self.roll = roll
#         self.lap = self.Laptop()

#     def show(self): # Instance Method acting kind of a Accessor which prints the details of Student
#         print(self.name, self.roll)

#     class Laptop(): # Initializing the Inner Class
#         def __init__(self):
#             self.brand = 'HP'
#             self.cpu = 'i5'
#             self.ram = '16GB'
             
# # Creating the Objects of the Class         
# s1 =  Student('Apurba', 31)
# s2 =  Student('John', 4)

# # Calling the Show Method for getting the details of the Student/Object
# s1.show()


# class Student: # Initializing the Class

#     def __init__(self, name, roll): # Initializing the constructor with two Instance variables
#         self.name = name
#         self.roll = roll
#         self.lap = self.Laptop() # Object/Instance of the Inner Class 

#     def show(self): # Instance Method acting kind of a Accessor which prints the details of Student
#         print(self.name, self.roll)

#     class Laptop(): # Initializing the Inner Class
#         def __init__(self):
#             self.brand = 'HP'
#             self.cpu = 'i5'
#             self.ram = '16GB'
             
# # Creating the Objects of the Class         
# s1 =  Student('Apurba', 31)
# s2 =  Student('John', 4)

# # Calling the Inner Class Constructor from the Outer/Parent Class Object
# print(s1.lap.brand)

# # Calling the Inner Class using a new Object
# lap1 = s1.lap
# print(lap1.brand)


# class Student: # Initializing the Class

#     def __init__(self, name, roll): # Initializing the constructor with two Instance variables
#         self.name = name
#         self.roll = roll
#         self.lap = self.Laptop() # Object/Instance of the Inner Class 

#     def show(self): # Instance Method acting kind of a Accessor which prints the details of Student
#         print(self.name, self.roll)
#         self.lap.show()

#     class Laptop(): # Initializing the Inner Class
#         def __init__(self):
#             self.brand = 'HP'
#             self.cpu = 'i5'
#             self.ram = '16GB'
        
#         def show(self): # Although the name is same as of the Parent Class but the existance is 
#             # different, it has dofferent Memory Location
#             print(self.brand, self.cpu, self.ram)
             
# # Creating the Objects of the Class         
# s1 =  Student('Apurba', 31)
# s2 =  Student('John', 4)

# # Using the Object of the Parent Class to get Data of both Parent and Child/Inner Class
# s1.show()


# class A: # Super/Parent Class is Initialized

#     def f1(self): # First Instance is Decleared
#         print("Feature 1 Working")
    
#     def f2(self): # Second Instance is Decleared
#         print("Feature 2 Working")


# class B(A): # Child/Inherited Class is Initialized

#     def f3(self): # First Instance is Decleared
#         print("Feature 3 Working")
    
#     def f4(self): # Second Instance is Decleared
#         print("Feature 4 Working")


# # Declearing Objects of the Child/Inherited Class
# s1 = B()

# # Printing the Values of both the Classes just using the Object of the Child/Inherited Class
# s1.f1(), s1.f2(), s1.f3(), s1.f4()




# class A: # Super/Parent Class is Initialized

#     def f1(self): # First Instance is Decleared
#         print("Feature 1 Working")
    
#     def f2(self): # Second Instance is Decleared
#         print("Feature 2 Working")


# class B(A): # Child/Inherited Class is Initialized

#     def f3(self): # First Instance is Decleared
#         print("Feature 3 Working")
    
#     def f4(self): # Second Instance is Decleared
#         print("Feature 4 Working")


# class C(B): # Child/Inherited Class is Initialized, It is Child Class of Class B which is Child
#     # Class of Class A

#     def f5(self): # First Instance is Decleared
#         print("Feature 5 Working")

# # Creating Object of Class C and getting the Values of all the Classes
# s1 = C(); s1.f1(), s1.f2(), s1.f3(), s1.f4(), s1.f5()




# class A: # Super/Parent Class is Initialized

#     def f1(self): # First Instance is Decleared
#         print("Feature 1 Working")
    
#     def f2(self): # Second Instance is Decleared
#         print("Feature 2 Working")


# class B(): # Another Super/Parent Class is Initialized

#     def f3(self): # First Instance is Decleared
#         print("Feature 3 Working")
    
#     def f4(self): # Second Instance is Decleared
#         print("Feature 4 Working")


# class C(A,B): # Child/Inherited Class is Initialized, It is Child Class of Class B which is 
#     # Child Class of Class A,B

#     def f5(self): # First Instance is Decleared
#         print("Feature 5 Working")

# # Creating Object of Class B,C and getting the Values available in eacch classes
# s1 = B(); s2 = C();s1.f3(), s1.f4();print(); s2.f1(), s2.f2(), s2.f3(), s2.f4(), s2.f5()

# class A: # Super/Parent Class is Initialized

#     def __init__(self): # Constructor of Parent Class is Initialized
#         print("In A Init")

#     def f1(self): # First Instance is Decleared
#         print("Feature 1 Working")
    
#     def f2(self): # Second Instance is Decleared
#         print("Feature 2 Working")


# class B(A): # Child/Inherited Class is Initialized

#     def __init__(self): # Constructor of Child Class is Initialized with a Super method
#         super().__init__() # Super() method is called for calling the Parent Class Constructor.
#         print("In B Init")

#     def f3(self): # First Instance is Decleared
#         print("Feature 3 Working")
    
#     def f4(self): # Second Instance is Decleared
#         print("Feature 4 Working")

# # Declearing Objects of the Child/Inherited Class
# s1 = B()


# class A: # Super/Parent Class is Initialized

#     def __init__(self): # Constructor of Parent Class is Initialized
#         print("In A Init")

#     def f1(self): # First Instance is Decleared
#         print("Feature 1 Working")


# class B(): #  Class is Initialized

#     def __init__(self): # Constructor of the second Parent Class is Initialized 
#         print("In B Init")

#     def f2(self): # First Instance is Decleared
#         print("Feature 2 Working")
    

# class C(A,B): # Another Super/Parent Class is Initialized.
#     # Remember here A is Passed before B as a Parent Class. So, here we will follow MRO
#     def __init__(self): # Constructor of the Child Class is Initialized
#         super().__init__() # Super() method is called for calling the Parent Classes Constructor.
#         print("In C Init")

# # Creating an Object for the class C and then testing the Constructor calls
# s1 = C()

# class A: # Super/Parent Class is Initialized

#     def __init__(self): # Constructor of Parent Class is Initialized
#         print("In A Init")

#     def f1(self): # First Instance is Decleared
#         print("Feature 1 Working")


# class B(): #  Class is Initialized

#     def f2(self): # First Instance is Decleared
#         print("Feature 2 Working")
    

# class C(A,B): # Another Super/Parent Class is Initialized.
#     # Remember here A is Passed before B as a Parent Class. So, here we will follow MRO
#     def __init__(self): # Constructor of the Child Class is Initialized
#         super().__init__() # Super() method is called for calling the Parent Classes Constructor.
#         print("In C Init")
    
#     def feat(self):
#         super().f1()

# # Creating an Object for the class C and then trying to call f1 method from Class C using Super()
# s1 = C(); s1.feat()


# class Laptop(): # Parent/Super Class gets Initialized 

#     def mode(self, ide): # Parent Class method gets created with two Instance Variable
#         ide.execute() # Now we don't have a Execute Method in the Laptop Class, but since we know
#         # that if the IDE class will have a method called execute with a Self Argument the IDE will
#         # replace that argument and run whatever is Specified in the Method.

# class PyCharm(): # IDE class gets Initialized with Execute method.

#     def execute(self):
#         print("Working")
#         print("Compiling")
#         print("Ending")

# class VsCode(): # Initializing the New IDE Class

#     def execute(self):
#         print("Working");print("Compiling");print("Checking");print("Ending")

# # Declearing the Object of the IDE Class
# ide = PyCharm()

# # Declearing the Object of the Parent Class
# s1 = Laptop()

# # Changing the IDE will work on the Same Way provided that the IDE class has the method execute
# ide = VsCode(); s1.mode(ide)


# a = '5' # Declear Variable a
# b = '7' # Declear variable b

# print(a + b) # Add the following in Conventional Method

# print(str.__add__(a,b)) # Does the Same thing of adding but shows us that how the adding is done.

# class Student: # Parent/Super class getting Initialized

#     def __init__(self, m1, m2): # The Parent Class Constrcutor is getting Decleared with two Instance
#         self.m1 = m1 
#         self.m2 = m2
        
#     def __add__ (self, other): # The Student class Magic Method is getting decleared
#         m1 = self.m1 + other.m1 # Adds the first value of the first and second Objct respectively
#         m2 = self.m2 + other.m2 # Aadds the Second value of the first and second Object respectively
#         s3 = Student(m1, m2) # Updates the Constructor with the new m1, m2 values.
#         return s3 # Returns the upadted values of m1, m2 to the variable and makes it a new Student
#         # Object

# # Objects of the Parent/Super Class are getting decleared
# s1 = Student(58, 65)
# s2 = Student(50, 69)

# # Adds two Objects and finally gets the status of a Student Object with two elements each of which
# # is the addition of the first number of two Objects and the Second number of two Objects 
# s3 = s1 + s2
# print(s3.m1, s3.m2) # Prints the First and Second element of the new Student Object respectively 


# class Student: # Parent/Super class getting Initialized

#     def __init__(self, m1, m2): # The Parent Class Constrcutor is getting Decleared with two Instance
#         self.m1 = m1 
#         self.m2 = m2
        
#     def __gt__ (self, other): # The Student class Magic Method is getting decleared
#         m1 = self.m1 + self.m2 # Adds the first value of the first Object
#         m2 = other.m1 + other.m2 # Aadds the Second value of the second Object 
#         if m1 > m2: # Checks if the sum of the values of the first Object is greater than the other
#             return True # return True if yes
#         else:
#             return False # else returns False

# # Objects of the Parent/Super Class are getting decleared
# s1 = Student(1, 20)
# s2 = Student(50, 69)

# if s1 > s2: # checks which Object is greater
#     print("S1 is Greater")
# else:
#     print("S2 is Greater")


# class Student: # Parent/Super class getting Initialized

#     def __init__(self, m1, m2): # The Parent Class Constrcutor is getting Decleared with two Instance
#         self.m1 = m1 
#         self.m2 = m2
        
#     def __gt__ (self, other): # The Student class Magic Method is getting decleared
#         m1 = self.m1 + self.m2 # Adds the first value of the first Object
#         m2 = other.m1 + other.m2 # Aadds the Second value of the second Object 
#         if m1 > m2: # Checks if the sum of the values of the first Object is greater than the other
#             return True # return True if yes
#         else:
#             return False # else returns False
    
#     def __str__(self):
#         return f"{self.m1}, {self.m2}" # return the Values of the Object in a String Form

# # Objects of the Parent/Super Class are getting decleared
# s1 = Student(1, 20)
# s2 = Student(50, 69)

# a = 9 # Variable with a Memory gets decleared
# print(a) # prints the value of the Variable, exactly it does a.__str__() 

# print(s1) # Prints in the same way as anything gets print undelying, which gets the Address



# class Student: # Parent Class Student is Initialized 

#     def sum(self, a = None, b = None, c = None): # Prent Class Method Sum is decleared with 4 Instance
#         s = 0 # Initializes the default value of the sum variable to 0
        
#         if a != None and b != None and c !=  None: # Checks if all three are not Nonw
#             s = a + b + c
#         elif a !=  None and b != None: # Checks if the first two Parameters are not None
#             s = a + b
#         else: # Checks if only the first Parameter is not None
#             s = a 

#         return s # returns the Sum according to the Number of Variable Passed into the method

# # Object of the Student Class gets decleared
# s1 = Student()

# # Passing and Printing different values and results respectively, This is a trick we used to sort
# # # of achieve Method Overloading in Python Indirectly 
# print("Two values", s1.sum(4, 5)) # Passed Two Values
# print("Three values", s1.sum(4, 5, 8)) # Passed Three Values




# class Parent: # Parent/Super Class gets Initialized

#     def show(self): # Parent Class Method with 1 Instance Param gets decleared
#         print("In Class Parent")


# class Child(Parent): # Child Class gets Initialized by Inheritng from Parent Class

#     def show(self): # Child Class Instance with 1 Instance Param gets decleared
#         print("In Class Child")
#     pass


# # Object of the first Class gets Decleared
# s1 = Parent()

# # Call the Show method with the help of the Parent Object
# s1.show()

# # Object of Child class gets Decleared
# s2 = Child()

# # Call the Show method with the help of Child Object
# s2.show()
































































