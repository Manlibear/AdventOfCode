import os
from inspect import getsourcefile
from os.path import abspath
import sys

def open_file(debug_file):
    namespace = sys._getframe(1).f_globals  # caller's globals
    curr_dir = os.path.dirname(namespace['__file__']) #<-- absolute dir the script is in
    abs_file_path = os.path.join(curr_dir, "input_test.txt" if debug_file else "input.txt")
    return open(abs_file_path, "r").read()

