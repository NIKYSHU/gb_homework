import os
import shutil
project = r'C:/Users/nikys/PycharmProjects/gb_homework'
folders = []
def get_roots(path):
    for root, dirs, files in os.walk(path):
        if os.path.basename(root) == 'templates':
            folders.append(root)
def copy_anything(src, dst):
    dist_folder = os.path.join(dst, os.path.basename(os.path.dirname(src)))
    if not os.path.exists(dst):
        os.mkdir(dst)
    shutil.copytree(src, dist_folder)
get_roots(project)
f_templates = os.path.join(project, 'templates')
for path in folders:
    copy_anything(path, f_templates)