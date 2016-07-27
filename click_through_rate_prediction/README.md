# Click-Through Rate Prediction

Create a click-through rate (**CTR**) prediction pipeline.

Use **logistic regression** model to predict the click-through rate.(*Cause we also want to know the probabilities of the our predictions.*)

## Data

The dataset was taken from [Criteo Labs](http://labs.criteo.com/downloads/2014-kaggle-display-advertising-challenge-dataset/).

## Process

- Parse CTR dataset.
    - Accept the Criteo's data sharing agreement and download the data.
    - Split the data into **training, validation and test** set using **randomSplit** method.
    - Store the datasets using **RDDs** and cache them.
    - **Extract features** from each data point which is a string containing several fields.


- Featurize categorical data using one-hot-encoding ([OHE](https://www.quora.com/What-is-one-hot-encoding-and-when-is-it-used-in-data-science)).
*Categorical features -> numerical features.*
    - Define a function to generate OHE features from original categorical data and represent OHE data in SparseVector.       
    - Create an **OHE dictionary** from the dataset.
    - Apply OHE to the dataset.

<p align="justify">
  <img src="https://github.com/xuwenyihust/Distributed-Machine-Learning-Exercise/blob/master/images/CTR_data.JPG" width="900"/>
</p>

- Handle unseen features.
    - Some categorical values will likely appear in new data that did not exist in the training data.
    - When compute OHE features for the validation & test datasets, **ignore previously unseen features**.

- Reduce feature dimension.
    - Via **feature hashing**.

- Model construction.
    - Use **logistic regression** model.
    - **Train** the model.
    - Generate **predictions**.
    ```python
    rawPrediction = weights.dot(point.features) + intercept
    # Bound the raw prediction value
    rawPrediction = min(rawPrediction, 20)
    rawPrediction = max(rawPrediction, -20)
    return 1/(1 + exp(-rawPrediction))
    ```

- Model evaluation.
    - Use **log loss** to evaluate the model.
    ```python
    if y == 1:
         return -log(p)
    else:
         return -log(1 - p)
    ```      
    - Compute the **baseline log loss** (fix the predicted probability to be the fraction of label 1 in the true labels). 

    - Use the predicted probabilities to compute the log loss.

## Libraries Used


## Appendix

- One-Hot-Encoding

- [Log Loss](https://www.kaggle.com/wiki/LogarithmicLoss)
    - A standard evaluation criterion when **predicting rare-events** such as click-through rate prediction.
    - This metric should be used when we need to **predict** that something is **true or false with a probability** (likelihood) ranging from definitely true (1) to equally true (0.5) to definitely false(0).
    - The use of **log** on the error provides **extreme punishments** for being both confident and wrong.
    - Fit a **log linear probability model** to a set of **binary labeled examples**.
    - The **log linear model** assumes that the log-odds of the conditional probability of the target given the features is a **weighted linear combination of features**. 

## Resources
- [Kaggle Display Advertising Challenge](https://www.kaggle.com/c/criteo-display-ad-challenge)
- [edX CS120x Distributed Machine Learning with Apache Spark](https://courses.edx.org/courses/course-v1:BerkeleyX+CS120x+2T2016/info)

- [Logarithmic Loss](https://www.kaggle.com/wiki/LogarithmicLoss)

- [What is an intuitive explanation for the log loss function](https://www.quora.com/What-is-an-intuitive-explanation-for-the-log-loss-function)

