import omdb_api
import plotly.graph_objects as go
import plotly.offline
from plotly.subplots import make_subplots

def build_hover_label(d):
    return '<br>'.join([f'{k}: {v}' for k, v in d.items()])

def build_go_scatter(series_data):
    ratings = []
    ep_info = []
    for s in series_data['season_data'].keys():
        [ratings.append(ep['imdbRating']) for ep in series_data['season_data'][s]['Episodes']]
        [ep_info.append(build_hover_label(ep)) for ep in series_data['season_data'][s]['Episodes']]

    trace_ret = go.Scatter(y=ratings,
                           mode='lines+markers',
                           line={'shape': 'hv'},
                           name=series_data['series_data']['Title'],
                           text=ep_info,
                           connectgaps=True
                           )
    return trace_ret

def series_subplotter(data):

    fig = make_subplots(rows=len(data), cols=1,
                        subplot_titles=[d['series_data']['Title'] for d in data])

    for i in range(len(data)):

        try:
            fig.append_trace(build_go_scatter(data[i]), row=i + 1, col=1)
        except:
            print(f'error creating plots for {data[i]["series_data"]["Title"]}')

    fig.update_layout(showlegend=False)
    fig.update_xaxes(showticklabels=False)

    return fig

if __name__ == '__main__':
    import pickle

    with open('listfile.data', 'rb') as filehandle:
        data = pickle.load(filehandle)

    fig = series_subplotter(data)
    plotly.offline.plot(fig, filename='p1.html')