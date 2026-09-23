class ConsoleIO:
    
    @classmethod
    def console_in(cls, data_class):
        data = {}
        for key in data_class.__dict__:
            data[key] = input(f"{key}: ")
            
        return data_class(**data)
    
    
    @classmethod
    def console_out(cls, data):
        print(str(data))