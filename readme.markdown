##Python API for Google Chart Tools

**PyGChart** generates all the necessary html/js to simply visualize your data via <a href="https://developers.google.com/chart/">Google Chart Tools</a>.

#### Usage

    export PYTHONPATH=$PYTHONPATH:. # add current directory to PYTHONPATH
    python examples/geo_chart_regions.py
    python examples/geo_chart_markers.py
    python examples/line_chart.py

#### Example (geo_chart_regions.py)
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

#### Generated chart
<img src="https://github.com/floreskul/floreskul.github.com/blob/master/repository/pygchart/geo_chart_regions.png?raw=true">

