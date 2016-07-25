# Click-Through Rate Prediction

Create a click-through rate (**CTR**) prediction pipeline.

## Data

The dataset was taken from [Criteo Labs](http://labs.criteo.com/downloads/2014-kaggle-display-advertising-challenge-dataset/)

## Process

- Parse CTR dataset.
    - Accept the Criteo's data sharing agreement and download the data.
    - Split the data into **training, validation and test** set.
    - Store the datasets using **RDDs** and cache them.
    - **Extract features** from each data point which is a string containing several fields.


- Featurize categorical data using one-hot-encoding ([OHE](https://www.quora.com/What-is-one-hot-encoding-and-when-is-it-used-in-data-science)).
*Categorical features -> numerical features.*
    - Define a function to generate OHE features from original categorical data and represent OHE data in SparseVector.       
    - Create an OHE dictionary from the dataset.

- Reduce dimensionality.

- CTR prediction.

- Model evaluation.

## Libraries Used


## Resources
- [Kaggle Display Advertising Challenge](https://www.kaggle.com/c/criteo-display-ad-challenge)
- [edX CS120x Distributed Machine Learning with Apache Spark](https://courses.edx.org/courses/course-v1:BerkeleyX+CS120x+2T2016/info)
