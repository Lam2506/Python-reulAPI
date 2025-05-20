# Viết hàm tính tổng các số lẻ trong list.
def sum_odd_numbers(numbers):
    total = 0
    for number in numbers:
        if number % 2 != 0:
            total += number
    return total     
#Viết hàm tính tổng các số chẵn trong list.
def sum_even_numbers(numbers):
    totol = 0
    for number in numbers:
        if number % 2 == 0:
            totol += number
    return totol
#goi hàm
numbers = [1, 2, 3, 4, 5]   
print("Tổng các số lẻ trong danh sách là:", sum_odd_numbers(numbers))
print("Tổng các số chẵn trong danh sách là:", sum_even_numbers(numbers))
# Viết hàm kiểm tra số nguyên tố.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n*0.5) + 1):
        if n % i == 0:
            return False
    return True


# Viết hàm nhận vào chuỗi, trả về chuỗi viết ngược.
def reverse_string(s):
    return s[::-1]
# Viết chương trình sử dụng hàm tính điểm trung bình của 3 môn và xếp loại học lực:
# Giỏi >= 8, Khá >= 6.5, Trung bình >= 5 ,Yếu < 5
def calculate_average_score(subject1, subject2, subject3):
    average_score = (subject1 + subject2 + subject3) / 3
    if average_score >= 8:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5:
        return "Trung bình"
    else:
        return "Yếu"
# Nhập điểm 3 môn

