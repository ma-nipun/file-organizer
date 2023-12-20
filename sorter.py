import os
import logging
import shutil
import time

import argparse
import magic

location = "D:\\UserData\\Mike\\Downloads\\"
log_file = f"cleanup on {int(time.time())}.log"

cat = {"image": ["Pictures", ["png", "webp"]], "document": ["Documents", ["pdf", "xlsx"]],
       "archive": ["Compressed", ["xz", "gz", "tar"]], "executable": ["Programs", ["exe", "msi"]],
       "source": ["Scripts", ["ino", "cpp", "js"]]}
logging.basicConfig(filename=log_file, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)


def setup_logging(log_file):
    logging.basicConfig(filename=log_file, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',
                        level=logging.DEBUG)


def sort_file(file, file_info):
    logging.info(f"processing file {file}")
    logging.debug(file_info)
    for catagory in list(cat.keys()):
        if catagory in file_info or file.split(".")[-1] in cat[catagory][1]:
            if not os.path.exists(os.path.join(location, cat[catagory][0])):
                logging.info(f"Creating Folder {cat[catagory][0]}")
                os.makedirs(os.path.join(location, cat[catagory][0]))
            logging.info(f"matched into {catagory}")
            logging.info(f"Moving File {file} to {os.path.join(location, cat[catagory][0], file)}")
            shutil.move(os.path.join(location, file), os.path.join(location, cat[catagory][0], file))
            return True


def check_directory(loc_dir):
    total_items = os.listdir(loc_dir)
    total_files = [file for file in os.listdir(loc_dir) if os.path.isfile(os.path.join(loc_dir, file))]
    logging.info(f"found {len(total_files)} Files, out of {len(total_items)} Items")
    for file in total_files:
        try:
            idk = magic.from_buffer(open(os.path.join(loc_dir, file), "rb").read(2048))
            sort_file(file, idk)
        except magic.MagicException as e:
            logging.error(f"Error identifying file type for {file}: {e}")


def main():
    parser = argparse.ArgumentParser(description='Clean up files in a directory based on categories.')
    parser.add_argument('--location', type=str, default=location, help='The directory to clean up')
    parser.add_argument('--log_file', type=str, default=f"cleanup_on_{int(time.time())}.log", help='The log file name')
    args = parser.parse_args()

    setup_logging(args.log_file)
    logging.info("Starting cleanup script.")

    # Call the check_directory function with the specified location
    check_directory(args.location)

    logging.info("Cleanup script completed.")


if __name__ == "__main__":
    main()

# excutable
# media
# other
