from lexer import Lexer
from parser import Parser
from codegen import CodeGen
import os

def get_last_element(lst):
    if isinstance(lst, list):
        return get_last_element(lst[-1])
    else:
        return lst


text_input = """ 
begin


int result = 0;
int numb = 6;


if ( numb != 0){
    if (result == 0){ 
        result = 10;
        };
};


print(result);

end                                                                   

"""

lexer = Lexer().get_lexer()
try:
    tokens = lexer.lex(text_input)

    codegen = CodeGen()

    module = codegen.module
    builder = codegen.builder
    printf = codegen.printf

    pg = Parser(module, builder, printf)
    pg.parse()
    parser = pg.get_parser()

    nodes = parser.parse(tokens)
    for node in nodes:
        if type(node) == type(list()):
            item = get_last_element(node)
            item.eval()
        else:
            node.eval()

    codegen.create_ir()
    codegen.save_ir("output.ll")
    os.system("llc -filetype=obj output.ll")
    os.system("gcc output.o -no-pie -o output")
    os.system("./output")
except Exception as e:
    if hasattr(e, "source_pos"):
        line = e.source_pos.lineno
        print("Parsing Error at line", line)
    else:

        print("Parsing Error:", e)