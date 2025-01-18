import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def ml_performance_metrics():
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')

    st.info(
        f"* The dataset was divided into 3 parts, a train set, a test set, and a validation set"
        f"This is the most common way to proportion data for Machine Learning.\n"
        f"* The train set, being the largest, was the first data the ML model was introduced to."
        f" The larger size of this dataset ensures that the model will be exposed to a sufficient amount of data"
        f" that it will be able to fully learn the difference between both kinds of images.\n"
        f"* The validation set was then used to improve the model's performance.\n"
        f"* Finally, the test set was used as a final check to ensure that the model can handle new data and that"
        f" it had learned as intended."
    )
    st.write("---")


    st.write("### Model History")
    col1, col2 = st.columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')

    st.info(
        f"* As the above graphs show, the model performed generally at a high level of accuracy.\n"
        f"* Initial performance on the training set improved quickly in the first few epochs. "
        f"Despite a drop in performance at epoch 7, the model regained accuracy in the next one"
        f" and continued to improve.\n"
        f"* The graph for loss, which indicates how well a model performs by examining how different"
        f" the predictions it makes are from the truth, shows that the model performed well on both"
        f" the training and validation sets. Overfitting has also been kept to a minimum."
    )

    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))
    st.info(
        f"* The client at the outset of this project requested a ML model that could predict"
        f" with 97% accuracy whether a leaf had mildew or note based on the image.\n"
        f"* As the above table shows, the model predicted with 99% accuracy the status of"
        f" images in the test dataset. We may therefore consider this requirement satisfied."
    )