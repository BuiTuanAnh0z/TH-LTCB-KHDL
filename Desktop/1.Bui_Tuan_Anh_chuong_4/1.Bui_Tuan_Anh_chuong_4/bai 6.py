so_bang_chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
so = input("Nhập một số: ")
i = 0
while so[i:]:
    print(so_bang_chu[int(so[i])], end=" ")
    i += 1 
