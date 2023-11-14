# Slot-Machine

The Python script is a concise simulation of a slot machine game. Players begin by depositing an initial amount and then proceed to place bets on a specified number of lines, with each line accommodating a set wager. The game features symbols (A, B, C, D) with varying frequencies and corresponding values.

Key functions in the script include:

1. **`check_winnings`**: This function determines if there are any winning combinations on the selected lines. It iterates through the columns, checking for matching symbols on each line.

2. **User Interaction Functions**:
    - **`deposit`**: Asks the user to deposit an initial amount, ensuring a positive integer input.
    - **`get_number_of_lines`**: Prompts the user to specify the number of lines to bet on within the range of 1 to 3.
    - **`get_bet`**: Obtains the user's bet amount per line within the specified range of 1 to 100.

3. **`get_slot_machine_spin`**: Simulates the spinning of the slot machine by randomly selecting symbols based on their frequencies. The resulting combinations are stored in columns.

4. **`print_slot_machine`**: Prints the outcome of the slot machine spin, displaying the symbols in a matrix-like format.

The main game loop, implemented in the `main` function, continually prompts the user to play or quit. It displays the current balance, allows the user to spin the slot machine, and calculates the winnings based on the outcomes. The game continues until the user decides to quit, providing a final balance at the end.

The script emphasizes user input validation, ensuring that deposited amounts, number of lines, and bet amounts fall within acceptable ranges. The game also checks if the total bet exceeds the available balance.

In summary, this script provides a streamlined and interactive slot machine experience, demonstrating key aspects of Python programming such as random selection, input validation, and modular design.
## Output
![image](https://github.com/bitsonymous/Slot-Machine/assets/115882395/0a01ae7c-9643-4f48-b2d5-3307d3d7e279)
