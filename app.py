import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import mlflow
import mlflow.sklearn

# Load Iris dataset
data = pd.read_csv('data/iris.csv')

# Sidebar for user input parameters
st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal Length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal Width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal Length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal Width', 0.1, 2.5, 0.2)

    data = {
        'Sepal_Length': sepal_length,
        'Sepal_Width': sepal_width,
        'Petal_Length': petal_length,
        'Petal_Width': petal_width
    }

    features = pd.DataFrame(data, index=[0])
    return features

# Main app content
st.write("""
# Iris Flower Prediction App
This app predicts the **Iris flower species** based on user input parameters!
""")

# Sidebar - User input features
df = user_input_features()

# Display user input parameters
st.subheader('User Input Parameters')
st.write(df)

# Train-test split
X = data.drop('Species', axis=1)
y = data['Species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Models
models = {
    'K-Nearest Neighbors': KNeighborsClassifier(),
    'Support Vector Machine': SVC()
}

# User selects a model
selected_model = st.sidebar.selectbox('Select Model', list(models.keys()))

# Initialize the selected model
model = models[selected_model]

# Train the model
model.fit(X_train, y_train)

# Ensure input features match training features
df = df.reindex(columns=X.columns, fill_value=0)

# Make predictions
prediction = model.predict(df)

# Display prediction
st.subheader('Prediction')
st.write(prediction[0])

# MLflow Tracking
with mlflow.start_run():
    mlflow.log_param("Sepal_Length", df['Sepal_Length'].values[0])
    mlflow.log_param("Sepal_Width", df['Sepal_Width'].values[0])
    mlflow.log_param("Petal_Length", df['Petal_Length'].values[0])
    mlflow.log_param("Petal_Width", df['Petal_Width'].values[0])

    # Make predictions
    prediction = model.predict(df)

    # Log metrics to MLflow
    mlflow.log_param("prediction", data[data['Species'] == prediction[0]]['Sepal_Length'].values[0])


# Visualization
st.subheader("Visualization")

# Scatter Plot
st.subheader("Scatter Plot:")
scatter_fig = px.scatter(data, x='Sepal_Length', y='Sepal_Width', color='Species')
st.plotly_chart(scatter_fig)

# Pie Plot
st.subheader("Pie Plot:")
pie_fig = px.pie(data, names='Species')
st.plotly_chart(pie_fig)

# Bar Plot
st.subheader("Bar Plot:")
bar_fig = px.bar(data, x='Species', y='Petal_Length')
st.plotly_chart(bar_fig)

# Line Plot
st.subheader("Line Plot:")
line_fig = px.line(data, x='Petal_Width', y='Sepal_Width', color='Species')
st.plotly_chart(line_fig)
