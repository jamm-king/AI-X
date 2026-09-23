def add(a: int | float, b: int | float) -> int | float:
    return a + b

def sub(a: int | float, b: int | float) -> int | float:
    return a - b

pi = 3.14159

if __name__ == '__main__':
    print("mymath 모듈 작성")
    print("mymath 모듈에서 호출 =>", add(1, 2))