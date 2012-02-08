import os

def geochart(columns, data, options={}, style={'width' : 600, 'height' : 350}):
    
    # replace collections and generators with lists
    data_with_lists = []
    for row in data:
        data_with_lists.append(list(row))
    
    data_and_options = {'data' : str(data_with_lists), 'options' : str(options)}
    # merge data, style and options
    substitution = dict(data_and_options.items() + style.items())
    
    # read template file
    module_path = os.path.dirname(__file__)
    path = os.path.join(module_path, 'templates/geochart.html')
    f = open(path)        
    # generate final html
    html = f.read(-1) % substitution
    return html
    