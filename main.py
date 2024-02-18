import random


MAX_LINES = 3
MAX_BET = 200
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "DRINK" : 2,
    "BULL" : 4,
    "777" : 6,
    "melon" : 8
}

def get_slot_machine_spin():
    all_symbols = []
    for symbol, symbol.count in symbol.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for cols in range(COLS):
        column = []
        current_symbols = all_symbols[:]
        for row in range(ROWS):
            value = random.choice(all_symbols)

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0,")
        else:
            print("Please enter a number.")
            
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines. ")
        else:
            print("Please enter a number.")
            
    return lines
    
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")
            
    return amount


def main():
    
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet >  blaance:
            print(f"You do not have enough to bet that amount, yoru current balance is: ${balance}")
        else: 
            break
            
   
    print(f"You are betting ${bet} on {lines}. Total bet is equal to: ${total_bet}")
    
    #print(balance, lines)
                 

main()              