import os
project_name = 'my_project'
dirs_names = ['settings', 'mainapp', 'adminapp', 'authapp']
def make_dirs(root_folder, subfolders):
    if not os.path.exists(root_folder):
        os.mkdir(root_folder)
    for sub in subfolders:
        path = os.path.join(root_folder, sub)
        if not os.path.exists(path):
            os.mkdir(path)
make_dirs(project_name, dirs_names)