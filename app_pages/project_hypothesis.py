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

    st.error(
        f"**Validation**\n"
        f"* The accuracy and loss results produced by "
        f"this model shows that it did not perform as "
        f"well as the model trained with colour images. "
        f"model. We may therefore not"
        f" consider this hypothesis validated."
    )

    st.info(
        f"**Hypothesis 3**\n"
        f"* We hypothesized that an ML model which used "
        f"softmax as its activation function on the output " 
        f"layer would be less accurate than one which used "
        f"sigmoid."
    )

    st.success(
        f"**Validation**\n"
        f"* When the model trained using softmax was "
        f"trained and deployed ot the dashboard, it "
        f"proved unable to accurately predict whether "
        f"a leaf was infected or not. We may therefore "
        f"consider the hypothesis validated."   
    )
