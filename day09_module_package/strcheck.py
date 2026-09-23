def is_5_to_10(string: str) -> bool:
    if len(string) >= 5 and len(string) <= 10:
        return True
    else:
        return False
    
if __name__ == '__main__':
    str1 = "hello"
    str2 = "hi"
    print(f'is_5_to_10("{str1}")  ~>  {is_5_to_10(str1)}')
    print(f'is_5_to_10("{str2}")  ~>  {is_5_to_10(str2)}')
