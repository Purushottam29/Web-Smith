import os

def save_code_to_file(code: str, filename:str = "generated_code.py"):
    output_dir = "generated"

    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, filename)

    with open(file_path, "w") as f:
        f.write(code)

    return file_path

