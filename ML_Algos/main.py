import streamlit as st
from multiapp import MultiApp
from apps import linear_regression_1,linear_regression_2,logistic_regression_1,logistic_regression_2 # import your app modules here

st.title('Self Learn ML')

app = MultiApp()

# Add all your application here
app.add_app("Linear Regression with Single Variable", linear_regression_1.app)
app.add_app("Linear Regression with Multiple Variables", linear_regression_2.app)
app.add_app("Logistic Regression with Single Class", logistic_regression_1.app)
app.add_app("Logistic Regression with Multiple Classes", logistic_regression_2.app)
# The main app
app.run()

