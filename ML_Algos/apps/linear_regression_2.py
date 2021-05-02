import streamlit as st 

def app():
	st.write("Predicting House Prices with multiple variables")
	import pandas as pd
	import matplotlib.pyplot as plt
	import numpy as np
	from sklearn import linear_model

	data = pd.read_csv('housing.csv')
	data = data[:50] #taking just 50 rows from the excel file
	st.subheader('Contents of the Housing Excel File')
	st.write(data)


	st.subheader('Choosing the variables which best correspond to median_house_value')

	plt.xlabel('households')
	plt.ylabel('median_house_value (in dollars)')
	plt.scatter(data.households,data.median_house_value)
	st.set_option('deprecation.showPyplotGlobalUse', False)
	st.pyplot()

	plt.xlabel('total rooms')
	plt.ylabel('median_house_value (in dollars)')
	plt.scatter(data.total_rooms,data.median_house_value)
	st.pyplot()


	plt.xlabel('median_income')
	plt.ylabel('median_house_value (in dollars)')
	plt.scatter(data.median_income,data.median_house_value)
	st.pyplot()

	st.write('As the plot above indicates, there is a strong correlation between the above three predictor variables and our target variable')
	
	st.subheader('We will now use these to train our model')

	model = linear_model.LinearRegression() #loading the model from the library
	model.fit(data[['median_income','total_rooms','households']],data.median_house_value)

	st.subheader('We have trained our model')

	st.subheader('We will predict the house prices for values 7.2574,1467,177 for the 3 predictors respectively')
	st.subheader('Prediction : {}'.format(model.predict([[7.2574,1467,177]]))) #I took values from row 3 of our dataframes :)

	st.subheader("We will now see the relation between our 3-dimensional prediction and each of the predictor variables")
	
	plt.xlabel('households')
	plt.ylabel('median_house_value(in dollars)')
	plt.scatter(data.households,data.median_house_value)
	plt.plot(data.households,model.predict(data[['median_income','total_rooms','households']]),color='red')
	st.pyplot()

	plt.xlabel('median income(in 10 thousand dollars)')
	plt.ylabel('median house value(in dollars)')
	plt.scatter(data.median_income,data.median_house_value)
	plt.plot(data.median_income,model.predict(data[['median_income','total_rooms','households']]),color='red') #plotting our model predicted line
	st.pyplot()

	plt.xlabel('total rooms')
	plt.ylabel('median house value(in dollars)')
	plt.scatter(data.total_rooms,data.median_house_value)
	plt.plot(data.total_rooms,model.predict(data[['median_income','total_rooms','households']]),color='red') #plotting our model predicted line
	st.pyplot()