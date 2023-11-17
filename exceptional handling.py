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
    raise ValueError("Error: Please use Integer")


# 곱하기 함수
def multiply(x, y):
  if not (isinstance(x, int)) or not (isinstance(y, int)):
    raise ValueError("Error: Please use Integer")
  result = x * y
  return result


# 예외 처리 - 연산자 확인
def check_operator(operator):
  if operator not in ('+', '-', '*'):
    return "Error: Invalid operator. Please use '+', '-', '*'"
  return None


# 예외 처리 - 정수 확인
def check_integer(value):
  try:
    int(value)
  except ValueError:
    return "Error: Please enter an Integer"
  return None


# 메인 함수
def main():
  print("간단한 계산기 입니다. 더하기, 빼기, 곱하기만 가능합니다.")

  try:
    num1 = input()

    while True:
      operator = input()
      num2 = input()

      if operator == '=':
        error_message_num1 = check_integer(num1)
        error_message_num2 = check_integer(num2) # 연산자 예외 처리
        error_message_operator = check_operator(operator)
        
        if error_message_num1:
          raise ValueError(error_message_num1)
        elif error_message_num2:
          raise ValueError(error_message_num2)
        elif error_message_operator:
          raise ValueError(error_message_operator)
        
        print(num1)
        break

      if operator == '+':
        num1 = add(num1, num2)
      elif operator == '-':
        num1 = subtract(num1, num2)
      elif operator == '*':
        num1 = multiply(num1, num2)

  except ValueError as e:
    print(f"Error: {e}")


if __name__ == "__main__":
  main()
