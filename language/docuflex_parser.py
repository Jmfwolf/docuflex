from lark import Lark, Transformer, v_args
from df_ast import Attribute, Function, Variable, Conditional, Lambda, Validate, Document, Block
grammar = open("docuflex_grammar.lark").read()

class DocuFlexTransformer(Transformer):
    @v_args(inline=True)
    def document(self, items):
        name, parent_doc, blocks = items[0], items[1] if len(items) > 1 else None, items[2:]
        return Document(name, parent_doc, blocks)

    def _parent_doc(self, items):
        return items[0]

    @v_args(inline=True)
    def block(self, items):
        name, _, attributes = items
        return Block(name, None, False, attributes)

    def _parent_block(self, items):
        return items[0]

    def _is_primitive(self, items):
        return True

    @v_args(inline=True)
    def attribute(self, _, items):
        return Attribute(items[0], items[1])

    def value(self, items):
        return items[0]

    def function(self, items):
        return Function(items[0], items[1:])

    def variable(self, items):
        return Variable(items[0])

    def conditional(self, items):
        return Conditional(items[0], items[1], items[2] if len(items) > 2 else None)

    def lambda_(self, items):
        return Lambda(items[0], items[1:], items[-1])

    def validate(self, items):
        return Validate(items)


docuflex_parser = Lark(grammar, parser='lalr', transformer=DocuFlexTransformer())

def parse(code):
    return docuflex_parser.parse(code)

if __name__ == "__main__":
    sample_code = '''
        doc SampleDoc {
            block Title {
                text: "Welcome to DocuFlex"
            }
        }
    '''
    ast = parse(sample_code)
    print(ast)
