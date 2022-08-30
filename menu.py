from SanPham import SP 
import os.path

file_exists = os.path.exists('Menu.txt')

ds = [] 

if file_exists:
    readfile = open("Menu.txt","r") #write mode
    Lines = readfile.readlines()

    count = 0

    for line in Lines:
        count += 1
        Id = line.split('.')[0]
        TenSP = line.split('.')[1].split('(')[0]
        DonGia = line.split('.')[1].split('(')[1].split(')')[0]
        sp = SP(Id, TenSP, DonGia)
        ds.append(sp)

    readfile.close()


while True:
    print(f'''\n
    0. Thoát Chương trình
    1. Thêm Mới Các Sản Phẩm Vào Menu
    2. Cập Nhật Thông Tin Sản Phẩm
    3. Xóa Sản Phẩm
    4. Xem Thông Tin Tất Cả Sản Phẩm 
    5. Lưu Thông Tin Menu Ra File
    6. Mua Hàng
    ''')

    select = input("Mời chọn chức năng:  ")
    if str(select).isdigit():
        select = int(select)
        if select == 0:
            break
        elif select == 1:
            Id = input("Nhập Vào Id: ")
            while(str(Id).isdigit() != True):
                print("\nBạn phải nhập số. Vui Lòng nhập lại !")
                Id = input("Nhập Vào Id: ")
            
            for i in ds:
                while(i.get_Id() == Id):
                    print("\n Id này đã tồn tại!! Vui lòng nhập số khác số : ", Id)
                    Id = input("Nhập Vào Id: ")

            TenSP = input("Nhập Tên Sản Phẩm: ")

            for i in ds:
                while(i.get_TenSP() == TenSP):
                    print("\n Sản Phẩm này đã tồn tại!! Vui lòng nhập tên khác: ", TenSP)
                    TenSP = input("Nhập Tên Sản Phẩm: ")

            DonGia = input("Nhập Giá Sản Phẩm: ")
            while(str(DonGia).isdigit() != True):
                print("\nBạn phải nhập số. Vui Lòng nhập lại !")
                DonGia = input("Nhập Giá Sản Phẩm: ")
            sp = SP(Id , TenSP , DonGia)
            ds.append(sp)

        elif select == 2:
            id = input("Nhập Id sản phẩm cần sửa :  ")
            while(str(id).isdigit() != True):
                print("\nBạn phải nhập số. Vui Lòng nhập lại !")
                id = input("Nhập Id sản phẩm cần sửa : ")

            for i in ds:
                if i.get_Id() == id:
                    TenSP = input("Nhập Tên Sản Phẩm Mới: ")
                    for i in ds:
                        while(i.get_TenSP() == TenSP):
                            print("\n Sản Phẩm này đã tồn tại!! Vui lòng nhập tên khác: ", TenSP)
                            TenSP = input("Nhập Tên Sản Phẩm Mới: ")
                    i.set_TenSP(TenSP)
                    DonGia = input("Nhập Giá Sản Phẩm: ")
                    while(str(DonGia).isdigit() != True):
                        print("\nBạn phải nhập số. Vui Lòng nhập lại !")
                        DonGia = input("Nhập Giá Sản Phẩm Mới: ")
                    i.set_DonGia(DonGia)
                    i.show_SP()

        elif select == 3:
            id = input("Nhập Id sản phẩm cần xóa:  ")
            while(str(id).isdigit() != True):
                print("\nBạn phải nhập số. Vui Lòng nhập lại !")
                id = input("Nhập Id sản phẩm cần sửa : ")
            for i in ds:
                if i.get_Id() == id:
                    ds.remove(i)
                    print("Bạn đã Sản Phẩm thành công ")
                    continue

        elif select == 4:
            if len(ds) == 0:
                print("\n Hiện Danh Mục Sản Phẩm Đang Trống . Bạn Vui Lòng Thêm Mới Vào Danh Sách!")
            else:
                print(f"\n     Menu : ")
                for i in ds:
                    i.show_SP()
                print(f"\n -------------------------------------------")
        
        elif select == 5:
            file = open("Menu.txt","w") #write mode   
            for i in ds:     
                file.write(i.get_Id() + "." + i.get_TenSP() + "(" + i.get_DonGia() + ")")
                file.write("\n") 
            print("Lưu Thông Tin Menu ra File Success")
            file.close()

        elif select == 6:
           TongTien = 0
           while(True):
                print("Hãy Chọn Dịch Vụ Muốn Sử Dụng")
                print("1. Để Mua Hàng")
                print("2. Để Thanh Toán")
                print("0. Để Kết Thúc")

                choose = input("Hãy Nhập Lựa Chọn Của Bạn : ")
                
                match choose:
                    case "1":
                        file = open("HoaDon.txt","w")#write mode
                        file.write("Hóa Đơn Của Bạn Bao Gồm: ")
                        file.write("\n") 

                        print("Cửa hàng Xin Kính Chào Quý Khách")
                        print("Để chọn Sản Phẩm Quý Khách Hãy Lựa Chọn Theo Số Thứ Tự Bên Dưới")
                        print(f"\n     Menu : ")
                        for i in ds:
                            i.show_SP()
                            
                        print(f"\n -------------------------------------------")

                        print("Xin Mời Quý Khách Chọn Sản Phẩm")
                        print("Quý Khách Có Thể Nhập 0 Để Kết Thúc Đặt Hàng ")
                        count = 1
                        while(1):
                            Id_SanPham = input("Sản Phẩm " + str(count) +" :")
                            
                            while(str(Id_SanPham).isdigit() != True):
                                print("\nBạn phải nhập số. Vui Lòng nhập lại !")
                                Id_SanPham = input("Nhập lại sản phẩm ", count, " :")

                            if Id_SanPham == "0":
                                break
                            SoLuong = input("Nhập Vào Số Lượng: ")

                            for i in ds:
                                if i.get_Id() == Id_SanPham:
                                    file.write(SoLuong + " " + i.get_TenSP() + "(" + i.get_DonGia() + ")")
                                    file.write("\n")  
                                    TongTien = TongTien + int(SoLuong) * int(i.get_DonGia()) 
                            count = count + 1
                        print("Tổng Hóa Đơn Của Bạn Là: ", TongTien)
                        file.write("\n")  
                        file.write("Tổng Hóa Đơn Hết: " + str(TongTien) + " VND") 
                        file.close()

                    case "2":
                        print("Tổng Hóa Đơn Của Bạn Là: ", TongTien)

                    case "0":
                        break
           
    else:
        print("\nBạn phải nhập số. Vui Lòng nhập lại !")