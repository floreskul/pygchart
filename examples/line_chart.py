import pygchart

if __name__ == '__main__':
    columns = [('string', 'Year'), ('number', 'Sales'), ('number', 'Expenses')]
    data = [
              ['2004', 1000, 400],
              ['2005', 1170, 460],
              ['2006',  860, 580],
              ['2007', 1030, 540]
            ]
    options = {
        'width': 600,
        'height': 320,
        'title': 'Company Performance'
        }
    pygchart.linechart(columns, data, options, chart_name='line_chart')