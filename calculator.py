while True:
    

    try:
        
        operand_one = float(input("Please Enter First Operand: "))
        operand_two = float(input("Please Enter Second Operand: "))
        
          
        
    except:
        
        print("Wrong Input Types, please try again ")
        
        continue
        
    
    operation = input("Please Choose Arithmetic Operation [ + , - , * , /] ")
    
    try:
        
       print( operand_one,operation,operand_two,"=",eval (f"{operand_one}{operation}{operand_two}"))
        
    except:
        
        print("Wrong Operation or ZeroDivision Error , Please Try Again:")
        
        continue
    
    question = input("Press Enter continue or Input any symbol to exit :  ")
    
    if question == "":
        continue
    else:
        break 
        