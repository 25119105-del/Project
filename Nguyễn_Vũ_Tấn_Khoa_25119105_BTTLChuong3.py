#Tính giá trị biểu thức 1/(1/3)+(1/5)+...+(1/99)
tong_mau1 = 0.0
S1= 0.0
for i in range(3,100,2):
    mau = 1/(i)
    tong_mau1 += mau
S1 = 1/tong_mau1
print(f'Tổng mẫu là: {tong_mau1}')
print(f'Giá trị biểu thức S1: {S1}')
print('-'*40)
#Tính giá trị biểu thức 1/(1/3**3)+(1/5**5)+...+(1/99**99)
tong_mau2 = 0.0
S2= 0.0
for i in range(3,100,2):
    mau = 1/(i**i)
    tong_mau2 += mau
S2 = 1/tong_mau2
print(f'Tổng mẫu là: {tong_mau2}')
print(f'Giá trị biểu thức S2: {S2}')
print('-'*40)
#Tính giá trị biểu thức 1/(1/3**2)+(1/5**4)+....+(1/99**98)
tong_mau3 = 0.0
S3=0.0
for i in range(3,100,2):
    mau = 1/(i**(i-1))
    tong_mau3 += mau   
S3 = 1/tong_mau3
print(f'Tổng mẫu là: {tong_mau3}')
print(f'Giá trị biểu thức S3: {S3}')
print('-'*40)
