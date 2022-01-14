import os

def separate_files_by_their_type(path):
    all_files = os.listdir(path)
    for file in all_files:
        extention = file.split('.')[-1:][0]
        
        # move the file
        if extention != "py":
            print(extention)
            new_path = os.path.join(path, extention)

            try:
                os.mkdir(new_path)
            except:
                print(new_path + " - Already exists")
            
            # move file
            old_path = os.path.join(path, file)
            new_path = os.path.join(new_path, file)

            try:
                os.rename(old_path, new_path)
            except:
                print("There is a permission issue")

