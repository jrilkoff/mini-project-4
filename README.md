# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals

    The goal of this project is to automate the loan eligibilty process based on customer details using Machine Learning.
    Various customer attributes are provided and feature engineering will be used to create a more robust dataset.
    The target variable will be a Loan Status approval boolean of Yes or No.

## Hypothesis
(fill in your hypothesis about which subset of applicants will be most likely to have their loan approved, and why. Give some examples of how you will test this hypothesis)

    Success loan applicants will be:
        - Married 
        - Have a credit history 
        - Have at least one dependent 
        - Have a combined income higher than the median single income
        - Will not be self employed

    Some potential reasons for this are:
        - Higher income generally indicates more excess cash available, more likely to pay back amounts owing
        - Marriage generally creates a more cohesive unit and will tend towards being more risk adverse, thus more likely to avoid debt related costs or penalties
        - Dependents in a relationship also generate a more risk adverse couple, the ability to provide can be impacted greatly through bankruptcy
        - Self employment can generally be seen as higher risk, therefore non self employed applicants may be more successful
    
    Testing approach:
        - Looking at the mix in the dataset between married/not, #dependents/none, combined incomes
        - Feature engineering additional parameters around these potential reasons
            -- total combined income
            -- dependents (Y/N)
            -- two incomes (Y/N)
            -- combined income > median single (Y/N)
            -- coapplicant income > applicant income (Y/N)
        - Due to time constraints all features were removed except 'total combined income'

    Hypothesis Testing:
        - Once model has been created and trained, testing will occur
        - The predictions will be scored and measured against the target test data
        - Statistical modelling will be done on those predictions to determine accuracy (did not have time)

## EDA 
(fill in what you discovered in your exploration of the dataset)

    Data that will impact loan approval:
        - Married
        - Dependents
        - Self Employed
        - Applicant Income
        - Coapplicant Income
        - Credit History

    Data that will not impact loan approval:
        - Gender
        - Education
        - Property Area

    Data to drop:
        - Loan Amount (to be dropped)
        - Loan Amount Term (to be dropped)
        - Loan ID (to be dropped, it is a serial number)
        - Dropped as they may bias the model as they directly show results of an approval/non-approval

## Process
(fill in what you did during EDA, cleaning, feature engineering, modeling, deployment, testing)

EDA:
 - Overall look of the data
 - Reviewing .describe() to see distrubtions, min/max
 - Looking at each column from a numeric/categorical perspective
 - For categorical, looking at distributions, is one parameter heavily favoured?
 - For numerical, looking for outliers, are there data points to remove?

Cleaning:
 - Analyzing NaN's, determining the best method for imputing those values
 - Reviewing for outlier removal, is that outlier representative of the dataset?
 - Creating clean column names for visuals

Feature Engineering:
 - Created combined income column (ApplicantIncome + CoapplicantIncome)
 - Other features planned but not executed:
 -- dependents (Y/N)
 -- two incomes (Y/N)
 -- combined income > median single (Y/N)
 -- coapplicant income > applicant income (Y/N)
 - Review of logarithmic scaling

Modeling:
 - Creation of pipeline
 - Split into numerical and categorical paths
 - Imputation, Scaling, Dimensionality Reduction done on data pre-classifier
 - Three classifiers, Logistic Regression, Random Forest, Gradient Boost
 - Model was put into a pickle and uploaded into the cloud

Deployment:
 - AWS EC2 had a deployment of a Python app.py
 - app.py running Flask to facilitate web traffic
 - Model was used to analyze JSON response and send back a 0 or 1
 
Testing:
 - Sent api call from notebook
 - Successfully received a response and the model return a value without error
 - Occassional errors did occur when Credit History = None

## Results/Demo
(fill in your model's performance, details about the API you created, and (optional) a link to an live demo)

- The model performed well and the various scores were:

Logistic Regression model is: 0.7073170731707317
Random Forest model is: 0.7398373983739838
Gradient Boost model is: 0.7967479674796748

- The API had a couple of issues depending on the data going into it, but worked properly for the most part
- API was running Flask through a python app running on an AWS EC2 cloud server
- Goal was to work backwards, make the api call work properly then go onto the rest of the project

## Challanges 
(discuss challenges you faced in the project)

- I struggled with EDA initially, I wanted to do some real statistical analysis but did not have the time
- Getting the logarithmic transformations into the pipeline properly had to be scrapped, non-log values were used
- The pipeline itself I do not think is set up properly, I need to review the Feature Union aspect

## Future Goals
(what would you do if you had more time? are there any potential issues/biases with your model/use case?)

- Statistical analysis
- Better engineered pipeline
- Webform to populate with an applicants data, try the model with fresh inputs
- Better graphics and visuals