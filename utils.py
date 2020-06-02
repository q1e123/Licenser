## @package utils
# Contains utility functions

import os

## Adds content at the start of a file
# @param filename The file
# @param text Content to be added
def line_prepender(filename, text):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(text + '\n' + content)

## Gets content from a file
# @param filename The file 
def get_content(filename):
    with open(filename, 'r') as f:
        content = f.read()
        return content
     
