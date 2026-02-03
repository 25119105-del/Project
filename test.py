import math
print('hello python')
def Phep_cong():
    a = 1 
    b = 2
    c= a + b
    return c
khoa = Phep_cong()
#cách 1 - thông dụng nhất
print(f"Giá trị của hàm phép cộng là {khoa}")
#cách 2 
print("Giá trị của hàm phép cộng là {}".format(khoa))
#cách 3
print("Giá trị của hàm phép cộng là %d" % khoa)
#cách 4
print("Giá trị của hàm phép cộng là", khoa)

k = 9.5
if k>=9: 
    print('Xuất sắc')
elif k >= 8:
    print('Giỏi')
elif k >= 7:
    print('Khá')
elif k >= 5:
    print('Trung bình')
else: print('Yếu/Kém')
for i in range(5):
    print(f'Nguyễn Vũ Tấn Khoa ')
