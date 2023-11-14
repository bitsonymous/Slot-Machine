import random
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
ROWS = 3
COLS = 3
symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}
symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}
def check_winnigs(columns, lines, bet, values):
    winings = 0
    winings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            symbol_to_check = col[line]
            if symbol_to_check != symbol:
                break
        else:
            winings += values[symbol]*bet
            winings_lines.append(line + 1)
    return winings, winings_lines

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the nummbers of lines to bet on (1-{MAX_LINES}) : ")
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= 3:
                break
            else:
                print(f"Number of lines must be between 1-{MAX_LINES}")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True:
        bet = input(f"What would you like bet on each line ({MIN_BET}-{MAX_BET}) $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between {MIN_BET}-{MAX_BET}")
        else:
            print("Please enter a vaild bet")
    return bet

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        curr_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(curr_symbols)
            curr_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,col in enumerate(columns):
            if i!= len(columns) -1:
                print(col[row], end = " | ")
            else:
                print(col[row])

def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines*bet
        if(total_bet> balance):
            print(f"Your betting amount is higher than balance, You need {total_bet-balance} more $.")
        else:
            break
    print(f"You are betting {bet}$ on {lines} lines, Total bet is equal to : {total_bet}$")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    wining, winings_lines = check_winnigs(slots,lines, bet, symbol_value)
    print(f"You won {wining}$ winings lines : ", *winings_lines)
    return wining - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is {balance}$.")
        spin = input("Press enter to play (q to quit). ")
        if(spin == "q"):
            break
        balance += game(balance)
    print(f"You left with {balance}$.")
    
main()