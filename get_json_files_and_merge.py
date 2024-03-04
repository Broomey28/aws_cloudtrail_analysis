import os
import json

RED = "\033[31m"
BOLD = "\033[1m"
NOCOLOUR = "\033[0m"
GREEN = "\033[0;32m"

def merge_logs(source_dir):
    merged_data = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file).replace('\\','/')
            if file_path.endswith('.json'):
                try:
                    with open(f"{file_path}", 'r') as jsonfile:
                    #read in one char to check if there's content (skip if not for efficiency)
                        merged_data.append(json.load(jsonfile))
                except (FileNotFoundError, json.JSONDecodeError) as e:
                        print(f"{BOLD}Skipping{NOCOLOUR} {RED}'{file_path}'{NOCOLOUR} becuase it's empty")
    extracted = []                        
    for item in merged_data:
        try:
            records = item.get("Records")
            if records:
                extracted.extend(records)
        except AttributeError:
            print(f"Skipping item without 'records' key")
    with open('merged_cloudtrail_logs.json', 'w') as savefile:
        json.dump(extracted, savefile, indent=2)    
    print(f"\n{BOLD}Finished!{NOCOLOUR} \nYour singular log file has been made here: \n{GREEN}{os.getcwd()}\\merged_cloudtrail_logs.json{NOCOLOUR}")
        
source_directory = input("Enter the source path where your cloudtrial logs are: ")
list_of_json = merge_logs(source_directory)