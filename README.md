# DocuFlex

DocuFlex is a programming language designed for creating structured documents and data representation. It provides a simplified syntax for defining classes and their content, allowing you to easily organize and manipulate data in a hierarchical manner.

## Installation

To use DocuFlex, you need to have Python installed. You can download Python from the official website: [python.org](https://www.python.org/).

## Getting Started

1. Clone the DocuFlex repository:

   ```shell
   git clone https://github.com/jmfwolf/docuflex.git
   ```

2. Navigate to the project directory:

   ```shell
   cd docuflex
   ```

3. Create a virtual environment (optional but recommended):

   ```shell
   python3 -m venv env
   source env/bin/activate
   ```

4. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

To use the DocuFlexInterpreter, follow these steps:

1. Import the necessary module and classes:

   ```python
   import re

   class DocuFlexInterpreter:
       # Implementation of the interpreter
   ```

2. Create an instance of the `DocuFlexInterpreter` class:

   ```python
   interpreter = DocuFlexInterpreter()
   ```

3. Parse a DocuFlex file using the `parse_file` method:

   ```python
   interpreter.parse_file('docuflex_sample.txt')
   ```

4. Retrieve the parsed data using the `get_parsed_data` method:

   ```python
   parsed_data = interpreter.get_parsed_data()
   ```

5. Iterate over the parsed data to access the class information:

   ```python
   for class_name, class_info in parsed_data.items():
       print(f'\n{class_name} (extends {class_info["parent"]}):')
       for key, value in class_info['content'].items():
           print(f'  {key}: {value}')
   ```

## DocuFlex Syntax

DocuFlex uses a simple syntax for defining classes and their content. Here's an example:

```java
class MyClass extends ParentClass {
    attribute1: "value1";
    attribute2: "value2";
}
```

- Classes are defined using the `class` keyword, followed by the class name and the `extends` keyword, if the class has a parent.
- The class content is enclosed in curly braces `{}`.
- Attributes are defined using the format `key: value;`, where the key and value are separated by a colon `:` and terminated with a semicolon `;`.
- String values can be enclosed in double quotes `""`.

## Contributing

Contributions to DocuFlex are welcome! If you find any issues or have suggestions for improvements, please create a GitHub issue or submit a pull request. 

When contributing, please adhere to the following guidelines:
- Fork the repository and create your branch from `main`.
- Follow the existing code style and naming conventions.
- Write clear commit messages and provide a detailed description of your changes.

## License

This project is licensed under the [GNULicense](LICENSE).

## Acknowledgments

- The DocuFlexInterpreter was developed by the DocuFlex team:
    - [Jmfwolf](https://github.com/Jmfwolf)
    - [RawBoeuf](https://github.com/RawBoeuf)
- Inspiration and ideas were drawn from:
    - YAML
    - Java

## Contact

If you have any questions or inquiries, please contact [Jmfwolf](https://github.com/Jmfwolf) at [jmfwolf@hacksomniac.com].

---
**Note**: The code provided in the README is just a starting point for the interpreter implementation. You need to further refine and enhance it according to the specific requirements and syntax of the DocuFlex language.
