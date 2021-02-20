import os
import shutil
folder_names = []
for entry_name in os.listdir('.'):
    entry_path = os.path.join('.', entry_name)
    if os.path.isdir(entry_path):
        folder_names.append(entry_name)

for i in folder_names:
    print(i)
    if os.path.exists(i + '/' + 'abc'):
        print("Folder exists")
        shutil.rmtree(i + '/' + 'abc')


print(folder_names)
