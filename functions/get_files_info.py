import os


# use os to get the current path

def get_files_info(working_directory, directory=None):

    

    absolute_path_wd = os.path.abspath(working_directory)

    #the permitted working directory is calcualtro but I am runnign my test from the root so I have to join calculator to the working_directory so that the code knows to only run from there
    absolute_path_d = os.path.abspath(os.path.join(working_directory, directory))

    # print(f"working_directory: {working_directory}")
    # print(f"absolute working_directory: {os.path.abspath(working_directory)}")
    # print(f"directory: {directory}")
    # print(f"absolute directory: {os.path.abspath(directory)}")


    if not absolute_path_d.startswith(absolute_path_wd) :
        return f"Error: Cannot list {directory} as it is outside the permitted working directory"
    elif os.path.isdir(absolute_path_d) == False :
        return f'Error: "{directory}" is not a directory'
    
    directory_content = os.listdir(absolute_path_d)

    for f in directory_content:
        return f" - {f}: file_size={os.path.getsize(f)} bytes, is_dir={os.path.isdir(f)}"