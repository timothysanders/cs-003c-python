# Fundamentals of Computer Science - Chapter 3

## 3.1 The if Statement
- Essential feature of computer programs is their ability to make decisions based on input or other circumstances
- If statements are like a fork in the road, when a condition in the statement is fulfilled, one set of statements is executed. Otherwise another is executed
- Think of a flowchart with branching behavior
  - ![Figure 3.1.1](./images/figure-3.1.1-flowchart-for-if-statement.png)
- These `if/else` branches can include many statements, or they may include no statements
- Some constructs in Python are called compound statements, which have a header and a statement block
  - Headers in compound statements require a colon `:` at the end of the header line
  - Statement block begins on the line following the header, must be indented at the same level as the other statements in the block
- Statement blocks indicate that one or more statements are part of a given compound statement
- Common errors occur with indentations in statement blocks of compound statements
  - Best to save your files with spaces instead of tabs
- Sometimes code can be duplicated in branches of compound statements, in these instances, it is good to move the code outside of the compound statement
### Definitions
- `compound statement`: statement construct that consists of a header and statement block
- `statement block`: a group of one or more statements, all of which are indented at the same indentation level

## 3.2 Special Topic: Conditional Expressions
- Python's conditional operator form `value1 if condition else value2`
  - For example, `actualFloor = floor - 1 if floor > 13 else floor` is equivalent to
    - ```python
      if floor > 13:
          actualFloor = floor - 1
      else:
          actualFloor = floor
      ```
- Conditional expressions must be a single statement on a single line or explicitly continued on the next line

## Relational Operators
- Python has six different relational operators for comparing values
- Relational Operators table
  - ![Table 3.3.1: Relational Operators](./images/table-3.3.1-relational-operators.png)
- Important to remember that `=` does not mean "equal" in Python, it is used for assignment
  - Use `==` for measuring equality
- Strings can be compared using relational operators
- Relational operators have a lower precedence than arithmetic operators, which means the arithmetic operators can be used on either side of the relational operator without parentheses
- Comparing strings with operators like less than or greater than can sometimes yield interesting results
- Typically, you do not want to use `==` operator with floating point numbers
- Floating point numbers do not have infinite precision and calculations introduce roundoff errors
- If you specifically need to do a comparison, you can test that the numbers are "close enough" by using epsilon (Greek letter used to denote very small quantity, typically 1E-14)
```python
from math import sqrt
EPSILON = 1E-14
r = sqrt(2.0)
if abs(r * r - 2.0) < EPSILON:
    print("sqrt(2.0) squared is approximately 2.0")
```
### Definitions
- `relational operator`: an operator that compares two values, yielding a Boolean result

## 3.4 Special Topic: Lexicographic Ordering of Strings
- Python's relational operators compare strings in "lexicographic" order
  - This is similar to how words are sorted in a dictionary
- Slight differences between dictionary ordering and lexicographic ordering
  - All uppercase letters come before the lowercase letters. For example, "Z" comes before "a".
  - The space character comes before all printable characters.
  - Numbers come before letters.
  - Punctuation marks have specific ordering, to be discussed elsewhere

## 3.7 Nested Branches
- Often, you will need to include an `if` statement inside of another if statement, this is called a nested set of statements
- Nesting can go many levels deep, if needed
- Hand-tracing is the technique of simulating the program's activities on a sheet of paper, either with pseudocode or Python code

## 3.9 Multiple Alternatives
- Python has a special `elif` syntax that allows for creating if statements with multiple branches
- As soon as one of the branches is satisfied, no other branch is executed
- If no branch matches, then a final `else` can be used to clean up any of the remaining statements
- Generally, we want to go from the most specific use case to the most generic

## 3.10 Toolbox: Sending E-mail
- MIME - Multi-Purpose Internet Mail Extensions
- SMTP - Simple Mail Transport Protocol