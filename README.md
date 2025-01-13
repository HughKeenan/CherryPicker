# Detection of mildew on cherry leaves

## Introduction

The client, an agri-food business, is facing difficulties with an outbreak of powdery midew on its cherry tree plantations. At present, trees must be inspected manually to determine whether they are disease free or not and then treated if mildew is found. This process is both labour intensive and time consuming. Our proposition is to create a Machine Learning (ML) model that can determine from photographs of cherry leaves whether mildew is present or not, reducing the amount of time taken to determine the status of the tree and enable sick trees to be treated with greater efficiency and accuracy. 

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). 
- The dataset contains over 4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis

- Our hypothesis is that leaves where mildew is present show a pattern of pale spots on the leaf. 

Powdery mildew presents itself as a pattern of white patches on leaves where the fungal infection is present.

### Validation

We intend to validate this by conducting a study of the image data provided by the client. We will create an average image of both healthy and infected leaves. Once compared we hope to be able to distinguish visually between the two using the ML model.

The below images show a selection of healthy leaves:

And leaves where powdery mildew is present:

Below also are the average and variability images for both kinds of leaves.

From the photographs, it appears that the hypothesis is correct and there is a visual difference. We may therefore consider the hypothesis validated.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

- The business requirements are as follows:

1. The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.

This is an issue of classification between healthy leaves and those infected with mildew. We can map the requirements to our data visualisation and ML tasks through [User Stories](https://github.com/users/HughKeenan/projects/8). Please see this link for further detail, but in summary, the following relate to requirement 1: 

* As a data scientist I can collect & prepare data so that it can be used for analysis & training ML models.
To conduct an effective study, we must first acquire relevant data. The dataset acquired through Kaggle had to be downloaded, and then examined to ensure it contained no non-relevant data, for example as part of this process, a notebook was ran to remove any non-image files present in the dataset.

* As an end user, I can review a page of project findings so that I can receive more detailed information on what conclusions the development team came to.
The image visualizer page of the dashboard shows the results of our study, including the average images for healthy and sick leaves, and the variability in images for both. The study found that there are visual differences between them. 

* As an end user I can view a page detailing the project hypothesis so that I can understand the reasoning behind the developer's analysis
We hypothesised at the outset that there was a visual difference in healthy and sick leaves, which was validated by our analysis.

2. The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

The client wanted a dashboard that would let them upload images of leaves to the site and have an accurate reading of whether they were healthy or sick. This requirement was considered in the below user story:

* As an end user I can upload an image of a leaf so that I can learn if it is diseased or not. 
The mildew detector page enables the client to do this. They can upload images of the leaves which are then run through the ML model which can accurately predict whether or not powdery mildew is present.


## ML Business Case

The client has requested a solution that will enable them to quickly and efficiently differentiate between healthy & diseased leaves. 

The aim behind the ML task is to develop a ML model that is able to distinguish a cherry leaf that is healthy from one that has powdery mildew.

The model will be trained to recognise the difference using a convolutional neural network. An ideal outcome to this would be a model that can predict with minimum 97% accuracy whether a leaf is infected or not, per the client's request. We may consider this successfully accomplished if it is capable of achieving an accuracy rating of at least 97% on the test dataset. If this is not accomplished, the model has failed.

The relevance to the user of this kind of ML model output is that it may be relied upon to deliver trustworthy readings when presented with new data. In addition, the model will output visuals such as the average image for healthy and sick leaves, which will provide a useful reference to the users.

The data is provided by the user and downloaded from Kaggle. It is split into train, test and validation subsets. It is confidential in nature and as such appropriate measures will be taken to protect it. It may only be downloaded from Kaggle if the data practitioner has the appropriate JSON key.

### CRISP-DM 

## Dashboard Design

The dashboard contains the following pages:

- Dashboard information: This page contains a summary of the project and the dataset as well as a list of objectives
- Project Findings: Displays an analysis of healthy & diseased leaves, an analysis of the difference between the average image & variability image for healthy & diseased leaves and an image montage of both kinds on request
- Image Analysis: The user will here be able to download a clean dataset and upload images of either kind of leaf to receive an analysis of its status
- Project Hypothesis: Displays the project hypothesis and the method by which it was validated
- Performance Metrics: This will show the results of our analysis, including graphics to show model accuracy, and how it performed on the test dataset as well as an explanation of what the metrics mean.

## Unfixed Bugs

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


## Credits

### Content

- Information on powdery midlew was taken from https://en.wikipedia.org/wiki/Powdery_mildew

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements (optional)

- Thank the people who provided support throughout this project.
