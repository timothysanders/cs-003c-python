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

## 2.8 Strings
### The String Type
- Strings can be stored in variables and accessed as needed, just like numerical values
- String literals refer to particular strings (like 'hello'), which are specified as characters enclosed in a matching pair of single or double quotes
- Empty strings contain zero characters
### Concatenation and Repetition
- If you have two strings, they can be concatenated into one longer string, which results in all the characters of the first string followed by all the characters of the second
- In Python, you can concatenate strings by using `+`
  - Cannot concatenate a string with a numeric value
- Can also use the `*` operator and an integer value to repeat an instance of a string
  - For example, `"tim" * 3 == "timtimtim"`
### Converting Between Numbers and Strings
- The function `str()` can be used to convert numbers to strings, both `int` and `float`
- Additionally, you can use the `int()` and `float()` functions to convert a string into the respective data type
### Strings and Characters
- Strings are sequences of Unicode characters, individual characters can be accessed based on their position within the string
- The first character has an index of 0, second is 1, etc.
- Individual characters of a string are accessed using a subscript notation
  - `name = "tim"`
  - `name[0] == "t"`
- If you try to access an index that does not exist, you will get an index out of range exception
### String Methods
- In computer programs, objects are entities that represent values with certain behavior
- Behavior of an object is given through its methods, which are collections of programming instructions
- Method name follows the object and is separated by a dot
  - For example, `name.upper()` where `upper()` is the method
  - Methods are defined within classes and are called on instances of that class
    - Versus functions, which can be standalone
- Method calls can have arguments and return new versions of the literal, they do not change the object in place
### Definitions
- `character`: a single letter, digit, or symbol
- `string`: a sequence of characters
- `concatenation`: placing one string after another to form a new string
- `unicode`: a standard code that assigns code values to characters used in scripts around the world
- `object`: a value of a class type
- `method`: a sequence of statements that has a name, may have parameter values, and may have a return value. A method (like a function) can be invoked any number of times, with different values for parameters, but can only be applied to an object of the type for which it was defined

## 2.9 Special Topic: Character Values
- Characters are stored internally as integer values, which are based on standard sets of codes
- Python has functions for character encodings, such as `ord()`, which returns the number used to represent a given character, and `chr()`, which is used to return the character associated with a given code

## 2.10 Special Topic: Escape Sequences
- If you need to use double quotes within a string enclosed in double quotes, you can use the `\` character to escape the double quotes
  - For example, `"You're \"Welcome\""`
- Backslashes are not included in the strings
- Backslashes can be used to escape backslashes as well
### Definitions
- `escape sequence`: sequence of characters that starts with an escape character, such as `\n` or `\`

## 2.11 Computing and Society: International Alphabets and Unicode
- In 1988, consortium of hardware and software manufacturers started developing a uniform encoding scheme, called "unicode"
- Unicode is meant to encode text in almost all written languages of the world
- Python3 fully supports unicode and you can create strings with any unicode characters
- Unicode contains over 100,000 characters today, with plans to add unicode characters for extinct languages
### Definitions
- `unicode`: a standard code that assigns code values to characters used in scripts around the world

## 2.12 Input and Output
- Most programs ask the user to provide input values
- User input can be gathered by using the `input()` function
- The input function should first print a message that tells the user what to enter, this is called a prompt
- The function then places the cursor immediately following the prompt string
- Once the user supplies the input, it is returned from the input function as a string which can be stored in a variable
- To get numeric input from a user, need to convert the string to the appropriate data type, such as `int` or `float`
- Output can be formatted in a few different ways
  - Ex: `print("%.2f" % price)` will display the price with two digits after the decimal
  - Can also right justify by using `print("%10.2f" % price)`
  - These are examples of format specifiers
- Format strings can contain one or more format specifiers and literal characters
- When retrieving numeric values from input, convert them immediately after the input operation
  - Don't save the input to a string and then reconvert it every time it's used
### Definitions
- `prompt`: A string that tells the user what to input
- `string format operator`: the percent sign `%` used to format a string

## 2.13 How To: Writing Simple Programs
- Step 1: Understand the problem: What are the inputs? What are the desired outputs?
- Step 2: Work out examples by hand
- Step 3: Write pseudocode for computing the answers
- Step 4: Declare the variables and constants you need, and decide what types of values they hold
- Step 5: Turn the pseudocode into Python statements
- Step 6: Provide input and output
- Step 7: Provide a Python program

## 2.16 Graphics: Simple Drawings
### Definitions
- `window`: a desktop component that contains a frame and title bar

## 2.17 How To: Graphics: Drawing Graphical Shapes
- Problem Statement: Create a program to draw a national flag
- Step 1: Determine the shapes that you need for the drawing
- Step 2: Find the coordinates for the shapes
- Step 3: Write Python statements to draw the shapes
- Step 4: Write the program that creates the graphics window and includes the drawing instructions at the proper spot in the template