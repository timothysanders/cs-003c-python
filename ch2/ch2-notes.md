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