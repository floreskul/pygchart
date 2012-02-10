# list of possible charts in the format:
# {python function name} : {js class}, {js package}
CHARTS_TYPES = {
    'geochart' : ('GeoChart', 'geochart'),
    'linechart' : ('LineChart', 'corechart')
}

class ChartFunctionGenerator(object):
    '''Generator of the funcions that generate charts of different types.'''
    
    def __init__(self, wrapped_module):
        self.wrapped_module = wrapped_module
    
    def __getattr__(self, name):
        charts = self.wrapped_module.charts
        if name in CHARTS_TYPES:
            class_name, package = CHARTS_TYPES[name]
            return charts.generate_chart(class_name, [package])
        else:
            raise AttributeError(name)