import logging
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas
from os import listdir
from os.path import join as pathjoin


class GalleryBuilder:
    """
    Class manages process of finding batch of photos.

    -----------
    Attributes:
    canvas: reportlab.pdfgen.canvas.Canvas object used to build gallery page
    pdf_write_path: filename for generated PDF file
    photo_directory: filepath to directory containing photo files
        to include in gallery

    """
    def __init__(
        self,
        photo_directory: str = ".",
        pdf_write_path: str = "gallery.pdf",
        img_width: int = 100,
        img_height: int = 75,
        x_padding: int = 15,
        y_padding: int = 15,
        x_margin: int = 10,
        y_margin: int = 10,
        logger: logging.Logger = None
    ):
        """
        Inputs: None
        """
        self.photo_directory = photo_directory
        self.pdf_write_path = pdf_write_path
        self.canvas = canvas.Canvas(pdf_write_path)
        self.canvas.setPageSize(landscape(letter))
        self.img_width = img_width
        self.img_height = img_height
        self.NUM_IMGS_IN_ROW = 6
        self.num_imgs_written = 0
        self.x_margin = x_margin  # remember that padding will also be applied
        self.y_margin = y_margin
        self.y_padding = y_padding
        self.x_padding = x_padding
        self.logger = logger
        if not self.logger:
            logging.basicConfig(
                filename="log.log",
                level=logging.DEBUG
            )
            self.logger = logging.getLogger()

    def make_gallery(self):
        self.logger.info(f"Working on folder {self.photo_directory}")
        filenames = listdir(self.photo_directory)
        for filename in filenames:
            try:
                photo_path = pathjoin(self.photo_directory, filename)
                self.logger.debug(f"Trying to write preview of f{photo_path}")
                self.canvas.drawImage(
                    photo_path,
                    x=self.x_margin + (self.num_imgs_written % self.NUM_IMGS_IN_ROW) * (self.img_width + self.x_padding),
                    y=self.y_margin + (self.num_imgs_written // self.NUM_IMGS_IN_ROW) * (self.img_height + self.y_padding),
                    width=self.img_width,
                    height=self.img_height
                )
                self.logger.debug(f"Found and drew thumbnail of {photo_path}.")
                self.num_imgs_written += 1
            except OSError as e:
                print(e)
                self.logger.debug(e)

    def save_pdf(self):
        self.canvas.save()
        self.logger.info(f"Saved PDF {self.pdf_write_path}")