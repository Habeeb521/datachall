import json
def load_specifications(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

spec = load_specifications('spec.json')


def generate_fixed_width_file(spec, data, output_file):
    with open(output_file, 'w', encoding=spec['FixedWidthEncoding']) as f:
        widths = [int(offset) for offset in spec['Offsets']]
        
        if spec['IncludeHeader'].lower() == 'true':
            header = ''
            for name, width in zip(spec['ColumnNames'], widths):
                header += name.ljust(width + 1)
            f.write(header.rstrip() + '\n')
        
        for record in data:
            line = ''
            for column, width in zip(record, widths):
                formatted_column = str(column)[:width]
                line += formatted_column.ljust(width + 1)
            f.write(line.rstrip() + '\n')

spec = load_specifications('spec.json')
data = [
    ('John', 'Doe', '321', 'M', 'Engineer', '123', 'DeptA', '1234 Main St', 'Info1', 'Extra1'),
    ('Jane', 'Smith', '123', 'F', 'Scientist', '456', 'DeptB', '5678 Elm St', 'Info2', 'Extra2'),
    ('Alice', 'Johnson', '231', 'F', 'Manager', '789', 'DeptC', '9101 Pine St', 'Info3', 'Extra3'),
    ('Bob', 'Brown', '432', 'M', 'Clerk', '012', 'DeptD', '1213 Oak St', 'Info4', 'Extra4'),
    ('Carol', 'Davis', '543', 'F', 'Director', '345', 'DeptE', '1415 Maple St', 'Info5', 'Extra5')
]

generate_fixed_width_file(spec, data, 'output.txt')
