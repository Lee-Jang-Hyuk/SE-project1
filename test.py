# 곱셈 함수 정의
def multiply(a, b):
    result = a * b
    return result

# main 함수
def main():
    # 사용자로부터 두 숫자를 입력 받습니다
    num1 = float(input())
    num2 = float(input())

    # multiply 함수를 호출하여 두 숫자를 곱하고 결과를 출력합니다
    product = multiply(num1, num2)
    print(product)

if __name__ == "__main__":
    main()
