import os
from PIL import Image

def image_to_ascii(image_path, new_width=100):
    try:
        # 1. 이미지 열기
        img = Image.open(image_path)
    except Exception as e:
        print(f"이미지를 열 수 없습니다: {e}")
        return

    # 2. 이미지 크기 조절 (콘솔 화면에 맞게 저화질 축소)
    # 💡 팁: 콘솔의 글자 한 칸은 가로보다 세로가 더 깁니다. 
    # 비율 왜곡을 막기 위해 세로 길이를 축소할 때 0.55를 곱해 보정합니다.
    orig_width, orig_height = img.size
    aspect_ratio = orig_height / orig_width
    new_height = int(new_width * aspect_ratio * 0.55)
    img = img.resize((new_width, new_height))

    # 3. 이미지를 흑백(Grayscale) 모드로 변경
    # 픽셀값이 0(완전 어두움) ~ 255(완전 밝음) 사이의 숫자로 단순화됩니다.
    img = img.convert("L")

    # 4. 밝기별로 매핑할 텍스트 문자 배열 (왼쪽이 어두운 곳, 오른쪽이 밝은 곳)
    # 어두운 곳은 밀도가 높은 문자를, 밝은 곳은 공백에 가까운 문자를 배치합니다.
    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    num_chars = len(ASCII_CHARS)

    # 5. 픽셀 데이터를 문자열로 변환
    pixels = img.getdata()
    ascii_str = []
    
    for pixel in pixels:
        # 0~255 값을 ASCII_CHARS 인덱스(0~10) 범위로 변환
        char_index = pixel * (num_chars - 1) // 255
        ascii_str.append(ASCII_CHARS[char_index])
    
    # 리스트를 문자열로 합침
    ascii_str = "".join(ascii_str)

    # 6. 콘솔에 출력하기 위해 가로 너비(new_width) 단위로 줄바꿈 처리
    print("\n" + "="*new_width + "\n") # 구분선
    for i in range(0, len(ascii_str), new_width):
        print(ascii_str[i : i + new_width])
    print("\n" + "="*new_width + "\n")


if __name__ == "__main__":
    # ⚠️ 테스트해 볼 실제 이미지 파일 경로를 적어주세요.
    # 예: "my_photo.jpg" 또는 "test.png"
    print("Image Viewer Console 프로그램을 시작합니다.")
    while True:
        IMAGE_PATH = input("파일명을 입력해주세요(빈 칸 입력 시 종료): ") 
        
        if os.path.exists(IMAGE_PATH):
            # 콘솔 가로 너비에 맞게 조절 (기본값 100자 너비)
            image_to_ascii(IMAGE_PATH, new_width=200)
        elif IMAGE_PATH == "":
            print("프로그램을 종료합니다.")
            break
        else:
            print(f"'{IMAGE_PATH}' 파일이 존재하지 않습니다. 실제 이미지 경로로 수정해 주세요!")
