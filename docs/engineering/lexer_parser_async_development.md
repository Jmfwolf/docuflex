# Tokenizer & Parser

## DSL Description:

DocuFlex is a domain-specific language designed to facilitate the dynamic and automated generation of software documentation. It uses object-oriented principles, such as classes, inheritance, and polymorphism, to create accurate, comprehensive, and customizable documents. Documents in DocuFlex are made up of different sections or blocks, including an introduction, content, conclusion, and metadata. The language supports the use of variables, built-in functions, conditional logic, inversions, lambdas, and validation rules.

## Language Specification:

DocuFlex's syntax includes documents and blocks, with blocks being either primitive or extended from existing blocks. The language uses the `extends` keyword for inheritance and the `@` symbol for variables. Conditional logic and inversions are represented by `?` and `!` symbols, respectively. Custom logic can be defined with the `lambda` keyword, and validation rules can be set with the `validate` keyword. There are also built-in functions like `peekAt`, `extract`, `readFile`, and `formatDate`.

## Token Definition:

Token types in DocuFlex include keywords (`doc`, `block`, `extends`, `is_primitive`, `lambda`, `validate`), variables (prefixed with `@`), symbols (`{}`, `()`, `:`, `++`, `>`, `!`, `@`, `.`, `?`), string literals (enclosed in double quotes), identifiers (names of documents, blocks, functions), and comments (anything after `//` on a line).

## Token Hierarchy:

The token hierarchy in DocuFlex starts with documents and blocks as the highest level constructs. These are followed by properties within blocks, which can be primitive types or other blocks. Then there are the operators and keywords, which include the `extends` keyword for inheritance, the `@` symbol for variables, the `?` and `!` symbols for conditional logic and inversions, and the `lambda` keyword for defining custom logic.

## Lexical Rules:

DocuFlex's lexical rules include:
- Identifiers are case-sensitive.
- String literals are enclosed in double quotes and can include any printable character.
- Keywords are reserved and cannot be used as identifiers.
- Variables are defined using the `@` symbol.
- The scope of a variable is within the block or document where it is defined.
- Whitespace, including line breaks, is ignored except as a separator between tokens.

## Grammar Definition:

The grammar in DocuFlex includes documents and blocks, defined with their respective keywords. Blocks can be defined as either primitive or extended from other blocks. Each block can have one or more properties, which can be of primitive types, other blocks, or the result of functions. Blocks and properties are defined within braces `{}`. Expressions within properties can involve operators (`++`, `>`, `!`, `@`, `.`), variables (`@`), and literals.

## AST Structure:

The AST for DocuFlex is based on the following classes:

- `AbstractNode`: This is the base class for all nodes. It includes a `type` attribute that indicates the type of node.

- `Document`: Represents a document in DocuFlex, consisting of a name, a parent document (if any), and a list of blocks.

- `Block`: Represents a block in a document. It includes a name, a parent block (if any), a boolean indicating whether it is a primitive block, and a list of attributes.

- `Attribute`: Represents an attribute within a block, consisting of a name and a value.

- `Validate`: Represents a validation rule, consisting of a list of expressions that form the rule.

- `Lambda`: Represents a user-defined function, consisting of a name

, a list of parameters, and a body.

- `Function`: Represents a function call, consisting of a name and a list of arguments.

- `Variable`: Represents a variable, consisting of a name.

- `Conditional`: Represents a conditional expression, consisting of a condition and blocks to be executed when the condition is true and when it is false (if provided).

- `Inversion`: Represents an inversion (not) operation, consisting of a condition and a block to be executed when the condition is not true.

## Error Handling:

Errors in DocuFlex could include lexical errors (e.g., unrecognized tokens), syntactic errors (e.g., missing or mismatched braces, incorrect use of keywords), semantic errors (e.g., referencing a non-existent variable, mismatched data types), and runtime errors (e.g., division by zero, file not found). The lexer and parser should detect these errors and provide meaningful error messages, including the type of error, the location in the code, and a suggestion for fixing the error.

## Compatibility Considerations:

As DocuFlex is a new language, there are no specific compatibility requirements with existing systems or languages. However, the generated documentation should be compatible with common documentation formats and tools, such as Markdown, HTML, and documentation generators.

## Development Constraints:

The lexer and parser for DocuFlex will be developed using Python, utilizing the LARK library for parsing. The development should follow Python's PEP 8 coding standards and use Git for version control. The preferred development environment is a text editor or IDE with Python support, and a command-line interface for running and testing the lexer and parser.

## Testing and Validation:

The lexer and parser should be tested using unit tests, functional tests, and integration tests. The tests should cover all aspects of the language and all possible edge cases. The LARK library provides tools for testing parsers, and Python's built-in unittest module can be used for general testing. The validation should ensure that the generated documentation matches the expected output for given DocuFlex code.

## Documentation Needs:

The lexer and parser should be well-documented, with comprehensive API documentation, inline code comments, and user guides or tutorials. The API documentation should describe the purpose and usage of each class, method, and function. The code comments should explain the purpose and functionality of each section of code. The user guides or tutorials should explain how to use the lexer and parser, with examples and walkthroughs of common use cases.

## Regular Communication and Coordination:

Regular communication and coordination between the lexer and parser developers is crucial. This could involve regular meetings or discussions, shared documentation or notes, and collaborative tools like version control systems and project management software.

## Clear Interfaces or Specifications:

Clear interfaces or specifications should be defined for the lexer and parser. This could involve defining specific input and output formats, function or method signatures, and data structures for representing tokens and AST nodes. These interfaces or specifications should be agreed upon by both developers and should be flexible enough to accommodate changes or additions to the language.

## Additional Information:

The AST provided seems comprehensive and fits well with the nature of the DocuFlex language. However, to refine this document further, it would be beneficial to have:
- More specific examples of DocuFlex code and the corresponding tokens and ASTs.
- More specific plans or strategies for testing and validation.
- Examples of potential errors and how they should be handled.
- Any planned or potential future additions or changes to the language.
- Documentation of the Python classes that represent the AST nodes, including their methods and attributes, and how they are used in the lexer and parser.
