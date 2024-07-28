# Fundamentals of Computer Science - Chapter 9

## 9.1 Object-Oriented Programming
- Object-oriented techniques are used for writing complex programs
- Instead of only working with strings or numbers, you work with objects in the application
- Objects with the same behavior are grouped in classes
- Object-oriented programming is a programming style where tasks are solved by collaborating objects
- Have already been using this programming style with strings, lists, files, as they are objects that have sets of methods
- Class describes a set of objects with the same behavior, and each class defines a specific set of methods you can use with its objects
- Set of methods provided by a class, together with a description of their behavior is called the public interface
  - This allows you to work with a class without having to know all the details
  - Public interface tells you the "what", not the "how"
- Encapsulation allows you to set public details without having to expose the inner workings
  - Also allows you to make improvements without impacting programmers who use the objects
### Definitions
- `object-oriented programming`: designing a program by discovering objects, their properties, and their relationships
- `class`: a programmer-defined data type
- `public interface`: the features (methods, variables, and nested types) of a class that are accessible to all clients
- `encapsulation`: the hiding of implementation details

## 9.2 Implementing a Simple Class
- Objects store their data in instance variables
- An instance of a class is an object of a class, therefore, an instance variable is a storage location that is present in each object of the class
- By convention, start instance variables with an underscore, which indicates to users that they should not directly access it
- Methods are defined as part of the class definition and the first parameter variable of each method is called `self`
- 
### Definitions
- `instance variable`: a variable defined in a class for which every object of the class has its own value

## 9.3 Specifying the Public Interface of a Class
- When designing a class, start by specifying its public interface
- Add comments for a class definition that specify what the class does
- Supply comments for each method within the class as well, as you would with functions
- The data and method bodies make up the "private implementation" of the class
- Can be useful to classify methods of a class as "mutators" and "accessors"
  - Mutator methods modify the object upon which they operator
  - Accessor methods query the object for some data, but do not change it
### Definitions
- `public interface`: the features (methods, variables, and nested types) of a class that are accessible to all clients
- `mutator method`: a method that changes the state of an object
- `accessor method`: a method that accesses an object but does not change it

## 9.4 Designing the Data Representation
- Objects store their data in instance variables, which are variables that are declared inside the class
- Each object needs to have the data necessary to carry out any method calls
- When implementing a class, go through all methods and think about what data they need
  - Can be good to start with accessor methods
- Method calls can come in any order, so should not make order assumptions between different methods
### Definitions
- `instance variable`: a variable defined in a class for which every object of the class has its own value

## 9.5 Constructors
- A constructor defines and initializes the instance variables of an object
- The constructor is automatically called whenever an object is created
- After the constructor is completed, a reference to the new object is returned
- Python uses `__init__()` for constructors
```python
def __init__(self):
    self._item_count = 0
    self._total_price = 0
```
- First parameter of every constructor must be `self`
- You can only define one constructor per class, but you can use arguments to define different behavior
- Once an object has been created, you should not directly call the constructor again
- Instead, you should initialize a new object if you need the values back in their original state
- Generally should not ever call a method that starts with `__` double underscore, these are intended for internal purposes
### Definitions
- `constructor`: a sequence of statements for initializing a newly instantiated object

## 9.6 Special Topic: Default and Named Arguments
- In Python, you can specify default values for parameter variables in any function or method
- If you call the function/method without supply values to those parameters with defaults, the defaults will be used
- If you want to pass arguments in different order than they are specified, need to use the named arguments
  - This however, only applies to those parameters that are specified out of order

## 9.7 Implementing Methods
