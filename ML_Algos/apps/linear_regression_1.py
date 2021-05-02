import streamlit as st 


def app():
	st.write("Predicting House Prices")
	import pandas as pd
	import matplotlib.pyplot as plt
	import numpy as np
	from sklearn import linear_model

	data = pd.read_csv('housing.csv')
	data = data[:50]

	st.subheader('Contents of the Housing Excel File')
	st.write(data)

	st.subheader('Choosing the variable which best corresponds to median_house_value')
	plt.xlabel('median income(in 10 thousand dollars)')
	plt.ylabel('median house value(in dollars)')
	plt.scatter(data.median_income,data.median_house_value)
	st.set_option('deprecation.showPyplotGlobalUse', False)
	st.pyplot()
	st.write('As the plot above indicates, there is a strong correlation between median income and median house value.So we select it as our predictor variable')

	model = linear_model.LinearRegression()
	model.fit(data[['median_income']],data.median_house_value)


	num = st.selectbox('median income in 10 thousand dollars',[4,5,6,7,8,9])
	st.subheader('Prediction :{}'.format(model.predict([[num]])))

	st.subheader('The red line shows predictions generated by our model')
	plt.xlabel('median income(in 10 thousand dollars)')
	plt.ylabel('median house value(in dollars)')
	plt.scatter(data.median_income,data.median_house_value)
	plt.plot(data.median_income,model.predict(data[['median_income']]),color='red')
	st.pyplot()





# # to make sure a window dosent pop on your screen and we get the plot in the page itself
# plt.xlabel('median income(in 10 thousand dollars)') # labelling x-axis
# plt.ylabel('median house value(in dollars)') # labelling y-axis
# plt.scatter(data.median_income,data.median_house_value) # scatter plot

    

# model = linear_model.LinearRegression() #loading the linear regression model into a variable 'model'

# model.fit(data[['median_income']],data.median_house_value) # we passed the median income inside a 
# 	                                                           #list as the model requires a 2d array as input

# model.predict([[7]]) #if median income is 70,000 dollars , probably price of their house is 372658.8098301 dollars


# plt.xlabel('median income(in 10 thousand dollars)')
# plt.ylabel('median house value(in dollars)')
# plt.scatter(data.median_income,data.median_house_value)
# plt.plot(data.median_income,model.predict(data[['median_income']]),color='red') #plotting our model predicted line

