#In các số từ 1 đến 100 chia hết cho 3 và 5.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
#In bảng cửu chương từ 2 đến 9.
for i in range(2, 10):
    print("Bảng cửu chương số", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()
#Tạo hình tam giác sao
for i in range(1, 10):
    print("*" * i)