import requests
import json
import re
from lib import mock_data

def _fetch_data(keyword):
    response = requests.get("http://www.google.com/trends/fetchComponent?q="+ keyword +"&cid=TIMESERIES_GRAPH_0&export=3").content.decode("utf-8")
    start = response.index("{")
    end = len(response) - response[::-1].index("}")
    data = json.loads(re.sub(r'new Date\([0-9]+,[0-9]+,[0-9]+\)' ,"0",response[start:end]))
    return data

def _fetch_mock(keyword):
    return mock_data.MOCK_DATA

def _parse_data(data):
    parsed_data = []
    for c in data["table"]["rows"]:
        parsed_data.append(c["c"][1]["v"])

    return parsed_data

def fetch_trend_vector(keyword, mock=False):
    '''
    Returns a list of numbers. Set mock=True to use mock data and avoid hitting the request limit of Google Trends.
    '''
    fetch = _fetch_mock if mock else _fetch_data
    data = fetch(keyword)

    return _parse_data(data)

