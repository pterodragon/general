# # for code completion
import sys
sys.path.append('/usr/share/gdb/python')

import gdb
from colorama import Fore, Back, Style

def gprint(*args):
    gdb.write(' '.join(str(x) for x in args) + '\n')

def cwrap(x, c, s):
    return getattr(c, s) + str(x) + getattr(c, 'RESET')


class BtFuncOnly(gdb.Command):
    """Backtrace with function names only
"""
    def __init__(self):
        super(self.__class__, self).__init__('btf', gdb.COMMAND_FILES)
    def invoke(self, argument, from_tty):
        frame: gdb.Frame = gdb.selected_frame()
        while frame is not None:
            func = frame.function()
            file_name = func.symtab.filename
            frame_name = cwrap(frame.name(), Fore, "RED")
            gprint(f'{file_name}:{func.line}', frame_name)
            frame = frame.older()
BtFuncOnly()

