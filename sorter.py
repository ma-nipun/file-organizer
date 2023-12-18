import os
import mimetypes

import magic

# location = os.getcwd()
location = "D:\\UserData\\Mike\\Downloads\\"

cat = {"image": ["destination", ["png", "jpg"]]}


def sort_file(file, idk):
    if 'image' in idk:
        print(file, idk)
    #     move the file according to the file tipye
    # pass


for file in os.listdir(location):
    file_path = os.path.join(location, file)
    if os.path.isfile(file_path):
        # sortfile(location, file)
        try:
            file_type = magic.Magic()
            idk = magic.from_buffer(open(file_path, "rb").read(2048))
            # print(f"File: {file}, Type: {idk}")
            sort_file(file, idk)
            split = file_type.from_file(file_path).split(", ")
        except magic.MagicException as e:
            print(f"Error identifying file type for {file}: {e}")

# get file types and names
# way to sort file types
# archive
# documents
# excutable
# images
# media
# other
