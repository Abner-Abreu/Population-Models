import plotly.express as px
import plotly.graph_objects as go
def scatter_plot(data):
    fig = px.scatter(data, 'Tiempo', 'Población', animation_frame=data)
    return fig

def line_plot(data):
    fig = go.Figure(data = go.Scatter(y = data,mode ='lines', name= 'Función'))
    return fig