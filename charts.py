import os
import webbrowser
import tempfile
import json

def generate_chart_function(class_name, packages):
    '''Generate function that is used to draw the chart of the given class.'''
    def chart(columns, data, options={},
                style={'width' : 600, 'height' : 350}):
        '''Return html snippet that draws a chart.'''
    
        # replace collections and generators with lists
        data_with_lists = []
        for row in data:
            data_with_lists.append(list(row))
    
        # generate column appending javascript code snippet
        column_lines = ["data.addColumn('{0}', '{1}');".format(column_type, name)
            for column_type, name in columns]
        column_snippet = '\n'.join(column_lines)
    
        data_and_options = {'data' : json.dumps(data_with_lists, indent=4),
            'options' : json.dumps(options, indent=4), 'class_name' : class_name,
            'packages' : packages, 'column_snippet' : column_snippet}
        # merge data, style and options
        substitution = dict(data_and_options.items() + style.items())
    
        # read template file
        module_path = os.path.dirname(__file__)
        path = os.path.join(module_path, 'templates/simple_chart.html')
        f = open(path)        
        # generate final html
        html = f.read(-1) % substitution
        
        temporary_directory = tempfile.gettempdir()
        
        temporary_file = open(os.path.join(temporary_directory + 't.html'), 'w')
        temporary_file.write(html)
        webbrowser.open('file:///' + temporary_file.name)
        return html
    return chart
