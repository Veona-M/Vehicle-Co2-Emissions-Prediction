# Vehicle-Co2-Emissions-Prediction
This is a project on calculating the amount of carbon dioxide (Co2) that a vehicle emits depending on its features. Using the obtained dataset I performed advanced analysis to come up with a model that could accurately predict the vehicle's Co2 Emissions. This information can help the user understand their vehicle's impact on the environment.

# Understanding the data
Make: Vehicle brand.

Model: Specific model of the car: 

    4WD/4X4 = Four-wheel drive
	AWD = All-wheel drive
	FFV = Flexible-fuel vehicle
	SWB = Short wheelbase
	LWB = Long wheelbase
	EWB = Extended wheelbase     
 
Vehicle class: Car body type.

Engine size: Size of the car engine in liters.

Cylinders: Number of cylinders.

Transmission: Type of transmission:

    A = automatic
	AM = automated manual
	AS = automatic with select shift
	AV = continuously variable
	M = manual
	3 - 10 = Number of gears
 
Fuel type: Type of fuel used by the car:

    X = regular gasoline
	Z = premium gasoline
	D = diesel
	E = ethanol (E85)
	N = natural gas
 
Fuel consumption city(L/100km): City fuel consumption ratings in liters per 100 kilometers.

Fuel consumption hwy(L/100km): Highway fuel consumption ratings in liters per 100 kilometers.

Fuel consumption comb(L/100km): Combined fuel consumption rating (city and highway) in L/100 km.

Fuel consumption comb(mpg): Combined fuel consumption rating in miles per gallon (mpg).

Co2 emissions (g/km): Tailpipe emissions of carbon dioxide for combined city and highway driving, in grams per kilometer.

# Prerequisites
 During development of this project, various tools and technologies were used:
 
    > Python programming language
    > Libraries such as NumPy, Matplotlib, Plotly, Scikit-learn and Streamlit
    > Models; Linear Regression, Random Forest, K-Nearest Neighbors (KNN), and Support Vector Regression (SVR) 
    > Deployment on the cloud using Streamlit

