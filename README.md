# Python-WEEK-5-OOP
# Object-Oriented Programming (OOP) in Python

This repository contains examples of Object-Oriented Programming (OOP) concepts in Python, focusing on key concepts such as **classes**, **inheritance**, and **polymorphism**. The exercises in this repo demonstrate how these OOP principles are applied in real-world scenarios.

## Assignment Overview

### **Assignment 1: Design Your Own Class! 🏗️**
In this assignment, I designed a `Smartphone` class with attributes and methods to simulate basic functionality like charging and making calls. I also created a subclass `GamingPhone` to demonstrate **inheritance** and **polymorphism**, where the derived class adds new features to the base class.

### **Activity 2: Polymorphism Challenge! 🎭**
In this activity, I created a base class `Vehicle` with a common method `move()`. Then, I created subclasses (`Car`, `Plane`, and `Bicycle`) that each implement the `move()` method differently, showcasing **polymorphism**. This demonstrates how different classes can have the same method with different behaviors.

## Key Concepts

### 1. **Classes and Objects**
A class is a blueprint for creating objects. Each object has attributes (characteristics) and methods (actions). In the `Smartphone` class, for example, each phone object has attributes like `brand`, `model`, and `battery_percentage`, and methods like `charge()` and `make_call()`.

### 2. **Inheritance**
Inheritance allows one class to inherit attributes and methods from another class. The `GamingPhone` class inherits from `Smartphone`, adding its own features like `ram_size` and the method `play_game()`. This promotes code reuse and makes it easier to extend the functionality of existing classes.

### 3. **Polymorphism**
Polymorphism allows objects of different classes to respond to the same method in different ways. In the `Vehicle` example, the `move()` method is implemented differently for `Car`, `Plane`, and `Bicycle`, but we can call `move()` on any of the vehicle objects, and it will behave according to the type of object.

## How to Use

1. **Clone the Repository**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/oop-python-assignment.git
   cd oop-python-assignment
