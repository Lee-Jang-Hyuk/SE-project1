#빼기 함수
def subtract(x, y):
    if (isinstance(x, int) and isinstance(y, int)):
        return x - y
    else:
        print("ERROR!")


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
        num2 = int(input())

        if operator == '+':
            num1 = add(num1, num2)
        elif operator == '-':
            num1 = subtract(num1, num2)
        elif operator == '*':
            num1 = multiply(num1, num2)


if __name__ == "__main__":
    main()
