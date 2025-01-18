import streamlit as st
from app_pages.multipage import MultiPage

# pages scripts
from app_pages.project_summary import project_summary_body
from app_pages.image_visualizer import image_visualizer_body
from app_pages.mildew_detector import mildew_detector_body
from app_pages.project_hypothesis import project_hypothesis_body
from app_pages.ml_performance_metrics import ml_performance_metrics

app = MultiPage(app_name="Cherry Picker")  # Create an instance of the app

# app pages
app.add_page("Project Summary", project_summary_body)
app.add_page("Image Visualizer", image_visualizer_body)
app.add_page("Mildew Detector", mildew_detector_body)
app.add_page("Project Hypothesis", project_hypothesis_body)
app.add_page("ML Performance Metrics", ml_performance_metrics)

app.run()