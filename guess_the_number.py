import random

first_number =  1
last_number = 10

random_number = random.randint(first_number, last_number)

attemps = 0

while True:
    
    try:
        guess_number = int(input(f"Guess The Integer number from range {first_number} - {last_number} : \n "))
    
    except:
        
        print("Wrong Input type Try Again (This will be added to your attemps)")
        continue
    
    
    if guess_number < first_number or guess_number > last_number:
        
        print("Number out of Range, Try Again ")
        continue
    
    attemps += 1
    
    if guess_number == random_number : 
        
        print(f"Good Job , You took Only {attemps} attemps to guess number : {random_number} \n")
        
        attemps = 0
    
    elif guess_number < random_number :
        
        print(f"Random number is Higher , your attemps is {attemps} \n")
        
        continue
        
    elif guess_number > random_number:
        
        print(f"Random number is Lower , your attemps is {attemps} \n")
        
        continue
        
        
    question = input("Press Enter Play Again or Input any symbol to exit :  ")
    
    if question == "":
        continue
    else:
        break 
        