# from json import loads
import os
from PIL import Image, UnidentifiedImageError
# from reportlab.lib.pagesizes import landscape, letter
# from reportlab.pdfgen import canvas

from src.GalleryBuilder import GalleryBuilder

photo_dirpaths = [
    "C:/Users/FamilyAdmin/Downloads/wetransfer_12176_2023-05-31_1859",
    "C:/Users/FamilyAdmin/Downloads/wetransfer_zmou8816871-gaia6_2023-05-26_2024/",
    "C:/Users/FamilyAdmin/Downloads/wetransfer_zmou8866553-gaia9_2023-05-26_2022/",
    "C:/Users/FamilyAdmin/Downloads/wetransfer_zmou8884979-gaia7_2023-05-26_2026/",
    "C:/Users/FamilyAdmin/Downloads/wetransfer_zmou8885975-gaia8_2023-05-26_2020/"
]
# mappings_file = open("mappings.json")
# mappings = loads(mappings_file.read())

# for k in mappings:
#     pass

for photo_dirpath in photo_dirpaths:
    resizedir = f"{photo_dirpath.removesuffix('/')}_shrunk/"
    try:
        os.mkdir(resizedir)
    except FileExistsError:
        pass
    photo_slugs = os.listdir(photo_dirpath)

    for photo in photo_slugs:
        try:
            im = Image.open(os.path.join(photo_dirpath, photo))
        except UnidentifiedImageError:
            continue
        sm_im = im.resize((100, 75))
        sm_im.save(os.path.join(resizedir, photo))

    pdfname = f"{os.path.split(photo_dirpath)[~0]}.pdf"
    if pdfname == ".pdf":
        # trim trailing junk
        pdfnames = os.path.split(photo_dirpath)
        # split only the trimmed portion
        pdfname = f"{os.path.split(pdfnames[0])[~0]}.pdf"
    gr = GalleryBuilder(
        photo_directory=resizedir,
        pdf_write_path=pdfname
    )
    gr.make_gallery()
    gr.save_pdf()
