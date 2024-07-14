# Fundamentals of Computer Science - Chapter 5

## 5.1 Functions as Black Boxes
- Functions package a computation that consists of multiple steps into a form that can be easily understood and reused
- Functions are sets of instructions with names
- Functions are called to execute their instructions
- Inputs to functions are called arguments
- Outputs of functions are called return values
- Functions can have multiple (or no) arguments, but can only return one value
### Definitions
- `function`: sequence of statements that can be invoked multiple times, with different values for its parameter values
- `argument`: values supplied in a function or method call, or one of the values combined by an operator
- `return value`: the value returned by a method through a return statement

## 5.2 Implementing and Testing Functions
- When implement a function, you need a name, arguments
- This information is put together with the `def` keyword
- The `def` line is called the header of the function
- This is followed by the body of the function
- To return a result from a function, use the `return` statement
- Statements in the body must be indented from the function header
- To test a function, you need to define it and then write statements that call the function and print the result
- Functions must be defined in the file before they are called in a program
- The function `main()` is the conventional starting point of a program
- Good practice is to place all functions in statements, then use one function (`main()`) as the starting point
- When writing a function, you should comment the behavior for human readers and not compilers, these are docstrings
- Never use the same name for a function and a variable
### Definitions
- `parameter variable`: a variable of a method or function that is initialized with a value when the method or function is called
- `header`: a component of a compound statement that ends with a colon `:`
- `body`: all statements of a function or method or statement block

## 5.3 Parameter Passing
- When a function is called, variables are created for each of the functions arguments, these are called parameter variables/formal parameters
- Each parameter is initialized with the corresponding argument
- New parameters are created each time the function is called and they are removed when the function ends
- A generally accepted programming practice is to not modify parameter variables, instead create a new variable
- When you call a function with a variable as a parameter, you don't pass the variable itself, just the value of the variable
### Definitions
- `parameter variable`: a variable of a method or function that is initialized with a value when the method or function is called
- `formal parameter`: parameter variable
- `argument`: value supplied in a function or method call, or one of the values combined by an operator
- `actual parameter`: the argument actually passed to a function or model

## 5.4 Return Values
- The `return` statement is used to specify the results of the function
- The return does not always have to be a variable, rather it can also be a value of an expression
- When the return statement is processed, the function exits immediately
  - This can be beneficial if you want to exit a function early
- Every branch of a function should return a value

## 5.5 Special Topic: Using Single-Line Compound Statements
- Compound statements are typically written across multiple lines
- However, if the body is a single statement, it can be written on one line
- Generally recommended to stay away from this syntax as it may not be as clear for readers

## 5.6 How To: Implementing a Function
- First, identify the problem statement
- Step 1: Describe what the function should do, using simple English descriptions
- Step 2: Determine the function's "inputs" (all the parameters), try not to be overly specific
- Step 3: Determine the types of the parameter variables and the return value
- Step 4: Write pseudocode for obtaining the desired result
- Step 5: Implement the function body
- Step 6: Test your function, testing functions in isolation is called "unit testing"
### Definitions
- `unit test`: a test of a function or method by itself, isolated from the remained of the program

## 5.8 Functions Without Return Values
- Sometimes a sequence of instructions does not need to explicitly return a value
- In these instances, the function returns `None`

## 5.10 Problem Solving: Reusable Functions
- Often you can save yourself time by writing functions that can be used for multiple problems
- If you find yourself writing code multiple times, consider using a function
- Generally, you want to provide parameter variables for the values that vary when a function is reused 

## 5.11 Problem Solving: Stepwise Refinement
- To solve a difficult task, break it down into simpler tasks
- Functions should be kept short, ideally so that they fit on a single screen of the development environment
- Longer functions become more difficult to understand and to test
- Similar to loops, it can be a good idea to trace functions by hand
- Stubs are functions that return a simple value that is sufficient for testing another function
### Definitions
- `stepwise refinement`: The process of solving a problem that starts out with a subdivision of steps, then continues by further subdividing those steps
- `stub`: a function or method with no or minimal functionality

## 5.13 Worked Example: Using a Debugger
- Computer programs rarely run perfectly the first time, and it can be frustrating to find errors, or bugs in your code
- Print statements can be very helpful, but they may not always make it obvious what is happening
- Most modern IDEs contain what's called a debugger, that allows you to follow the flow of execution of a program
- Debuggers typically have commands to set breakpoints, run until a breakpoint, step over, or step inside
- When the application reaches a breakpoint, it will pause (before executing the line), displaying the values of variables at that point

## 5.14 Variable Scope
- The "scope" of a variable is the part of the program in which you can access it
- For example, with a function, the function parameter variable scopes are the entire function (but not outside of it)
- Variables that are defined in functions are called "local variables", these variables are available until the function ends
- It is possible to use the same variable name more than once in a program (though probably a bad idea)
- Python also has "global variables", which are available to all functions and scopes
  - These variables must be updated with the `global` declaration, however
- Generally, you should avoid global variables, they can be difficult to determine what the values are at different points
- While global variables are not a great idea, global constants can be very helpful
### Definitions
- `scope`: the part of the program in which a variable is defined
- `local variable`: a variable whose scope is a function or method
- `global variable`: a variable whose scope is not restricted to a single function or method