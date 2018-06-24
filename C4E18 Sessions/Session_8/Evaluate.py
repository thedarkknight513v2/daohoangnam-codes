from random import choice

def calculation(x_variable, y_variable,operation_choice):
    # operation_choice = choice(["+", "-", "*", "/"])
    # x_variable =3
    # y_variable = 7
    correct_result =0

    if operation_choice == "+":
        # give_result = x_variable + y_variable + error_choice
        correct_result =  x_variable + y_variable 
    elif operation_choice == "-":
        # give_result = x_variable - y_variable + error_choice
        correct_result =  x_variable - y_variable 
    elif operation_choice == "*":
        # give_result = x_variable * y_variable + error_choice
        correct_result =  x_variable * y_variable 
    elif operation_choice == "/":
        # give_result = x_variable / y_variable + error_choice
        correct_result =  x_variable / y_variable 

    return correct_result

# print("Hello world")
# # print(correct_result)
# result = calculation(1,2,"+")
# print(result)