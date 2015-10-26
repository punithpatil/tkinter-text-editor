# tkinter-text-editor
Simple text editor designed in Python using the Tkinter library.
This project has been developed on Ubuntu 14.04 LTS using Python 2.7

# Library required
For Python 2.7

`sudo apt-get install python-tk`

For Python 3.0 and above

`sudo apt-get install python3-tk`

# Bugs
Format menu
-----------
+ Changing font type and font size is non functional.
+ Font styles (Bold, Italic, Underline, Overstrike) are only applicable if text is already selected.

Edit menu
---------
+ Cut, copy, paste are not synced when selected from editmenu/rightclick and keyboard shortcuts(*i.e.* both may store different instances, and hence output different values)

Python 3
--------
+ Packages are named differently in Python 3 and hence have to be manually corrected.
