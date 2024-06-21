# Fundamentals of Computer Science - Chapter 2

## 2.1 Variables
- Numbers and characters are important data types in almost all Python programs
- When creating programs, they will store values to be used later
- In Python, these values are stored in items called variables
### Defining Variables
- Variables are storage locations in a computer program, which have a name and hold a value
- Think of variables as a parking space in a parking garage, with a name and a value
- Assignment statements are used to place a value into a variable
- Left hand side of an assignment statement consist of the variable name, the right hand side is an expression that has a value
  - The value is what is stored in the variable
- After the variable has been defined, it can be used in other statements
- If existing variable is assigned a new value, that replaces the previous contents
- The `=` sign in the assignment operator is not the same as the algebraic `=` (which denotes equality)
- Statements are executed in the order they are defined, so if you try to use a variable before it is defined, you will get an "undefined name" error
### Number Types
- Computers can manipulate data of many different types of values, and each value is a specific type
- Data types determine how data is represented in the computer and what can be done with the value
- Data types provided by the language itself are called primitive data types
- Python has many primitive data types, such as numbers, text strings, files, containers, etc.
- Programmers can also create their own user-defined data types
- Python has several different types of numbers
  - Integers are whole numbers, without a fractional part. This is the `int` data type
  - Floating point numbers are used when fractional parts are required, these are `float` data types
- The numbers themselves in Python are called number literals, if it has a decimal point, it is a float, otherwise it is an int
- Variables in python can store values of any type, data type is associated with the value, not the variable
- You can change the data type of the value stored in a variable, but this is not a great idea
### Variable Names
- When naming variables, give them names that explain their purpose
- Names must follow the following rules
  - Names must start with a letter or an underscore
  - Remaining characters must be letters, numbers, or underscores
  - Cannot use special characters (such as `?` or `<`) or spaces within variable names
  - Conventions like camelCase can be used to help distinguish word boundaries in variables
  - Names are case sensitive
  - Cannot use reserved words such as `if` or `class` as names
- It is also good to follow certain python rules of "good taste" for naming
  - It is better to use descriptive names, than very terse names (for example, use `cansPerPack` instead of `cpp`)
  - Most programmers use names for variables that start with a lowercase letter and all uppercase variable names are used for constants
    - Names starting with uppercase letters are typically reserved for class names/user defined types
### Constants
- Constants are variables whose value should not be changed after it is initialized
- Common practice to specify constant names as all uppercase characters
- Constants help eliminate the problem of using "magic numbers" and can help make code self-documenting
### Comments
- Comments are explanations for human readers of your code
- Comments can help other programmers understand the intent of your code, and it can be helpful for yourself when revisiting older code
### Definitions
- `variable`: symbol in a program that identifies a storage location that can hold different values
- `assignment`: placing a new value into a variable
- `type`: named set of values and operations that can be carried out with them
- `primitive type`: data type provided by the language itself
- `user-defined data types`: data type, not provided by the language, that is defined by the user. In Python, class definitions are used to specify user-defined data types
- `integer`: a number that cannot have a fractional part
- `floating-point number`: a number that can have a fractional part
- `number literal`: a constant value in a program explicitly written as a number
- `case sensitive`: distinguishing upper and lowercase characters
- `reserved word`: a word that has special meaning in a programming language and therefore cannot be used as a name by the programmer
- `comment`: an explanation to help the reader understand a section of a program; ignored by the interpreter
- `magic number`: a number that appears in a program without explanation

## 2.2 Arithmetic
### Basic Arithmetic Operations
- Python supports basic arithmetic operations: addition, subtraction, multiplication, and division
  - Addition: `a + b`
  - Subtraction: `a - b`
  - Multiplication: `a * b`
  - Division: `a / b`
- The symbols used for these operations are called operators
- Combination of variables, literals, operations and parentheses is called an expression
- Parentheses are used just like in algebra
- If you mix `int` and `float` in an expression, the result is `float`
### Powers
- Python uses the exponential operator `**` to denote the power operation, there can be no space between the asterisks
- Unlike other arithmetic operators, power operators are evaluated from right to left
### Floor Division and Remainder
- When dividing two integers with `/`, you get a `float` value returned
- Floor division can be performed by using `//`
  - For positive integers, floor division computes the quotient and discards the fractional part
  - For example `7 / 4 == 1.75` but `7 // 4 == 1`
- To get the remainder of floor division, use the `%` operator (modulus)
  - For example, `7 % 4 == 3`
- Floor division and modulus can be used for negative integers and floating-point numbers, but is not covered in this book
### Calling Functions
- Functions are collections of instructions to carry out a particular task
- Most functions return a value, which means the function passes back a value once it has completed its task
- Values returned by functions can be stored in variables
- Data provided to the function is called an argument
- Some functions have optional arguments that are only used in certain situations
- Pythons documentation will often use square brackets to denote optional arguments
  - For example, `round(x[, n]) # Returns x rounded to a qholw number or to n decimal places`
- Some functions take an arbitrary number of functions
  - For example, `min(7.25, 10.95, 5.95, 6.05)`
### Mathematical Functions
- Python contains a standard library that can be used to create a number of powerful programs
- A library is a collection of code that can be used in your program
- Python's standard library is organized into a number of modules, with related functions and data types
- To use functions from a module, you must first import it
- Many functions are defined within a module, but some can be used without importing any module
  - These functions are called built-in functions
### Definitions
- `expression`: syntactical construct that is made up of constants, variables, functions, and method calls, and operators combining them
- `floor division`: taking the quotient of two integers and discarding the remainder, notated with `//`
- `modulus`: the `%` operator that computes the remainder of an integer division
- `library`: set of modules that can be included in programs
- `standard library`: collection of modules that come with the interpreter and are available for use in every Python program
- `built-in function`: a function defined by the language itself that can be used without having to import a module

## 2.3 Special Topic: Other Ways to Import Modules
- Python has a few different ways to import modules
  - `from math import sqrt, sin, cos`
  - `from math import *`
  - `import math`
    - If you do this last one, you will need to reference your functions like what is shown
      - `y = math.sqrt(x)`

## 2.4 Special Topic: Combining Assignment and Arithmetic
- You can use combinations of assignment and arithmetic operations like the examples below
  - `total += cans`
    - Is the same as `total = total + cans`
  - `total *= 2`
    - Is the same as `total = total * 2`

## 2.5 Special Topic: Line Joining
- If you have expressions that are too long for a single line, you can continue it on another line if the line break is inside parentheses
- One can also use `\` to join lines, but this is not as common