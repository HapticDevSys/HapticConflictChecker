import os
import shutil
import json
from colorama import init, Fore, Style
init()

CONFIG_FILE = "directories_config.json"

def load_directories():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {
        "test_dir": "",
        "tested_dir": "",
        "temp_dir": ""
    }

def save_directories(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def scan_directory(path):
    file_paths = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file.endswith(('.fxap', '.lua', '.txt', '.ymf', '.ymt')):  # Ignore specific file extensions
                file_paths[file] = os.path.join(root, file)
    return file_paths

def move_file_to_temp(source_path, temp_dir):
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    destination = os.path.join(temp_dir, os.path.basename(source_path))
    shutil.move(source_path, destination)
    return destination

def option_1(test_dir, maps_dir, temp_dir, json_file):
    test_files = scan_directory(test_dir)
    maps_files = scan_directory(maps_dir)
    moved_files = {}

    for file, path in maps_files.items():
        if file in test_files:
            source_dir = os.path.dirname(path)
            target_dir = os.path.dirname(test_files[file])
            choice = input(f"Collision for {file} between source ({Fore.GREEN}{source_dir}{Style.RESET_ALL}) "
                           f"and target ({Fore.YELLOW}{target_dir}{Style.RESET_ALL}).\n"
                           f"Choose action: Move from source (1), target (2), or skip (3)? ")

            action_msg = "Moving from source" if choice == '1' else ("Moving from target" if choice == '2' else "Skipping")
            print(Fore.CYAN + action_msg + Style.RESET_ALL)

            if choice == '1':
                new_location = move_file_to_temp(path, temp_dir)
                moved_files[path] = new_location
            elif choice == '2':
                new_location = move_file_to_temp(test_files[file], temp_dir)
                moved_files[test_files[file]] = new_location
            elif choice == '3':
                continue 
    with open(json_file, 'w') as f:
        json.dump(moved_files, f, indent=4)
    print(Fore.GREEN + "Duplicated Stream Files Finished." + Style.RESET_ALL)

def option_2(json_file, temp_dir):
    with open(json_file, 'r') as f:
        moved_files = json.load(f)

    for original, temp in moved_files.items():
        if not original.endswith(('.fxap', '.lua', '.txt', '.ymf', '.ymt')):
            shutil.move(temp, original)

def option_3():
    config = load_directories()
    print(f"Current Directories:\n"
          f"1. Test Directory: {config['test_dir']}\n"
          f"2. Tested Directory: {config['tested_dir']}\n"
          f"3. Temp Directory: {config['temp_dir']}\n")

    config['test_dir'] = input("Enter the Test Directory: ")
    config['tested_dir'] = input("Enter the Tested Directory: ")
    config['temp_dir'] = input("Enter the Temp Directory: ")

    save_directories(config)
    print(Fore.GREEN + "Directories saved successfully." + Style.RESET_ALL)

def main():
    config = load_directories()

    print(Fore.LIGHTBLUE_EX + "Haptic Conflict Tool" + Style.RESET_ALL)

    menu = f"""{Fore.LIGHTBLUE_EX}Please choose an option:
    1. Compare files and optionally move duplicates to Temp
    2. Restore files from Temp
    3. Setup Directories{Style.RESET_ALL}
    """
    choice = input(menu)
    
    if choice == '1':
        option_1(config['test_dir'], config['tested_dir'], config['temp_dir'], "moved_files.json")
    elif choice == '2':
        option_2("moved_files.json", config['temp_dir'])
    elif choice == '3':
        option_3()

if __name__ == "__main__":
    main()