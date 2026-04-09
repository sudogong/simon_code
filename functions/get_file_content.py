import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    error = ''
    working_dir_abs = os.path.abspath(working_directory)
    file_path_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_target_file = os.path.commonpath([working_dir_abs, file_path_abs]) == working_dir_abs

    if not valid_target_file:
        error = f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        return error

    if not os.path.isfile(file_path_abs):
        error = f'Error: File not found or is not a regular file: "{file_path}"'
        return error

    try:
        file = open(file_path_abs)
        content = file.read(MAX_CHARS)
        
        if file.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content
    except:
        return error