name = "Le Tùng Lâm"
age = 20
hobby = "Học lập trình"
diem = 8.5
print("Điểm của tôi là", diem)
print("Tên tôi là", name, "tuổi", age, "tuổi và sở thích của tôi là", hobby) 
# Tính chu vi và diện tích hình chữ nhật
chieudai = input("Nhập chiều dài: ")
chieungang = input("Nhập chiều rộng: ")
chuvi = 2 * (int(chieudai) + int(chieungang))
dientich = int(chieudai) * int(chieungang)
print("Chu vi hình chữ nhật là:", chuvi)
print("Diện tích hình chữ nhật là:", dientich)
# Tính chu vi và diện tích hình tròn
# Nhập bán kính hình tròn
ban_kinh = input("Nhập bán kính hình tròn: ")   
# Tính chu vi hình tròn
chuvi_hinh_tron = 2 * 3.14 * float(ban_kinh)
# Tính diện tích hình tròn
dientich_hinh_tron = 3.14 * float(ban_kinh) * 2   
print("Chu vi hình tròn là:", chuvi_hinh_tron)
print("Diện tích hình tròn là:", dientich_hinh_tron)