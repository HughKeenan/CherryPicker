import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.project_summary import project_summary_body
from app_pages.image_visualizer import image_visualizer_body

app = MultiPage(app_name="Cherry Picker")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Project Summary", project_summary_body)
app.add_page("Image Visualizer", image_visualizer_body)


app.run()  # Run the app