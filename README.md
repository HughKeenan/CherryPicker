# Detection of mildew on cherry leaves

## Introduction

The client, an agri-food business, is facing difficulties with an outbreak of powdery midew on its cherry tree plantations. At present, trees must be inspected manually to determine whether they are disease free or not and then treated if mildew is found. This process is both labour intensive and time consuming. Our proposition is to create a Machine Learning (ML) model that can determine from photographs of cherry leaves whether mildew is present or not, reducing the amount of time taken to determine the status of the tree and enable sick trees to be treated with greater efficiency and accuracy. 

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). 
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis

- Our hypothesis is that leaves where mildew is present show a pattern of pale spots on the leaf. We intend to validate this hypothesis by examining the data provided, and if all images marked as having mildew present show this characteristic, we may assume the hypothesis is validated.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

- The business requirements are as follows:

1. The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.

This is an issue of classification between healthy leaves and those infected with mildew. 

2. The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.




## ML Business Case

The client has requested a solution that will enable them to quickly and efficiently differentiate between healthy & diseased leaves. To provide this we will develop a ML model using a convolutional neural netwrok which has been trained to recognise both kinds of leaves. We may consider this successfully accomplished if it is capable of generating an image montage consisting of healthy or diseased leaves on request and if it can accurately determine the status of a leaf when uploaded to the dashboard.

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

- The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
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

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements (optional)

- Thank the people who provided support throughout this project.
