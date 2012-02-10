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
    print pygchart.geochart(columns, data)