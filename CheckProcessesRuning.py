import subprocess

def list_background_processes():
    try:
        output = subprocess.check_output("tasklist", shell=True, text=True)
        lines = output.strip().split('\n')[3:]  # Skip the first 3 lines of the header
        
        print("Processes running in the background:")
        for line in lines:
            fields = line.split()
            pid = fields[1]
            name = fields[0]
            print(f"PID: {pid}, Name: {name}")
    except subprocess.CalledProcessError as e:
        print("Error. Unable to get process list:", e)

if __name__ == "__main__":
    list_background_processes()