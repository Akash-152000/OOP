# OOPS
### Object-Oriented-programming in python

Everything in Python is an object.

There are many different ways, models, or paradigms to write computer programs.

One of the most popular programming paradigms is called object-oriented programming (OOP).

In object-oriented programming, an object refers to a particular instance of a Class.

And a Class is like a blueprint of the state and actions that an object can take.

For example, in Python, a Person Class might look something like this.

```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def get_name(self):
    return self.name
```

The class declared above describes the state and actions of any ***Person*** object.

For example, any Person object will have a ***name*** and an ***age***. These two fields are what determines the state of the object.

In OOP’s terminology, ***name*** and ***age*** are called the object attributes.

You can also call `get_name()` on any Person object to return the name of the person.

We call get_name a method.

And this method, in addition to any other methods that we define, is what determines the object’s actions.

In other words, a Python object has attributes and methods that are defined in the object’s Class.

Here’s how to create a Person object

```
>>> p = Person('Alice', 22)
>>> p.get_name()
'Alice'
```


Object-oriented programming is essentially one way of structuring and designing your code.


