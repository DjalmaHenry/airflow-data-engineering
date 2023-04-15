def lr_model(**context):
    """
    Example function that will be performed as a task in airflow.

    Code for calculating accuracy from Logistic Regression model
    """
    import numpy as np
    import pandas as pd

    from sklearn.model_selection import train_test_split
        # Import train_test_split function

    data=pd.read_csv("gs://mlpipelinetest/data2.csv")
    X=data[['sepal length', 'sepal width', 'petal length', 'petal width']]  # Features
    Y=data['species']  # Labels
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    # Fitting Logistic Regression to the Training set
    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression(random_state = 0, solver='lbfgs', multi_class='auto')
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    from sklearn import metrics
    # Model Accuracy, how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    ti = context['ti']
    ti.xcom_push(key='lr_model', value="Accuracy:"+ str(metrics.accuracy_score(y_test, y_pred)))
