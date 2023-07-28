import shutil
import magic
import os

def move_pe32_executables(source_dir, destination_dir, limit=100):
    count = 0
    
    # Iterate over the files in the source directory
    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)
        
        # Check if the file type is PE32 executable (GUI)
        file_type = magic.from_file(file_path)
        if "PE32 executable (GUI)" in file_type:
            # Create the destination path
            destination_path = os.path.join(destination_dir, file_name)
            
            # Move the file to the destination directory
            shutil.move(file_path, destination_path)
            
            print(f"File {file_name} moved to {destination_dir}")
            
            count += 1
            if count >= limit:
                break
    
    print(f"Moved {count} files")

# Specify the source and destination directories
source_dir = "F:\\BK\\malware"
destination_dir = "F:\\BK\\1101-1200"

# Call the function to move the PE32 executable files
move_pe32_executables(source_dir, destination_dir, limit=100)