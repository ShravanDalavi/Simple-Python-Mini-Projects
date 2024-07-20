# Snake Game

This is a classic Snake Game implemented using Python and the Pygame library.

## Description

This game allows users to control a snake to eat food, which makes the snake grow longer. The objective is to eat as much food as possible without colliding with the walls or the snake's own body.

## Requirements

- Python 3.x
- Pygame

## Installation

1. **Clone the repository:**
```bash
              git clone https://github.com/yourusername/snake-game.git
              cd snake-game
```   

2. **Install the required Python modules:**
If you haven't installed Pygame, you can do so using pip:
```bash
                pip install pygame 
```
Pygame is required to run this game as it provides functionalities for graphics, sounds, and user inputs.
    

## How to Run the Script

1. Once you have installed Pygame and navigated to the project directory:
```bash
           python snake_game.py
```          

## Game Controls

- Use the arrow keys (UP, DOWN, LEFT, RIGHT) to control the direction of the snake.
- The game ends if the snake collides with the wall or itself.
- Press `Q` to quit the game or `C` to play again when the game is over.

## Game Features

- Score Display: Your current score is displayed on the screen.
- Game Over: When the snake collides with the wall or itself, a "Game Over" message will appear with options to quit or play again.
- Real-time score display.
- Simple and intuitive controls.

## Acknowledgments

- [Pygame](https://www.pygame.org/news)

## Code Structure
The main game logic is implemented in snake_game.py. Here's a brief overview of its components:

- Initialization: Pygame is initialized, colors are defined, and the game window is set up.
- Game Loop (gameLoop function): Manages the game's main loop where snake movement, collision detection, score display, and game over conditions are handled.
- Functions: Includes functions for displaying the score (display_score), drawing the snake (draw_snake), and handling the game over message (game_over_message).
```bash
                      # Place your entire Python script code here, including imports and functions.
```