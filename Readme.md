# Fresh Pro Gallery Builder
This tool takes a directory path, finds all images in the directory, and outputs a PDF containing a thumbnail gallery of all images.

## Installation

### Initial installation -- a programmer's brief
*Intended Audience -- the initial installation will require familiarity with Python development tools and environment setup. It's not friendly.*
This packages requires Python 3.11, poetry, and a virtual environment system compatible with poetry. Clone the github link of the project, install Python 3 on your computer, pip install poetry, if necessary (for me it's always been necessary) install pyenv and use pyenv commands to install a runnable consistent with the `.python-version` file, poetry install the package, and poetry run the package.

### Updates -- a friendlier process
Given an environment where the package has already been used successfully, updating should be far simpler. Open a terminal, and type the following commands  
```
git update
poetry lock
poetry update
```
Automatic updates are envisioned later, but for now, this process should fetch the latest version and install it.

### Requirements
Python 3.11
Poetry
Python packages `reportlab`, `pillow` and `pypdf`
<!--- Still need anything other than reportlab? -->

## Usage
### Overview
The process consists of: Make directory(ies) on your system containing files, specify path to directory and corresponding pdf name in `mappings.json`, run gallery builder.
#### Make Directories
If you are using a computer with Google Drive Desktop installed, you probably already have the folder you need. Find out where the pictures were stored when they were taken. If someone took photos using an iPad and uploaded them to a new folder using the Google Drive app, then that new folder should have synced to your desktop Google Drive folder.  
If you aren't using Google Drive, or don't have it installed on your desktop, download the pictures and unzip the downloaded pictures to a new folder if necessary. Then, find the new folder containing those photos and copy the full path to that folder.
#### Grab full path to directories
In Windows, you can click on the folder and then click "copy path" in the ribbon at the top of file explorer. On Mac that option is disabled by default, but you can click while holding Control to bring up a menu, and then hold the Option key to let you copy the full path to the folder.
#### Paste full path into `mappings.json` file
The mappings file contains pairs of names: Names of source directories containing photos paired with names of PDF galleries to fill with those photos. The format of each pair should match
```
"name_of_folder_with_the_photos": "name_of_gallery.pdf",
```
keeping the quotes around the names as shown. The first line of the file should be an opening curly brace ('{') and the last line should be a closing curly brace ('}').  
If confused, find the example file included, and replace the lines of text with actual names of your folders. When you're done, remove all of the extra text.
#### Run the generator
`poetry run python main.py --mapping_file mappings.json`  
*What if I get a weird error message?*  
Then try
`python3 -m poetry run python main.py --mapping_file mappings.json`  
The two commands above can be copied and pasted into the terminal. Hit Enter after pasting one in.  

### Other usage modes
*Is that really the only way to use it? I have to match the format of your "mappings.json" exactly?*
There are other run-modes, available to anyone comfortable with trying from the terminal. I don't recommend that you try running this way if you don't know how to work in a command line.
Run `main.py --help` to see the options currently supported. There is no need to use a mapping file. `main.py -i "my_photos_directory_path" -o "my_pdf_name.pdf"` is a valid invocation.  
