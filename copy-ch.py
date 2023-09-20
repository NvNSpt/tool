import os
import shutil
import time

while True:
    # Tạo thông báo nhập dữ liệu theo network
    check_network = "Nhập số để chọn mạng: "
    network = open('network.txt', mode='r')
    all_file = network.readlines()
    line_number = 0

    for line in all_file:
        tach_hang = line.strip().split(',')
        path = tach_hang[0]
        input_string = f"{line_number}({path}), "
        check_network += input_string
        line_number += 1

    network.close()

    print(check_network)

    #tạo ô để nhập network
    while True:
        try:
            ob = int(input("Nhập mạng cần copy: "))
            network = open('network.txt', mode='r')
            all_file = network.readlines()

            if 0 <= ob < len(all_file):
                line = all_file[ob]
                tach_hang = line.strip().split(',')
                path, mint, claim = tach_hang[0], tach_hang[1], tach_hang[2]
                print("Path:", path)
                print("Mint:", mint)
                print("Claim:", claim)
                break
            else:
                print("Nhập mạng không hợp lệ. Vui lòng nhập lại.")
        except ValueError:
            print("Nhập mạng không hợp lệ. Vui lòng nhập lại.")
    network.close()

    # Lấy đường dẫn tới tệp Python hiện tại (script đang thực thi)
    current_script_path = os.path.abspath(__file__)

    chrome_path = current_script_path.replace("copy-ch.py", "chrome\\")

    # Chuyển thành file cần copy
    sample_path = current_script_path.replace("copy-ch.py", "chrome\\" + path)

    while True:
        name_network = input("Nhập tên network cần tạo:")
        mint = input("Nhập số ví mint:")
        claim = input("Nhập số ví claim:")

        # Kiểm tra xem thư mục đã tồn tại hay chưa
        if os.path.exists(os.path.join(chrome_path, name_network)):
            print(f"Thư mục '{name_network}' đã tồn tại trong network.")
        else:
            # Đường dẫn của thư mục chưa network mới
            duong_dan_moi = os.path.join(chrome_path, name_network)

            # Tạo bản sao của thư mục sample và đổi tên thành network
            shutil.copytree(sample_path, duong_dan_moi)

            print(f"Thư mục {path} đã được sao chép và đổi tên thành '{name_network}'")

            break

    # Ghi thêm dữ liệu vào tệp tin
    new_data = f"{name_network},{mint},{claim}"
    with open("network.txt", "a") as file:
        file.write(new_data + "\n")

    print("Đã ghi dữ liệu mới vào tệp tin network.txt.")
    
    choice = input("Bạn có muốn copy tiếp không? (y/n): ")
    if choice.lower() != 'y':
        break
    time.sleep(3)
