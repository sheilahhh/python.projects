
#collect user input(deposit and their bet)
#create a function that collects deposit. A function is called to execute a block of code and potentially return a value
#while loop to continue asking for input until a valid amount is entered
#check if the entered amount is a number
#if it is a number convert it to an integer as amount was initially defined as a string
#check if amount is>0 
#BET IS THE AMOUNT YOU WANT TO BET PER LINE AND LINES ARE THE ROWS
import random
MAX_LINES= 4 # This is a global constant. 
MIN_BET=1
MAX_BET=300
ROWS=4
COLS=4
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = { #the nos are multipliers, the more rare the symbol is the more it gets multiplied    
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines=[]
    for line in range(lines): #looping through each row
        symbol=columns[0][line] #symbol being checked is the symbol on the first column of the current row 
        for column in columns: #loop through every column to check for symbol at current row
            symbol_to_check=column[line]
            if symbol != symbol_to_check: #check if symbols are not the same
                break
        else:
            winnings += values[symbol] * bet 
            winning_lines.append(line + 1)
    return winnings, winning_lines
def get_slot_machine_spins(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():#this loops through symbol_count
     for _ in range(symbol_count):#this loops through the count itself 
         all_symbols.append(symbol)# adds the symbol according to the count into the dictionary symbol_count
    
    columns = [] #define column list
    for _ in range(cols):#generate a column for every column we have i.e 
        column=[] #picks random values for each row in each column for each value we have
        current_symbols=all_symbols[:]#copies list
        for _ in range(rows):  #loops through no of values we need to generate i.e no of rows in slot machine 
            value = random.choice(current_symbols) #picks random value from current symbols
            current_symbols.remove(value) # removes value so it's not picked again 
            column.append(value) #add value to column
        columns.append(column) #add column to column list
    return columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):#loop through all rows
        for i,column in enumerate(columns):#gives index as well as item. for every row loop through every column and for every column only print the current row were on
            if i != len(columns) - 1: #length of columns -1 is the max index we have to access an element in column index
                print(column[row], end="|")
            else:    
             print(column[row],end=" ")
        print()
def deposit():
    while True:
        amount=input("How much would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("The amount must be greater than 0")
        else:
            print("Please enter a number:")
    return amount

def get_number_of_lines():
   while True:
       lines=input("Enter the number of lines you want to bet on(1-" + str(MAX_LINES)+") : ")
       if lines.isdigit:
           lines=int(lines)
           #validating range
           if 1 <= lines <= MAX_LINES:
               break
           else:
               print("Enter a number between 1 and 4")
       else:
           print("Please enter a number")
    
   return lines


    
def get_bet():
    while True:
        amount=input("How much would you like to bet on each line?")
        if amount.isdigit:
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET} ")
        else:
            print("Please enter a number")
 
    return amount



#define the main function. This reruns the program again if called once the program is ended

def spin(balance):
    lines=get_number_of_lines()
    while True:
     bet=get_bet()
     total_bet = bet * lines
     if total_bet>balance:
         print("You do not have enough to bet")
     else:
        break

    print(f"You are betting ${bet} on {lines} lines and the total bet equals {total_bet}")
 
    slots = get_slot_machine_spins(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines:", * winning_lines)
    return winnings- total_bet

def main():
    balance=deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer=input("press enter to play(q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"you're left with ${balance}")
main()
