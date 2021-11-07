import glob
import multiprocessing
import os
import sys
import time
import timeit
from datetime import datetime
from typing import Union

from PySide2 import QtCore

file_generated = False


def write_in_file(filename, root):
    global file_generated
    file_generated = True
    venv_name = os.path.basename(root)
    with open(filename, 'a') as text_file:
        text_file.write(venv_name + ':' + root + '\n')


def match_feature(file_name, dir_path, signal_object: 'QtCore.Signal'):
    # this is the check pattern for windows only
    if sys.platform == 'win32':
        checks = ["Lib", "Scripts/activate.bat", "Scripts/activate.ps1"]
    else:  # sys.platform == 'linux':
        checks = ["lib/*/site-packages", "bin/python"]

    check_flag = True
    for check_ in checks:
        if os.name == 'nt':
            complete_path = os.path.realpath(os.path.join(dir_path, check_))
            if not os.path.exists(complete_path):
                check_flag = False  # if any of the path is missing, then discard the folder
        elif sys.platform == 'linux':
            complete_path = os.path.join(dir_path, check_)
            results = glob.glob(complete_path)
            if not results:
                check_flag = False
    if check_flag:
        if sys.platform == 'win32':
            signal_object.emit(f"Windows 10 venv found, name:{os.path.basename(dir_path)}")
        elif sys.platform == 'linux':
            signal_object.emit(f"Linux venv found, name: {os.path.basename(dir_path)}")

        write_in_file(file_name, dir_path)


def begin_scan(dir_path, signal_object: 'QtCore.Signal', save_dir: Union['str', None] = None):
    """
    Function to scan a directory recursively and generate a text file
    :param save_dir: directory path to save results file. If not provided, uses the same directory path as the scan dir
    :param signal_object: PySide signal object, used to emit relevant information in runtime
    :param dir_path: starting dir for the scan
    :return: filename as generated
    """
    file_name = f'test_op_{datetime.today().timestamp():.00f}.txt'

    if save_dir is not None and os.path.isdir(save_dir):
        file_path = os.path.join(save_dir, file_name)
    elif save_dir is None:
        file_path = os.path.join(os.path.dirname(dir_path), file_name)
    else:
        file_path = save_dir  # if save_dir, is already a file-name to be created

    if os.path.exists(file_path):
        os.remove(file_path)

    signal_object.emit(f"Checking: {os.path.basename(dir_path)}")

    for root, dirs, files in os.walk(dir_path):
        if os.path.isdir(root):
            for dir_ in dirs.copy():
                if dir_.startswith('_') or dir_.startswith('.'):
                    dirs.remove(dir_)  # ignore hidden directories from the scan (for any OS)
            match_feature(file_path, root, signal_object)

    return os.path.realpath(file_path)


if __name__ == '__main__':
    count = int(input("Enter number of multiple searches:"))
    check_paths = []

    for i in range(count):
        check_path = input("Enter checking path: (add :relpath) at end to search relative directory:")
        if check_path.endswith(':relpath'):
            path = os.path.expanduser(check_path.split(':')[0])
        else:
            path = check_path
        check_paths.append(path)
    print(check_paths, '\n')
    time.sleep(1.0)
    a = timeit.default_timer()
    with multiprocessing.Pool() as pool:
        for check_path in check_paths:
            # check_path = os.path.realpath(check_path)
            print("searching in path:", check_path)
            pool.map(begin_scan, (check_path,))
    b = timeit.default_timer()
    print(f"Time taken:{(b - a):.03f}, seconds")
