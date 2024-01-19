def value():    
    return float(input("Numero: "))
    
def operator():
    valid_ope = ["+","-","*","/","="]
    ope = input("Operação: [+, -, *, / ou =]")
    if ope not in valid_ope:
        print("Operação inválida!")        
    return ope

def calc(value1, operator, value2):
    res = 0.0
    if operator == "+":
        res = value1 + value2
    elif operator == "-":
        res = value1 - value2
    elif operator == "*":
        res = value1 * value2
    elif operator == "/":
        res = value1 / value2
    else:
        print("Operação inválida!")
    return res

def calculator():
    dic ={}
    while True:
        new_value = value()
        ope = operator()
        res = calc(dic["value1"], dic["operator"], new_value) if len(dic) > 1 else new_value 

        if ope == "=":
            print("Resultado: ", res)
            break
        else:
            dic["value1"] = res
            dic["operator"] = ope
            
if __name__ == "__main__":
    print("************** CALCULATOR *****************")
    calculator()
