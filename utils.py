# Copyright (C) 2020 Robert-Nicolae Șolcă
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/

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
     
