import os
import shutil


def copy_static(origin_path, target_path):
    origin_path = os.path.join("/Users/karl/coding/boot.dev/ssg", origin_path)
    target_path = os.path.join("/Users/karl/coding/boot.dev/ssg", target_path)
    if os.path.exists(target_path):
        shutil.rmtree(target_path)
    os.mkdir(target_path)
    for entry in os.listdir(origin_path):
        entry_path = os.path.join(origin_path, entry)
        if os.path.isfile(entry_path):
            shutil.copy(entry_path, target_path)
        else:
            sub_origin_path = os.path.join(origin_path, entry)
            sub_target_path = os.path.join(target_path, entry)
            copy_static(sub_origin_path, sub_target_path)    



def main():
    copy_static("static", "public")



if __name__ == "__main__":
    main()
