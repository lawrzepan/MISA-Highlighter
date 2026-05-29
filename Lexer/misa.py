from pygments.lexer import RegexLexer, words, include, bygroups
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

_all_types = _types + _types_embed_only

_conditions = (
    'eq', 'neq', 'lt', 'lte', 'gt', 'gte', 'ltu', 'lteu', 'gtu', 'gteu', 'feqa', 'fneqa', 'flt', 'fgt', 'fnan', 'finf'
)

_data_directives = (
    'emb', 'res'
)

_constant_directives =  (
    'def'
)

_bookmark_directives = (
    'bmk', 'sbmk'
)

#a0|a1|a2|a3|a4|a5|a6|a7|a8|a9|a10|a11|a12|a13|a14|a15
_argument_registers = (
    'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12', 'a13', 'a14', 'a15'
)

#s0|s1|s2|s3|s4|s5|s6|s7|s8|s9|s10|s11|s12|s13|s14|s15
_saved_registers = (
    's0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15'
)

#t0|t1|t2|t3|t4|t5|t6|t7|t8|t9|t10|t11|t12|t13|t14|t15
_temporary_registers = (
    't0', 't1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't14', 't15'
)

_zeroadic_instructions = (
    'nop', 'ret', 'break', 'yield', 'exit'
)

_monadic_instructions = (
    'psh', 'pop', 'inc', 'dec', 'cal', 'jmp', 'jtr', 'jfs', 'syscall', 'vpsh', 'vpop'
)

_dyadic_instructions = (
    'tpr', 'tpa', 'mov', 'mvc', 'swp', 'neg', 'abs', 'sgn', 'fcti', 'fctf', 'fneg', 'fabs', 'fsgn', 'fsqrt', 'frsqrt', 'fflo',
    'fcei', 'frou', 'ftru', 'ffra', 'fsin', 'fcos', 'ftan', 'fasin', 'facos', 'fatan', 'frtd', 'fdtr', 'flog', 'fexp', 'not',
    'rvb', 'ppc', 'clz', 'ctz'
)

_triadic_instructions = (
    'lod',  'str', 'cea', 'lde', 'ste', 'sel', 'add', 'sub', 'mul', 'mlh', 'pow', 'div', 'rem', 'mod', 'min', 'max', 'rnd',
    'cmp', 'and', 'orr', 'xor', 'sar', 'sll', 'slr', 'rol', 'ror', 'pbx', 'pbd', 'fadd', 'fsub', 'fmul', 'fpow', 'fdiv', 'frem',
    'fmod', 'fmin', 'fmax', 'frnd', 'gbpx', 'sbpx', 'vfadd', 'vfsub', 'vfmul', 'vfdiv'
)

_tetradic_instruction = (
    'clp', 'sbx', 'ubx', 'bfi', 'fwrp', 'fclp', 'flrp', 'gtpx', 'stpx', 'vffma'
)

_all_instructions = _zeroadic_instructions + _monadic_instructions + _dyadic_instructions + _triadic_instructions + _tetradic_instruction

Instruction = Keyword.Instruction

Separator = Punctuation.Separator

Register = Name.Register

Label = Name.Label

Directive = Keyword.Directive

class MisaLexer(RegexLexer):
    name = 'Misa'
    aliases = ['misa']
    filenames = ['*.misa']

    tokens = {
        'root': [
            (r'\s+', Whitespace),
            (r'\#.*', Comment),
            (words(_zeroadic_instructions), Instruction.Zeroadic),
            (words(_monadic_instructions), Instruction.Monadic, 'instruction'),
            (words(_dyadic_instructions), Instruction.Dyadic, 'instruction'),
            (words(_triadic_instructions), Instruction.Triadic, 'instruction'),
            (words(_tetradic_instruction), Instruction.Tetradic, 'instruction'),

            (words(('_start:', '_update:', '_draw:', '_input:')), Label.Process),
            (r'\.\w+?:', Label.Local),
            (r'@\w+?:', Label.Reusable),
            (r'\w+?:', Label.Global),

            (words(_data_directives), Directive.Data, 'data_directive'),
            (r'def', Directive.Constant, 'constant_directive'),
            (words(_bookmark_directives), Directive.Bookmark, 'bookmark_directive')
        ],

        'data_directive' : [
            (r'[^\S\r\n]+', Whitespace),
            (words(_types_embed_only), Keyword.Type.Embed),

            #literals that preceed a newline (with whitespace inbetween), end a data directive
            (r'0[x][a-zA-Z0-9_]+?[\t ]*?\n', Literal.Hexadecimal, '#pop'),
            (r'0[b][01_]+?[\t ]*?\n', Literal.Binary, '#pop'),
            (r'[0-9_]+?\.[0-9_]+?[\t ]*?\n', Literal.Float, '#pop'),
            (r'[0-9_]+?[\t ]*?\n', Literal.Integer, '#pop'),
            (r'".*?[\t ]*?"\n', Literal.String, '#pop'),
            (r'\w+?[\t ]*?\n', Name.Constant, '#pop'),

            include('numeric'),
            (r'".*?"', Literal.String),
            (r',', Separator),
        ],

        'constant_directive': [
            (r'[^\S\r\n]+', Whitespace),
            include('numeric'),
            (r'\w+', Name.Constant),
            (r'\n', Whitespace, '#pop'),
        ],

        'bookmark_directive': [
            (r'[^\S\r\n]+', Whitespace),
            (r'"\w+?"', Name),
            (r'\n', Whitespace, '#pop'),
        ],

        'numeric': [
            (r'0[x][a-zA-Z0-9_]+', Literal.Hexadecimal),
            (r'0[b][01_]+', Literal.Binary),
            (r'[0-9_]+?\.[0-9_]+', Literal.Float),
            (r'[0-9_]+', Literal.Integer),
            (r'[+\-\/\*\^\%]+', Operator),
            (r'\w+', Name.Constant),
        ],

        'operrand': [
            (r'[^\S\r\n]+', Whitespace),
            (words(_argument_registers), Register.Argument),
            (r'(a0|a1|a2|a3|a4|a5|a6|a7|a8|a9|a10|a11|a12|a13|a14)(\.\.)(a1|a2|a3|a4|a5|a6|a7|a8|a9|a10|a11|a12|a13|a14|a15)', 
                bygroups(Register.Argument, Punctuation.Range, Register.Argument)),
            (r'(a0|a1|a2|a3|a4|a5|a6|a7|a8|a9|a10|a11|a12|a13|a14)(\.\.)', 
                bygroups(Register.Argument, Punctuation.Range)),

            (words(_saved_registers), Register.Saved),
            (r'(s0|s1|s2|s3|s4|s5|s6|s7|s8|s9|s10|s11|s12|s13|s14)(\.\.)(s1|s2|s3|s4|s5|s6|s7|s8|s9|s10|s11|s12|s13|s14|s15)', 
                bygroups(Register.Saved, Punctuation.Range, Register.Saved)),
            (r'(s0|s1|s2|s3|s4|s5|s6|s7|s8|s9|s10|s11|s12|s13|s14)(\.\.)', 
                bygroups(Register.Saved, Punctuation.Range)),

            (words(_temporary_registers), Register.Temporary),
            (r'(t0|t1|t2|t3|t4|t5|t6|t7|t8|t9|t10|t11|t12|t13|t14)(\.\.)(t1|t2|t3|t4|t5|t6|t7|t8|t9|t10|t11|t12|t13|t14|t15)', 
                bygroups(Register.Temporary, Punctuation.Range, Register.Temporary)),
            (r'(t0|t1|t2|t3|t4|t5|t6|t7|t8|t9|t10|t11|t12|t13|t14)(\.\.)', 
                bygroups(Register.Temporary, Punctuation.Range)),

            (words(_syscalls), Name.Syscall),
            (words(_types), Keyword.Type),
            (words(_conditions), Keyword.Condition),
            (words(_variables), Keyword.VariableBuiltIn),
            (words(_constants), Name.ConstantBuiltIn),
            (words(_button_constants), Name.ConstantBuiltIn.Button),
            include('numeric'),
            (r'".*?"', Literal.String),
            (r'\.\w+', Label.Local),
            (r'@\w+?[+-]', Label.Reusable),
            (r'\w+', Label.Global),
        ],

        'instruction' : [
            (r',', Separator),
            (r'\n', Whitespace, '#pop'),
            (r'#.*', Comment, '#pop'),
            include('operrand'),
        ]
    }

    #python -m pygments -x -f html -O full,debug_token_types -l Lexer/misa.py:MisaLexer tests/helloworld.misa
    #python -m pygments -x -l Lexer/misa.py:MisaLexer tests/helloworld.misa