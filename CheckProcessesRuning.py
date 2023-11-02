import subprocess
import platform

def list_background_processes():
    processes = []
    try:
        operating_system = platform.system()

        if operating_system == 'Windows':
            output = subprocess.check_output(["tasklist"], text=True)
            lines = output.strip().split('\n')[3:]  # Skip the first 3 lines of the header
            for line in lines:
                fields = line.split()
                pid = fields[1]
                name = fields[0]
                processes.append((pid, name))

        elif operating_system == 'Linux':
            output = subprocess.check_output(["ps", "-e"], text=True)
            lines = output.strip().split('\n')[1:]  # Skip the header
            for line in lines:
                fields = line.split()
                pid = fields[0]
                name = fields[-1]
                processes.append((pid, name))

        # Add support for other operating systems if needed
        else:
            print("Unsupported operating system.")

    except subprocess.CalledProcessError as e:
        print("Error. Unable to get process list:", e)

    return processes

if __name__ == "__main__":
    background_processes = list_background_processes()
    print("Processes running in the background:")
    for pid, name in background_processes:
        print(f"PID: {pid}, Name: {name}")