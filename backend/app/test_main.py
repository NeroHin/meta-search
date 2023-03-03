from .main import app
from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.getcwd())


client = TestClient(app)


def test_read_root():
    '''
        Description: test the root path
        Request: api_path/
        Response: 200, json
    '''
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "Welcome": "to the search engine API, Author: @NeroHin"}


def test_read_engine():
    '''
        Description: test the engine path
        Request: api_path/v1/engine
        Response: 200, json
    '''
    response = client.get("/api/v1/engine")
    assert response.status_code == 200
    assert response.json() == {"engine": [
        "duckduckgo", "web_search", "google_search"]}


def test_read_doc():
    '''
        Description: test the doc path
        Request: api_path/v1/doc
        Response: 200, True
    '''
    response = client.get("/docs")
    assert response.status_code == 200
    # test doc is not empty
    assert response is not None


def test_read_search():
    '''
        Description: test the search path
        Request: api_path/v1/search/{ search_keyword }
        Response: 200, True
    '''
    response = client.get("/api/v1/search/ncku")

    assert response.status_code == 200
    # test search result is not empty
    assert response.json() != {}
