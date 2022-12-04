This program is a version of hang man, where you are trying not to destroy your parachute.

The _main_ class is what is used to initialize the game by calling the director start game method

The director class will call from The terminal class, word class, and player class.

The terminal class is used to read inputs from the terminal

The player class stores the parachute picture, and controls whether you die or not

The word class stores a secret word which than will compare your guess against it


The project files and folders are organized as follows:
```
root                    (project root folder)
+-- jumper             (source code for game)
  +-- game              (specific game classes)
  +-- __main__.py       (entry point for program)
  +-- README.md           (general info)
```


## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* Blake Lofgreen -blakelof@byui.edu
