from random import choice
from random import randint
# C1
# from Evaluate import calculation
# C2:
import Evaluate

x_variable = randint(1, 10)
y_variable = randint(1, 10)
operation_list = ["+" , "-" , "*", "/"]
operation_choice = choice(operation_list)
error_list = [-1, 1, 0]
error_choice = choice(error_list)

# C1
# correct_result = calculation(x_variable,y_variable,operation_choice)
# C2
correct_result = Evaluate.calculation(x_variable,y_variable,operation_choice)

if operation_choice == "+":
    give_result = x_variable + y_variable + error_choice
    # correct_result =  x_variable + y_variable 
elif operation_choice == "-":
    give_result = x_variable - y_variable + error_choice
    # correct_result =  x_variable - y_variable 
elif operation_choice == "*":
    give_result = x_variable * y_variable + error_choice
    # correct_result =  x_variable * y_variable 
elif operation_choice == "/":
    give_result = x_variable / y_variable + error_choice
    # correct_result =  x_variable / y_variable 
    
player_response = input("{0} {1} {2} = {3} Y/N".format(x_variable,operation_choice,y_variable,give_result)).upper()

if error_choice == 0:
    if player_response == "Y":
        pass
    elif player_response == "N":
        print("You are wrong")
        # break
elif error_choice != 0:
    if player_response == "Y":
        print("You are wrong")
    elif player_response == "N":
        pass

    
