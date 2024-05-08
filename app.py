import streamlit as st 
import streamlit.components.v1 as stc 
from EDAapp import run_eda_app
from MLMODELapp import run_ml_app
from PIL import Image
import webbrowser

html_temp = """
		<div style="background-color:#35858B;padding:10px;border-radius:10px">
		<h1 style="color:#AEFEFF;text-align:center;">Diabetes Prediction Web app</h1>
		</div>
		"""

def main():
	st.set_page_config(page_title="Diabetes Prediction",page_icon='🍫',layout="wide")
	stc.html(html_temp)
	
	menu = ["Diabetic Diagnosis","EDA","About"]
	st.sidebar.write("1.Select EDA option to see detailed analysis of the datset")
	st.sidebar.write("2.Select Diabetic Diagnosis to use Diabetes Risk Predictor")
	choice = st.sidebar.selectbox("Choose One of the Option",menu)

	if choice == "Home":
		st.subheader("Home")
		st.write("""
			
			This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
			#### Datasource
				- https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App

			""")
	elif choice == "EDA":
		run_eda_app()
	elif choice == "Diabetic Diagnosis":
		run_ml_app()
	
		

		

if __name__ == '__main__':
	main()