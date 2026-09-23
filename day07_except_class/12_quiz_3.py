"""
3. 원본파일명과 복사본 파일명을 입력받아 복사하는 프로그램을 작성해 보세요
( 모든 파일형태가 다 복사되도록 해보세요 )
"""

src_path = input("원본 파일명: ")
copy_path = input("복사본 파일명: ")

with open(src_path, "rb") as f_in, open(copy_path, "wb") as f_out:
    data = f_in.read()
    f_out.write(data)