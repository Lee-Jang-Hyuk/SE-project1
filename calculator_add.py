# 더하기 함수
def add(x, y):
    if not (isinstance(x, int)) or not (isinstance(y, int)):
        raise ValueError("Error: Please use Integer")
    result = x + y
    return result

# 입력값이 정수인지 확인하고 정수가 아니면 예외를 발생시키는 함수
def get_integer_input():
    while True:
        try:
            value = int(input())
            return value
        except ValueError:
            print("Error: Please enter an integer.")

# 메인 함수
def main():

    print("간단한 계산기 입니다. 더하기, 빼기, 곱하기만 가능합니다.")

    num1 = int(input())
    # 이스터에그
    while True:
        operator = input()
        if operator == '=':
            print(num1)
            break

        num2 = get_integer_input() //변경된 부분

        if operator == '+':
            num1 = add(num1, num2)
            elif operator == '-':
            num1 = subtract(num1, num2)
        elif operator == '*':
            num1 = multiply(num1, num2)
        else:
            print("잘못된 연산자입니다. 더하기(+), 빼기(-), 곱하기(*)만 가능합니다.")


if __name__ == "__main__":
    main()
