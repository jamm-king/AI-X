with open("cat.jpg", "rb") as f_in, open("cat_copy.jpg", "wb") as f_out:
    data = f_in.read()
    f_out.write(data)
    
data_list = list(data)
data_int = list(map(int, data))
print(type(data_list[0]))
print(type(data_int[0]))