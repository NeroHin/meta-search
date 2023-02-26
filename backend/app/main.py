import http.client
from duckduckgo_search import ddg
import requests
from typing import Optional
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import urllib.parse

# create a FastAPI instance
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return {'Hello: World'}


def get_top_ddg_result(keyword: Optional[str], top_number: int = 3):
    '''
        input: keyword, top_number
        process: get top_number of ddg search result
        output: top_number of ddg search result title and link

    '''

    ddg_result = ddg(keywords=keyword, safesearch='Off', region="t")

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


def get_top_google_search_result(keyword: Optional[str], top_number: int = 3):

    # get the API KEY here: https://developers.google.com/custom-search/v1/overview
    API_KEY = "AIzaSyAEltei7_fvI0S1CIxyhg_4QMBgPzcdtlk"
    # get your Search Engine ID on your CSE control panel
    SEARCH_ENGINE_ID = "13c5e1a0875b947ba"

    # using the first page
    page = 1

    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={keyword}"

    # make the API request
    data = requests.get(url).json()

    # get the result items
    search_items = data.get("items")

    # initialize the result lists
    google_result_title = []
    google_result_link = []
    google_result_description = []

    # select the title, link and snippet with top_number
    for item in search_items[:top_number]:
        google_result_title.append(item["title"])
        google_result_link.append(item["link"])
        google_result_description.append(item["snippet"].replace("\xa0", ""))

    return google_result_title, google_result_link, google_result_description


@app.get('/search/{keyword}')
def search(keyword: str):
    
    # encode the keyword with utf-8
    
    keyword = urllib.parse.quote(keyword)

    ddg_result_title, ddg_result_link, ddg_result_description = get_top_ddg_result(
        keyword=keyword)
    web_search_result_title, web_search_result_link, web_search_result_description = get_top_web_search_result(
        keyword=keyword)
    google_result_title, google_result_link, google_result_description = get_top_google_search_result(
        keyword=keyword)

    return {"duckduckgo": {"title": ddg_result_title, "link": ddg_result_link, "description": ddg_result_description},
            "web_search": {"title": web_search_result_title, "link": web_search_result_link, "description": web_search_result_description},
            "google_search": {"title": google_result_title, "link": google_result_link, "description": google_result_description}}


if __name__ == '__main__':

    uvicorn.run(app)
