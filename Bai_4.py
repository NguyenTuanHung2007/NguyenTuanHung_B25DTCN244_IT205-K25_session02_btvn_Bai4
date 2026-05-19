age = int(input("Nhap tuoi: "))
sbp = int(input("Nhap huyet ap tam thu: "))
blood_sugar = int(input("Nhap duong huyet: "))

if age < 0 or sbp < 0 or blood_sugar < 0:
    print("Dữ liệu không hợp lệ")
else:
    if age < 75 and 90 <= sbp <= 140 and blood_sugar < 150:
        print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT")
    else:
        print("TỪ CHỐI PHẪU THUẬT")