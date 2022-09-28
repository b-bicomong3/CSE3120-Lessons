// Notes.md

# CSE3120 - Object-Oriented Programming 1 - Notes

## Definitions

__Object-Oriented Analysis (OOA)__ is the process of looking at a problem, system or task and identifying the objects
and interactions between those objects. It answers the questions, _what needs to be done_.

* This term is often called a use case analysis

__Object-Oriented Design (OOD)__ is the process of converting the identified objects and interactions from OOA into
object behaviours. It answers the question, _how things need to be done_.

* This term is often called a behavioural analysis

__Object-Oriented Programming (OOP)__ is the process of implementing the outcome of OOD into a functioning program. It
uses class templates to create objects that have attributes and method.

A __Class__ is a model of an object. Classes contain _attributes_ and _behaviours_ which are inherited when objects
are _instantiated_ from the class. Another definition of a class is a blueprint or template.

* An __Attribute__ is a property or characteristics an object processes. Each object can have a different values for the
  attribute, but all objects instantiated from the class inherits the same attributes, which can thought of as the
  object's variables.
* A __Behaviour__ is an action that can reformed on the data within an object. Behaviours are formally name _Methods_
  and are written in teh same manner as a function. Therefore, methods can accept arguments into parameters and return
  values.
* Methods can accept and return data externally from the object. It also has access to all attributes to all objects.
    * NOTE: An object never has to pass an attribute globally to a method.
    * Methods always have at least one parameter, ```self```, which indicates that the function is referencing the
      current object.
        * __Constructors__ are methods that provide the object with the default set of attributes. In python, it
          is ```self.__int__(self)```. Constructors create the objects from the class template with values within the
          attributes. The constructor can pass arguments that are stored as attributes in the construction of the
          object.
            * In general, all attributes of the object should be present in the Constructor, even if their default value
              is None.

```python
from random import randint


class Die:
    """
    A die object that can be rolled
    """

    # Constructor
    def __init__(self, SIDES):
        # Attributes of the object
        self.MAX_NUM = SIDES

    # Method
    def getRoll(self):
        return randint(1, self.MAX_NUM)


DIE_1 = Die(6)
print(DIE_1.getRoll())  # Output a random number between 1 and 6
DIE_2 = Die(20)
```
An __Object__ is a unique set of data and functions instantiated from a class. An object accesses attributes and methods using _dot notation_ which identifies the object, then the attribute or method.

```python
<object name>.<attribute name> --> Value
<object name>.<method name>(arugments) --> Calls the method
```

## Why OOP? (This section is important)
1. __Encapsulation__ is the process of protecting or hiding data through the implementation of an _interface_. The interface is often a collection of methods such as setter (modifier) methods and getter (accessor) methods that other objects can interact with.
    * A television encapsulates all hardware and software into a small box which the user interact with through a series of buttons (on the device or on a remote control).
    * It is important to empathize the need for setter and getter methods and how each of the attributes within a class should only be accessed through these methods.
```python
class Main:
    def __init__(self):
        self.UNPROTECTED = 0
        self.__PROTECTED = 1
MAIN = Main()
print("MAIN.UNPROTECTED") # print 0
print("MAIN.__PROTECTED") # ERROR!
```
