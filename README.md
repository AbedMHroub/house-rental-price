# Modeling

###### Predicting the price using three basic machine learning methods:
- Linear regression
- Decision trees
- Random Forest.

I applied the models to the train set.
> I applied the models to the train set.
RMSE is the main metric for evaluating model performance. I also used cross-validation to determine the best performance model, which I then fine-tuned.RMSE is the main metric for evaluating model performance. I also used cross-validation to determine the best performance model, which I then fine-tuned.



> RMSE is a measure of how widespread these residues are. It tells me how focused the data is around the line of fit. The square root of the error is used in prediction and regression analysis to verify experimental results.RMSE is a measure of how widespread these residues are. It tells me how focused the data is around the line of fit. The square root of the error is used in prediction and regression analysis to verify experimental results.

> I used the mean absolute percentage error (MAPE) to compute the most compelling resolution scale for understanding.

###### Model comparison

 - cross-validate the three models and compare them

###### Fine-tune Random Forest

- Grid Search
- Randomized search

###### Most important hyperparameters of the random forest:

- n_estimators = n of trees
- max_features = max number of features considered for splitting a node
- max_depth = max number of levels in each decision tree
- min_samples_split = min number of data points placed in a node before the node is split
- min_samples_leaf = min number of data points allowed in a leaf node
- bootstrap = method for sampling data points (with or without replacement)

###### Evaluate the best model on the test set
