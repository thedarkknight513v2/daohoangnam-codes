from random import *

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x_variable = randint(1, 10)
    y_variable = randint(1, 10)
    operation_list = ["+" , "-" , "*", "/"]
    operation_choice = choice(operation_list)
    error_list = [-1, 1, 0]
    error_choice = choice(error_list)

    if operation_choice == "+":
        give_result = x_variable + y_variable + error_choice
        correct_result =  x_variable + y_variable 
    elif operation_choice == "-":
        give_result = x_variable - y_variable + error_choice
        correct_result =  x_variable - y_variable 
    elif operation_choice == "*":
        give_result = x_variable * y_variable + error_choice
        correct_result =  x_variable * y_variable 
    elif operation_choice == "/":
        give_result = x_variable / y_variable + error_choice
        correct_result =  x_variable / y_variable 
        
    return [x_variable, y_variable, operation_choice, give_result]

def check_answer(x_variable, y_variable, operation_choice, give_result, player_response):
    
    correct_or_not = True
    if x_variable + y_variable == give_result:
        if player_response == "Y":
            correct_or_not = True
        elif player_response == "N":
            correct_or_not = False
    elif x_variable + y_variable != give_result:
        if player_response == "Y":
            correct_or_not = False
        elif player_response == "N":
            correct_or_not = True
            
    return correct_or_not
