import os
import shutil

from_dir = os.makedirs("C:/Users/lrnfw/OneDrive/Documents/Anahita/Coding")
to_dir = shutil.move("C:/Users/lrnfw/OneDrive/Documents/Anahita/Coding/Project 102")

list_of_files = os.listdir(from_dir)
print(list_of_files)

if os.path.exists(path2):
    print("Moving" + file_name + ".....")

    shutil.move(path1, path3)

else:
    os.makedirs(path2)
    print("Moving" + file_name + ".....")
    shutil.move(path1, path3)