import omdb_api
import plotly.graph_objects as go
import plotly.offline
from plotly.subplots import make_subplots
import numpy as np


def build_hover_label(d):
    return '<br>'.join([f'{k}: {v}' for k, v in d.items()])


def build_go_scatter(series_data):
    ratings = []
    ep_info = []
    x = []
    for s in series_data['season_data'].keys():
        eps_in_season = len(series_data['season_data'][s]['Episodes'])
        [ratings.append(ep['imdbRating']) for ep in series_data['season_data'][s]['Episodes']]
        [ep_info.append(build_hover_label(ep)) for ep in series_data['season_data'][s]['Episodes']]
        [x.append(s + i / eps_in_season) for i in range(eps_in_season)]

    ratings = [np.nan if r == 'N/A' else float(r) for r in ratings]
    min_rating = min(ratings)
    trace_seasons = []
    for s in series_data['season_data'].keys():
        trace_season = go.Scatter(x=[s, s],
                                  y=[min_rating, 10],
                                  mode="lines",
                                  legendgroup="b",
                                  showlegend=False,
                                  line=dict(color='white',
                                            width=.7),
                                  hoverinfo="text",
                                  text=f"Season {s}")
        trace_seasons.append(trace_season)

    trace_ratings = go.Scatter(y=ratings, x=x,
                               mode='lines+markers',
                               line=dict(shape='hv',
                                         color='white',
                                         width=.5),
                               marker=dict(color=[float(r) for r in ratings],
                                           colorscale='RdYlGn',
                                           cmin=5,
                                           cmax=10,
                                           size=5,
                                           opacity=.7),
                               name=series_data['series_data']['Title'],
                               hoverinfo="text",
                               text=ep_info,
                               connectgaps=True)

    return trace_ratings, trace_seasons


def series_subplotter(data):
    fig = make_subplots(rows=len(data), cols=1,
                        row_titles=[d['series_data']['Title'] for d in data],
                        vertical_spacing=0)

    for i in range(len(data)):

        try:
            trace_ratings, trace_seasons = build_go_scatter(data[i])
            fig.append_trace(trace_ratings, row=i + 1, col=1)
            for trace_season in trace_seasons:
                fig.append_trace(trace_season, row=i + 1, col=1)

        except:
            print(f'error creating plots for {data[i]["series_data"]["Title"]}')

    fig.update_layout(showlegend=False,
                      plot_bgcolor='rgba(0,0,0,0)',
                      paper_bgcolor='black')
    fig.update_xaxes(showticklabels=False,
                     showgrid=False,
                     zeroline=False)
    fig.update_yaxes(showticklabels=False,
                     showgrid=False,
                     zeroline=False)
    for i in fig['layout']['annotations']:
        i['font']['size'] = 10
        i['font']['color'] = 'white'

    return fig


if __name__ == '__main__':
    import pickle

    with open('listfile.data', 'rb') as filehandle:
        data = pickle.load(filehandle)

    fig = series_subplotter(data)
    plotly.offline.plot(fig, config={'scrollZoom': True}, filename='p1.html')
