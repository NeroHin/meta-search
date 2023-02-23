# Meta Search Engine
Meta-search engine: dispatch the user query to several search engines at the same time, collect and merge the results into one list for the user.
![Meta Search Engine](/images/what's-meta-search-engine.png)
## Scope
Homework: Develop a meta-search engine that responds to user queries with combined search results from a few search engines.

# HW requirements

- Using input component to get  query
 
- three search engines: Google, Baidu, DuckDuckGo

## Bonus
- 送不同 Type 的 Search Engine （Bonus）
  - Text、Video、Image
- 串 Chat-GPT （Bonus）

## Tech stack
1. API Framework: FastAPI
2. Search Engine: Google CSE, WebSearch(RAPIDS), DuckDuckGo
3. Frontend: React

## Project architecture
![Project architecture](./images/HW-2-flowchart.png)


# How to run
1. Clone the repo
2. Install dependencies
   - Backend: `pip install -r requirements.txt`
   - Frontend: `cd frontend && npm install`
3. Run the backend
   - `uvicorn main:app --reload`
- 4. Run the frontend
   - `cd frontend && npm start`