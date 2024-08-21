a, b = 0, 1 #gán giá trị với a = 0 ( số đầu của dãy fibonacci) và b = 1 (số thứ 2 của dãy ) 
while a < 10: 
    print(a)
    a,b = b, a+b 
#  dùng vòng lặp while với điều kiện a < 10, trong vòng lặp cập nhật giá trị của a và b.
# Với a nhận giá trị của b và b nhận giá trị của tổng 2 số trước ( a+b )


#  Hàm print()
i = 255*255
print('Gia Tri Cua i la: ', i) #hoạt động tương tự C++


#Mở rộng điều kiện của hàm lặp.

c,d = 0, 1
while c < 1000:
    print(c,end=',') #In ra c với dấu , mỗi khi in 1 giá trị
    c,d = d, c+d 



