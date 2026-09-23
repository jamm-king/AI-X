class Student:
    
    def __init__(
        self,
        name:str,
        score_kor: int,
        score_math: int
    ):
        self.name = name
        self.score_kor = score_kor
        self.score_math = score_math
        
    def __str__(self):
        return f"{self.name},{self.score_kor},{self.score_math}"
    
    def to_string(self) -> str:
        return self.__str__()
    
    @classmethod
    def from_string(cls, line: str):
        name, kor, math = line.split(",")
        return cls(name, int(kor), int(math))
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("'name' must be string")
        self._name = value
        
    @property
    def score_kor(self) -> int:
        return self._score_kor
    
    @score_kor.setter
    def score_kor(self, value: int):
        if not isinstance(value, int):
            raise TypeError("'score_kor' must be integer")
        if value < 0 or value > 100:
            raise ValueError("'score_kor' must be between 0 and 100")
        self._score_kor = value
        
    @property
    def score_math(self) -> int:
        return self._score_math
    
    @score_math.setter
    def score_math(self, value: int):
        if not isinstance(value, int):
            raise TypeError("'score_math' must be integer")
        if value < 0 or value > 100:
            raise ValueError("'score_math' must be between 0 and 100")
        self._score_math = value
        
    @property
    def score_total(self) -> int:
        return self.score_kor + self.score_math
    
    @property
    def score_avg(self) -> int:
        return self.total / 2