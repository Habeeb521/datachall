import csv
import json

def load_specifications(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        spec = json.load(file)
    spec['Offsets'] = [int(width) for width in spec['Offsets']]
    return spec

def parse_fixed_width_to_csv(input_file, spec, csv_file):
    with open(input_file, 'r', encoding=spec['FixedWidthEncoding']) as file, \
         open(csv_file, 'w', newline='', encoding=spec['DelimitedEncoding']) as csvfile:
        
        writer = csv.writer(csvfile, delimiter='|', quotechar='"', quoting=csv.QUOTE_ALL)
        
        if spec.get('IncludeHeader', False).lower() == 'true':
            writer.writerow(spec['ColumnNames'])
        
        header_row = True
        for line in file:
            if header_row == True:
                header_row = False
                continue
            start = 0
            row = []
            for width in spec['Offsets']:
                end = start + width + 1
                field = ' '.join(line[start:end].strip().replace(',', ' ').split())
                row.append(field)
                start = end
            writer.writerow(row)

spec = load_specifications('spec.json')
parse_fixed_width_to_csv('output.txt', spec, 'output.csv')
