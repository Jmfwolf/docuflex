class AbstractNode:
    def __init__(self, _type):
        self.type = _type
        self.line_number = None
        self.column_number = None

class Document(AbstractNode):
    def __init__(self, name, parent_doc, blocks):
        super().__init__('Document')
        self.name = name
        self.parent_doc = parent_doc
        self.blocks = blocks

class Block(AbstractNode):
    def __init__(self, name, parent_block, is_primitive, attributes):
        super().__init__('Block')
        self.name = name
        self.parent_block = parent_block
        self.is_primitive = is_primitive
        self.attributes = attributes

class Attribute(AbstractNode):
    def __init__(self, name, value):
        super().__init__('Attribute')
        self.name = name
        self.value = value

class Validate(AbstractNode):
    def __init__(self, expressions):
        super().__init__('Validate')
        self.expressions = expressions

class Lambda(AbstractNode):
    def __init__(self, name, parameters, body):
        super().__init__('Lambda')
        self.name = name
        self.parameters = parameters
        self.body = body

class Function(AbstractNode):
    def __init__(self, name, arguments):
        super().__init__('Function')
        self.name = name
        self.arguments = arguments

class Variable(AbstractNode):
    def __init__(self, name):
        super().__init__('Variable')
        self.name = name

class Conditional(AbstractNode):
    def __init__(self, condition, true_block, false_block=None):
        super().__init__('Conditional')
        self.condition = condition
        self.true_block = true_block
        self.false_block = false_block

class Inversion(AbstractNode):
    def __init__(self, condition, block):
        super().__init__('Inversion')
        self.condition = condition
        self.block = block
