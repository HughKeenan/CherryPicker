# Detection of mildew on cherry leaves

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset Content](#dataset-content)
3. [Business Requirements](#business-requirements)
4. [Hypotheses and validation](#hypotheses)
    1. [Hypothesis 1](#hypothesis-1)
    2. [Hypothesis 1 Validation](#hypothesis-1-validation)
    3. [Hypothesis 2](#hypothesis-2)
    4. [Hypothesis 2 Validation](#hypothesis-2-validation)
5. [The rationale to map the business requirements to the Data Visualizations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)
6. [ML business case](#ml-business-case)
7. [CRISP-DM](#crisp-dm)
8. [Dashboard Design](#dashboard-design)
9. [Unfixed Bugs](#unfixed-bugs)
10. [Deployment](#deployment)
    1. [Heroku](#heroku)
11. [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
12. [Credits]
    1. [Content](#content)
    2. [Media](#media)
13. [Acknowledgements](#acknowledgements)

## Introduction

Cherrypicker is a data science and machine learning (ML) project that uses predictive analytics to tell the difference between 2 different sets of images. The business goal is to assist the client, an agri-food business who is dealing with an infestation of powdery mildew in its cheery tree plantations. 

Currently the client is inspecting trees manually to determine whether they are infected or not and then treated if found to be diseased. This process is both labour intensive and time consuming. We propose the creation of a ML model that can determine from photographs of leaves whether mildew is present, reducing the amount of time taken to determine the status of the tree and enable sick trees to be treated with greater efficiency and accuracy. 

The project is hosted on the streamlit app and a live version may be found [here](https://cherry-picker-7809e87f232b.herokuapp.com/)

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). 
- The dataset contains over 4 thousand images taken from the client's cherry tree plantations. The imagesare divided into 2 sets, one of healthy leaves and one of leaves that are infected with powdery mildew. a fungal disease that affects many plant species. The client is concerned that the outbreak may be compromising the quality of their crop, which in turn would have serious ramifications for their business at large. 

[Back to top](#table-of-contents)

## Business Requirements

This project's main objective is to create a machine learning model that can detect whether a given tree has powdery mildew or not based on photographs uploaded to the dashboard as opposed to manual inspections of each tree, reducing costs in time and labour. This will result in more effective treatment and prevent a decline in crop quality. 

Key stakeholders for this are Farmy & Foods themselves, and their customers.

When considering the business requirements and how to meet them, attention must be paid to the following:

* The ML model produced must be accurate in its predictions of whether a leaf is infected or not
* The model should be able to handle multiple items concurrently
* The results produced from uploads must be easy to understand for both technical and non-technical personnel.
* The model must be able to return a prediction quickly

The specific requirements are as follows:

1. The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew. This should provide average images of both kinds of leaves, as well as a variability image for each.
2. The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew. To meet this requirement, a Convolutional Neural Network (CNN) should be developed to classify images as healthy or infected.

[Back to top](#table-of-contents)

## Hypotheses

### Hypothesis 1
Our first hypothesis is that there is a distinct visual difference between leaves where mildew is present and absent. It is our hypothesis that leaves with powdery mildew show a pattern of pale spots on the leaf. 

### Hypothesis 1 Validation

We intend to validate this by conducting a study of the image data provided by the client. We will create an average image of both healthy and infected leaves. Once compared we hope to be able to distinguish visually between the two using the ML model.

The below images show a selection of healthy leaves:

And leaves where powdery mildew is present:

Below also are the average and variability images for both kinds of leaves.

From the photographs, it appears that the hypothesis is correct and there is a visual difference. We may therefore consider the hypothesis validated.

### Hypothesis 2
Our second hypothesis is that the ML model will be just as accurate using grayscale images as colour ones.

It is possible that colour images may not be available in future. To prepare for this, we will test whether grayscale images may also be used.

### Hypothesis 2 Validation
To validate this, a second version of the ML model was created where during image augmentation, the color mode was set to grayscale. 

Below are the results for accuracy and loss when the model was trained using grayscale images:

And the generalised performance on the test set:

The results do not show a loss in accuracy. The model trained using grayscale images in fact performed marginally better than the one trained in colour.

[Back to top](#table-of-contents)

## The rationale to map the business requirements to the Data Visualisations and ML tasks

As stated above, we must take into consideration the accuracy of our results and the speed at which they are provided. It must also be scalable and easily understood.

- The business requirements are as follows:

**Requirement 1** - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.

This is an issue of classification between healthy leaves and those infected with mildew. We can map the requirements to our data visualisation and ML tasks through [User Stories](https://github.com/users/HughKeenan/projects/8). Please see this link for further detail, but in summary, the following relate to requirement 1: 

* As a data scientist I can collect & prepare data so that it can be used for analysis & training ML models.
To conduct an effective study, we must first acquire relevant data. The dataset acquired through Kaggle had to be downloaded, and then examined to ensure it contained no non-relevant data, for example as part of this process, a notebook was ran to remove any non-image files present in the dataset.

* As an end user, I can review a page of project findings so that I can receive more detailed information on what conclusions the development team came to.
The image visualizer page of the dashboard shows the results of our study, including the average images for healthy and sick leaves, and the variability in images for both. The study found that there are visual differences between them. 

* As an end user I can view a page detailing the project hypothesis so that I can understand the reasoning behind the developer's analysis
We hypothesised at the outset that there was a visual difference in healthy and sick leaves, which was validated by our analysis.

**Requirement 2** - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

The client wanted a dashboard that would let them upload images of leaves to the site and have an accurate reading of whether they were healthy or sick. This requirement was considered in the below user story:

* As an end user I can upload an image of a leaf so that I can learn if it is diseased or not. 
The mildew detector page enables the client to do this. They can upload images of the leaves which are then run through the ML model which can accurately predict whether or not powdery mildew is present.

[Back to top](#table-of-contents)

## ML Business Case

The client has requested a solution that will enable them to quickly and efficiently differentiate between healthy & diseased leaves. 

The aim behind the ML task is to develop a ML model that is able to distinguish a cherry leaf that is healthy from one that has powdery mildew.

The model will be trained to recognise the difference using a convolutional neural network. An ideal outcome to this would be a model that can predict with minimum 97% accuracy whether a leaf is infected or not, per the client's request. We may consider this successfully accomplished if it is capable of achieving an accuracy rating of at least 97% on the test dataset. If this is not accomplished, the model has failed.

The relevance to the user of this kind of ML model output is that it may be relied upon to deliver trustworthy readings when presented with new data. In addition, the model will output visuals such as the average image for healthy and sick leaves, which will provide a useful reference to the users.

The data is provided by the user and downloaded from Kaggle. It is split into train, test and validation subsets. It is confidential in nature and as such appropriate measures will be taken to protect it. It may only be downloaded from Kaggle if the data practitioner has the appropriate JSON key.

## CRISP-DM 

To effectively guide the development of this project, we adopt the Cross-Industry Standard Process for Data Mining (CRISP-DM), which provides a methodology over 6 steps:

1. Business Understanding

Before beginning data mining efforts, it is important to understand what the client expects to gain from them. This begins with setting business goals and examining where the client stands in relation to those at present. A plan must then be written out and goals set for data mining specifically.

To meet this requirement, we have agreed business requirements with the client and prepared our [User Stories](https://github.com/users/HughKeenan/projects/8)

2. Data Understanding

Having completed step 1, we can look to the available data. Data must be collected and explored, and its quality must be verified. 

Data was collected from Kaggle

3. Data Preparation

As it is unlikely that all data collected will be fit for purpose, it must next be prepared. This can take the form of removing irrelvant data or imputation of missing data, among other options

4. Modelling

Having processed the data, a machine learning model may be developed. An appropriate technique must be selected and tested with the available data. Different combinations of hyperparameters should be tried

5. Evaluation

The ML model should then be evaluated, against training and validation sets to determine accuracy, and then against the test set to see how it performs on unfamiliar data.

6. Deployment

Finally, it should be deployed on an appropriate platform


## Dashboard Design

The dashboard was made using streamlit and has been designed with clarity and ease of use in mind. It contains the following pages:

1. Dashboard information 

* General Information
* Dataset Information
* Link to project README 
* Business Requirements

This is the introductory page the user will see on accessing the dashboard. Its intended purpose is to provide a new user with essential information both general and specific, so that they may gain a full understanding of the project before proceeding to more technical pages.

The general information provided is there to inform users about the nature of powdery mildew and its implications for the client's business, as well as the reason for the project's inception.

It also provides more specific information concerning the dataset and provides a link to where it might be downloaded, as well as a summary of the buiness requirements.

2. Project Findings 

* Business requirement 1
* Checkbox 1 - Difference between average and variability image
* Checkbox 2 - Differences between average healthy and average infected leaves
* Checkbox 3 - Image Montage

This page is intended to anwer buiness requirement 1: the client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew. To this end it provides options for what the user may wish to see; it can display an image montage of healthy or infected leaves, as well as the results of an analysis of the images. The page displays the average image & variability image for healthy & diseased leaves as well as the differences between the average images for both and the difference between the variability images.

3. Mildew Detector 

* Business requirement 2
* Link to Kaggle dataset
* Widget to upload images for analyis
* Link to download report in .csv format

This page answers business requirement 2: the client is interested in predicting if a cherry leaf is healthy or contains powdery mildew. The page contains a link to the Kaggle page where an authorised user will here be able to download a clean dataset. It also allows a user to upload images of either kind of leaf to receive an analysis of its status.

4. Project Hypothesis 

* Project Hypothesis
* Validation

This page displays the project hypothesis and  explaines the method by which it was validated

5. Performance Metrics 

* Train, Validation and Test Set: Labels Frequencies
* Model History
* Generalised Performance on test set

This page shows the results of our analysis.The page explains how the dataset was used for testing purposes. It also shows the results of the ML model training, including graphics to show model accuracy and loss on the training and validation set, and an explanation of the graphs. It also shows how the model performed on the test set after it had been trained, and explains what that means for the business requirements.

## Unfixed Bugs
During ML model training, a bug was encountered where data would run out during the second epoch.

## Deployment

### Heroku

- The App live link is: `https://cherry-picker-7809e87f232b.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries
The main libraries used were: 
* numpy 1.26.1 - used to convert information to arrays
* pandas 2.1.1 - used for converting information to a dataframe and saving as such
* matplotlib 3.4.0 - used to plot the distribution of datasets
* seaborn 0.13.2 - used for making statistical graphics
* plotly 5.10.0 - used for plotting results of ML model training
* Pillow 10.0.1 - used to adjust images
* streamlit 1.40.2 - used to create the dashboard's interface
* scikit-learn 1.3.1 - used for model evaluation
* tensorflow-cpu 2.16.1 - used for model creation
* keras 3.0.0 - used to set hyperparameters for the model

## Credits

### Content

- Information on powdery midlew was taken from https://en.wikipedia.org/wiki/Powdery_mildew
- The dataset was created by Code institute and taken from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves)
- The Malaria Walkthrough Project from Code Institute was used as a guide when assembling this project.

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements

- I would like to acknowledge my mentor, Mo Shami, who provided valuable insights and guidance during the project.
