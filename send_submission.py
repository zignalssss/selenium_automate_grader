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
    
    try:
        logout_button = driver.find_element(By.XPATH, 'website_XPATH')  
        logout_button.click()
        time.sleep(2)  

   
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'username')) 
        )
        print("กลับไปที่หน้าล็อกอินแล้ว")

    except Exception as e:
        print(f"เกิดข้อผิดพลาดระหว่างการออกจากระบบ: {e}")


edge_options = Options()
edge_options.use_chromium = True 
edge_options.add_experimental_option("detach",True)

driver_path = r"path_webdriver"  
service = Service(driver_path)


driver = webdriver.Edge(service=service, options=edge_options)
driver.get('your_website_link') 

students = readfile() 
count = 1
for student in students:
    id = student['id'] 
    password_id = student['password']
    print(f"คนที่{count} กำลังอัปโหลดไฟล์สำหรับนักเรียน: {id}")

    try:
       
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'username'))  
        )

        username = driver.find_element(By.ID, 'username')
        password = driver.find_element(By.ID, 'password')

        username.send_keys(id)  
        password.send_keys(password_id)  
        password.send_keys(Keys.RETURN)  

       
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, 'website_XPATH')) 
        )

       
        submit_link = driver.find_element(By.XPATH, 'website_XPATH')
        submit_link.click()

     
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'website_element_id'))  
        )

        
        files_sub_folder1 = get_files_from_folder(id, 'sub_folder1')
        if files_sub_folder1:
            for file in files_sub_folder1:
                
                upload_button = driver.find_element(By.ID, 'website_element_id')
                upload_button.send_keys(file)

               
                submit_button = driver.find_element(By.XPATH, 'website_XPATH')
                submit_button.click()
                time.sleep(3) 

        submit1_link = driver.find_element(By.XPATH, 'website_XPATH')
        submit1_link.click()

       
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'website_element_id'))  
        )

        
        files_sub_folder2 = get_files_from_folder(id, 'sub_folder1')
        if files_sub_folder2:
            for file in files_sub_folder2:
                
                upload_button = driver.find_element(By.ID, 'website_element_id')
                upload_button.send_keys(file)

               
                submit_button = driver.find_element(By.XPATH, 'website_XPATH')
                submit_button.click()
                time.sleep(3)  

        print(f"อัปโหลดสำเร็จสำหรับนักเรียน: {id}")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดกับนักเรียน {id}: {e}")
    
    logout_and_login()  
    count = count + 1
time.sleep(5)  
driver.quit()

