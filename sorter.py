import os
import logging
import shutil
import time

import magic

location = "D:\\UserData\\Mike\\Downloads\\"
log_file = f"cleanup on {int(time.time())}.log"

cat = {"image": ["Pictures", ["png", "webp"]], "document": ["Documents", ["pdf", "xlsx"]],
       "archive": ["Compressed", ["xz", "gz", "tar"]], "executable": ["Programs", ["exe", "msi"]],
       "source": ["Scripts", ["ino", "cpp", "js"]]}
logging.basicConfig(filename=log_file, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)


def sort_file(file, idk):
    logging.info(f"processing file {file}")
    logging.debug(idk)
    for catagory in list(cat.keys()):
        if catagory in idk or file.split(".")[-1] in cat[catagory][1]:
            if not os.path.exists(os.path.join(location, cat[catagory][0])):
                logging.info(f"Creating Folder {cat[catagory][0]}")
                os.makedirs(os.path.join(location, cat[catagory][0]))
            logging.info(f"matched into {catagory}")
            logging.info(f"Moving File {file} to {os.path.join(location, cat[catagory][0], file)}")
            shutil.move(os.path.join(location, file), os.path.join(location, cat[catagory][0], file))
            return True


def check_directory(loc_dir):
    total_files = os.listdir(loc_dir)
    logging.info(f"found {len(total_files)} files")
    for file in os.listdir(loc_dir):
        file_path = os.path.join(loc_dir, file)
        if os.path.isfile(file_path):
            try:
                idk = magic.from_buffer(open(file_path, "rb").read(2048))
                sort_file(file, idk)
            except magic.MagicException as e:
                logging.error(f"Error identifying file type for {file}: {e}")


if __name__ == "__main__":
    check_directory(location)

# excutable
# media
# other
