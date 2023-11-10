# 더하기 함수 
def add(x, y):
    if not (isinstance(x, int)) or not (isinstance(y, int)):
        raise ValueError("Error: Please use Integer")
    result = x + y
    return result

# 빼기 함수
def subtract(x, y):
      if (isinstance(x, int) and isinstance(y, int)):
          return x - y
      else:
          print("ERROR!")

# 곱하기 함수
def multiply(x, y):
    if not (isinstance(x, int)) or not (isinstance(y, int)):
        raise ValueError("Error: Please use Integer")
    result = x * y
    return result

# 예외 처리
def check_operator(operator):
    if operator not in ('+', '-', '*'):
        raise ValueError("Error: Invalid operator. Please use '+', '-', '*'")

# 메인 함수
def main():

    print("간단한 계산기 입니다. 더하기, 빼기, 곱하기만 가능합니다.")

    num1 = int(input())
    
    while True:
        operator = input()
        
        if operator == '=':
            print(num1)
            break
        
        check_operator(operator)  # 예외 처리

        num2 = int(input())

        if operator == '+':
            num1 = add(num1, num2)
        elif operator == '-':
            num1 = subtract(num1, num2)
        elif operator == '*':
            num1 = multiply(num1, num2)


if __name__ == "__main__":
    main()
