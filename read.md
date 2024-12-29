### README: Number Guessing Game

#### Overview
This Python script is an interactive number-guessing game where the user tries to guess a randomly generated number within a range they specify. The program provides feedback on whether the guesses are too high, too low, or correct and counts the number of attempts the user makes.

---

#### How It Works
1. **User Input**:
   - The user specifies the upper limit for the range of the random number.
   - The program ensures that the input is valid (a positive integer greater than 0).

2. **Random Number Generation**:
   - A random number is generated between `0` and the user-defined upper limit.

3. **Guessing Loop**:
   - The user is repeatedly prompted to guess the number.
   - After each guess, the program provides feedback:
     - If the guess is correct, the user is congratulated, and the total number of attempts is displayed.
     - If the guess is too high or too low, the program informs the user accordingly.
   - The game continues until the correct number is guessed.

---

#### Features
- **Dynamic Range**: The range of numbers is defined by the user, making the game customizable.
- **Feedback on Guesses**: Users are informed whether their guesses are too high, too low, or correct.
- **Attempts Tracking**: The program keeps track of how many guesses the user makes.

---

#### Requirements
- Python 3.x installed on your system.

---

#### How to Run
1. Save the script in a `.py` file, e.g., `number_guessing_game.py`.
2. Open a terminal or command prompt.
3. Run the script by typing:
   ```bash
   python number_guessing_game.py
   ```
4. Follow the on-screen instructions.

---

#### Example Interaction
```plaintext
Type a number: 10
Make a guess: 5
You are above the number
Make a guess: 3
You were below the number
Make a guess: 4
You got it!
You got it in 3 guesses
```

---

#### Customization
- **Change the Random Number Range**: By modifying the `random.randint(0, top_of_range)` line, you can adjust the starting point or range of the random number.
- **Add More Feedback**: Customize the feedback messages to make the game more engaging.

---

#### Notes
- The program gracefully handles invalid inputs by prompting the user to enter a valid number.
- The game exits cleanly if the user enters invalid inputs for the upper limit or guesses.

Enjoy the game! 🎉