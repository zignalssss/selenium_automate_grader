from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import os

def readfile():
    with open('your_csv_file', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
        return data

def get_files_from_folder(id, folder_name):
    folder_path = f'path_to_folder/{id}/{folder_name}'
    files = []
    if os.path.exists(folder_path):
        # ค้นหาไฟล์ .cpp ในโฟลเดอร์
        for filename in os.listdir(folder_path):
            if filename.endswith('.cpp'):
                files.append(os.path.join(folder_path, filename))
    return files

def logout_and_login():
    # ออกจากระบบ
    try:
        logout_button = driver.find_element(By.XPATH, 'website_XPATH')  # ปรับ XPath ให้ตรงกับปุ่ม Logout
        logout_button.click()
        time.sleep(2)  # รอให้แน่ใจว่าล็อกเอาต์เสร็จสิ้น

        # กลับไปที่หน้าล็อกอิน
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'username'))  # รอให้ฟอร์ม Username ปรากฏ
        )
        print("กลับไปที่หน้าล็อกอินแล้ว")

    except Exception as e:
        print(f"เกิดข้อผิดพลาดระหว่างการออกจากระบบ: {e}")

# ตั้งค่า EdgeDriver
edge_options = Options()
edge_options.use_chromium = True  # ใช้ Chromium-based Edge
edge_options.add_experimental_option("detach",True)
# กำหนด path ของ msedgedriver.exe
driver_path = r"path_webdriver"  # ปรับ path ให้ตรงกับที่คุณดาวน์โหลด WebDriver
service = Service(driver_path)

# เปิด Edge browser
driver = webdriver.Edge(service=service, options=edge_options)
driver.get('your_website_link')  # URL ของเว็บไซต์ 

students = readfile()  # อ่านข้อมูลจากไฟล์ CSV
count = 1
for student in students:
    id = student['id']  # แก้ไขตามชื่อคอลัมน์ในไฟล์ CSV
    password_id = student['password']
    print(f"คนที่{count} กำลังอัปโหลดไฟล์สำหรับนักเรียน: {id}")

    try:
        # ล็อกอิน
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'username'))  # รอให้ฟอร์ม Username ปรากฏ
        )

        username = driver.find_element(By.ID, 'username')
        password = driver.find_element(By.ID, 'password')

        username.send_keys(id)  # ใส่ id สำหรับล็อกอิน
        password.send_keys(password_id)  # รหัสผ่าน
        password.send_keys(Keys.RETURN)  # กด Enter เพื่อล็อกอิน

        # รอจนกระทั่งลิงก์ไปยังหน้าส่งปรากฏ
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, 'website_XPATH'))  # รอให้แท็ก <a> ปรากฏ
        )

        # คลิกที่ลิงก์ที่ต้องการไปยังหน้าส่ง
        submit_link = driver.find_element(By.XPATH, 'website_XPATH')
        submit_link.click()

        # รอจนกระทั่งหน้าส่งโหลด
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'website_element_id'))  # รอจนกระทั่งปุ่มอัปโหลดปรากฏ
        )

        # ค้นหาไฟล์ในโฟลเดอร์ sub1
        files_sub_folder1 = get_files_from_folder(id, 'sub_folder1')
        if files_sub_folder1:
            for file in files_sub_folder1:
                # อัปโหลดไฟล์ sub1
                upload_button = driver.find_element(By.ID, 'website_element_id')
                upload_button.send_keys(file)

                # ส่งไฟล์
                submit_button = driver.find_element(By.XPATH, 'website_XPATH')
                submit_button.click()
                time.sleep(3)  # รอให้การอัปโหลดเสร็จ

        submit1_link = driver.find_element(By.XPATH, 'website_XPATH')
        submit1_link.click()

        # รอจนกระทั่งหน้าส่งโหลด
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'website_element_id'))  # รอจนกระทั่งปุ่มอัปโหลดปรากฏ
        )

        # ค้นหาไฟล์ในโฟลเดอร์ sub2
        files_sub_folder2 = get_files_from_folder(id, 'sub_folder1')
        if files_sub_folder2:
            for file in files_sub_folder2:
                # อัปโหลดไฟล์ sub2
                upload_button = driver.find_element(By.ID, 'website_element_id')
                upload_button.send_keys(file)

                # ส่งไฟล์
                submit_button = driver.find_element(By.XPATH, 'website_XPATH')
                submit_button.click()
                time.sleep(3)  # รอให้การอัปโหลดเสร็จ

        print(f"อัปโหลดสำเร็จสำหรับนักเรียน: {id}")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดกับนักเรียน {id}: {e}")
    
    logout_and_login()  
    count = count + 1
time.sleep(5)  # รอให้แน่ใจว่าอัปโหลดเสร็จ
driver.quit()

