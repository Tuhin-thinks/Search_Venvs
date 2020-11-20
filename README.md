# Search_Venvs
**Search all available Python Virtual environments under a specific given directory location.**

# Python Version

python 3.7+

# Packages Required

- No extra packages required, all built-in python modules are used
  - os
  - time
  - timeit
  - multiprocessing

## Run The program

- python detect_venv.py

**[x] Inputs:**

- Enter the number of parallel searches you want to do
  - Example, Search inside, Desktop, Documents,and Music Folders at the same time (used multiprocessing pool)
  
- Enter the path to the folder you want to search inside [suppose, venv is a vritualenvironment of Python, and is under Desktop, if you put location to Dekstop, my script will detect the virtualenvironment]

**[x] Outputs:**

- It'll output series of all virtualenvironments found
- You'll also get a text file named in the format <strong>test_op_{dir_name_searching}.txt</strong>
  - For example, If you search in Desktop, you'll get a text file generated as <strong>test_op_Desktop.txt</strong>.
  - The location of the generated text file is same as the directory from where you are running the [detect_venv.py](https://github.com/Tuhin-thinks/Search_Venvs/blob/main/detect_venv.py)
  
# USAGE
I recently thought of copying all my python related coding projects into another drive, but I see almost 3 GB consists of only <em>virtualenvs</em>!
So, I thought, if I can filter the directory to the virtualenvs, I can exclude them from being copied and copy only the Python project folders.

It basically, searches for a pattern of files and folder inside a directory to consider it as a virtualenvironment
**Presently I am searching for the following logic:**
  _*(pseudocode)*_
  ```python
  
  if ['Lib', 'Scripts/active.ps1', 'Scripts/activate.bat'] in searh_directory:
    **search_directory is a virtualenv
    **Note down search directory in the respective text file
  ```
I'll add the logic for searching virtualenvs ob linux environments too, very soon, stay updated.
