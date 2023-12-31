#!/usr/bin/python3

import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

SYMBOL_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

SYMBOL_VALUE = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    """
    Check the winnings based on the symbols in the columns and the bet amount.

    Args:
        columns (list): List of columns in the slot machine.
        lines (int): Number of lines to bet on.
        bet (int): Bet amount on each line.
        values (dict): Dic mapping symbols to their corresponding values.

    Returns:
        int: Total winnings.
        list: List of winning lines.

    """
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    """
    Get a random spin result for the slot machine.

    Args:
        rows (int): Number of rows in the slot machine.
        cols (int): Number of columns in the slot machine.
        symbols (dict): Dictionary mapping symbols to their counts.

    Returns:
        list: List of columns in the slot machine spin result.

    """
    all_symbols = []
    for symbol, SYMBOL_COUNT in symbols.items():
        for _ in range(SYMBOL_COUNT):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    """
    Print the slot machine spin result.

    Args:
        columns (list): List of columns in the slot machine spin result.

    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    """
    Prompt the player to deposit money into their account.

    Returns:
        int: The deposited amount.

    """
    while True:
        amount = input("How much do you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    """
    Prompt the player to choose the number of lines to bet on.

    Returns:
        int: The chosen number of lines.

    """
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Enter a valid number of lines (1-{MAX_LINES}).")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    """
    Prompt the player to choose the bet amount on each line.

    Returns:
        int: The chosen bet amount.

    """
    while True:
        amount = input(f"Place a bet on each line (${MIN_BET}-{MAX_BET}): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    """
    Perform a spin on the slot machine.

    Args:
        balance (int): The current balance of the player.

    Returns:
        int: The change in balance after the spin.

    """
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Balance insufficient. Your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet = ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, SYMBOL_COUNT)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, SYMBOL_VALUE)

    if winnings > 0:
        print(f"You won ${winnings}!")
        print(f"You won on lines:", *winning_lines)
    else:
        print("You didn't win anything.")

    return winnings - total_bet


def main():
    """
    Main function to run the slot machine game.

    """
    balance = deposit()

    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

        if balance <= 0:
            print("Your balance is zero. Add more money to play (q to quit).")
            answer = input("Press enter to add money (q to quit).")
            if answer == "q":
                break
            else:
                balance = deposit()

    print(f"You left with ${balance}")


if __name__ == "__main__":
    main()
