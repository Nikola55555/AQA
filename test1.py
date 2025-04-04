# input_str = "AAXXXCC"
 
# def foo(input_str):
#     exit_str = {}
#     for i in input_str:
#         if i in exit_str:
#             exit_str[i] = 
        
   
   



# # res_str = "2A3X2C"

# Senior Pomidorov
# 20:11
# x = {1,2,3}
# y = {3, 4, 5}
# print(x ^ y)
# Senior Pomidorov
# 20:12
# def foo(x=[])
#     x.append(1)
#     return x

# print(foo())
# print(foo())
# print(foo())
# Senior Pomidorov
# 20:26
# input_str = "AAXXXCC"
# res_str = "2A3X2C"

def get_time(func):
    def wrapper():
        a = time.time()
        func()
        b = time.time() 
        return b - a
    return wrapper