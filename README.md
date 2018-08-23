# Python terminal Super Mario
========================================================<br/>
By Meher Shashwat Nigam

## Introduction

This is a terminal based implementation that tries to simulate the classic Super Mario<br/>
Written in python3 without using pygame and curses.<br/>
Only *colorama* has been used to bring in colours.<br/>
The game has been tested only on Linux based operating systems, may not work on Windows.<br/>
Sounds have been added but commented out due to submission restrictions.

### Prerequisites

- First, install all the requirements
	- `pip install -r requirements.txt`
- Running the game using python3
	- `python3 game.py`

### GamePlay

  Select the level you want to play by entering 1, 2 or 3 when prompted.<br/>
  Mario has 3 lives. Make sure they count.
  Higher levels have :
  - Higher gravity
  - More enemies
  - Faster enemy movement
  - More coins ;)

##### Controls
 You can move mario around using the following controls(make sure *CAPS_LOCK* is off):
 - `d` or `right arrow` to move right
 - `a` or `left arrow` to move left
 - `w` or `up arrow` or `Space_bar` key to jump
 - `q` to quit the game


 Mario can collect coins as it moves --- 200 points<br/>

 Mario can kill enemies by jumping over them. Enemies reduce lives by one if they hit mario from the side; but also die in the process --- 500 points<br/>

 A base score is generated according to the maximum distance traveled in the game.<br/>

 Mario doesn't know how to swim! Mario dies instantly after it falls into the pit.

### Code Structure

The game has been written keeping in mind OOP principles.<br/>
The application demonstrates inheritance, encapsulation and polymorphism.<br/>
- There are three major classes: `Scene` , `Person` and `Obstacle`
- `Mario` and `Enemy` are derived classes of the `Person` class defined in ***people.py***
- Each obstacle/item (`Walls`,`Pits`,`Clouds`,`Grass`,`Coins`) inherits from the `Obstacle` class in ***obstacles.py***
- The `Scene` class holds the full map and all object matrices are blitted into its matrix defined in ***scene.py***
- The ***config.py*** file holds the constant values and variables used throughout the game, in one place
- ***Game.py*** holds the main game engine, and has all object initializations.
- ***scene_gen.py*** makes the basic scene by blitting walls, pits, grass and clouds onto the scene  
- ***gamefunctions.py*** has all necessary gamefunctions like checking object clashes and blitting one matrix over the other after updating
- ***input.py*** defines how character input is taken at runtime
- Code is PEP8 compliant