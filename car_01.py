import pandas as pd
import numpy as np


car_data = pd.read_csv('input/car_train.csv')
all_columns = ['sale_date', 'class_id', 'sale_quantity', 'brand_id', 'compartment',
               'type_id', 'level_id', 'department_id', 'TR', 'gearbox_type',
               'displacement', 'if_charging', 'price_level', 'price', 'driven_type_id',
               'fuel_type_id', 'newenergy_type_id', 'emission_standards_id','if_MPV_id', 'if_luxurious_id',
               'power', 'cylinder_number', 'engine_torque', 'car_length', 'car_width',
               'car_height', 'total_quality', 'equipment_quality', 'rated_passenger', 'wheelbase',
               'front_track', 'rear_track']
total_items = len(car_data)-3


def find_nan(object_name):
    objects = car_data[object_name].fillna('XXXX')
    x = 0
    for object in objects:
        if object != 'XXXX':
            x = x + 1
    return x
# no Nan
# for i in all_columns:
#     print (find_nan(i))

car_overview = {}
def into_dic(object_name):
    def count_classes(object_name):
        L = []
        L.append(set(car_data[object_name]))
        L.append(len(set(car_data[object_name])))
        return L
    car_overview[object_name] = count_classes(object_name)

def check_fuel_type_id():
    x = 0
    for i in car_data['fuel_type_id']:
        x = x+1
        if i == '-':
            print(i, x)

def check_power():
    m = 0
    for i in car_data['power']:
        m = m+1
        if i == '81/70':
            print(i, m)

# have mixed data types-----------
# print(car_overview['power'])   # 3 '81/70' remain
# print(car_overview['fuel_type_id'])  # several '-' remain
# 17933  18555 18601 data are wrong after check functions
car_data = car_data.drop(17932)
car_data = car_data.drop(18554)
car_data = car_data.drop(18600)
# after checking, there no more wrong data
# check_power()
# check_fuel_type_id()

car_data['fuel_type_id'] = car_data['fuel_type_id'].apply(lambda x: int(x)) # if x != '-' else x
car_data['power'] = car_data['power'].apply(lambda x: float(x) ) # if x != '81/70' else x

for i in all_columns:
    into_dic(i)


