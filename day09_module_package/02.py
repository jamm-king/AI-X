"""
문자열이 5자에서 10자 사이면 True 아니면 False를 반환하는 함수를 모듈 파일로 만들어보세요.
strcheck.py

해당 모듈을 불러와서 사용해보세요
"""

from strcheck import is_5_to_10

user_id = "hello1234"
print(f'5 <= len("{user_id}") <= 10  ~>  {is_5_to_10(user_id)}')