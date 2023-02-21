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

    for result in ddg_top:
        ddg_top_title.append(result['title'])
        ddg_top_link.append(result['href'])

    return ddg_top_title, ddg_top_link


@app.get('/search/{keyword}')
def search(keyword: str):

    ddg_top_title, ddg_top_link = get_top3_ddg_result(keyword)

    return {'keyword': keyword, 'top3_title': ddg_top_title, 'top3_link': ddg_top_link}
