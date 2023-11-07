def multiply(x, y):
    if not (isinstance(x, int)) or not (isinstance(y, int)):
        raise ValueError("Error: Please use Integer")
    result = x * y
    return result

# 메인 함수
def main():  
    
    num1 = input("간단한 계산기 입니다. 더하기, 빼기, 곱하기만 가능합니다.")
    if num1 = ' ':#이스터에그
    
    operator = input
    num2 = input
            
    num1, num2 = get_numbers()
    
    if operator == '+':
        print("결과: ", add(num1, num2))
    elif operator == '-':
        print("결과: ", subtract(num1, num2))
    elif operator == '*':
        print("결과: ", multiply(num1, num2))
    

if __name__ == "__main__":
    main()