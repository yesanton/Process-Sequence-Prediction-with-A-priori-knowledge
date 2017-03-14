import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from plotly import tools

from prepare_graph_results import trace0, trace0_11, trace1_11, trace2_11, trace3_11, trace4_11, trace5_11, trace0_12, \
    trace1_12, trace2_12, trace3_12, trace4_12, trace5_12, trace0_17, trace1_17, trace2_17, trace3_17, trace4_17, \
    trace5_17, trace0_help, trace1_help, trace2_help, trace3_help, trace4_help, trace5_help, trace0_env, trace1_env, \
    trace2_env, trace3_env, trace4_env, trace5_env
from prepare_graph_results import trace1
from prepare_graph_results import trace2
from prepare_graph_results import trace3
from prepare_graph_results import trace4
from prepare_graph_results import trace5

plotly.__version__


# Edit the layout
layout = dict(title = 'BPI13 incidents results',
              xaxis = dict(title = 'Prefix'),
              yaxis = dict(title = 'Damerau Levenshtein Similarity'),
              )

fig = tools.make_subplots(rows=3, cols=2,subplot_titles=('BPI13','BPI11', 'BPI12','BPI17','HelpDesk','Environmental Permit'))

fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 1)
fig.append_trace(trace3, 1, 1)
fig.append_trace(trace4, 1, 1)
fig.append_trace(trace5, 1, 1)

fig.append_trace(trace0_11, 1, 2)
fig.append_trace(trace1_11, 1, 2)
fig.append_trace(trace2_11, 1, 2)
fig.append_trace(trace3_11, 1, 2)
fig.append_trace(trace4_11, 1, 2)
fig.append_trace(trace5_11, 1, 2)

fig.append_trace(trace0_12, 2, 1)
fig.append_trace(trace1_12, 2, 1)
fig.append_trace(trace2_12, 2, 1)
fig.append_trace(trace3_12, 2, 1)
fig.append_trace(trace4_12, 2, 1)
fig.append_trace(trace5_12, 2, 1)

fig.append_trace(trace0_17, 2, 2)
fig.append_trace(trace1_17, 2, 2)
fig.append_trace(trace2_17, 2, 2)
fig.append_trace(trace3_17, 2, 2)
fig.append_trace(trace4_17, 2, 2)
fig.append_trace(trace5_17, 2, 2)

fig.append_trace(trace0_help, 3, 1)
fig.append_trace(trace1_help, 3, 1)
fig.append_trace(trace2_help, 3, 1)
fig.append_trace(trace3_help, 3, 1)
fig.append_trace(trace4_help, 3, 1)
fig.append_trace(trace5_help, 3, 1)

fig.append_trace(trace0_env, 3, 2)
fig.append_trace(trace1_env, 3, 2)
fig.append_trace(trace2_env, 3, 2)
fig.append_trace(trace3_env, 3, 2)
fig.append_trace(trace4_env, 3, 2)
fig.append_trace(trace5_env, 3, 2)



fig['layout'].update(height=1000, width=900, title='Results unfolded')
plotly.offline.plot(fig, filename='simple-subplot')

#fig = dict(data=data, layout=layout)
#plotly.offline.plot(fig, filename='styled-line')