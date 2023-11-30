import os
import sys

def create_folder_and_files(folder_name):
    # Create the new folder
    os.makedirs(folder_name, exist_ok=True)

    # Path for the new files inside the folder
    text_file_path = os.path.join(folder_name, 'input.txt')
    python_file_path = os.path.join(folder_name, 'solution.py')

    # Create an empty text file
    with open(text_file_path, 'w') as file:
        pass
        
    # Create a python file with the specified lines
    with open(python_file_path, 'w') as file:
        file.write("with open('.\input.txt', 'r') as file:\n    input=file.read().splitlines()\n\n")
        file.write("# ---------------------------------------- Del 1 -------------------------------------------\n\n")
        file.write("# ---------------------------------------- Del 2 -------------------------------------------\n\n")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_name>")
        sys.exit(1)
    
    folder_name = sys.argv[1]
    create_folder_and_files(folder_name)