import pygchart

if __name__ == '__main__':
    columns = [('string', 'City'), ('number', 'Population'), ('number', 'Area')]
    data = [
          ['Rome', 2761477, 1285.31],
          ['Milan', 1324110, 181.76],
          ['Naples', 959574, 117.27],
          ['Turin', 907563, 130.17],
          ['Palermo', 655875, 158.9],
          ['Genoa', 607906, 243.60],
          ['Bologna', 380181, 140.7],
          ['Florence', 371282, 102.41]
        ]
    options = {
          'region': 'IT',
          'displayMode': 'markers',
          'colorAxis': {'colors': ['green', 'blue'] }
          }
    pygchart.geochart(columns, data, options, chart_name='geo_chart_markers')