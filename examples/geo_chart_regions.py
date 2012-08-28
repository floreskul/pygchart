import pygchart

if __name__ == '__main__':
    columns = [('string', 'Country'), ('number', 'Popularity')]
    data = [
        ('Germany', 200),
        ('United States', 300),
        ('Brazil', 400),
        ('Canada', 500),
        ('France', 600),
        ('RU', 700)
    ]
    pygchart.geochart(columns, data, chart_name='geo_chart_regions')