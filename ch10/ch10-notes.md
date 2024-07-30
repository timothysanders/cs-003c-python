# Fundamentals of Computer Science - Chapter 10

## 10.1 Inheritance Hierarchies
- Objects from related classes usually share common characteristics and behavior
- Inheritance expresses the relationship between specialized and general classes
- In object-oriented design, inheritance is a relationship between a more general class (called the superclass) and a more specialized class (called the subclass)
- Subclasses inherit data and behavior from the superclass
- For example, all cars are vehicles
- If an algorithm uses a superclass, it can also use the subclass in that algorithm
- Substitution principle means you can always use a subclass object when a superclass object is expected
- In general, when grouping classes in an inheritance hierarchy, we can share common code among classes
- Programming tip: use a single class for variation in values, inheritance for variation in behavior
  - Inheritance is meant to model objects with different behavior
### Definitions
- `inheritance`: the relationship between a more general superclass and a more specialized subclass
- `superclass`: a general class from which a more specialized class (subclass) inherits
- `subclass`: a class that inherits variables and methods from a superclass but adds instance variables, adds methods, or redefines methods
- `substitution principle`: the principle that a subclass object can be used in place of any superclass object

## 10.2 Special Topic: The Cosmic Superclass: object
- In Python, every class declared without an explicit superclass automatically extends the class `object`
- This class is a direct or indirect superclass of every other class in Python
- Object defines a few different methods, such as `__repr__`

## 10.3 Implementing Subclasses
- In Python, you form a subclass by specifying what makes the subclass different from the superclass
- Subclasses automatically have all instance variables that are declared in the superclass
  - You only need to declare instance variables that not part of the superclass
- Subclasses inherit all methods from the superclass, and you define any method that is new to the subclass, or change the implementation of inherited methods
- When you change the implementation of an inherited method, you are "overriding" the method
- The class name inside the parentheses of a class header denotes inheritance
```python
class Vehicle:
    ...
  
class Car(Vehicle):
    ...
    # Car inherits all instance variables and methods from Vehicle()
```
- Instance variables of the superclass are private to that class and only methods from the superclass should access its instance variables
- This is not strictly enforced by Python, but it is good programming practice
- A common error is confusing the super- and subclasses
  - The terminology for superclass and subclass comes from set theory
  - If Car() is our subclass and Vehicle() is our superclass
    - All cars are vehicles, but not all vehicles are cars
### Definitions
- `overriding`: redefining a method in a subclass

## 10.4 Calling the Superclass Constructor
- To call the superclass constructor, you can use the `__init__` special method, using `super()`
```python
class Question:
    ...

class ChoiceQuestion(Question):
    def __init__(self):
        super().__init__()
        self._choices = []
```
- The superclass constructor should be called before subclass defines its own instance variables
  - Note that `self` must still be used for defining the instance variables of the subclass
- If superclass constructor requires arguments, those can be provided as arguments in the `__init__()` method
```python
class Vehicle:
    def __init__(self, number_of_tires):
        self._number_of_tires = number_of_tires

class Car(Vehicle):
    def __init__(self):
        super().__init__(4)
        self._plate_number = "-------"
```

## 10.5 Overriding Methods
- If you want to change the behavior of an inherited method, you override it by specifying new behavior
- If you want to use a method of the superclass, you need to use the `super()` function
- A common error is forgetting to use the `super()` function when invoking superclass methods
  - If you are not careful, you can start making recursive calls that lead to infinite loops

## 10.6 Polymorphism
- Method class are always determined at run time based on the type of the actual object
- This is called dynamic method lookup, which allows us to treat objects of different classes in a uniform way

### Definitions
- `dynamic method lookup`: selecting a method to be invoked at run time. In Python, dynamic method lookup considers the class of the actual object (implicit parameter) to select the appropriate model
- `polymorphism`: selecting a method among several methods that have the same name on the basis of the actual types of the implicit parameters