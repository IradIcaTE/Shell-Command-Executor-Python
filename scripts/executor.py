import subprocess

def execute_commands(file_path):
    with open(file_path, "r") as file:
        commands = file.readlines()

    for cmd in commands:
        print(f"Running: {cmd.strip()}")
        result = subprocess.run(cmd.strip(), shell=True, capture_output=True, text=True)
        print("Output:\n", result.stdout)
        if result.stderr:
            print("Error:\n", result.stderr)

if __name__ == "__main__":
    execute_commands("commands/basic.txt")
