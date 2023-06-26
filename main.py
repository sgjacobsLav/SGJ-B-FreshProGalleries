import argparse
import configparser
import json
from src.GalleryBuilder import GalleryBuilder


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_folder",
        "-i",
        help=(
            "path to folder containing photos for gallery "
            "(takes precedence over mapping file)"
        ),
    )
    parser.add_argument(
        "--output_file", "-o", help="filename for generated gallery"
    )
    parser.add_argument(
        "--mapping_file",
        "-m",
        help="path to JSON file mapping input folders to gallery filenames",
    )
    parser.add_argument(
        "--config_file",
        help=(
            "INI formatted file containing settings for gallery builder "
            "under 'GalleryBuilder' heading"
        ),
    )

    args = parser.parse_args()

    gb_configs = (
        dict()
        if not args.config_file
        else configparser.ConfigParser().read(args.config_file)[
            "GalleryBuilder"
        ]
    )

    if args.input_folder:
        gb = GalleryBuilder(*gb_configs, photo_directory=args.input_folder)
        gb.make_gallery()
        gb.save_pdf()

    elif args.mapping_file:
        try:
            mapping_fh = open(args.mapping_file)
            mappings = json.loads(mapping_fh.read())
        except OSError as e:
            print(f"Error reading mapping file...\n{e}")
            exit()
        for dir in mappings:
            gb = GalleryBuilder(
                *gb_configs, photo_directory=dir, pdf_write_path=mappings[dir]
            )
            gb.make_gallery()
            gb.save_pdf()


if __name__ == "__main__":
    main()
