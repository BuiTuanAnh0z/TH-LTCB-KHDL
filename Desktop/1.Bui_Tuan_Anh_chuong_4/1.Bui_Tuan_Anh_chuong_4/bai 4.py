tu_so = int(input("Nhập tử số: "))
while True:
    mau_so = int(input("Nhập mẫu số: "))
    if mau_so != 0:
        break
    print("Mẫu số không được bằng 0. Vui lòng nhập lại.")

# Xuất phân số
print("Phân số:", tu_so, "/", mau_so)
