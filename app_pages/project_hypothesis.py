import streamlit as st
import matplotlib.pyplot as plt


def project_hypothesis_body():
    st.write("### Project Hypotheses")

    st.info(
        f"**Hypothesis 1**\n"
        f"* We hypothesised that powdery mildew would manifest as a pattern of "
        f"white spots on leaves infected with it."
    )

    st.success(
        f"**Validation**\n"
        f"* Analysis of the average image data for all leaves infected with powdery"
        f" mildew shows that such a pattern is present on infected leaves."
    )

    st.info(
        f"**Hypothesis 2**\n"
        f"* We hypothesized that an ML model trained using grayscale image would be just "
        f"as accurate as one trained using color images."
    )

    st.success(
        f"**Validation**\n"
        f"* Evaluation of the ML model using the test set shows that it"
        f" performed marginally better than the original model. We may therefore"
        f" consider this hypothesis validated."
    )

    st.info(
        f"**Hypothesis 3**\n"
        f"* We hypothesized that an ML model which used softmax as an activation funstion would"
        f" perform as well as one that used sigmoid."
    )

    st.error(
        f"**Validation**\n"
        f"* Evaluation of the ML model using the test set shows that it"
        f" performed several orders of magnitude waorse tha the original. We may therefore"
        f" not consider this hypothesis validated."
    )
