import csv
import os
import shutil


def print_csv(folder_name,data):
    print(f"สร้างไฟล์ในโฟลเดอร์ '{folder_name}' สำเร็จ!")
    for index, row in enumerate(data, start=1):
        print(f"Row {index}:")
        for key, value in row.items():
            print(f"  {key}: {value}")
        print("-" * 20)


# def create_nisitfolder(folder_name,data):
#   for index, row in enumerate(data, start=1):
#     id = row["your_key"]
#     if not os.path.exists(id):
#         filename = os.path.join(folder_name, f'{id}')
#         os.makedirs(filename)

def copy_matching_files_to_data(submissions_path, folder_name, data):
    for index, row in enumerate(data, start=1):
        id = row["your_key"]

        
        student_folder = os.path.join(folder_name, f'{id}')
        if not os.path.exists(student_folder):
            os.makedirs(student_folder)

       
        for subfolder in ['sub_folder1', 'sub_folder2']:
            subfolder_path = os.path.join(submissions_path, subfolder)
            if not os.path.exists(subfolder_path):
                print(f"Subfolder '{subfolder}' does not exist. Skipping.")
                continue

          
            subfolder_student_folder = os.path.join(student_folder, subfolder)
            if not os.path.exists(subfolder_student_folder):
                os.makedirs(subfolder_student_folder)

           
            for filename in os.listdir(subfolder_path):
                if filename.startswith(id):  
                   
                    source_file = os.path.join(subfolder_path, filename)
                    destination_file = os.path.join(subfolder_student_folder, filename)
                    shutil.copy2(source_file, destination_file)
                    print(f"Copied '{filename}' from '{subfolder}' to '{subfolder_student_folder}'.")

    
def del_nisitfolder(folder_name,data):
    for index, row in enumerate(data, start=1):
        id = row["your_key"]
        if not os.path.exists(id):
            filename = os.path.join(folder_name, f'{id}')
            os.rmdir(filename)

def readfile():
  with open('your_csv_file', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]
    return data
  
if __name__ == "__main__":
    submissions_path = 'your_folder_submissions'
    output_folder = 'your_out_folder'  
    data = readfile()
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    copy_matching_files_to_data(submissions_path, output_folder,data)
    print("จัดการไฟล์เสร็จสิ้น!")

