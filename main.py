import argparse
import datetime
import os
import shutil

def main():
    parser = argparse.ArgumentParser(description="Sort files by modified year.")
    parser.add_argument("target_dir", help="Path to the target directory")
    parser.add_argument("output_dir", help="Path to the output directory")
    args = parser.parse_args()

    target_dir = args.target_dir
    output_dir = args.output_dir
    output_dir_name = os.path.basename(output_dir)

    counter = 0
    for dirpath, dirnames, filenames in os.walk(target_dir):
        if output_dir_name in dirnames:
            dirnames.remove(output_dir_name)

        for filename in filenames:
            source_file = dirpath + "/" + filename
            
            stats = os.stat(source_file)
            modified_time = datetime.datetime.fromtimestamp(stats.st_mtime)
            modified_year = modified_time.year

            dest_folder = f"{output_dir}/{modified_year}"
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(source_file, dest_folder)
            counter += 1
            print(f"Moved {source_file} to {dest_folder}.")

    print(f"Moved {counter} files.")


if __name__ == "__main__":
    main()
