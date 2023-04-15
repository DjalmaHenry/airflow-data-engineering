def load_data():
    """
    Example function that will be performed as a task in airflow

    Importing iris data and storing it in a gcs bucket.
    """
    #Import scikit-learn dataset library
    from sklearn import datasets

    #Load dataset
    iris = datasets.load_iris()

    import pandas as pd
    data=pd.DataFrame({
        'sepal length':iris.data[:,0],
        'sepal width':iris.data[:,1],
        'petal length':iris.data[:,2],
        'petal width':iris.data[:,3],
        'species':iris.target
    })
    print(data.head())
    data.to_csv("gs://mlpipelinetest/data2.csv")
