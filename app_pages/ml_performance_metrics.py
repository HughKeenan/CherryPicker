import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def ml_performance_metrics():
    """
    Display text and images for
    the Performance Metrics page
    """
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    distribute_label = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(distribute_label,
             caption='Labels Distribution on Train, Validation and Test Sets')

    st.info(
        f"* The dataset was divided into 3 parts, "
        f"a train set, a test set, and a validation set"
        f"This is the most common way to proportion data for "
        f"Machine Learning.\n"
        f"* The train set, being the largest, was the first "
        f"data the ML model was introduced to."
        f" The larger size of this dataset ensures that the "
        f"model will be exposed to a sufficient amount of data"
        f" that it will be able to fully learn the difference "
        f"between both kinds of images.\n"
        f"* The validation set was then used to improve "
        f"the model's performance.\n"
        f"* Finally, the test set was used as a final check "
        f"to ensure that the model can handle new data and that"
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
        f"* As the above graphs show, the model performed "
        f"generally at a high level of accuracy.\n"
        f"* Initial performance on the training set "
        f"improved quickly in the first few epochs. "
        f"Despite a drop in performance at epoch 7, "
        f"the model regained accuracy in the next one"
        f" and continued to improve.\n"
        f"* The graph for loss, which indicates how well "
        f"a model performs by examining how different"
        f" the predictions it makes are from the truth, "
        f"shows that the model performed well on both"
        f" the training and validation sets. Overfitting has "
        f"also been kept to a minimum."
    )

    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version),
                 index=['Loss', 'Accuracy']))
    st.info(
        f"* The client at the outset of this project "
        f"requested a ML model that could predict"
        f" with 97% accuracy whether a leaf had mildew "
        f"or note based on the image.\n"
        f"* As the above table shows, the model predicted "
        f"with 99% accuracy the status of"
        f" images in the test dataset. We may therefore "
        f"consider this requirement satisfied."
    )
