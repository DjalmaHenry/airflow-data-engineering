def rf_model(**context):
    """
    Example function that will be performed as a task in airflow.

    Code for calculating accuracy from Randon Forest model
    """
    import numpy as np
    import pandas as pd
    from sklearn.model_selection import train_test_split
    # Import train_test_split function

    data=pd.read_csv("gs://mlpipelinetest/data2.csv")

    X=data[['sepal length', 'sepal width', 'petal length', 'petal width']]  # Features
    y=data['species']  # Labels

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% 

    #Import Random Forest Model
    from sklearn.ensemble import RandomForestClassifier

    #Create a Gaussian Classifier
    clf=RandomForestClassifier(n_estimators=100)

    #Train the model using the training sets y_pred=clf.predict(X_test)
    clf.fit(X_train,y_train)

    y_pred=clf.predict(X_test)

    #Import scikit-learn metrics module for accuracy calculation
    from sklearn import metrics
    # Model Accuracy, how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    ti = context['ti']
    ti.xcom_push(key='rf_model', value="Accuracy:"+ str(metrics.accuracy_score(y_test, y_pred)))
