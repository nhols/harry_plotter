import requests
import json


def build_omdb_query(query_params):
    query = '&'.join(f"{key}={val}" for (key, val) in query_params.items())
    return f'http://www.omdbapi.com/?{query}'


def get_omdb_respone(query_params):
    url = build_omdb_query(query_params)
    resp = json.loads(requests.get(url).text)
    return resp


def get_all_episodes(query_params):
    data_out = dict()
    series_resp = get_omdb_respone(query_params)
    data_out['series_data'] = series_resp
    data_out['season_data'] = dict()

    for s in range(1, int(series_resp['totalSeasons'])+1):
        query_params['season'] = s
        season_resp = get_omdb_respone(query_params)
        data_out['season_data'][s] = season_resp

    return data_out
