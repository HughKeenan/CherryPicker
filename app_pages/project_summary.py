import streamlit as st
import matplotlib.pyplot as plt


def project_summary_body():
    """
    Display content for the Project Summary
    page
    """
    st.write("### Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a disease affecting several "
        f"plant species. "
        f"Caused by several species of ascomycete fungi, "
        f"it manifests as distictive "
        f"white spots on the leaves and stem of an infected plant.\n"
        f"* The disease grows best in environments where there "
        f"is a moderate temperature "
        f"and high humidity and is a common problem in horticultural crops, "
        f"where it is known to substantially reduce yields.\n"
        f"* The client is experiencing an outbreak of this disease "
        f"in several of its cherry tree plantations. "
        f"The current method of manually inspecting the trees has been "
        f"deemed time-inefficient. "
        f"The client has instead requested development of a Machine Learning "
        f"(ML) model "
        f"that will be able to predict based on uploaded photographs "
        f"whether a given leaf shows signs of infection."
        )

    st.info(
        f"**Dataset Information**\n"
        f"* The dataset provided by the client contains 4,208 images "
        f"of leaves taken from their cherry trees (2,104 each for both "
        f"healthy and infected leaves).\n"
        f"* It is available to download from "
        f"[Kaggle]"
        f"(https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)"
    )

    st.write(
        f"* For more information, please see the "
        f"[Project README file]"
        f"(https://github.com/HughKeenan/CherryPicker/blob/main/README.md).")

    st.success(
        f"**Business Requirements**\n"
        f"* The current method of dealing with this employed by the "
        f"client is to manually inspect the trees"
        f" for powdery mildew and treat them when it is found. The "
        f"ability to do this by use of phtographs"
        f" would cut down on time and expenses. The specific business "
        f"requirents are as follows:\n"
        f"* **Requirement 1** - The client is interested in conducting "
        f"a study to visually differentiate "
        f"a healthy cherry leaf from one with powdery mildew.\n"
        f"* In order to develop a system like the proposed one, it must "
        f"first be established that infected"
        f" and healthy leaves can be visually differentiated through "
        f"photographs. To this end we will analyse"
        f" pictures of infected and healthy leaves to see if there "
        f"are differences.\n"
        f"* **Requirement 2** - The client is interested in predicting "
        f"if a cherry leaf is healthy or contains "
        f" powdery mildew.\n"
        f"* Having established there is a visual difference between "
        f"healthy and infected leaves, a machine"
        f" learning model will be built using the results of our study "
        f"to predict whether an image uploaded"
        f" to it has powdery mildew or not."
        )
