# # for code completion
# import sys
# sys.path.append('/usr/share/gdb/python')

import gdb

def gprint(*args):
    gdb.write(' '.join(str(x) for x in args) + '\n')


class BtFuncOnly(gdb.Command):
    """Backtrace with function names only
"""
    def __init__(self):
        super(self.__class__, self).__init__('btf', gdb.COMMAND_FILES)
    def invoke(self, argument, from_tty):
        frame: gdb.Frame = gdb.selected_frame()
        while frame is not None:
            f = frame.function()
            fn = f.symtab.filename
            gprint(f'{fn}:{f.line}', frame.name())
            frame = frame.older()
BtFuncOnly()


