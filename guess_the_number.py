import random

# Random numbers to verify range 

first_random_number =  1
last_random_number = 20

# Random number initialization 

random_number = random.randint(first_random_number, last_random_number)


# Attemps count 
attemps = 0


# Main Code
while True:
    
    try:
        your_number = int(input(f"Guess The Integer number from range {first_random_number} - {last_random_number} : \n "))
    
    except(ValueError):
        
        print("Wrong Input type Try Again (This will not be added to your attemps count)")
        continue
    
    
    if your_number < first_random_number or your_number > last_random_number:
        
        print("Number out of Range, Try Again (This will not be added to your attemps count) ")
        continue
    
    attemps += 1
    
    if your_number == random_number : 
        
        print(f"Good Job , You took Only {attemps} attemps to guess number : {random_number} \n")
        
        attemps = 0
    
    elif your_number < random_number :
        
        print(f"\n Choose Higher , your attemps count is {attemps} \n")
        
        continue
        
    elif your_number > random_number:
        
        print(f" \n Choose Lower , your attemps count is {attemps} \n")
        
        continue
        
    # Continue or finish program      
    
    question = input("Press Enter Play Again or Input any symbol to exit :  ")
    
    if question == "":
        continue
    else:
        break 
        
