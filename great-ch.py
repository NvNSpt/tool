import os
import shutil
import time



# Lấy đường dẫn tới tệp Python hiện tại (script đang thực thi)
current_script_path = os.path.abspath(__file__)
print("Đường dẫn tới tệp Python hiện tại là:", current_script_path)

chrome_path = current_script_path.replace("great-ch.py", "chrome\\")

# Chuyển thành sample
sample_path = current_script_path.replace("great-ch.py", "chrome\sample")



while True:
    name_network = input("nhập tên network cần tạo:")
    mint =input("nhập số ví mint:")
    claim =input("nhập số ví claim:")

    # Kiểm tra xem thư mục đã tồn tại hay chưa
    if os.path.exists(os.path.join(chrome_path, name_network)):
        print(f"Thư mục '{name_network}' đã tồn tại trong network.")
    else:
        # Đường dẫn của thư mục mới
        duong_dan_moi = os.path.join(chrome_path, name_network)

        # Tạo bản sao của thư mục sample và đổi tên thành network
        shutil.copytree(sample_path, duong_dan_moi)

        print(f"Thư mục sample đã được sao chép và đổi tên thành '{name_network}'")
        
        break


# Ghi thêm dữ liệu vào tệp tin
new_data = f"{name_network},{mint},{claim}"
with open("network.txt", "a") as file:
    file.write(new_data + "\n" )

print("Đã ghi dữ liệu mới vào tệp tin network.txt.")
time.sleep(3)