import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random


def image_visualizer_body():
    """
    Display average and variability images
    for both kinds of leaves
    """
    st.write("### Image Visualizer")
    st.info(
      f"* This page will examine Business Requirement 1.\n"
      f"* The client is interested in conducting a study to visually "
      f"differentiate a healthy leaf from one with powdery mildew.")

    version = 'v1'
    if st.checkbox("Difference between average and variability image"):

        avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")
        avg_mildew = plt.imread(f"outputs/{version}/"
                                f"avg_var_powdery_mildew.png")

        st.image(avg_healthy,
                 caption='Healthy Leaf - Average and Variability')
        st.image(avg_mildew,
                 caption='Infected Leaf - Average and Variability')

        st.warning(
          f"* The images, particularly the variability images, "
          f"do make it possible "
          f"to differentiate healthy and diseased leaves."
          f"The white spots created by the mildew create a pattern"
          f" across the leaf that is visible in the "
          f"variability image for diseased leaves.\n"
          f"* Additionally, the average images show a difference in "
          f"colour between"
          f" the healthy & infected leaves, with"
          f" infected leaves being a lighter shade of green."
          )

        st.write("---")

    if st.checkbox("Differences between average healthy and infected leaves"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

        st.warning(
          f"* The study uncovered slight differences in "
          f"patterns that allowed us to "
          f"differentiate healthy & infected leaves.")
        st.image(diff_between_avgs,
                 caption='Difference between average images')
        st.write("---")

    if st.checkbox("Image Montage"):
        st.write("* To refresh the montage, click the 'Create Montage' button")
        my_data_dir = 'inputs/cherry_leaves_dataset/cherry-leaves'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(label="Select label",
                                        options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(dir_path=my_data_dir + '/validation',
                          label_to_display=label_to_display,
                          nrows=8, ncols=3, figsize=(10, 25))
        st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    """
    Display image montage of requested image type
    """
    sns.set_style("white")
    labels = os.listdir(dir_path)

    if label_to_display in labels:
        images_list = os.listdir(dir_path + '/' + label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return

        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows*ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0],
                 plot_idx[x][1]].set_title(f"{img_shape[1]}px x"
                                           f" {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)

    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")
