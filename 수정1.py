# 더하기 함수 
def add(x, y):
      if (isinstance(x, int) and isinstance(y, int)):
          return x + y
      else:
          print("ERROR!: 정수가 아닙니다.")

# 빼기 함수 
def subtract(x, y):
      if (isinstance(x, int) and isinstance(y, int)):
          return x - y
      else:
          print("ERROR!: 정수가 아닙니다.")

# 곱하기 함수
def multiply(x, y):
      if (isinstance(x, int) and isinstance(y, int)):
          return x * y
      else:
          print("ERROR!: 정수가 아닙니다.")

# 연산자 확인
def check_operator(operator):
    if operator not in ('+', '-', '*'):
        raise ValueError("ERROR!: 더하기, 빼기, 곱하기만 가능합니다.")

"""
def check_integer(value):
    try:
        int(value)
    except ValueError:
        raise ValueError("Error: Please enter an Integer")
"""

# 메인 함수
def main():

    print("간단한 계산기 입니다. 더하기, 빼기, 곱하기만 가능합니다.")

    num1 = int(input())
    
    while True:
        operator = input()
        
        if operator == '=':
            print(num1)
            break

        num2 = int(input())

        if operator == '+':
            num1 = add(num1, num2)
        elif operator == '-':
            num1 = subtract(num1, num2)
        elif operator == '*':
            num1 = multiply(num1, num2)

if __name__ == "__main__":
    main()