class FileIO:
    
    @classmethod
    def read_file(cls, file_path: str) -> list:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = f.read()
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(e)
        else:
            return data
    
    @classmethod
    def write_file(cls, file_path: str, data: str):
        if not isinstance(data, str):
            raise TypeError("'data' must be string")
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(data)
        except Exception as e:
            print(e)        
