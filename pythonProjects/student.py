class Student: 
    def __init__(self, fname, lname, id, energy_level = 10.0):
          self.fname = fname
          self.lname = lname
          self.id = id
          self.energy_level = energy_level

    def __str__(self):
         return f"{self.fname}: {self.id}"
    
    def greeting(self):
         print("Hello there")
    
    def take_exam(self):
         if self.energy_level > 0 :
              self.energy_level -= 1
    
    def get_energy_level(self):
         return f"Student's energy level is: {self.energy_level}"
    
'''
Naming convention:
     Class should be in its own file. The name should be all lower case with words separated by
     underscores.
     All words in a class name should start with an uppercase letter.
Dunder methods:
     Classes should include the dunder (stands for double underscore) methods:
     __init__ - this method is called when the object is created. It initializes the object. It is like the
     constructor in Java.
     __str__ -this method returns a string representation of the object when the object is printed. Make
     sure to return the string, not print it.
     Make sure to precede and end each dunder method with a “double underscore”. Otherwise, the
     methods are not recognized and will not work as expected.
Self reference
     The first parameter of any class method must be self.
     All instance variables within the class should use self before the variable name. Eg.
     self.account_balance
     If calling a call method within a class the self keyword must precede the method call. For example,
     self.get_balance() The self keyword should not be used outside of the class like in the demo file. 
     
     '''