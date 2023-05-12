import re

class DocuFlexInterpreter:
    def __init__(self):
        self.data = {}

    def parse_file(self, filename):
        with open(filename, 'r') as file:
            content = file.read()
            self.parse_content(content)

    def parse_content(self, content):
        class_pattern = r'class (\w+) extends (\w+) \{(.*?)\}'
        matches = re.findall(class_pattern, content, re.DOTALL)
        for match in matches:
            self.parse_class(match)

    def parse_class(self, class_info):
        class_name, parent_name, class_content = class_info
        self.data[class_name] = {
            'parent': parent_name,
            'content': self.parse_class_content(class_content)
        }

    def parse_class_content(self, class_content):
        # further parsing can be done here based on your syntax
        content = {}
        lines = [line.strip() for line in class_content.split('\n') if line.strip()]
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                content[key.strip()] = value.strip().strip('";')
        return content

    def get_parsed_data(self):
        return self.data


interpreter = DocuFlexInterpreter()
interpreter.parse_file('docuflex_sample.txt')
parsed_data = interpreter.get_parsed_data()

for class_name, class_info in parsed_data.items():
    print(f'\n{class_name} (extends {class_info["parent"]}):')
    for key, value in class_info['content'].items():
        print(f'  {key}: {value}')
