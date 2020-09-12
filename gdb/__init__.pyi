# works for 
# GNU gdb (Ubuntu 9.1-0ubuntu1) 9.1
# __init__.pyi

from typing import Any

ARCH_FRAME: Any
BP_ACCESS_WATCHPOINT: Any
BP_BREAKPOINT: Any
BP_HARDWARE_WATCHPOINT: Any
BP_NONE: Any
BP_READ_WATCHPOINT: Any
BP_WATCHPOINT: Any
COMMAND_BREAKPOINTS: Any
COMMAND_DATA: Any
COMMAND_FILES: Any
COMMAND_MAINTENANCE: Any
COMMAND_NONE: Any
COMMAND_OBSCURE: Any
COMMAND_RUNNING: Any
COMMAND_STACK: Any
COMMAND_STATUS: Any
COMMAND_SUPPORT: Any
COMMAND_TRACEPOINTS: Any
COMMAND_USER: Any
COMPLETE_COMMAND: Any
COMPLETE_EXPRESSION: Any
COMPLETE_FILENAME: Any
COMPLETE_LOCATION: Any
COMPLETE_NONE: Any
COMPLETE_SYMBOL: Any
DUMMY_FRAME: Any
FRAME_UNWIND_INNER_ID: Any
FRAME_UNWIND_MEMORY_ERROR: Any
FRAME_UNWIND_NO_REASON: Any
FRAME_UNWIND_NO_SAVED_PC: Any
FRAME_UNWIND_NULL_ID: Any
FRAME_UNWIND_OUTERMOST: Any
FRAME_UNWIND_SAME_ID: Any
FRAME_UNWIND_UNAVAILABLE: Any
FrameDecorator: Any
FrameIterator: Any
GdbSetPythonDirectory: Any
HOST_CONFIG: Any
INLINE_FRAME: Any
NORMAL_FRAME: Any
PARAM_AUTO_BOOLEAN: Any
PARAM_BOOLEAN: Any
PARAM_ENUM: Any
PARAM_FILENAME: Any
PARAM_INTEGER: Any
PARAM_OPTIONAL_FILENAME: Any
PARAM_STRING: Any
PARAM_STRING_NOESCAPE: Any
PARAM_UINTEGER: Any
PARAM_ZINTEGER: Any
PARAM_ZUINTEGER: Any
PARAM_ZUINTEGER_UNLIMITED: Any
PYTHONDIR: Any
SENTINEL_FRAME: Any
SIGTRAMP_FRAME: Any
STDERR: Any
STDLOG: Any
STDOUT: Any
SYMBOL_COMMON_BLOCK_DOMAIN: Any
SYMBOL_FUNCTIONS_DOMAIN: Any
SYMBOL_LOC_ARG: Any
SYMBOL_LOC_BLOCK: Any
SYMBOL_LOC_COMMON_BLOCK: Any
SYMBOL_LOC_COMPUTED: Any
SYMBOL_LOC_CONST: Any
SYMBOL_LOC_CONST_BYTES: Any
SYMBOL_LOC_LABEL: Any
SYMBOL_LOC_LOCAL: Any
SYMBOL_LOC_OPTIMIZED_OUT: Any
SYMBOL_LOC_REF_ARG: Any
SYMBOL_LOC_REGISTER: Any
SYMBOL_LOC_REGPARM_ADDR: Any
SYMBOL_LOC_STATIC: Any
SYMBOL_LOC_TYPEDEF: Any
SYMBOL_LOC_UNDEF: Any
SYMBOL_LOC_UNRESOLVED: Any
SYMBOL_MODULE_DOMAIN: Any
SYMBOL_STRUCT_DOMAIN: Any
SYMBOL_TYPES_DOMAIN: Any
SYMBOL_UNDEF_DOMAIN: Any
SYMBOL_VARIABLES_DOMAIN: Any
SYMBOL_VAR_DOMAIN: Any
TAILCALL_FRAME: Any
TARGET_CONFIG: Any
TYPE_CODE_ARRAY: Any
TYPE_CODE_BITSTRING: Any
TYPE_CODE_BOOL: Any
TYPE_CODE_CHAR: Any
TYPE_CODE_COMPLEX: Any
TYPE_CODE_DECFLOAT: Any
TYPE_CODE_ENUM: Any
TYPE_CODE_ERROR: Any
TYPE_CODE_FLAGS: Any
TYPE_CODE_FLT: Any
TYPE_CODE_FUNC: Any
TYPE_CODE_INT: Any
TYPE_CODE_INTERNAL_FUNCTION: Any
TYPE_CODE_MEMBERPTR: Any
TYPE_CODE_METHOD: Any
TYPE_CODE_METHODPTR: Any
TYPE_CODE_NAMESPACE: Any
TYPE_CODE_PTR: Any
TYPE_CODE_RANGE: Any
TYPE_CODE_REF: Any
TYPE_CODE_RVALUE_REF: Any
TYPE_CODE_SET: Any
TYPE_CODE_STRING: Any
TYPE_CODE_STRUCT: Any
TYPE_CODE_TYPEDEF: Any
TYPE_CODE_UNION: Any
TYPE_CODE_VOID: Any
VERSION: Any
WP_ACCESS: Any
WP_READ: Any
WP_WRITE: Any
block_for_pc: Any
breakpoints: Any
command: Any
convenience_variable: Any
current_objfile: Any
current_progspace: Any
current_recording: Any
decode_line: Any
default_visualizer: Any
events: Any
execute: Any
find_pc_line: Any
flush: Any
frame_filters: Any
frame_stop_reason_string: Any
frame_unwinders: Any
frames: Any
function: Any
history: Any
inferiors: Any
invalidate_cached_frames: Any
lookup_global_symbol: Any
lookup_objfile: Any
lookup_static_symbol: Any
lookup_static_symbols: Any
lookup_symbol: Any
lookup_type: Any
newest_frame: Any
objfiles: Any
os: Any
packages: Any
parameter: Any
parse_and_eval: Any
post_event: Any
pretty_printers: Any
printer: Any
printing: Any
progspaces: Any
prompt: Any
prompt_hook: Any
rbreak: Any
reload: Any
selected_frame: Any
selected_inferior: Any
selected_thread: Any
set_convenience_variable: Any
solib_name: Any
start_recording: Any
stop_recording: Any
string_to_argv: Any
sys: Any
target_charset: Any
target_wide_charset: Any
traceback: Any
type_printers: Any
types: Any
write: Any

class Symbol:
    addr_class: Any
    is_argument: Any
    is_constant: Any
    is_function: Any
    is_variable: Any
    line: Any
    linkage_name: Any
    name: Any
    needs_frame: Any
    print_name: Any
    symtab: Symtab
    type: Any
    def is_valid(self): ...
    def value(self): ...





class Architecture:
    def disassemble(self): ...
    def name(self): ...



class Block:
    end: Any
    function: Any
    global_block: Any
    is_global: Any
    is_static: Any
    start: Any
    static_block: Any
    superblock: Any
    def is_valid(self): ...



class BlockIterator:
    def is_valid(self): ...



class Breakpoint:
    commands: Any
    condition: Any
    enabled: Any
    expression: Any
    hit_count: Any
    ignore_count: Any
    location: Any
    number: Any
    pending: Any
    silent: Any
    task: Any
    temporary: Any
    thread: Any
    type: Any
    visible: Any
    def delete(self): ...
    def is_valid(self): ...



class BreakpointEvent:
    pass


class ClearObjFilesEvent:
    pass


class Command:
    def dont_repeat(self): ...



class ContinueEvent:
    pass


class Event:
    pass


class EventRegistry:
    def connect(self): ...
    def disconnect(self): ...



class ExitedEvent:
    pass


class Field:
    pass


class FinishBreakpoint:
    commands: Any
    condition: Any
    enabled: Any
    expression: Any
    hit_count: Any
    ignore_count: Any
    location: Any
    number: Any
    pending: Any
    return_value: Any
    silent: Any
    task: Any
    temporary: Any
    thread: Any
    type: Any
    visible: Any
    def delete(self): ...
    def is_valid(self): ...



class Frame:
    def architecture(self): ...
    def block(self): ...
    def find_sal(self): ...
    def function(self) -> Symbol: ...
    def is_valid(self): ...
    def name(self): ...
    def newer(self): ...
    def older(self): ...
    def pc(self): ...
    def read_register(self): ...
    def read_var(self): ...
    def select(self): ...
    def type(self): ...
    def unwind_stop_reason(self): ...



class Function:
    pass


class GdbError:
    args: Any
    def with_traceback(self): ...



class Inferior:
    num: Any
    pid: Any
    progspace: Any
    was_attached: Any
    def architecture(self): ...
    def is_valid(self): ...
    def read_memory(self): ...
    def search_memory(self): ...
    def thread_from_handle(self): ...
    def thread_from_thread_handle(self): ...
    def threads(self): ...
    def write_memory(self): ...



class InferiorCallPostEvent:
    pass


class InferiorCallPreEvent:
    pass


class InferiorDeletedEvent:
    pass


class InferiorThread:
    global_num: Any
    inferior: Any
    name: Any
    num: Any
    ptid: Any
    def handle(self): ...
    def is_exited(self): ...
    def is_running(self): ...
    def is_stopped(self): ...
    def is_valid(self): ...
    def switch(self): ...



class LineTable:
    def has_line(self): ...
    def is_valid(self): ...
    def line(self): ...
    def source_lines(self): ...



class LineTableEntry:
    line: Any
    pc: Any



class LineTableIterator:
    def is_valid(self): ...



class Membuf:
    pass


class MemoryChangedEvent:
    pass


class MemoryError:
    args: Any
    def with_traceback(self): ...



class NewInferiorEvent:
    pass


class NewObjFileEvent:
    pass


class NewThreadEvent:
    pass


class Objfile:
    build_id: Any
    filename: Any
    frame_filters: Any
    frame_unwinders: Any
    owner: Any
    pretty_printers: Any
    progspace: Any
    type_printers: Any
    username: Any
    xmethods: Any
    def add_separate_debug_file(self): ...
    def is_valid(self): ...
    def lookup_global_symbol(self): ...
    def lookup_static_symbol(self): ...



class Parameter:
    pass


class PendingFrame:
    def create_unwind_info(self): ...
    def read_register(self): ...



class Progspace:
    filename: Any
    frame_filters: Any
    frame_unwinders: Any
    pretty_printers: Any
    type_printers: Any
    xmethods: Any
    def block_for_pc(self): ...
    def find_pc_line(self): ...
    def is_valid(self): ...
    def objfiles(self): ...
    def solib_name(self): ...



class RegisterChangedEvent:
    pass


class SignalEvent:
    pass


class StopEvent:
    pass


class Symtab:
    filename: Any
    objfile: Any
    producer: Any
    def fullname(self): ...
    def global_block(self): ...
    def is_valid(self): ...
    def linetable(self): ...
    def static_block(self): ...



class Symtab_and_line:
    last: Any
    line: Any
    pc: Any
    symtab: Any
    def is_valid(self): ...



class ThreadEvent:
    pass


class Type:
    alignof: Any
    code: Any
    name: Any
    objfile: Any
    sizeof: Any
    tag: Any
    def array(self): ...
    def const(self): ...
    def fields(self): ...
    def get(self): ...
    def has_key(self): ...
    def items(self): ...
    def iteritems(self): ...
    def iterkeys(self): ...
    def itervalues(self): ...
    def keys(self): ...
    def optimized_out(self): ...
    def pointer(self): ...
    def range(self): ...
    def reference(self): ...
    def strip_typedefs(self): ...
    def target(self): ...
    def template_argument(self): ...
    def unqualified(self): ...
    def values(self): ...
    def vector(self): ...
    def volatile(self): ...



class TypeIterator:
    pass


class UnwindInfo:
    def add_saved_register(self): ...



class Value:
    address: Any
    dynamic_type: Any
    is_lazy: Any
    is_optimized_out: Any
    type: Any
    def cast(self): ...
    def const_value(self): ...
    def dereference(self): ...
    def dynamic_cast(self): ...
    def fetch_lazy(self): ...
    def format_string(self): ...
    def lazy_string(self): ...
    def reference_value(self): ...
    def referenced_value(self): ...
    def reinterpret_cast(self): ...
    def rvalue_reference_value(self): ...
    def string(self): ...



class _GdbFile:
    encoding: Any
    errors: Any
    def close(self): ...
    def flush(self): ...
    def isatty(self): ...
    def writelines(self): ...



class _GdbOutputErrorFile:
    encoding: Any
    errors: Any
    def close(self): ...
    def flush(self): ...
    def isatty(self): ...
    def write(self): ...
    def writelines(self): ...



class _GdbOutputFile:
    encoding: Any
    errors: Any
    def close(self): ...
    def flush(self): ...
    def isatty(self): ...
    def write(self): ...
    def writelines(self): ...



class error:
    args: Any
    def with_traceback(self): ...


