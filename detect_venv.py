import multiprocessing
import time
import os, sys
import glob
import timeit

def write_in_file(filename, root):
    venv_name = os.path.basename(root)
    with open(filename, 'a') as text_file:
        text_file.write(venv_name + ':' + root+'\n')

def match_feature(file_name, dir_path):
    # this is the check pattern for windows only
    if os.name == 'nt':
        checks = ["Lib", "bin/activate", ""]
    elif sys.platform == 'linux':
        checks = ["lib/*/site-packages", "bin/python"]

    # will update the check pattern for Linux soon...
    
    check_flag = True
    for locs in checks:
        if os.name == 'nt':
            path = os.path.realpath(os.path.join(dir_path, locs))
            if not os.path.exists(path):
                check_flag = False  # if any of the path is missing, then discard the folder
        elif sys.platform == 'linux':
            path = os.path.join(dir_path, locs)
            results = glob.glob(path)
            if not results:
                check_flag = False
    if check_flag:
        if os.name == 'nt':
            print(f"Windows 10 venv found, name:{os.path.basename(dir_path)}")
        elif sys.platform == 'linux':
            print(f"Linux venv found, name: {os.path.basename(dir_path)}")
        write_in_file(file_name, dir_path)

def main_runner(dir_path):
    file_name = 'test_op_'+ os.path.basename(dir_path) + '.txt'
    if os.path.exists(file_name):
        os.remove(file_name)
    print("Checking:",os.path.basename(dir_path))
    
    for root, dirs, files in os.walk(dir_path):
        if os.path.isdir(root):
            for dir in dirs.copy():
                if dir.startswith('_') or dir.startswith('.'):
                    dirs.remove(dir)
            match_feature(file_name, root)
    


if __name__ == '__main__':
    count = int(input("Enter number of parallel searches:"))
    check_paths =[]
    
    for i in range(count):
        check_path = input("Enter checking path:")
        check_paths.append(check_path)
    print(check_paths,'\n')
    time.sleep(1.0)
    a = timeit.default_timer()
    with multiprocessing.Pool() as pool:
        for check_path in check_paths:
            check_path = os.path.realpath(check_path)
            print("searching in path:", check_path)
            pool.map(main_runner, (check_path,))
    b = timeit.default_timer()
    print("Time taken:", (b-a), " seconds")