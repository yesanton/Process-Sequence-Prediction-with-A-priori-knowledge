import plotly.graph_objs as go

# Add data
month = ['Prefix 2', 'Prefix 3', 'Prefix 4', 'Prefix 5']

bpi13_weak_baseline = [0.0748,0.08869,0.31719,0.11824]
bpi13_weak_no_cycle = [0.45517,0.45344,0.50915,0.43151]
bpi13_weak_apriori = [0.5364,0.59216,0.62202,0.54976]

bpi13_strong_baseline = [0.08076,0.08208,0.23653,0.12041]
bpi13_strong_no_cycle = [0.54435,0.48001,0.48061,0.48877]
bpi13_strong_apriori = [0.61286,0.59255,0.59228,0.57764]


# Create and style traces
trace0 = go.Scatter(
    x = month,
    y = bpi13_weak_baseline,
    name = 'Baseline - weak',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4)
)
trace1 = go.Scatter(
    x = month,
    y = bpi13_weak_no_cycle,
    name = 'Nocycle - weak',
    line = dict(
        color =('rgb(205, 12, 24)'),
        width = 4,
        dash='dash')
)
trace2 = go.Scatter(
    x = month,
    y = bpi13_weak_apriori,
    name = 'Apriori - weak',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4,
        dash = 'dot'
        ) # dash options include 'dash', 'dot', and 'dashdot'
)
trace3 = go.Scatter(
    x = month,
    y = bpi13_strong_baseline,
    name = 'Baseline - strong',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4)
)
trace4 = go.Scatter(
    x = month,
    y = bpi13_strong_no_cycle,
    name = 'Nocycle - strong',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,
        dash = 'dash')
)
trace5 = go.Scatter(
    x = month,
    y = bpi13_strong_apriori,
    name = 'Apriori - strong',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,
        dash = 'dot')
)

bpi11_weak_baseline = [0.22497,0.22201,0.22002,0.2159]
bpi11_weak_no_cycle = [0.29494,0.29413,0.29073,0.28616]
bpi11_weak_apriori = [0.28765,0.28367,0.28001,0.27732]

bpi11_strong_baseline = [0.20743,0.20338,0.20477,0.20045]
bpi11_strong_no_cycle = [0.28713,0.28266,0.27931,0.27443]
bpi11_strong_apriori = [0.27595,0.28199,0.26894,0.26726]

prefix_bpi11 = ['Prefix 13', 'Prefix 14', 'Prefix 15', 'Prefix 16']



trace0_11 = go.Scatter(
    x = prefix_bpi11,
    y = bpi11_weak_baseline,
    name = 'Baseline - weak',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4)
)
trace1_11 = go.Scatter(
    x = prefix_bpi11,
    y = bpi11_weak_no_cycle,
    name = 'Nocycle - weak',
    line = dict(
        color =('rgb(205, 12, 24)'),
        width = 4,
        dash='dash')
)
trace2_11 = go.Scatter(
    x = prefix_bpi11,
    y = bpi11_weak_apriori,
    name = 'Apriori - weak',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4,
        dash = 'dot'
        ) # dash options include 'dash', 'dot', and 'dashdot'
)
trace3_11 = go.Scatter(
    x = prefix_bpi11,
    y = bpi11_strong_baseline,
    name = 'Baseline - strong',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4)
)
trace4_11 = go.Scatter(
    x = prefix_bpi11,
    y = bpi11_strong_no_cycle,
    name = 'Nocycle - strong',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,
        dash = 'dash')
)
trace5_11 = go.Scatter(
    x = prefix_bpi11,
    y = bpi11_strong_apriori,
    name = 'Apriori - strong',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,
        dash = 'dot')
)


bpi12_weak_baseline = [0.09333,0.09934,0.10799,0.11249]
bpi12_weak_no_cycle = [0.27597,0.27407,0.25284,0.22009]
bpi12_weak_apriori = [0.27981,0.26527,0.25814,0.23069]
bpi12_strong_baseline = [0.07049,0.06731,0.07316,0.07794]
bpi12_strong_no_cycle = [0.39648,0.41322,0.36329,0.31676]
bpi12_strong_apriori = [0.42005,0.42512,0.40415,0.3993]

prefix_bpi12 = ['Prefix 2', 'Prefix 3', 'Prefix 4', 'Prefix 5']



trace0_12 = go.Scatter(
    x = prefix_bpi12,
    y = bpi12_weak_baseline,
    name = 'Baseline - weak',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4)
)
trace1_12 = go.Scatter(
    x = prefix_bpi12,
    y = bpi12_weak_no_cycle,
    name = 'Nocycle - weak',
    line = dict(
        color =('rgb(205, 12, 24)'),
        width = 4,
        dash='dash')
)
trace2_12 = go.Scatter(
    x = prefix_bpi12,
    y = bpi12_weak_apriori,
    name = 'Apriori - weak',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4,
        dash = 'dot'
        ) # dash options include 'dash', 'dot', and 'dashdot'
)
trace3_12 = go.Scatter(
    x = prefix_bpi12,
    y = bpi12_strong_baseline,
    name = 'Baseline - strong',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4)
)
trace4_12 = go.Scatter(
    x = prefix_bpi12,
    y = bpi12_strong_no_cycle,
    name = 'Nocycle - strong',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,
        dash = 'dash')
)
trace5_12 = go.Scatter(
    x = prefix_bpi12,
    y = bpi12_strong_apriori,
    name = 'Apriori - strong',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,
        dash = 'dot')
)


bpi17_weak_baseline = [0.48013,0.43345,0.44369,0.41244]
bpi17_weak_no_cycle = [0.48013,0.43345,0.4437,0.41174]
bpi17_weak_apriori = [0.4848,0.46229,0.43386,0.48353]
bpi17_strong_baseline = [0.48013,0.43345,0.44369,0.41244]
bpi17_strong_no_cycle = [0.48013,0.43345,0.4437,0.41174]
bpi17_strong_apriori = [0.52728,0.47767,0.48721,0.54611]

prefix_bpi17 = ['Prefix 6', 'Prefix 7', 'Prefix 8', 'Prefix 9']



trace0_17 = go.Scatter(
    x = prefix_bpi17,
    y = bpi17_weak_baseline,
    name = 'Baseline - weak',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4)
)
trace1_17 = go.Scatter(
    x = prefix_bpi17,
    y = bpi17_weak_no_cycle,
    name = 'Nocycle - weak',
    line = dict(
        color =('rgb(205, 12, 24)'),
        width = 4,
        dash='dash')
)
trace2_17 = go.Scatter(
    x = prefix_bpi17,
    y = bpi17_weak_apriori,
    name = 'Apriori - weak',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4,
        dash = 'dot'
        ) # dash options include 'dash', 'dot', and 'dashdot'
)
trace3_17 = go.Scatter(
    x = prefix_bpi17,
    y = bpi17_strong_baseline,
    name = 'Baseline - strong',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4)
)
trace4_17 = go.Scatter(
    x = prefix_bpi17,
    y = bpi17_strong_no_cycle,
    name = 'Nocycle - strong',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,
        dash = 'dash')
)
trace5_17 = go.Scatter(
    x = prefix_bpi17,
    y = bpi17_strong_apriori,
    name = 'Apriori - strong',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,
        dash = 'dot')
)

help_weak_baseline = [0.56989,0.48202,0.56104,0.71422]
help_weak_no_cycle = [0.56989,0.48202,0.56104,0.71422]
help_weak_apriori = [0.71963,0.76109,0.79775,0.81098]
help_strong_baseline = [0.56989,0.48202,0.56104,0.71422]
help_strong_no_cycle = [0.56989,0.48202,0.56104,0.71422]
help_strong_apriori = [0.81141,0.83226,0.87589,0.89663]

prefix_help = ['Prefix 2', 'Prefix 3', 'Prefix 4', 'Prefix 5']



trace0_help = go.Scatter(
    x = prefix_help,
    y = help_weak_baseline,
    name = 'Baseline - weak',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4)
)
trace1_help = go.Scatter(
    x = prefix_help,
    y = help_weak_no_cycle,
    name = 'Nocycle - weak',
    line = dict(
        color =('rgb(205, 12, 24)'),
        width = 4,
        dash='dash')
)
trace2_help = go.Scatter(
    x = prefix_help,
    y = help_weak_apriori,
    name = 'Apriori - weak',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4,
        dash = 'dot'
        ) # dash options include 'dash', 'dot', and 'dashdot'
)
trace3_help = go.Scatter(
    x = prefix_help,
    y = help_strong_baseline,
    name = 'Baseline - strong',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4)
)
trace4_help = go.Scatter(
    x = prefix_help,
    y = help_strong_no_cycle,
    name = 'Nocycle - strong',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,
        dash = 'dash')
)
trace5_help = go.Scatter(
    x = prefix_help,
    y = help_strong_apriori,
    name = 'Apriori - strong',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,
        dash = 'dot')
)



env_weak_baseline = [0.25402,0.24585,0.24731,0.23624]
env_weak_no_cycle = [0.25402,0.24585,0.24731,0.23624]
env_weak_apriori = [0.07329,0.09213,0.09469,0.0755]
env_strong_baseline = [0.25777,0.24849,0.25303,0.23958]
env_strong_no_cycle = [0.25777,0.24849,0.25303,0.23958]
env_strong_apriori = [0.07421,0.07211,0.06632,0.06526]

prefix_env = ['Prefix 19', 'Prefix 20', 'Prefix 21', 'Prefix 22']



trace0_env = go.Scatter(
    x = prefix_env,
    y = env_weak_baseline,
    name = 'Baseline - weak',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4)
)
trace1_env = go.Scatter(
    x = prefix_env,
    y = env_weak_no_cycle,
    name = 'Nocycle - weak',
    line = dict(
        color =('rgb(205, 12, 24)'),
        width = 4,
        dash='dash')
)
trace2_env = go.Scatter(
    x = prefix_env,
    y = env_weak_apriori,
    name = 'Apriori - weak',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4,
        dash = 'dot'
        ) # dash options include 'dash', 'dot', and 'dashdot'
)
trace3_env = go.Scatter(
    x = prefix_env,
    y = env_strong_baseline,
    name = 'Baseline - strong',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4)
)
trace4_env = go.Scatter(
    x = prefix_env,
    y = env_strong_no_cycle,
    name = 'Nocycle - strong',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,
        dash = 'dash')
)
trace5_env = go.Scatter(
    x = prefix_env,
    y = env_strong_apriori,
    name = 'Apriori - strong',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,
        dash = 'dot')
)







