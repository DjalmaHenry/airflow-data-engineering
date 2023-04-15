def svm_model(**context):
    """
    Example function that will be performed as a task in airflow.

    Code for calculating accuracy from Support Vector Machine model
    """
    import numpy as np
    import pandas as pd

    from sklearn.model_selection import train_test_split
        # Import train_test_split function

    data=pd.read_csv("gs://mlpipelinetest/data2.csv")
    X=data[['sepal length', 'sepal width', 'petal length', 'petal width']]  # Features
    Y=data['species']  # Labels
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)
    from sklearn.svm import SVC
    classifier = SVC(kernel = 'linear', random_state = 0)
    #Fit the model for the data

    classifier.fit(X_train, y_train)

    #Make the prediction
    y_pred = classifier.predict(X_test)
    from sklearn.model_selection import cross_val_score
    accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)
    print("Accuracy:" ,accuracies.mean())
    ti = context['ti']
    ti.xcom_push(key='svm_model', value="Accuracy:"+ str(accuracies.mean()))
