# Detection of mildew on cherry leaves

![Responsivity image](/assets/images/dashboard_responsivity.png)

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset Content](#dataset-content)
3. [Business Requirements](#business-requirements)
4. [Hypotheses and validation](#hypotheses)
    1. [Hypothesis 1](#hypothesis-1)
    2. [Hypothesis 1 Validation](#hypothesis-1-validation)
    3. [Hypothesis 2](#hypothesis-2)
    4. [Hypothesis 2 Validation](#hypothesis-2-validation)
    5. [Hypothesis 3](#hypothesis-3)
    6. [Hypothesis 3 Validation](#hypothesis-3-validation)
5. [The rationale to map the business requirements to the Data Visualisations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-Data-Visualisations-and-ML-tasks)
6. [ML business case](#ml-business-case)
7. [Dashboard Design](#dashboard-design)
8. [Unfixed Bugs](#unfixed-bugs)
9. [Deployment](#deployment)
    1. [Heroku](#heroku)
10. [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
11. [Other technologies used](#other-technologies-used)
12. [Issues](#issues)
13. [Testing](#testing)
    1. [Manual Testing](#manual-testing)
    2. [Python Validation](#python-validation)
14. [Credits](#credits)
    1. [Content](#content)
    2. [Media](#media)
15. [Acknowledgements](#acknowledgements)

## Introduction

Cherrypicker is a data science and machine learning (ML) project that uses predictive analytics to tell the difference between 2 different sets of images. The business goal is to assist the client, an agri-food business who is dealing with an infestation of powdery mildew in its cherry tree plantations. 

Currently the client is inspecting trees manually to determine whether they are infected or not and then treated if found to be diseased. This process is both labour intensive and time consuming. We propose the creation of a ML model that can determine from photographs of leaves whether mildew is present, reducing the amount of time taken to determine the status of the tree and enable sick trees to be treated with greater efficiency and accuracy. 

The project is hosted on the streamlit app and a live version may be found [here](https://cherry-picker-7809e87f232b.herokuapp.com/)

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). 
- The dataset contains over 4 thousand images taken from the client's cherry tree plantations. The images are divided into 2 sets, one of healthy leaves and one of leaves that are infected with powdery mildew. a fungal disease that affects many plant species. The client is concerned that the outbreak may be compromising the quality of their crop, which in turn would have serious ramifications for their business at large. 

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

![Healthy Leaves](/assets/images/healthy_leaves.png)

And leaves where powdery mildew is present:

![Infected Leaves](/assets/images/infected_leaves.png)

To create the average and variability images that will serve as the basis for our validation, images such as those above were taken and loaded into an array with their shape, once found. A function was then created to plot the mean and variability of the data in this. Below also are the average and variability images for both kinds of leaves.

![Average & variability for healthy leaves](/assets/images/healthy_average.png)

![Average & variability for infected leaves](/assets/images/infected_average.png)

From the photographs and results of the analysis, it appears that the hypothesis is correct and there is a visual difference. We may therefore consider the hypothesis validated.

### Hypothesis 2
Our second hypothesis is that the ML model will be just as accurate using grayscale images as colour ones.

It is possible that colour images may not be available in future. To prepare for this, we will test whether grayscale images may also be used.

### Hypothesis 2 Validation
To validate this, a second version of the ML model was created where during image augmentation, the color mode was set to grayscale when augmenting data on each set. 

Below are the results for accuracy and loss when the model was trained using grayscale images:

![Accuracy for model trained on grayscale images](/outputs/v2/model_training_acc.png)

![Loss for model trained on grayscale images](/outputs/v2/model_training_losses.png)

And the generalised performance on the test set:

![Performance of model trained on grayscale images](/assets/images/grayscale_performance_on_test_set.png)

When compared to the results for the model trained in colour images, we see a loss in accuracy.

![Accuracy for model trained on colour images](/outputs/v1/model_training_acc.png)

![Loss for model trained on colour images](/outputs/v1/model_training_losses.png)

For this reason, we may not consider this hypothesis validated, and we do not recommend using grayscale images to train ML models.

### Hypothesis 3

Our third hypothesis is that ML model accuracy is affected by the activation function used in the output layer. Our first study used a sigmoid activation function and binary classification to determine whether a leaf was healthy or diseased. We propose instead to use a SoftMax activation function, which operates as a multi-class classification function.  We hypothesise this will result in reduced accuracy.

### Hypothesis 3 Validation

We validated this by creating a final version of the ML model. This time, when augmenting the dataset the class mode was changed to categorical and the activation function in the ML model was changed to softmax.

Below are the results for accuracy and loss when the model wthat used softmax as its activation function:

![Accuracy for model using softmax](/outputs/v3/model_training_acc.png)

![Loss for model using softmax](/outputs/v3/model_training_losses.png)

And the generalised performance on the test set:

![Performance of model using softmax](/assets/images/performance_on_test_set.png)

We can then compare to the sigmoid results:
When compared to the results for the model trained in colour images, we see a clear loss in accuracy.

![Accuracy for model using sigmoid function](/outputs/v1/model_training_acc.png)

![Loss for model using sigmoid function](/outputs/v1/model_training_losses.png)

The data suggests that the model using softmax performed at about the same level as the one using sigmoid. However, during testing it proved unable to correctly identify leaves. For this reason we would not recommend using softmax. We may also consider our hypothesis validated.

![Evaluation of model using softmax 1](/assets/images/softmax_evaluation_1.png)

![Evaluation of model using softmax 2](/assets/images/softmax_evaluation_2.png)

[Back to top](#table-of-contents)

## The rationale to map the business requirements to the Data Visualisations and ML tasks

As stated above, we must take into consideration the accuracy of our results and the speed at which they are provided. It must also be scalable and easily understood.

- The business requirements are as follows:

**Requirement 1** - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.

This is an issue of classification between healthy leaves and those infected with mildew. We can map the requirements to our data visualisation and ML tasks through [User Stories](https://github.com/users/HughKeenan/projects/8). Please see this link for further detail, but in summary, the following relate to requirement 1: 

* As a data scientist I can collect & prepare data so that it can be used for analysis & training ML models.
    * To conduct an effective study, we must first acquire relevant data. The dataset acquired through Kaggle had to be downloaded, and then examined to ensure it contained no non-relevant data, for example as part of this process, a notebook was ran to remove any non-image files present in the dataset.
    * The images were then converted to arrays and the average was of both kinds was plotted, along with the variability of each. They were then compared together with an image showing the differences in average and variability between both.

* As an end user, I can review a page of project findings so that I can receive more detailed information on what conclusions the development team came to.
    * The image visualizer page of the dashboard shows the results of our study, including the average images for healthy and sick leaves, and the variability in images for both. The study found that there are visual differences between them. An image montage is also available for either kind of leaf if the user wishes to see more examples. 

* As an end user I can view a page detailing the project hypothesis so that I can understand the reasoning behind the developer's analysis
    * We hypothesised at the outset that there was a visual difference in healthy and sick leaves, which was validated by our analysis.

**Requirement 2** - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

The client wanted a dashboard that would let them upload images of leaves to the site and have an accurate reading of whether they were healthy or sick. This requirement was considered in the below user story:

* As a data scientist, I can create a machine learning model to make predictions on uploaded images
    * We trained a machine learning model to recognise the difference between healthy & diseased leaves. This was done using a convolutional neural network, making use of different layers and activation functions to classify the images. This is available on the dashboard in the mildew detector page.

* As an end user I can upload an image of a leaf so that I can learn if it is diseased or not. 
    * The mildew detector page enables the client to do this. They can upload images of the leaves which are then run through the ML model which can accurately predict whether or not powdery mildew is present.    

[Back to top](#table-of-contents)

## ML Business Case

The client has requested a solution that will enable them to quickly and efficiently differentiate between healthy & diseased leaves. This will be done by creating a ML model.

The aim behind the ML task is to develop a ML model using a CNN that is able to distinguish a cherry leaf that is healthy from one that has powdery mildew. 

Ultimately, the goal is to develop a binary classification model that can predict with minimum 97% accuracy whether a leaf is infected or not, outputting an appropriate label for the status of a given leaf. Once output has been received, the tree in question may be recommended for treatment.

We may consider this successfully accomplished if it is capable of achieving an accuracy rating of at least 97% on the test dataset. If this is not accomplished, the model has failed. A high accuracy rating is crucial as failure to detect disease may have serious economic implications for the client.

The relevance to the user of this kind of ML model output is that it may be relied upon to deliver trustworthy readings when presented with new data. In addition, the model will output visuals such as the average image for healthy and sick leaves, which will provide a useful reference to the users.

The data is provided by the user and downloaded from Kaggle. It is split into train, test and validation subsets. It is confidential in nature and as such appropriate measures will be taken to protect it. It may only be downloaded from Kaggle if the data practitioner has the appropriate JSON key.

[Back to top](#table-of-contents)

## Dashboard Design

The dashboard was made using Streamlit and has been designed with clarity and ease of use in mind. It contains the following pages:

1. Project Summary 

![Project Summary page](/assets/images/project_summary.png)

This is the introductory page the user will see on accessing the dashboard. Its intended purpose is to provide a new user with essential information both general and specific, so that they may gain a full understanding of the project before proceeding to more technical pages. It contains the following:

* General Information
* Dataset Information
* Link to project README 
* Business Requirements

The general information provided is there to inform users about the nature of powdery mildew and its implications for the client's business, as well as the reason for the project's inception.

It also provides more specific information concerning the dataset and provides a link to where it might be downloaded, as well as a summary of the buiness requirements.

2. Image Visualizer 

![Image Visualizer Page](/assets/images/image_visualizer.png)

This page contains the following:

* Business requirement 1
* Checkbox 1 - Difference between average and variability image
* Checkbox 2 - Differences between average healthy and average infected leaves
* Checkbox 3 - Image Montage

This page is intended to anwer buiness requirement 1: the client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew. To this end it provides options for what the user may wish to see; it can display an image montage of healthy or infected leaves, as well as the results of an analysis of the images. The page displays the average image & variability image for healthy & diseased leaves as well as the differences between the average images for both and the difference between the variability images.

3. Mildew Detector 

![Mildew Detector Page](/assets/images/mildew_detector.png)

This page contains the following:

* Business requirement 2
* Link to Kaggle dataset
* Widget to upload images for analyis
* Link to download report in .csv format

This page answers business requirement 2: the client is interested in predicting if a cherry leaf is healthy or contains powdery mildew. The page contains a link to the Kaggle page where an authorised user will here be able to download a clean dataset. It also allows a user to upload images of either kind of leaf to receive an analysis of its status.

4. Project Hypotheses 

![Project Hypotheses Page](/assets/images/project_hypotheses.png)

This page contains the following:

* Project Hypotheses
* Validation

This page displays the project hypotheses and explaines the method by which they were validated

5. Performance Metrics

![Performance Metrics Page](/assets/images/performance_metrics.png)

This page contains the following:

* Train, Validation and Test Set: Labels Frequencies
* Model History
* Generalised Performance on test set

This page shows the results of our analysis.The page explains how the dataset was used for testing purposes. It also shows the results of the ML model training, including graphics to show model accuracy and loss on the training and validation set, and an explanation of the graphs. It also shows how the model performed on the test set after it had been trained, and explains what that means for the business requirements.

[Back to top](#table-of-contents)

## Unfixed Bugs
There are no unfixed bugs

[Back to top](#table-of-contents)

## Deployment

### Heroku

- The App live link is: `https://cherry-picker-7809e87f232b.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and click on New in the top left corner. Select create an App from the dropdown.
![Heroku homepage](/assets/images/heroku_homepage.png)
2. Give the app a name(note: this must be unique) and choose a location, either Europe or the USA, depending on where you are. Click on create App
![Page to name and create a new app](/assets/images/create_app.png)
3. Navigate to the Deploy tab at the stop of the page, scroll to the Deployment Method section and select GitHub as the deployment method.
![Choose deployment method](/assets/images/deployment_method.png)
4. Enter the name of your repository and search. Once it comes up, click on the connect button beside the name.
![Search for repository](/assets/images/repo_name.png)
5. From the option below the location to search for repos, choose to deploy the main branch from the dropdown if it is not selected already. You may choose here to enable automatic deploys, which will build a new version of the app on Heroku every time you push to GitHub. Select Deploy Branch.
![Choose branch to deploy](/assets/images/deploy_branch.png)
6. As the app builds, pay attention to the build log on screen and watch out for any errors, as any problems with deployment will be displayed here.
7. The slug size being too large is a common issue, as the max size for deployment is 500MB. If this occurs, you must reduce the size of the file. You can do this by adding large files such as the README, which are not required to run the app to the .slugignore, or by changing the versions of some of the software you are using.

[Back to top](#table-of-contents)

## Main Data Analysis and Machine Learning Libraries
The main libraries used were: 
* numpy 1.26.1 - used to convert information to arrays
* pandas 2.1.1 - used for converting information to a dataframe and saving as such
* matplotlib 3.4.0 - used to plot the distribution of datasets
* seaborn 0.13.2 - used for making statistical graphics
* plotly 5.10.0 - used for plotting results of ML model training
* Pillow 10.0.1 - used to adjust images
* streamlit 1.40.2 - used to create the dashboard's interface
* joblib 1.4.2 - used for runnning tasks in parallel
* scikit-learn 1.3.1 - used for model evaluation
* tensorflow-cpu 2.16.1 - used for model creation
* keras 3.0.0 - used to set hyperparameters for the model

[Back to top](#table-of-contents)

## Other Technologies used

* Streamlit - used for dashboard development to present data and for final project delivery

* Heroku - used to deploy the project as a web app.

* Git/GitHub - used for version control and code storage

* Gitpod - IDE used to develop the project

* Am I responsive - used to produce screenshot of the project.

[Back to top](#table-of-contents)

## Issues

* Mildew Detector - when testing the mildew detector page, it was discovered that when multiple images were uploaded for analysis concurrently, the plots generated by the predictive analysis.py script were being assigned duplicated randomly generated IDs, which prevented the .csv report from being generated. To fix this a random number generator was implanted into the code that will assign a given plot an ID of any number from 1 to 100,000. Given the volume of trees, and therefore images, that the client deals with, it was decided that a sufficiently large range would be needed to allow for scalability.

* Deployment - When attempting to deploy the app, it was discovered that it was too large to be posted. Despite adding a number of items to the .slugignore, it was still too large. To find more space, older versions of some libraries were used, and the python version selected was changed from 3.12 to 3.9, and some images had to be removed from the validation set posted to the dashboard that is used for the image visualiser page.

Subsequent versions of the app were successfully run after these changes and performance was not affected.

[Back to top](#table-of-contents)

## Testing

### Manual Testing

*Business Requirements Testing*

**Requirement 1** - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.

* As an end user, I can review a page of project findings so that I can receive more detailed information on what conclusions the development team came to.

| Dashboard item | Test conducted | Expected result | Actual result |
| -- | -- | -- | -- |
| Navbar | Selecting button for Image Visualiser | Image Visualiser page opens | Success |
| Button for difference between average & variability image | Click button | Display average & variability image for healthy & infected leaves | Success |
| Button for difference between average healthy & infect leaves | Click button | Display both average images & difference image for average healthy & infect leaves | Success |
| Button for image montage | Click button | Display dropdown for montage creation | Success |
| Dropdown option for healthy leaves | Select & click button to create montage | See montage of healthy leaves| Success |
| Dropdown option for infected leaves | Select & click button to create montage | See montage of infected leaves| Success |

* As an end user I can view a page detailing the project hypothesis so that I can understand the reasoning behind the developer's analysis

| Dashboard item | Test conducted | Expected result | Actual result |
| -- | -- | -- | -- |
| Navbar | Selecting button for Project Hypotheses | Project Hypothesis page opens | Success |

**Requirement 2** - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

The client wanted a dashboard that would let them upload images of leaves to the site and have an accurate reading of whether they were healthy or sick. This requirement was considered in the below user story:

* As an end user I can upload an image of a leaf so that I can learn if it is diseased or not. 

| Dashboard item | Test conducted | Expected result | Actual result |
| -- | -- | -- | -- |
| Navbar | Selecting button for Mildew Detector |Mildew Detector page opens | Success |
| Link to Kaggle on Mildew Detector page | Click on link |Kaggle page for dataset opens | Success |
| Box for uploading data | Drag & drop leaf image into box | See report displaying analysis of the image | Success |
| Box for uploading data | Use browse files button | File explorer opens to enable selection | Success |
| Box for uploading data | Upload image from file explorer | See report displaying analysis of the image | Success |
| Box for uploading data | Repeat prior two items for multiple images | See report displaying analysis of all the images| Success |
| Image analysis report | Click button to download csv report of analysis | Report is downloaded containing the results shown on dashboard| Success |

### Python Validation
The code in the Jupyter notebooks was validated using pycodestyle, which was installed through the following command:
`pip install pep8 pycodestyle pycodestyle_magic`.

It was implemented using a cell at the top of each page containing the following:

```
%load_ext pycodestyle_magic
%pycodestyle_on
```

A copy was made of each notebook, which was run with pycodestyle enabled, any errors were then corrected in the corresponding cell in the primary notebook.

The python code for the app pages and files for data management and predictive analysis was validated using a [PEP8 linter](https://pep8ci.herokuapp.com/).

[Back to top](#table-of-contents)

## Credits

### Content

- Information on powdery midlew was taken from https://en.wikipedia.org/wiki/Powdery_mildew
- The dataset was created by Code institute and taken from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves)
- The Malaria Walkthrough Project from Code Institute was used as a guide when assembling this project.

### Media

- the favicon was obtained here: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

[Back to top](#table-of-contents)

## Acknowledgements

- I would like to acknowledge my mentor, Mo Shami, who provided valuable insights and guidance during the project. I would also like to thank the Slack community and Neil McEwen, who helped with technical issues.

[Back to top](#table-of-contents)