# python-screenshot-to-FTP
Uploads a screenshot to an FTP server when a hotkey is pressed. The hotkey can be changed into basically anything you want.

Table of contents
=================

  * [Installation](#installation)
  * [Behaviour](#behaviour)
  * [Customization](#customization)
    * [Hotkeys](#hotkeys)
    * [Filename](#filename)
    * [Screenshot folder](#screenshot-folder)
    * [Monitor specific screenshot](#monitor-specific-screenshot)
  * [Compile to executable](#compile-to-executable)

## Installation
In order to install this and run it, you need Python and two packages:

1) `pip install mss`
2) `pip install keyboard`

After installing these packages, you should edit all the FTP variables at the top to match your preferences. Then simply run:

`python screengrab.py`

## Behaviour
As default, if you press `SHIFT+0` it takes a screenshot, saves it to `%USERPROFILE%\AppData\Local\Temp\`, uploads it to the FTP servers folder, then removes the file afterwards.

To end the application, simply hit `ALT+END`.

## Customization
### Hotkeys
You can change the two hotkeys on the last two lines. Simply enter whatever combination you want (some might not work).

### Filename
You can change the filename on [line 17](https://github.com/mortenmoulder/python-screenshot-to-FTP/blob/master/screengrab.py#L17). Default it will be something like `11-09-2017 23-22-50 screenshot.png`.

### Screenshot folder
On [line 18](https://github.com/mortenmoulder/python-screenshot-to-FTP/blob/master/screengrab.py#L18) you can change the folder location it should save files to. Alternatively remove/comment out [line 32](https://github.com/mortenmoulder/python-screenshot-to-FTP/blob/master/screengrab.py#L32) if you wish to keep the screenshots locally.

### Monitor specific screenshot
On [line 20](https://github.com/mortenmoulder/python-screenshot-to-FTP/blob/master/screengrab.py#L20) it says `mon=-1` which basically means screenshot all the monitors you have (almost similar to your printscreen button on your keyboard). Change this to any number that Windows knows (open `desk.cpl` from Run or CMD to see your monitors), if you wish to screenshot a specific monitor.

## Compile to executable
Before you can compile to .exe, you need to install a package called [`PyInstaller`](http://www.pyinstaller.org/):

`pip install pyinstaller`

Then you can run this command to compile:

`pyinstall --onefile screengrab.py`

Add `--noconsole` if you want it to run in the background.

The compiled file size is about 3.7 megabyte for Windows 10 and 3.5 megabyte for Windows 7.
