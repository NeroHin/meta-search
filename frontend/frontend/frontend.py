"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config
import requests
import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):

    search_header: str = "WRDE HW2 'Meta Search Engine'"
    search_input_placeholder: str = "Enter your search term here"
    search_input: str
    search_result: any

    def clear_search_input(self):
        self.search_input = ""

    def fetch_search_api(self):
        # use requests to get the search result from the backend
        search_result_text = requests.get(f"http://localhost:8001/api/v1/search/{self.search_input}").json()
        self.search_result = search_result_text

        return self.search_result


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Welcome to Pynecone!", font_size="2em"),
            pc.box("Get started by editing ",
                   pc.code(filename, font_size="1em")),
            pc.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )


def search():
    return pc.center(
        pc.vstack(
            pc.heading(State.search_header, font_size="2em"),
            pc.center(

                pc.input(
                    placeholder=State.search_input_placeholder,
                    value=State.search_input,
                    on_change=State.set_search_input,
                ),
            ),
            pc.button_group(
                pc.button(
                    "Search", on_click=State.fetch_search_api
                ),
                pc.button(
                    "Clear", on_click=State.clear_search_input
                ),
            ),
            pc.text(State.search_result),
            pc.flex(
                pc.table_container(
                    pc.table(
                        headers=["Title", "Url"],
                        rows=[
                            ("John", 30),
                            ("Jane", 31),
                            ("Joe", 32),
                        ],
                    )
                ),
                pc.table_container(
                    pc.table(
                        headers=["Title", "Url"],
                        rows=[
                            ("John", 30),
                            ("Jane", 31),
                            ("Joe", 32),
                        ],
                    )
                ),
                pc.table_container(
                    pc.table(
                        headers=["Title", "Url"],
                        rows=[
                            ("John", 30),
                            ("Jane", 31),
                            ("Joe", 32),
                        ],
                    )
                ),
                # add some space between the two tables with css
                style={"gap": "3em"},
                
            ),
            spacing="1.5em",
            font_size="1em",
        ),
        padding_top="10%",

    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.add_page(search, route="/search")
app.compile()
