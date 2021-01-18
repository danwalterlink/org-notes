import os
import sys

directory = os.getcwd()
extension='md'

for root, dirs, files in os.walk(directory, topdown=False):
    dir_list=[]

    for file in files:
        if file.endswith(".md"):
            file_split = file.split(".md")
            command = f"pandoc -f markdown -t org -o {root}/{file_split[0]}.org {root}/{file}"
            del_command=f"rm {root}/{file}"
            #print(del_command)
            os.system(del_command)