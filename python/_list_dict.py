# Nhập vào danh sách 5 số, in ra số lớn nhất và nhỏ nhất.
list_numbers = []
for i in range(5):
    number = int(input("Nhập số thứ {}: ".format(i + 1)))
    list_numbers.append(number)
max_number = max(list_numbers)
min_number = min(list_numbers)
print("Số lớn nhất là:", max_number)
print("Số nhỏ nhất là:", min_number)
#Tính tổng và trung bình của 1 danh sách số.
sum_numbers = sum(list_numbers)
average_numbers = sum_numbers / len(list_numbers)
print("Tổng của danh sách là:", sum_numbers)
print("Trung bình của danh sách là:", average_numbers)
#Đảo ngược 1 list mà không dùng hàm reverse()
reversed_list = []
for i in range(len(list_numbers) - 1, -1, -1):
    reversed_list.append(list_numbers[i])
print("Danh sách đảo ngược là:", reversed_list)
#Loại bỏ phần tử trùng trong list.
unique_list = []
for number in list_numbers:
    if number not in unique_list:
        unique_list.append(number)
print("Danh sách không trùng lặp là:", unique_list)