# Exception을 상속받아 사용자 정의 예외 처리 클래스를 만들 수 있다.
class AgeError(Exception):
    pass

try:
    age = int(input("나이 입력: "))
    if age < 0 or age > 150:
        details = {
            "age": age
        }
        raise AgeError("나이가 유효하지 않습니다", details)
    print("당신의 나이 ==>", age)
except AgeError as e:
    print(f"[{e.__class__.__name__}] {e.args[0]}: {e.args[1]}")