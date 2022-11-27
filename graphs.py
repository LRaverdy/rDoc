import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

fifa_df = pd.read_csv("assets/data/fifa_v_pes.csv")
sales_data = pd.read_csv("assets/data/sales_data.csv")
ticker_data = pd.read_csv("assets/data/twitter_final_agg.csv")

def fifa():
    fig = px.bar(
        fifa_df,
        x='percentage',
        y='game',
        color='score',
        text='percentage',
        color_continuous_scale=['red', 'yellow', 'lightgreen'],
        hover_data=fifa_df
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        title="<b>Score : PES vs FIFA</b>",
        title_x=0.5,
        xaxis_title='Percentage',
        yaxis_title=None,
    )

    fig.update_traces(
        texttemplate='<b>%{text} %</b>',
        textposition='inside',
        textfont_size=12,
        insidetextanchor="middle"
    )

    return fig

#####################################
def sales_mrr():
    darkpink = "#e68c96"
    lightpink = "#f3c6cb"
    green = "#6a9b65"
    lightgreen = "#c3d7c1"
    purple = "#af8ce6"
    blue = "#8c96e6"
    lightblue = "#8cbae6"
    yellow = "#ffcd00"

    data = sales_data.sort_values(by=["amount"], ascending=False)

    fig = px.bar(
        data[data["talk_week"].astype(str) > "2022-10-01"],
        x="talk_week",
        y="amount",
        color="sales",
        text="amount",

        color_discrete_sequence=[
            lightblue,
            darkpink,
            yellow,
            lightpink,
            lightgreen,
            purple,
            "lightgrey"
        ],
        category_orders=
        {"sales": [
            'Amandine Gervis',
            'Anis Smida',
            'Arthur Foulard',
            'Mégane Ausset',
            'Sacha Benibri',
            'Siham Ben Baroud',
            'Other'
        ]}
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor='rgba(0, 0, 0, 0)',
        title=f"Weekly new MRR per sales",
        title_x=.5,
        xaxis_title=None,
        legend_orientation='h',
        legend_y=-1.2,
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="black",
            font_size=12,
            font_family="Rockwell"
        ),
        xaxis=dict(
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )

    fig.update_traces(
        hovertemplate="%{y:}"
    )

    return fig

sales_mrr_code = '''```python         
fig = px.bar(
    data,
    x="talk_week",
    y="amount",
    color="sales",
    text="amount",

    color_discrete_sequence=[
        lightblue,
        darkpink,
        yellow,
        lightpink,
        lightgreen,
        purple,
        "lightgrey"
    ],
    category_orders=
    {"sales": [
        'Amandine Gervis',
        'Anis Smida',
        'Arthur Foulard',
        'Mégane Ausset',
        'Sacha Benibri',
        'Siham Ben Baroud',
        'Other'
    ]}
)

fig.update_layout(
    paper_bgcolor='rgba(0, 0, 0, 0)',
    title=f"Weekly new MRR per sales",
    title_x=.5,
    xaxis_title=None,
    legend_orientation='h',
    legend_y=-.14,
    hovermode="x unified",
    hoverlabel=dict(
        bgcolor="black",
        font_size=12,
        font_family="Rockwell"
    ),
    xaxis=dict(
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

fig.update_traces(
    hovertemplate="%{y:}"
)
```'''

#####################################


def abonnement():

    data = pd.read_csv("assets/data/abonnement_data.csv")
    data = data[data["talk_week"].astype(str) > "2022-10-01"]

    annuel = data[data["type_abonnement"] == "Annuel"]
    mensuel = data[data["type_abonnement"] == "Mensuel"]
    semestriel = data[data["type_abonnement"] == "Semestriel"]

    dfs = [
        annuel,
        mensuel,
        semestriel
    ]

    hoverlist = []

    for data_frame in dfs:

        hovertext_count = [i for i in data_frame["count"].astype(str)]
        hovertext_percentage = [i for i in round(data_frame["percentage"], 1).astype(str)]
        hovertext = []

        for i, j in zip(hovertext_count, hovertext_percentage):
            k = str(i) + ' | ' + str(j) + "%"
            hovertext.append(k)

        hoverlist.append(hovertext)

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=annuel["talk_week"],
        y=annuel["count"],
        text=annuel["percentage"],
        marker_color="#ffcd00",
        name="<b>Annuel</b>",
        hovertemplate=hoverlist[0],
        legendrank=3

    ))

    fig.add_trace(go.Bar(
        x=mensuel["talk_week"],
        y=mensuel["count"],
        text=mensuel["percentage"],
        marker_color="#e3b3ab",
        name="<b>Mensuel</b>",
        hovertemplate=hoverlist[1],
        legendrank=2

    ))

    fig.add_trace(go.Bar(
        x=semestriel["talk_week"],
        y=semestriel["count"],
        text=semestriel["percentage"],
        marker_color="#bfe3ab",
        name="<b>Semestriel</b>",
        hovertemplate=hoverlist[2],
        legendrank=1

    ))

    fig.update_layout(
        template="plotly_dark",
        title="Payment terms",
        title_x=.5,
        yaxis_title="Count",
        barmode='stack',
        hovermode="x unified",
        paper_bgcolor='rgba(0, 0, 0, 0)',
        legend_orientation='h',
        legend_y=-.14,
        hoverlabel=dict(
            bgcolor="black",
            font_size=12,
            font_family="Rockwell"
        ),
    )

    fig.update_traces(
        texttemplate='<b>%{text:,.2s}%</b>',
        textposition='inside',
        textfont_size=10,
        insidetextanchor="middle"
    )

    return fig

abonnement_string = '''```python
# Data
data = data[data["talk_week"].astype(str) > "2022-10-01"]

annuel = data[data["type_abonnement"] == "Annuel"]
mensuel = data[data["type_abonnement"] == "Mensuel"]
semestriel = data[data["type_abonnement"] == "Semestriel"]

dfs = [
    annuel,
    mensuel,
    semestriel
]

# Hover text
hoverlist = []

for data_frame in dfs:

    hovertext_count = [i for i in data_frame["count"].astype(str)]
    hovertext_percentage = [i for i in round(data_frame["percentage"], 1).astype(str)]
    hovertext = []

    for i, j in zip(hovertext_count, hovertext_percentage):
        k = str(i) + ' | ' + str(j) + "%"
        hovertext.append(k)

    hoverlist.append(hovertext)
    
# Figure
fig = go.Figure()

# 1st trace
fig.add_trace(go.Bar(
    x=annuel["talk_week"],
    y=annuel["count"],
    text=annuel["percentage"],
    marker_color="#ffcd00",
    name="<b>Annuel</b>",
    hovertemplate=hoverlist[0],
    legendrank=3

))

# 2nd trace
fig.add_trace(go.Bar(
    x=mensuel["talk_week"],
    y=mensuel["count"],
    text=mensuel["percentage"],
    marker_color="#e3b3ab",
    name="<b>Mensuel</b>",
    hovertemplate=hoverlist[1],
    legendrank=2

))

# 3rd trace
fig.add_trace(go.Bar(
    x=semestriel["talk_week"],
    y=semestriel["count"],
    text=semestriel["percentage"],
    marker_color="#bfe3ab",
    name="<b>Semestriel</b>",
    hovertemplate=hoverlist[2],
    legendrank=1

))

fig.update_layout(
    template="plotly_dark",
    title="Payment terms",
    title_x=.5,
    yaxis_title="Count",
    barmode='stack',
    hovermode="x unified",
    paper_bgcolor='rgba(0, 0, 0, 0)',
    legend_orientation='h',
    legend_y=-.14,
    hoverlabel=dict(
        bgcolor="black",
        font_size=12,
        font_family="Rockwell"
    ),
)

fig.update_traces(
    texttemplate='<b>%{text:,.2s}%</b>',
    textposition='inside',
    textfont_size=10,
    insidetextanchor="middle"
)
```'''

############# Line ###############

##########################


def area(data):
    #data = pd.read_csv("assets/data/twitter_final_agg.csv")
    #data["date"] = pd.to_datetime(data["date"])
    #data = data.set_index("date")

    #dff_final = df_final[df_final["ticker"] == ticker]

    fig = go.Figure(data=[

        go.Scatter(name='Negative', x=data.index, y=data["negative_percentage"], marker_color='red',
                   stackgroup='one'),

        go.Scatter(name='Neutral', x=data.index, y=data["neutral_percentage"], marker_color='lightgrey',
                   stackgroup='one'),

        go.Scatter(name='Positive', x=data.index, y=data["positive_percentage"], marker_color='green',
                   stackgroup='one')

    ])

    # Change the bar mode
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor='rgba(0, 0, 0, 0)',
        title_font_size=15,
        title_text='<b>Sentiment trend over time</b>',
        title_x=.5,
        xaxis_title=None,
        yaxis_title='Percentage %',
        hovermode="x",
        legend_orientation='h',
        legend_valign='middle',
        legend_x=.05,
        legend_y=-.15,

    )

    fig.update_traces(hovertemplate=None)

    return fig


area_string = '''```python
fig = go.Figure(data=[

    go.Scatter(name='Negative', x=data.index, y=data["negative_percentage"], marker_color='red',
               stackgroup='one'),

    go.Scatter(name='Neutral', x=data.index, y=data["neutral_percentage"], marker_color='lightgrey',
               stackgroup='one'),

    go.Scatter(name='Positive', x=data.index, y=data["positive_percentage"], marker_color='green',
               stackgroup='one')

])

# Change the bar mode
fig.update_layout(
    paper_bgcolor='rgba(0, 0, 0, 0)',
    title_font_size=15,
    title_text='<b>Sentiment trend over time</b>',
    title_x=.5,
    xaxis_title=None,
    yaxis_title='Percentage %',
    hovermode="x",
    legend_orientation='h',
    legend_valign='middle',
    legend_x=.05,
    legend_y=-.15,

)

fig.update_traces(hovertemplate=None)
```'''

