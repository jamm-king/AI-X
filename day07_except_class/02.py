def division_pipeline():
    try:
        a, b = get_integers()
        print_divide(a, b)
    except ValueError:
        print("잘못된 입력입니다. 정수를 입력해주세요.")
    except ZeroDivisionError:
        print("0 으로 나눌 수 없습니다.")

def get_integers():
    print_section_line()
    a = int(input("첫 번째 정수 입력: "))
    b = int(input("두 번째 정수 입력: "))
    
    return a, b

def print_divide(a, b):
    c = a / b
    print(f"{a} / {b} = {c}")
    
def print_section_line():
    print("----------------------------------------")
    
def print_start():
    print_section_line()
    print("나누기 프로그램을 시작합니다.")
    
def print_stop():
    print("나누기 프로그램을 종료합니다.")
    print_section_line()
    
def get_continue():
    a = input("계속하시겠습니까?(y/n)")
    a = a.lower()
    if a != 'y' and a != 'n':
        raise ValueError("'y' or 'n' is required.")
    return a

def app():
    print_start()
    cont = 'y'
    while cont == 'y':
        division_pipeline()
        while True:
            try:
                cont = get_continue()
                break
            except ValueError:
                print("'y' 혹은 'n'을 입력해 주세요.")
            
    print_stop()
    
if __name__ == '__main__':
    app()