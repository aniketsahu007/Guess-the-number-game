# 🎯 Guess The Number – Two Player Python Game

## Overview

Guess The Number is a console-based Python game designed for two players.  
Each player attempts to guess a randomly generated number within a user-defined range.  
The player who guesses the correct number in the fewest attempts wins.

This project demonstrates core Python programming concepts such as loops, conditionals, random number generation, and user input handling.

---

## Features

- User-defined number range
- Two-player gameplay
- Separate random numbers for each player
- Attempt tracking for both players
- Hints for each incorrect guess (too high / too low)
- Automatic winner or draw declaration

---

## How the Game Works

1. The user enters a starting and ending number.
2. A list of numbers is generated within this range.
3. A random number is selected for Player 1.
4. Player 1 continues guessing until the correct number is found.
5. The total number of attempts is recorded.
6. A new random number is selected for Player 2.
7. Player 2 repeats the same process.
8. The game compares attempts and declares the winner or a draw.

---

## Rules

- Only integer inputs are allowed.
- The guessing range includes both start and end values.
- Each incorrect guess increases the attempt count.
- Players receive feedback after every guess.

---

## Example Output

Enter 1st number : 1
Enter 2nd number : 50

Player 1 :
Your chance to guess the number
Your guessed number is smaller than the actual number
TRY AGAIN !!!!!!

CONGRATULATION !!!!!!
you guessed the actual number in 3 attempts



---

## Technologies Used

- Python 3
- Standard Library:
  - random

---

## Code Logic Overview

| Component | Purpose |
|--------|---------|
| `random.choice()` | Selects a random number from the range |
| `while True` loop | Runs guessing until correct |
| `attempt_p1`, `attempt_p2` | Tracks attempts for each player |
| Conditional statements | Provide guessing hints |
| Final comparison | Determines the winner |

---

## How to Run

### Prerequisites
- Python 3.x installed

### Steps
```bash
git clone <repository-url>
cd guess-the-number
python guess_number.py
