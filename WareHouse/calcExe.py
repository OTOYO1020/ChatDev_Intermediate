import os
import py_compile

def compile_python_files(directory):
    """
    Compile all Python files in the specified directory.
    
    Parameters:
    directory (str): The directory to search for Python files.

    Returns:
    tuple: (success_count, total_files) where success_count is the number of files successfully compiled,
           and total_files is the total number of Python files found.
    """
    success_count = 0
    total_files = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                total_files += 1
                filepath = os.path.join(root, file)
                try:
                    py_compile.compile(filepath, doraise=True)
                    success_count += 1
                except py_compile.PyCompileError as e:
                    print(f"Failed to compile {filepath}: {e}")

    return success_count, total_files

if __name__ == "__main__":
    for i in range(1, 6):
        print(i)
        directory = f"./D_At{i}"
        success_count, total_files = compile_python_files(directory)

        print(f"{success_count} / {total_files}")
