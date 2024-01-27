#    Application Elements


Client Information


Utilize the sidebar to include boundaries like Sepal Length, Sepal Width, Petal Length, and Petal Width.


Model Expectation
Select a model from the sidebar (K-Closest Neighbors,  Support Vector Machine, Random Forest Classifier).

The application predicts the Iris blossom species in light of the information boundaries.


MLOps Incorporation
MLflow is incorporated for model following.
Boundaries and forecasts are logged to MLflow.


The prepared model is saved as a cured document (models/model.pkl).
Perceptions


scatter Plot, Pie Plot, Bar Plot, and Line Plot are incorporated for information investigation.


MLflow Following
The MLflow UI can be gotten to see the investigation subtleties and model ancient rarities.

MLFLOW_TRACKING_URI=https://dagshub.com/Mayankvlog/iris_ok.mlflow \
MLFLOW_TRACKING_USERNAME=Mayankvlog \
MLFLOW_TRACKING_PASSWORD=a163dc11889cf8831384598f795e7c53cd54b1d2 \
streamlit run main.py
