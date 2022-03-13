import os,shutil,json,platform
from time import sleep

# To clear the terminal screen.

if platform.system() == 'Windows':
    clear = lambda :os.system('cls')
else:
    clear = lambda :os.system('clear')

name = """
'  ___________.__ .__             ________         
'  \_   _____/|__||  |    ____   /  _____/   ____  
'   |    __)  |  ||  |  _/ __ \ /   \  ___  /  _ \ 
'   |     \   |  ||  |__\  ___/ \    \_\  \(  <_> )
'   \___  /   |__||____/ \___  > \______  / \____/ 
'       \/                   \/         \/         
"""
# Lambda function.
clear()

# Get file destination data.
file_destn = f"{os.getcwd()}\\file_path_defination.json"

# Reading file destination data.
with open(file_destn) as fd:
    file_path_data = json.load(fd)

# Source Path To Look For Files.
source_path=file_path_data.get("source_path")
soure_data_list=os.listdir(source_path)

doc_count = 0
filtered_file_list = []

# Iterating each item to check where it's a file or directory.
for li_item in soure_data_list:
    dynamic_file_path = f"{source_path}\\{li_item}"
    if os.path.isfile(dynamic_file_path):
        doc_count+=1
        # Filtering the file items and appending in a list.
        filtered_file_list.append(li_item)

# To check if any file exists. 
if doc_count == 0:
    print(" * No Files Found To Move !!")
    sleep(1)
    print(" * Quitting...")
    sleep(1)
    clear()
    exit()

# Grabbing the destination lables defined by user.
destination_path_list = list(file_path_data.get("destination_path").keys())

def filego():
    try:
        print(" 1. To move all files")
        print(" 0. To quit ")
        input_val=int(input("\n Enter A Value - "))
        if input_val==True:
            move_count = 0
            for i in filtered_file_list:
                ext=os.path.splitext(i)[-1].lower()

                # Iterating each label.
                for current_path in destination_path_list:

                    # Accessing the current path values i.e user defined directory path and extensions.
                    curentpath_dict = file_path_data.get("destination_path")[current_path]
                    dir_path = curentpath_dict["path"]
                    extensions = [x.lower() for x in curentpath_dict["extensions"]] 
                    if ext in extensions:
                        if os.path.exists(dir_path):
                            # If directory path exist then we will move the current file to that directory.
                            shutil.move(f"{source_path}\\{i}",curentpath_dict["path"])
                            move_count+=1
                        else:
                            # Else we will throw an error i.e. directory does not exist.
                            print("Error -",f"\n File_type - {current_path}",f"\n Incorrect Path Provided - {dir_path}")
                            exit()
            print(f"\n* Number Of Files Moved - {move_count}")
            sleep(1)
            print("\n* Quitting...")
            sleep(1)
            clear()
        elif input_val==False:
            clear()
            exit()  
        else:   
            clear()
            print(name)
            filego()   
    except Exception:
        # If user input is not an integer this block will execute.
        clear()
        print(name)
        filego()

# Initiate the file moving process.
print(name)
print(f"\n* Number Of Files Found - {doc_count} \n")
filego()


