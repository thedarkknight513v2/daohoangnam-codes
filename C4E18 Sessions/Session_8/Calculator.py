x_variable = int(input("x"))
operation_variable = input("Operation (+, -, *, /)")
y_variable = int(input("y"))

if operation_variable == "+":
    result = x_variable + y_variable
elif operation_variable == "-":
    result = x_variable - y_variable
elif operation_variable == "/":
    result = x_variable / y_variable
elif operation_variable == "*":
    result = x_variable * y_variable
     
print("{0} {1} {2} = {3}".format(x_variable, operation_variable, y_variable,result))
        
    
    
