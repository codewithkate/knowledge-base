This is based on the intermediate text by Irv Kalb called Object-Orients Python.

# Related Resources

- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/#code-lay-out)
# Keywords

- **Procedural or Structural Programming**: making calls to a set of functions
- **Object-Oriented Programming**: an object with methods for reusing information
- **Graphical User Interfaces (GUI)**: human-friendly way to give instructions to a program
- **Pygame**: python library to create games with guis
- **Encapsulation**: wrapping a bunch of methods together in a class
- **Polymorphism**: calls to methods can be used by multiple objects in a variety of ways
- **Inheritance**: a set of information known by one object is passed down to another object
- **Class**: object that holds reusable information and methods
- **Instance Variable**: data that depends on how a Class object is created 
- **Method**: a way to change or retrieve information from within a class object

# Projects

Start with procedural programs then show how OOP solves problems.
%%What's wrong with procedural programming%%

## Higher or Lower Card Game

The player guesses if the next card draw will be "higher" or "lower" than the selected card. They get 20 points for a correct answer and lose 15 points if they're wrong.

### Representing the data

Each card is a dictionary containing key value pairs.

```python
# Jack of Clubs
{'rank': 'Jack', 'suit': 'Clubs', 'value': 11}
```
*A deck of 52 would require you to do this 52 times!*

### About `HigherOrLowerProcedural.py`

**Prerequisites**: variables, assignment statements, functions and function calls, `if`/`else` statements, print statements, `while` loops, lists, strings, and dictionaries.

**Instructions**

>1. The program starts by creating a deck as a list 
>2. Each card is a dictionary made up of a rank, a suit, and a value. For each round of the game, I retrieve the first card from the deck and save the components in variables 
>3. For the next seven cards, the user is asked to predict whether the next card will be higher or lower than the most recently showing card 
>4. The next card is retrieved from the deck, and its components are saved in a second set of variables 
>5. The game compares the user’s answer to the card drawn and gives the user feedback and points based on the outcome 
>6. When the user has made predictions for all seven cards in the selection, we ask if they want to play again

\- Chapter 1

**New Techniques**: all caps for constants, `.casefold()`, `.pop()`, 