import json
import os

# đường dẫn đến file JSON
file_name = "students.json"

# hàm ghi dữ liệu vào file JSON
def save_data(data):
    with open(file_name, "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
# hàm đọc dữ liệu từ file JSON
def load_data():
    if os.path.exists(file_name):
        with open(file_name, "r", encoding='utf-8') as file:
            return json.load(file)
    return []
# hàm thêm sinh viên mới
def add_student(students):
    students = load_data()
    student_id = input("Nhập mã sinh viên: ")
    #kiem tra mã sinh viên đã tồn tại hay chưa
    for student in students:
        if student["id"] == student_id:
            print("Mã sinh viên đã tồn tại. Vui lòng nhập mã khác.")
            return
    name = input("Nhập tên sinh viên: ")
    age = int(input("Nhập tuổi sinh viên: "))
    student = {"id": student_id, "name": name, "age": age}
    students.append(student)
    save_data(students)
    print("Thêm sinh viên thành công!")
# hàm hiển thị danh sách sinh viên
def display_students():
    students = load_data()
    if not students:
        print("Danh sách sinh viên trống.")
        return
    print("Danh sách sinh viên:")
    for student in students:
        print(f"Mã sinh viên: {student['id']}, Tên: {student['name']}, Tuổi: {student['age']}")
# menu chính
def main():
    while True:
        print("1. Thêm sinh viên")
        print("2. Hiển thị danh sách sinh viên")
        print("3. Thoát")
        choice = input("Chọn chức năng: ")
        if choice == "1":
            add_student(load_data())
        elif choice == "2":
            display_students()
        elif choice == "3":
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
# chạy chương trình
if __name__ == "__main__":
    main()