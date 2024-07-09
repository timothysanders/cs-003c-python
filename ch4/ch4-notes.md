# Fundamentals of Computer Science - Chapter 4

## 4.1 The while loop
- Loops are a part of programs that are repeated over and over
- These are an important tool for processing calculations that require repeated steps
- In Python, the `while` loop can be used for types of repetition
- General syntax is as follows
- ```python
  while condition:
      statements
  ```
- As long as the condition is true, the statements inside the body of the loop are executed
- If you want to execute a set of statements a specific number of times, you can use a counter
- Different usage types of loops exist, such as *count-controlled*, or *event-controlled*
- Loops that will run a specific, pre-determined number of times are called "definite" loops, while ones that may run for an unknown number of iterations are called *indefinite*
- Common error in while loops is an `infinite loop`, which is a loop that will run forever because the condition will always be true
### Definitions
- `body`: all statements of a function or method or statement block
- `loop`: a sequence of instructions that is executed repeatedly
- `off-by-one error`: a common programming error where a value is one larger or smaller than it should be
  
## 4.2 Special Topic: Special form of the print function
- Python's `print()` function allows you to specify certain *named arguments* that can control the behavior of the output
- For example, the `end=` argument allows you to specify that the print function should not end with a new line
```python
print("00", end="")
print(3 + 4)
```
- Named arguments can be found in many of Python's built in functions

## 4.3 Computing and Society: The First Bug
- Legend tells of the first bug found in the Mark II computer at Harvard University, a moth trapped in a relay switch

## 4.4 Problem Solving: Hand-Tracing
- Hand tracing can be a technique used to determine the value of variables at particular points in time
- Another helpful way to do this is to set a debugger on your code at the condition of the loop (and elsewhere) that allows you to step through the logic

## 4.5 Application: Processing Sentinel Values
- Whenever you are reading sequences, you need a method to indicate the end of the sequence
- These values, which are not actual input, are called *sentinel values*
- When using a sentinel value, you typically need to initialize the value so that you can enter the loop
```python
salary = 0.0
total = 0
count = 0
while salary >= 0.0:
    salary = float(input("Enter a salary or -1 to finish: "))
    if salary >= 0.0:
        total = total + salary
        count = count + 1
```
- Another method is to have two input statements, with one before the loop itself
- This is what is called a *priming read*, because it prepares to initialize the loop
- The input operation in the loop itself is then called the *modification read*
### Definitions
- `sentinel`: a value in input that is not to be used as an actual input value but to signal the end of input

## 4.6 Special Topic: Processing Sentinel Values with a Boolean Variable
- One can also use a boolean variable for loop termination
- You can use a `break` statement as an alternative to the boolean sentinel
- The `break` statement breaks out of the closing loop, need to use caution when in nested loops
### Definitions
- `loop and a half`: a loop whose termination decision is neither at the beginning nor at the end

## 4.7 Special Topic: Redirection of Input and Output
- CLI of operating system allows you to link a file to the input of a program
- `python sentinel.py < numbers.txt` can be used to draw input from the file numbers.txt
- This is called `input redirection`
- This technique can be used for testing programs, where you can put the inputs in a file, then use redirection
- Output can also be redirected, it will contain the input prompts and outputs

## 4.8 Problem Solving: Storyboards
- When designing your application, need to think about what data the user provides, in what order, etc.
- Also, what information does the application display and in what order
- Storyboard can be used to show panels of each step in the process

## 4.9 Common Loop Algorithms
- Sum and Average Value
  - Computing sum of inputs is very common task, with a running total
- Counting Matches
  - This can be used to determine how many values fulfill a particular condition
  - This loop requires a counter that is incremented each time there is a match
- Prompting until a match is found
  - When asking for user input, you can keep asking the user for input until they enter a valid value (think input validation)
- Maximum and Minimum
  - To compute the largest/smaller values in a sequence, keep a variable that stores the largest/smallest element you have encountered and update the variable when a larger/smaller one is found
- Comparing Adjacent Values
  - When processing a sequence of values, sometimes need to compare a value with the value preceeding it

## 4.10 The for loop
- Often you will need to perform an activity like visiting each character in a string
- `for` loop syntax makes this easy
- For loops are used to iterate of the contents of any *container*
- Python has a `range()` function that can be used to generate sequences of integers for use in a loop
  - First argument of `range()` is the first value in the sequence
  - Second argument is the upper limit of the range, note that it is not included in the output
    - For example `range(1, 10)` will give 1,2,3,4,5,6,7,8,9
  - Range defaults to steps of 1, but this can be changed with a third argument
    - Example, `range(1, 10, 2)`
  - Range can also be used with a single argument, if so, the range starts at zero and terminates at the number given, incrementing by one
### Definitions
- `container`: a data structure, such as a list, that can hold a collection of objects and provides a mechanism for managing and accessing the collection

## 4.11 How To: Writing a Loop
- Identify your problem statement
- Step 1: Decide what work must be done inside the loop
  - If you have trouble identifying what should be in the loop, just start by writing out steps by hand, then identify what are the common actions
- Step 2: Specify the loop condition
  - What is the goal we want to reach with our loop?
- Step 3: Determine the loop type
  - Think of *count-controlled* loop with a definite number of events
    - These can be `for` loops
  - Another type is *event-controlled* loop where the loop is executed until some condition is met
    - These can be `while` loops
    - These can use a boolean variable that specifies when you are ready to leave the loop
- Step 4: Set up variables for entering the loop for the first time
- Step 5: Process the result after the loop has finished
- Step 6: Trace the loop with typical examples
  - Can use hand tracing as described in previous sections
- Step 7: Implement the loop in Python
### Definitions
- `flag`: a type with two possible values: true and false

## 4.12 Nested Loops
- Sometimes complex iterations require a nested loop, which is a loop inside of another loop statement
- 
### Definitions
- `nested loop`: a loop that is contained in another loop