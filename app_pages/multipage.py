import streamlit as st


class MultiPage:
    """
    Genrates Multiple pages on Streamlit dashboard
    """
    def __init__(self, app_name) -> None:
        """
        Create array for pages and 
        display title and favicon
        """
        self.pages = []
        self.app_name = "Cherry Leaf Powdery Mildew Detector"

        st.set_page_config(
            page_title=self.app_name,
            page_icon=":deciduous_tree:")

    def add_page(self, title, func) -> None:
        """
        Add pages to app
        """
        self.pages.append({"title": title, "function": func})

    def run(self):
        """
        Page titles in sidebar
        """
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages,
                                format_func=lambda page: page['title'])
        page['function']()
