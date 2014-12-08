import pygal
from pygal.style import TurquoiseStyle

def graph(data1, data2):
    graph = pygal.XY(stroke=True, style=TurquoiseStyle)
    graph.dots_size = 6
    graph.title = 'DevOps Bootcamp Head Counts'
    graph.title_font_size = 28
    graph.x_title = 'Week'
    graph.y_title = 'Student Attendees'
    graph.x_labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    graph.y_labels = [0, 5, 10, 15, 20, 25, 30, 35, 40]
    graph.add('2013-2014', data1)
    graph.add('2014-2015', data2)
    graph.render_to_file('headcounts.svg')

data1 = [(1, 34), (2, 27), (3, 21), (6, 14), (8, 14), (9, 22), (13, 8)]
data2 = [(1, 37), (2, 30), (3, 20), (4, 14), (5, 11), (6, 10), (7, 11), (8, 7), (9, 7)]
graph(data1, data2)
