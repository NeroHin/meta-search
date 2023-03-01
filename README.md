# Meta Search Engine
Meta-search engine: dispatch the user query to several search engines at the same time, collect and merge the results into one list for the user.
![Meta Search Engine](/images/what's-meta-search-engine.png)
## Scope
Homework: Develop a meta-search engine that responds to user queries with combined search results from a few search engines.

# HW requirements

- Using input component to get  query
 
- three search engines: Google, Web Search, DuckDuckGo

## Tech stack
![Tech stack](./images/tech-stack.png)
1. API Framework: FastAPI
2. Search Engine: Google CSE, WebSearch(RAPIDS), DuckDuckGo
3. Frontend: React


## Project architecture
![Project architecture](./images/HW-2-flowchart.png)

## Project Result
![Search by keyword 'ncku'](./images/wrdu-hw-2-result-1.png)
![Search by keyword 'chatgpt'](./images/wrdu-hw-2-result-2.png)

# How to run
1. Clone the repo
2. cd to the repo `cd meta-search`
3. run `docker-compose up`