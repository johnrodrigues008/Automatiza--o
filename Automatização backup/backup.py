import shutil
import os

src_folder = r'C:\Users\John Rodrigues\Desktop\pasta1'
dst_folder = r'C:\Users\John Rodrigues\Desktop\pasta2'


def backup_files(src_folder, dst_folder):
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = src_file.replace(src_folder, dst_folder, 1)

            dst_dir = os.path.dirname(dst_file)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)

            shutil.copy2(src_file, dst_file)

    for root, dirs, files in os.walk(dst_folder):
        for file in files:
            dst_file = os.path.join(root, file)
            src_file = dst_file.replace(dst_folder, src_folder, 1)

            if not os.path.exists(src_file):
                os.remove(dst_file)


backup_files(src_folder, dst_folder)
