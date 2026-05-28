from pygments.lexers import RegexLexer, words
from pygments.token import *

__all__ = ['MisaLexer']

_syscalls = (
    'SYS_PRINT_INT', 'SYS_PRINT_FLOAT', 'SYS_PRINT_STRING', 'SYS_DRAW_RECT', 'SYS_DRAW_TEXTURE', 'SYS_DRAW_TEXTURE_REGION',
    'SYS_STORAGE_READ', 'SYS_STORAGE_WRITE', 'SYS_MEM_COPY', 'SYS_MEM_SET', 'SYS_PRESERVE_BACK_BUFFER',
    'SYS_PRESERVE_FRONT_BUFFER', 'SYS_GET_INPUT', 'SYS_GET_UNIX_TIME', 'SYS_GET_RUNNING_TIME', 'SYS_GET_UPDATE_DELTA',
    'SYS_GET_DRAW_DELTA', 'SYS_SET_RNG_SEED'
)

_constants = (
    'true', 'false', 'PI', 'TAU', 'EXP1', 'INF', 'NAN', 'SCREEN_WIDTH', 'SCREEN_HEIGHT'
)

_button_constants = (
    'BTN_SELECT', 'BTN_START', 'BTN_LEFT', 'BTN_RIGHT', 'BTN_UP', 'BTN_DOWN', 'BTN_A', 'BTN_B', 'BTN_X', 'BTN_Y'
)

_variables = (
    '$'
)

_types = (
    'i8t', 'u8t', 'i16t', 'u16t', 'i32t', 'u32t', 'f32t'
)

_types_embed_only = (
    'string', 'file'
)

_conditions = (
    'eq', 'neq', 'lt', 'lte', 'gt', 'gte', 'ltu', 'lteu', 'gtu', 'gteu', 'feqa', 'fneqa', 'flt', 'fgt', 'fnan', 'finf'
)

_argument_registers = (
    'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13', 'a14', 'a15'
)

_saved_registers = (
    's0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15'
)

_temporary_registers = (
    't0', 't1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't14', 't15'
)

_zeroadic_instructions = (
    'nop', 'ret', 'break', 'yield', 'exit'
)

_monadic_instructions = (
    'psh', 'pop', 'inc', 'dec', 'neg', 'abs', 'sgn', 'fcti', 'fctf', 'fneg', 'fabs', 'fsgn', 'fsqrt', 'frsqrt', 'fflo',
    'fcei', 'frou', 'ftru', 'ffra', 'fsin', 'fcos', 'ftan', 'fasin', 'facos', 'fatan', 'frtd', 'fdtr', 'flog', 'fexp',
    'not', 'cal', 'jmp', 'jtr', 'jfs', 'syscall', 'rvb', 'ppc', 'clz', 'ctz', 'vpsh', 'vpop'
)

class MisaLexer:
    name = 'Misa'
    aliases = ['misa']
    filenames = ['*.misa']

    tokens = {
        'root': [
            (r'\s+', Whitespace),
            (r'#.*\n', Comment),
            (words(_zeroadic_instructions), instruction.Zeroadic),
            (words(_monadic_instructions), instruction.Monadic, 'instruction')
        ],

        'instruction': [
            
        ]
    }