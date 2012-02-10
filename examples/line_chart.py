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
        'width': 400,
        'height': 240,
        'title': 'Company Performance'
        }
    print pygchart.linechart(columns, data, options)