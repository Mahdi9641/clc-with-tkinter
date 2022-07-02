

def isOperator(c):
    if c != "": return (c in "+-*/")
    else: return False

def checkPriority(c):
    if c in "+-": return 0
    if c in "*/": return 1
    
def isNumber(c):
    if c != "": return (c in "0123456789.")
    else: return False

def runOperator(op, number1, number2):
    if op == "+": return str(float(number1) + float(number2))
    if op == "-": return str(float(number1) - float(number2))
    if op == "*": return str(float(number1) * float(number2))
    if op == "/": return str(float(number1) / float(number2))

def Calculation(expr):
    expr = list(expr)
    stack_operation = list()   #for operations
    stack_number = list()   #for numbers
    num = ""
    while len(expr) > 0:
        c = expr.pop(0)
        if len(expr) > 0: d = expr[0]
        else: d = ""
        if isNumber(c):
            num += c
            if not isNumber(d):
                stack_number.append(num)
                num = ""
        elif isOperator(c):
            while True:
                if len(stack_operation) > 0: top = stack_operation[-1]
                else: top = ""
                if isOperator(top):
                    if not checkPriority(c) > checkPriority(top):
                        number2 = stack_number.pop()
                        op = stack_operation.pop()
                        number1 = stack_number.pop()
                        stack_number.append(runOperator(op, number1, number2))
                    else:
                        stack_operation.append(c)
                        break
                else:
                    stack_operation.append(c)
                    break
        elif c == "(":
            stack_operation.append(c)
        elif c == ")":
            while len(stack_operation) > 0:
                c = stack_operation.pop()
                if c == "(":
                    break
                elif isOperator(c):
                    number2 = stack_number.pop()
                    number1 = stack_number.pop()
                    stack_number.append(runOperator(c, number1, number2))

    while len(stack_operation) > 0:
        c = stack_operation.pop()
        if c == "(":
            break
        elif isOperator(c):
            number2 = stack_number.pop()
            number1 = stack_number.pop()
            stack_number.append(runOperator(c, number1, number2))

    return stack_number.pop()