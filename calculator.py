while True:
    
    
    # First Operand Input and Validation
    
    while True:
        try:
            
            operand_one = eval(input("Please Enter First Operand: "))

            break
            
        except:
            
            print("Wrong Input Types, please try again ")
            
            continue


    # Second Operand Input and Validation
    
    while True:
        try:
            
            operand_two = eval(input("Please Enter Second Operand: "))

            break
            
        except:
            
            print("Wrong Input Types, please try again ")
            
            continue
    
    # Operation input and validation
    
    while True:
        
        operation = input("Please Choose Arithmetic Operation [ + , - , * , /] ")
        
        try:
            
            if len(operation) == 1: 
            
                print( operand_one,operation,operand_two,"=",eval (f"{operand_one}{operation}{operand_two}"))
            
                break
            
            
            print("Wrong Operation or ZeroDivision Error , Please Try Again:")
            continue
            
        except:
            
            print("Wrong Operation or ZeroDivision Error , Please Try Again:")
            
            continue
    
    # Continue or finish program
    
    question = input("Press Enter continue or Input any symbol to exit :  ")
    
    if question == "":
        continue
    else:
        break 
        
