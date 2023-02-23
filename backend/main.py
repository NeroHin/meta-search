import http.client
from duckduckgo_search import ddg
import requests
from typing import Optional
import json
from fastapi import FastAPI
from duckduckgo_search import ddg

# create a FastAPI instance
app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello: World'}


def get_top_ddg_result(keyword: Optional[str], top_number: int = 3):
    '''
        input: keyword, top_number
        process: get top_number of ddg search result
        output: top_number of ddg search result title and link

    '''

    ddg_result = ddg(keywords=keyword, region="tw-tzh", safesearch='Off')

    ddg_top = ddg_result[:top_number]
    ddg_top_title = []
    ddg_top_link = []
    ddg_top_description = []

    for result in ddg_top:
        ddg_top_title.append(result['title'])
        ddg_top_link.append(result['href'])
        ddg_top_description.append(result['body'])

    return ddg_top_title, ddg_top_link, ddg_top_description


def get_top_web_search_result(keyword: Optional[str], top_number: int = 3):
    '''
        input: keyword, top_number
        process: get top_number of web search result
        output: top_number of web search result title and link

    '''

    conn = http.client.HTTPSConnection(
        "contextualwebsearch-websearch-v1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "416132865dmshcd8a00c90d4dc07p13519ajsn32f2dc6b7525",
        'X-RapidAPI-Host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
    }

    conn.request(
        "GET", f"/api/Search/WebSearchAPI?q={ keyword }&pageNumber=1&pageSize={ top_number }&autoCorrect=true", headers=headers)

    res = conn.getresponse()
    data = res.read()
    search_result = json.loads(data.decode("utf-8"))["value"]

    web_search_result_title = []
    web_search_result_link = []
    web_search_result_description = []

    for result in search_result:
        web_search_result_title.append(result['title'])
        web_search_result_link.append(result['url'])
        web_search_result_description.append(result['description'])

    return web_search_result_title, web_search_result_link, web_search_result_description


@app.get('/search/{keyword}')
def search(keyword: str):

    ddg_top_title, ddg_top_link, ddg_top_description = get_top3_ddg_result(
        keyword=keyword)
    web_search_result_title, web_search_result_link, web_search_result_description = get_top3_web_search_result(
        keyword=keyword)

    return {'keyword': keyword, 'ddg_top_title': ddg_top_title, 'ddg_top_link': ddg_top_link, 'ddg_top_description': ddg_top_description, 'web_search_result_title': web_search_result_title, 'web_search_result_link': web_search_result_link, 'web_search_result_description': web_search_result_description}
