import os
import shutil

# providing a destination path for different extentions
progrms="C:/Users/ASUS/Downloads/programs"
music="C:/Users/ASUS/Downloads/Music"
image="C:/Users/ASUS/Pictures"
videos="C:/Users/ASUS/Videos"
text="C:/Users/ASUS/Documents"
zip="C:/Users/ASUS/Downloads/compressed"

# downlaod path
down="C:/Users/ASUS/Downloads"
downdir=os.listdir(down)


print(f"Available files in your downloads are :-  \n")
for li in downdir:
    print("*",li,"\n")

try:
    print(" Press 1 To move all files")
    print(" Press 0 To quit ")
    inu=int(input())
    if inu==True:
            for i in downdir:
                ext=os.path.splitext(i)[-1].lower()
            
                if ext == ".exe":
                    s=f"C:/Users/ASUS/Downloads/{i}"
                    shutil.move(s,progrms)
                elif ext == ".mp3":
                    s=f"C:/Users/ASUS/Downloads/{i}"
                    shutil.move(s,music)
                elif ext == ".mp4":
                    s=f"C:/Users/ASUS/Downloads/{i}"
                    shutil.move(s,music)
                elif ext == ".txt":
                    s=f"C:/Users/ASUS/Downloads/{i}"
                    shutil.move(s,text)
                elif ext == ".zip" or ext==".rar":
                    s=f"C:/Users/ASUS/Downloads/{i}"
                    shutil.move(s,zip)
                elif ext == ".jpg" or ext==".png":
                    s=f"C:/Users/ASUS/Downloads/{i}"
                    shutil.move(s,image)
                else:
                    print(i)
    elif inu==False:
        print("Quitting the program")
        exit()
    print("Task Completed !!!!")        
except ValueError:
    print("Enter a valid Number ")


