import os

def generate_chart(class_name, packages):
    def chart(columns, data, options={}, style={'width' : 600, 'height' : 350}):
    
        # replace collections and generators with lists
        data_with_lists = []
        for row in data:
            data_with_lists.append(list(row))
    
        # generate column appending javascript code snippet
        column_lines = ["data.addColumn('{0}', '{1}');".format(column_type, name)
            for column_type, name in columns]
        column_snippet = '\n'.join(column_lines)
    
        data_and_options = {'data' : str(data_with_lists),
            'options' : str(options), 'class_name' : class_name,
            'packages' : packages, 'column_snippet' : column_snippet}
        # merge data, style and options
        substitution = dict(data_and_options.items() + style.items())
    
        # read template file
        module_path = os.path.dirname(__file__)
        path = os.path.join(module_path, 'templates/geochart.html')
        f = open(path)        
        # generate final html
        html = f.read(-1) % substitution
        return html
    return chart
