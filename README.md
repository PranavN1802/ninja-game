# Ninja Dash Game

**Ninja Dash** is a 2D action game where the player controls a ninja character to defeat enemies, advance through levels, and collect points. The game is implemented using Python and Tkinter for the graphical user interface.

## Features

- **Multiple Levels**: The game has multiple levels, with each level featuring different enemy setups.
- **Character Movement**: The player can control the ninja's movement using either the arrow keys or WASD.
- **Shuriken Shooting**: The player can throw shurikens by pressing the space bar. However, shurikens are limited and cost points.
- **Game Cheats**: The game features several cheats that can be triggered by pressing specific keys:
  - `c` to add 100 points.
  - `k` to skip to the next level.
  - `f` to freeze enemies.
- **Pause Functionality**: The game can be paused by pressing `p`, and a "boss key" can minimize the game window by pressing `b`.
- **Score and Level Progression**: Players can earn points by defeating enemies and advancing through levels.
- **Save and Load Game**: The game allows players to save their progress and load it later.

## Requirements

To run the game, you need to have Python 3.x installed on your computer. Additionally, Tkinter is required for the graphical interface.

```bash
pip install tk
