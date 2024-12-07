import pandas as pd
from typing import Tuple, List
import re
import pickle
import pandas as pd
import numpy as np
df = pd.read_pickle('/Users/leonkul/projects/python/Session/API/df.pkl')

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

X = df[['Car Mileage', 'Year of Production', 'Transmission_rating', 
        'Engine Volume', 'Car Tier_rating', 'Specialness', 
        'Fuel Type_rating', 'Drivetrain_rating']]
y = df['Car Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

def predict_car_price(features):
    features_array = features.values if isinstance(features, pd.DataFrame) else np.array(features).reshape(1, -1)
    return model.predict(features_array)[0]



def filter_cars(param1: str, op1: str, value1: str, param2: str, op2: str, value2: str,param3: str, op3: str, value3: str) :
    if op1 in ['>', '<', '=', '!=']:
        value1 = float(value1)
    if op2 in ['>', '<', '=', '!=']:
        value2 = float(value2)
    if op3 in ['>', '<', '=', '!=']:
        value3 = float(value3)
    condition1 = None
    condition2 = None
    condition3 = None
    
    if op1 == '>':
        condition1 = df[param1] > value1
    elif op1 == '<':
        condition1 = df[param1] < value1
    elif op1 == '=':
        condition1 = df[param1] == value1
    elif op1 == '!=':
        condition1 = df[param1] != value1

    if op2 == '>':
        condition2 = df[param2] > value2
    elif op2 == '<':
        condition2 = df[param2] < value2
    elif op2 == '=':
        condition2 = df[param2] == value2
    elif op2 == '!=':
        condition2 = df[param2] != value2
        
    if op3 == '>':
        condition3 = df[param3] > value3
    elif op3 == '<':
        condition3 = df[param3] < value3
    elif op3 == '=':
        condition3 = df[param3] == value3
    elif op3 == '!=':
        condition3 = df[param3] != value3

    filtered_df = df[condition1 & condition2 & condition3]
    
    is_empty = filtered_df.empty
    
    headers = list(filtered_df.columns)
    data_rows = filtered_df.values.tolist()

    return filtered_df, is_empty

def new_row(value_name,value_price,value_mileage,value_exterior,value_interior,value_drivetrain,value_fuel,value_transmission,value_engine,value_VIN,value_time,value_source):
    answer = []
    final_value_year = value_name.split()[0]
    final_value_name = value_name.replace(final_value_year,'')
    final_value_price = float(value_price)
    final_value_mileage = value_mileage
    final_value_exterior = value_exterior
    final_value_interior = value_interior
    final_value_drivetrain = str(value_drivetrain).replace('4WD','Four-wheel Drive')
    final_value_drivetrain = str(value_drivetrain).replace('AWD','All-wheel Drive')
    final_value_drivetrain = str(value_drivetrain).replace('FWD','Front-wheel Drive')
    final_value_drivetrain = str(value_drivetrain).replace('RWD','Rear-wheel Drive')
    final_value_fuel = value_fuel
    final_value_transmission = value_transmission
    final_value_engine = value_engine
    
    final_value_brand = value_name.split()[1]
    final_engine_volume = re.search(r'(\d+\.\d+)\s*[Ll]', value_engine)

    if final_engine_volume:
        final_engine_volume = final_engine_volume.group(1)
    else:
        final_engine_volume = 0
    
    if int(value_price)<-10000:
        final_value_price_range = '0-10k'
    elif 10000<int(value_price)<=50000:
        final_value_price_range = '10k-50k'
    elif 50000<int(value_price)<=100000:
        final_value_price_range = '50k-100k'
    else:
        final_value_price_range = 'More than 100k'
    
    if final_value_brand in ['Ferrari', 'Lamborghini', 'McLaren', 'Bentley','Porsche','Rolls-Royce','Aston']:
        final_value_tier = "S-tier"
    elif final_value_brand in ['BMW', 'Mercedes-Benz', 'Audi','Rivian','Lotus','Maserati']:
        final_value_tier = "A-tier"
    elif final_value_brand in ['Volvo', 'Chevrolet', 'Cadillac', 'Land', 'Tesla','Jaguar', 'INFINITI','RAM','Lincoln','Nissan']:
        final_value_tier = "B-tier"
    elif final_value_brand in ['Ford', 'Mazda','Genesis','Toyota','GMC','Jeep','Acura','Lexus','Dodge','Alfa']:
        final_value_tier = "C-tier"
    elif final_value_brand in [ 'Buick', 'Chrysler', 'MINI', 'Mitsubishi', 'Scion', 'Subaru','Hyundai','Kia','Honda','Volkswagen']:
        final_value_tier = "D-tier"
    else:
        final_value_tier = "Undefined tier"
    
    special_name_keywords = ['Premium', 'Luxury', 'Sport', 'Grand', 'Edition', 'Turbo', 'Hybrid', 'Electric', 'Wagon', 'Limited','Touring','Ti']
    special_engine_keywords = ['Supercharged', 'Twin Turbo', 'Turbo Diesel','Turbocharged']
    final_value_specialness = 0
    if set(value_name).intersection(special_name_keywords):
            final_value_specialness += 1
    if set(value_engine).intersection(special_engine_keywords):
            final_value_specialness+=1
    final_value_drivetrain_rating = 0
    if final_value_drivetrain == 'All-wheel Drive':
        final_value_drivetrain_rating = 8
    elif final_value_drivetrain =='Four-wheel Drive':
        final_value_drivetrain_rating = 9
    elif final_value_drivetrain == 'Front-wheel Drive':
        final_value_drivetrain_rating = 5
    elif final_value_drivetrain == 'Rear-wheel Drive':
        final_value_drivetrain_rating = 6
    else:
        final_value_drivetrain_rating = 4
    
    final_value_transmision_rating = value_transmission
    final_value_transmision_rating = re.sub(r'(\d+)-Speed.*', r'\1', final_value_transmision_rating)
    final_value_transmision_rating = re.sub(r'(\d+)-Spd.*', r'\1', final_value_transmision_rating)
    final_value_transmision_rating = re.sub(r'Automatic', '6', final_value_transmision_rating)
    final_value_transmision_rating = final_value_transmision_rating if re.match(r'^\d+$', final_value_transmision_rating) else '4'
    final_value_transmision_rating = int(final_value_transmision_rating)

    if final_value_brand in ['Ferrari', 'Lamborghini', 'McLaren', 'Bentley','Porsche','Rolls-Royce','Aston']:
        final_value_tier_rating = 10
    elif final_value_brand in ['BMW', 'Mercedes-Benz', 'Audi','Rivian','Lotus','Maserati']:
        final_value_tier_rating = 9
    elif final_value_brand in ['Volvo', 'Chevrolet', 'Cadillac', 'Land', 'Tesla','Jaguar', 'INFINITI','RAM','Lincoln','Nissan']:
        final_value_tier_rating = 6
    elif final_value_brand in ['Ford', 'Mazda','Genesis','Toyota','GMC','Jeep','Acura','Lexus','Dodge','Alfa']:
        final_value_tier_rating = 4
    elif final_value_brand in [ 'Buick', 'Chrysler', 'MINI', 'Mitsubishi', 'Scion', 'Subaru','Hyundai','Kia','Honda','Volkswagen']:
        final_value_tier_rating = 2
    else:
        final_value_tier_rating = 5
    
    if value_fuel == 'Gasoline':
        final_value_fuel_rating = 6
    elif value_fuel == 'Diesel':
        final_value_fuel_rating = 9
    elif value_fuel == 'Electric':
        final_value_fuel_rating = 8
    elif value_fuel == 'E85 Flex Fuel':
        final_value_fuel_rating = 3
    elif value_fuel == 'Hybrid':
        final_value_fuel_rating = 7
    elif value_fuel == 'Flexible Fuel':
        final_value_fuel_rating = 5
    else:
        final_value_fuel_rating = 4
    stats = [final_value_mileage, final_value_year, final_value_transmision_rating, final_engine_volume, final_value_tier_rating, final_value_specialness, final_value_fuel_rating, final_value_drivetrain_rating]
    final_value_predicted = predict_car_price(stats)
    final_value_price = float(final_value_price) 
    final_value_predicted = float(final_value_predicted) 
    final_value_difference = 100 * abs(final_value_price - final_value_predicted) / final_value_price
    result = [['Car Name','Car Price','Car Mileage','Exterior Color','Interior Color','Drivetrain','Fuel Type','Transmission','Engine','Year of Production','Brand','Engine Volume','Price Range','Car Tier','Specialness','Drivetrain_rating','Transmission_rating','Car Tier_rating','Fuel Type_rating','Predicted Car Price','Difference'],[final_value_name,final_value_price,final_value_mileage,final_value_exterior,final_value_interior, final_value_drivetrain,final_value_fuel,final_value_transmission,final_value_engine, final_value_year, final_value_brand,final_engine_volume, final_value_price_range, final_value_tier,final_value_specialness,final_value_drivetrain_rating,final_value_transmision_rating,final_value_tier_rating,final_value_fuel_rating,final_value_predicted,final_value_difference]]
    return result, None

