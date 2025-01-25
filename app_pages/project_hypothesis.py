import streamlit as st
import matplotlib.pyplot as plt


def project_hypothesis_body():
    """
    Display content for Project Hypothesis Page
    """
    st.write("### Project Hypotheses")

    st.info(
        f"**Hypothesis 1**\n"
        f"* We hypothesised that powdery mildew "
        f"would manifest as a pattern of "
        f"white spots on leaves infected with it."
    )

    st.success(
        f"**Validation**\n"
        f"* Analysis of the average image data for "
        f"all leaves infected with powdery"
        f" mildew shows that such a pattern is "
        f"present on infected leaves."
    )

    st.info(
        f"**Hypothesis 2**\n"
        f"* We hypothesized that an ML model trained "
        f"using grayscale image would be just "
        f"as accurate as one trained using color images."
    )

    st.success(
        f"**Validation**\n"
        f"* Evaluation of the ML model using the test "
        f"set shows that it"
        f" performed marginally better than the original "
        f"model. We may therefore"
        f" consider this hypothesis validated."
    )
