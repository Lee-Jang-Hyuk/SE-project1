def multiply(x, y):
    if not (isinstance(x, int)) or not (isinstance(y, int)):
        raise ValueError("Error: Please use Integer")
    result = x * y
    return result

def main():
    a = int(input())
    b = int(input())
    result1 = multiply(a,b)
    print(result1)

if __name__ == "__main__":
        main()