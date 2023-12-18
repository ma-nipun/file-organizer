import os
import logging
import shutil

import magic

location = "D:\\UserData\\Mike\\Downloads\\"

cat = {"image": ["Pictures", ["png", "jpg"]], "document": ["Documents", ["pdf", "ocr"]],
       "archive": ["Compressed", ["zip", "rar"]]}
logging.basicConfig(level=logging.DEBUG)


def sort_file(file, idk):
    logging.info(f"processing file {file}")
    logging.debug(idk)
    for catagory in list(cat.keys()):
        if catagory in idk or file in cat[catagory][1]:
            if not os.path.exists(os.path.join(location, cat[catagory][0])):
                logging.info(f"Creating Folder {cat[catagory][0]}")
                os.makedirs(os.path.join(location, cat[catagory][0]))
            logging.info(f"matched into {catagory}")
            logging.info(f"Moving File {file} to {os.path.join(location, cat[catagory][0], file)}")
            shutil.move(os.path.join(location, file), os.path.join(location, cat[catagory][0], file))
            return True



for file in os.listdir(location):
    file_path = os.path.join(location, file)
    if os.path.isfile(file_path):
        try:
            file_type = magic.Magic()
            idk = magic.from_buffer(open(file_path, "rb").read(2048))
            # print(f"File: {file}, Type: {idk}")
            sort_file(file, idk)
            # split = file_type.from_file(file_path).split(", ")
        except magic.MagicException as e:
            print(f"Error identifying file type for {file}: {e}")


# excutable
# media
# other
