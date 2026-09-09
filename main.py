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

    # Collect all files to copy
    files_to_copy: list[str] = []
    for dirpath, dirnames, filenames in os.walk(target_dir):
        if output_dir_name in dirnames:
            dirnames.remove(output_dir_name)
        for filename in filenames:
            source_file = os.path.join(dirpath, filename)
            files_to_copy.append(source_file)

    # Copy all files
    for counter, source_file in enumerate(files_to_copy, start=1):
        stats = os.stat(source_file)
        modified_time = datetime.datetime.fromtimestamp(stats.st_mtime)
        modified_year = modified_time.year

        dest_folder = os.path.join(output_dir, str(modified_year))
        os.makedirs(dest_folder, exist_ok=True)
        shutil.copy2(source_file, dest_folder)
        print(f"Copied {counter}/{len(files_to_copy)} files: {source_file}")

    print(f"Finished copying {len(files_to_copy)} files.")


if __name__ == "__main__":
    main()
