import streamlit as st
import matplotlib.pyplot as plt


def project_hypothesis_body():
    st.write("### Project Hypothesis")

    st.info(
        f"* We hypothesised that powdery mildew would manifest as a pattern of "
        f"white spots on leaves infected with it."
    )

    st.write("### Validation")

    st.success(
        f"* Analysis of the average image data for all leaves infected with powdery"
        f" mildew shows that such a pattern is present on infected leaves."
    )
