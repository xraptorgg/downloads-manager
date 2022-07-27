# downloads-manager

A python program that removes clutter in Downloads folder by organizing files based on their file type. It uses `os` module, `shutil` module, `watchdog` module. Both `os` and `shutil` modules come under Python’s standard utility modules. The `watchdog` module monitors the specified directory and can notify if a file is created or changed. 

![Downloads Manager program in action](https://cdn.discordapp.com/attachments/954319966444851200/1001853539078906068/unknown.png)

## How to run

First we need to install the `watchdog` module. Run the following command in the terminal

```pip install watchdog```

Then open the ```.py``` file in any text editor and modify the source path and the destination paths

Run the program

## Purpose

As a university student I always download something or the other from the internet, be it books in PDF format, lecture videos in MP4 format or roadmaps in PNG format. In my busy schedule I hadly get any spare time to sit down and organize those files manually so that I can later look up those files when needed. Hence all those files pile up and create a mess making it harder to find something I am looking for. So I created a python program which can do all these manual work for me. My download directory has seperate folders for each type of file, and when I download something the program checks the file extension of the file and then moves it to its respective folder. My download directory thus stays clean and organized, when I want to retrieve a file, I go inside its respective folder and open it from there without having to browse through hundreds of files.

## Contribution

The list of file extensions is not complete. There are hundreds of other file extrensions that I am not aware of. I just included the ones that I know of and I use regularly. 

Feel free to update the file extensions list to your knowledge and purpose