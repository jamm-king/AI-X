class StudentScore:
    
    def __init__(self, kor: int, eng: int, math: int):
        self.kor = kor
        self.eng = eng
        self.math = math
        
    def show_total(self) -> int:
        return self.kor + self.eng + self.math
        
    @property
    def kor(self) -> int:
        return self._kor
    
    @kor.setter
    def kor(self, value: int):
        if not isinstance(value, int):
            raise TypeError("'kor' must be integer")
        if value < 0 or value > 100:
            raise ValueError("'kor' must be between 0 and 100")
        self._kor = value
        
    @property
    def eng(self) -> int:
        return self._eng
    
    @eng.setter
    def eng(self, value: int):
        if not isinstance(value, int):
            raise TypeError("'eng' must be integer")
        if value < 0 or value > 100:
            raise ValueError("'eng' must be between 0 and 100")
        self._eng = value
            
    @property
    def math(self) -> int:
        return self._math
    
    @math.setter
    def math(self, value: int):
        if not isinstance(value, int):
            raise TypeError("'math' must be integer")
        if value < 0 or value > 100:
            raise ValueError("'math' must be between 0 and 100")
        self._math = value
        
if __name__ == '__main__':
    
    # case1: 정상 케이스
    
    # given
    kor = 80
    eng = 90
    math = 95
    
    # when
    score = StudentScore(kor, eng, math)

    # then
    assert score.kor == 80, f"국어 점수 저장 오류: {score.kor}"
    assert score.eng == 90, f"영어 점수 저장 오류: {score.eng}"
    assert score.math == 95, f"수학 점수 저장 오류: {score.math}"
    assert score.show_total() == 265, f"show_total() 오류: {score.show_total()}"

    # case 2: 점수에 잘못된 타입(문자열)을 넣었을 때 TypeError 검증
    
    # given
    valid_kor_type, invalid_kor_type = 80, "80"
    valid_eng_type, invalid_eng_type = 90, "90"
    valid_math_type, invalid_math_type = 95, "95"

    # when & then
    try:
        StudentScore(invalid_kor_type, valid_eng_type, valid_math_type)
        StudentScore(valid_kor_type, invalid_eng_type, valid_math_type)
        StudentScore(valid_kor_type, valid_eng_type, invalid_math_type)
        assert False, f"점수에 문자열을 넣었으나 TypeError가 발생하지 않았습니다."
    except TypeError as e:
        assert str(e).endswith("must be integer"), f"엉뚱한 에러 메시지: {e}"

    # case 3: 점수에 음수를 넣었을 때 ValueError 검증
    
    # given
    valid_kor_value, invalid_kor_value = 80, -80
    valid_eng_value, invalid_eng_value = 90, -90
    valid_math_value, invalid_math_value = 95, -95
    
    # when & then
    try:
        StudentScore(invalid_kor_value, valid_eng_value, valid_math_value)
        StudentScore(valid_kor_value, invalid_eng_value, valid_math_value)
        StudentScore(valid_kor_value, valid_eng_value, invalid_math_value)
        assert False, f"점수에 음수 넣었으나 ValueError가 발생하지 않았습니다."
    except ValueError as e:
        assert str(e).endswith("must be between 0 and 100"), f"엉뚱한 에러 메시지: {e}"
        
    print("테스트 통과")