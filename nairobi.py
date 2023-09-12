from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR
import xgboost
import geopandas
from shapely.geometry import Point
import numpy as np
import pandas as pd
import statsmodels.api as sm
from file_handler import FileHandler
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.core.display import display, HTML

pd.options.mode.chained_assignment = None

#reading the crime reports in the csv files
crime16 = FileHandler.read_csv_file('nairobi_crimes16.csv')
crime17 = FileHandler.read_csv_file('nairobi_crimes17.csv')

#picking the longitude and latitude from the crime reports
crime16['geometry']=crime16.apply(lambda row: Point(row['X'],row['Y']),axis=1)

#getting crime reports and location in long and lat
geo_police_data = geopandas.GeoDataFrame(crime16, geometry='geometry')
geo_police_data.crs = {'init': 'epsg:4326'}

#geting the map
sf = FileHandler.set_map_geometry('nairobi_geo.json')

#spatial join the geo_police data and the sf keeping the points only in the geo police data
crime16 = geopandas.tools.sjoin(geo_police_data, sf, how='left')

#find out which day,hours and zipcodes have most crimes
day_time_zip_16 = crime16[['Date', 'DayOfWeek', 'Time', 'PdDistrict']]
day_time_zip_16.loc[:, 'Date'] = pd.to_datetime(day_time_zip_16['Date'])
day_time_zip_16.loc[:, 'Hour'] = pd.to_datetime(day_time_zip_16['Time'])
day_time_zip_16.loc[:, 'Hour'] = day_time_zip_16.Hour.apply(lambda x: x.hour)
day_time_zip_16.head()

#combine all the crimes into hours days and zipcodes
day_time_zip_16_final = day_time_zip_16[['DayOfWeek', 'PdDistrict', 'Hour']]
day_time_zip_16_final.loc[:, 'Crimes'] = 1
hour_totals_16 = day_time_zip_16_final.groupby(['DayOfWeek', 'PdDistrict', 'Hour']).sum().reset_index()
hour_totals_16.sort_values('Crimes', ascending = False).head()

#creating dummy variables to start doing analysis
hour_totals_16 = hour_totals_16[['Crimes', 'Hour', 'DayOfWeek', 'PdDistrict']]
totals_dummies_16 = pd.get_dummies(hour_totals_16)
X_16 = totals_dummies_16.iloc[:, 1:]
y_16 = totals_dummies_16.iloc[:, 0]

#linear regression with 2016 data
linear_regression = sm.OLS(y_16, X_16)
results = linear_regression.fit()
results.summary()

#2017 data
crime17['geometry'] = crime17.apply(lambda row: Point(row['X'], row['Y']), axis=1)
geo_police_data = geopandas.GeoDataFrame(crime17, geometry='geometry')
geo_police_data.crs = {'init': 'epsg:4326'}

sf = FileHandler.set_map_geometry('nairobi_geo.json')

crime17 = geopandas.tools.sjoin(geo_police_data, sf, how='left')

day_time_zip_17 = crime17[['DayOfWeek', 'Time', 'PdDistrict']]
day_time_zip_17['Hour'] = pd.to_datetime(day_time_zip_17['Time'])
day_time_zip_17['Hour'] = day_time_zip_17.Hour.apply(lambda x: x.hour)

day_time_zip_17 = day_time_zip_17[['DayOfWeek', 'PdDistrict', 'Hour']]
day_time_zip_17['Crimes'] = 1
hour_totals_17 = day_time_zip_17.groupby(['DayOfWeek', 'PdDistrict', 'Hour']).count().reset_index()
hour_totals_17.sort_values('Crimes', ascending = False).head()

hour_totals_17 = hour_totals_17[['Crimes', 'Hour', 'DayOfWeek', 'PdDistrict']]
totals_dummies_17 = pd.get_dummies(hour_totals_17)
X_17 = totals_dummies_17.iloc[:, 1:]
y_17 = totals_dummies_17.iloc[:, 0]

#testing different models
#linear regression
linear_regression = LinearRegression()
linear_regression.fit(X_16,y_16)
lr_score = linear_regression.score(X_17, y_17)


#Radom forest
rf = RandomForestRegressor()
rf.fit(X_16, y_16)
rf_score = rf.score(X_17,y_17)
list(zip(X_16.columns, rf.feature_importances_))

#KNN
knn = KNeighborsRegressor()
knn.fit(X_16, y_16)
knn_score = knn.score(X_17,y_17)

#svm
svm = SVR()
svm.fit(X_16, y_16)
svm_score = svm.score(X_17,y_17)

# #xgboost
# xgb = xgboost.XGBRegressor()
# xgb.fit(X_16, y_16)
# xgb_score = xgb.score(X_17,y_17)

#mlp regressor
mlp = MLPRegressor(hidden_layer_sizes = (100,100,100,100), random_state=444)
mlp.fit(X_16,y_16)
mlp_score = mlp.score(X_17, y_17)

#Combine all models into one data frame
mlp_predicts = mlp.predict(X_16)

hour_totals_17['Predicted_mlp'] = pd.Series(mlp_predicts)

hour_totals_17['Crimes'] = hour_totals_17['Crimes']/365
hour_totals_17['Predicted_mlp'] = hour_totals_17['Predicted_mlp']/365
hour_totals_17 = np.round(hour_totals_17,2)

hour_totals_17.to_json("./nairobi_crime_predictions.json", orient='records', double_precision=2)
