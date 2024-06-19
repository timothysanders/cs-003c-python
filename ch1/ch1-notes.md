# Fundamentals of Computer Science - Chapter 1

## 1.1 Computer Programs
### Definitions
- `computer program`: sequence of instructions executed by a computer
- `hardware`: physical equipment for a computer or another device
- `software`: intangible instructions and data that are necessary for operating a computer or other device

## 1.2 The Anatomy of a Computer
- Heart of the computer is the CPU (central processing unit), which are composed of hundreds of millions of transistors
- CPU locates and executes program instructions, fetches data, performs arithmetic operations, fetches data from storage, etc.
- Primary storage is made from memory chips, electronic circuits can store data as long as they have electric power
- Computer stores both data and programs in secondary storage and then are loaded into memory when needed
- Modified data is written back to secondary storage when it is updated
- Interaction with computers requires peripheral devices
  - Computer transmits output/information to the user through a screen, speakers, printers, etc.
  - User can enter information/input through keyboard, mouse, etc.
- Computers can connect to networks to read data/programs from central storage locations and send data to other computers
### Definitions
- `central processing unit (CPU)`: part of a computer that executes the machine instructions
- `primary storage`: electronic circuits that store data as long as they have electric power
- `secondary storage`: storage that persists without electricity, such as a hard disk
- `hard disk`: device that stores information on rotating platters with magnetic coating
- `network`: interconnected system of computers and other devices

## 1.3 Computing & Society: Computers Are Everywhere
- ENIAC: electronic numerical integrator and computer
- Computing facilitates search engines, websites, social networks, etc.
- Large computing centers are typically called data centers
- Smaller computers are all around us, in cars, cell phones, etc.
- Knowing how to use computers and program them is an essential skill
- Important for everyone to understand how computers are used

## 1.4 Python Programming Language
- Writing a computer program involves a sequence of instructions executed by the CPU
- Computer programs consist of large volumes of simple CPU instructions, which are tedious and error-prone when written one by one
- For this reason, high-level programming languages, such as Python, have been created to allow programmers to specify instructions at a higher level
- These instructions are then translated to more detailed instructions for the CPU
- Python was developed in the early 1990s by Guido van Rossum, with the intention of being easier to write and update quickly, without as much focus on optimum speed
- Python is very popular in many domains and is very suitable for beginners
- Python is also interoperable between operating systems, such as Windows, UNIX, Linux, and Mac
- Python has numerous packages (bundles of Python code) that can help solve common problems, such as ML, computational biology, statistics, data visualization, etc.
### Definitions
- `high-level programming language`: programming language that provides an abstract view of a computer and allows programmers to focus on their problem domain

## 1.5 Becoming Familiar with Your Programming Environment
- Install python, start python dev environment, write a simple program, run the program
- Python programs are executed using the python interpreter
- Writing programs often requires iterative work, keeping programs requires storing them in files
### Definitions
- `IDE (integrated development environment)`: a programming environment that includes an editor, compiler, and debugger
- `text editor`: a software application used to enter contents of a text file like the statements of a program or contents of a data file
- `terminal window`: window for interacting with an operating system through textual commands
- `case sensitive`: distinguishing upper- and lowercase characters
- `python interpreter`: program that translates python code into byte code and executes it in the python virtual machine
- `file`: a sequence of bytes stored on disk
- `folder`: structure on a disk that can hold files or other folders; also called a directory
- `directory`: structure on a disk that can hold files or other directories; also called a folder

## 1.6 The Python Interpreter
- Imagining a program running, you might think the interpreter reads the program and executes it, one step at a time
- Time-consuming task of reading a program and comprehending the instructions is done once, by a compiler
- Compiler reads the source code (Python instructions) and translates those instructions into byte code
- Byte codes are very simple instructions understood by the virtual machine, which is a separate program similar to the CPU of a computer
- After the compiler has translated your program into virtual machine instructions, they are executed by that virtual machine
- Your Python source code itself doesn't contain all the information that the virtual machine needs, many functions are implemented in the python standard library
- Specialized tasks may require the installation of packages
- Files containing virtual machine instructions have an extension of `.pyc` and are created by the compiler
### Definitions
- `compiler`: program that translates code from a high-level language (like Python) into machine instructions (such as byte code for the Python virtual machine)
- `source code`: instructions in a programming language that need to be translated before execution on a computer
- `byte code`: instructions for the python virtual machine
- `virtual machine`: a program that simulates a CPU that can be implemented efficiently on a variety of actual machines. A given program in Python byte code can be executed by any Python virtual machine, regardless of which CPU is used to run the virtual machine itself

## 1.7 Analyzing Your First Program
- Python programs contain one or more lines of instructions or statements that are translated/executed by the interpreter
- Comments begin with `#`, are not statements, and are often used to provide descriptive info to the programmer
- A function is a collection of instructions that carry out a specific task
- Using a function requires that you specify the name of the function and any values the function needs to carry out its task
- Sequence of characters enclosed in quotation marks is called a string, can use single or double quotes
- Indenting in Python must be consistent
### Definitions
- `statement`: syntactical unit in a program, in Python this is either a simple statement or a compound statement
- `comment`: explanation to help the human reader understand a section of a program; ignored by interpreter
- `function`: sequence of statements that can be invoked multiple times, with different values for its parameter variables
- `argument`: value supplied to a function or method call, or one of the values combined by an operator
- `string`: a sequence of characters

## 1.8 Errors
- Compile-time errors show up with translating python instructions into executable form, these are detected before your code actually runs
- Compile-time errors are sometimes called syntax errors, when these errors are found, no executable program is created
- Error messages may not always be super helpful
- Some errors only show up when the program is executed itself, these are called run-time errors (or exceptions)
- Sometimes the term logic error is used in place of a run-time error
- Errors are unavoidable in the program development process, many syntax errors are likely to show up, but will be found at compilation time
- Run-time errors are more insidious, harder to find and fix because the interpreter cannot flag them
- Responsibility of the programmer to test the program and prevent run-time errors
- Common errors are misspelling words, which can lead to non-obvious errors at compile-time or run-time
### Definitions
- `compile-time error`: An error that is detected when a program is compiled
- `syntax error`: An instruction that does not follow the programming language rules and is rejected by the compiler
- `exception`: class that signals a condition that prevents the program from continuing normally. when these occur, an object of the exception class is thrown
- `run-time error`: an error in a syntactically correct program that causes it to act differently from its specification
- `logic error`: error in a syntactically correct program that causes it to act different from its specification