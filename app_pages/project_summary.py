import streamlit as st
import matplotlib.pyplot as plt


def project_summary_body():

    st.write("### Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a disease affecting several plant species. "
        f"Caused by several species of ascomycete fungi, it manifests as distictive "
        f"white spots on the leaves and stem of an infected plant.\n"
        f"* The disease grows best in environments where there is a moderate temperature "
        f"and high humidity and is a common problem in horticultural crops, "
        f"where it is known to substantially reduce yields.\n"
        f"* The client is experiencing an outbreak of this disease "
        f"in several of its cherry tree plantations. "
        f"The current method of manually inspecting the trees has been deemed time-inefficient."
        f"The client has instead requested development of a Machine Learning (ML) model "
        f"that will be able to predict based on uploaded photographs "
        f"whether a given leaf shows signs of infection."
        )

    st.info(
        f"**Dataset Information**\n"
        f"* The dataset provided by the client contains 4,208 images "
        f"of leaves taken from their cherry trees (2,104 each for both healthy and infected leaves).\n"
        f"* It is available to download from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)"
    )

    st.write(
        f"* For more information, please see the "
        f"[Project README file](https://https://github.com/HughKeenan/CherryPicker/blob/main/README.md).")
    

    st.success(
        f"**Business Requirements**\n"
        f"* 1 - The client is interested in conducting a study to visually differentiate "
        f"a healthy cherry leaf from one with powdery mildew.\n"
        f"* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew. "
        )