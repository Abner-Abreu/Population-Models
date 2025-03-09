import src.models.verhulst_model as ver
import src.visualization.plotter as plot

x = ver.logistic_model(0.3,1000,100,50)

fig = plot.line_plot(x)
fig.show()