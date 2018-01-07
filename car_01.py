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
total_items = len(car_data)
# ab =  car_data.select_dtypes(include=['object'])
object_columns = ['level_id', 'TR', 'gearbox_type', 'if_charging', 'price_level',
                  'fuel_type_id', 'power', 'engine_torque', 'rated_passenger'] # 'price',

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

def check(object_name, to_check):
    x,y = 0,0
    num = []
    for i in car_data[object_name]:
        if i == to_check:
            y = y+1
            num.append(x)
            print(object_name, i, x)
        x = x+1
    if y == 0:
        print(object_name + ' is good')
    else:
        print('there are %d:' % y + to_check + 'in ' + object_name +'-----')
    return num


# # have mixed data types-----------
# # print(car_overview['power'])   # 3 '81/70' remain
# # print(car_overview['fuel_type_id'])  # several '-' remain
# # 17932 18554 18600 data are wrong after check functions
del car_data['price']
to_delete = []
for i in ['fuel_type_id', 'engine_torque', 'level_id']:
    to_delete = check(i, '-') + to_delete
for i in to_delete:
    car_data = car_data.drop(i)


car_data['fuel_type_id'] = car_data['fuel_type_id'].apply(lambda x: int(x)) # if x != '-' else x
car_data['power'] = car_data['power'].apply(lambda x: float(x) ) # if x != '81/70' else x
car_data['engine_torque'] = car_data['engine_torque'].apply(lambda x: float(x) )


for i in object_columns:
    into_dic(i)
    check(i, '-')
    print(i, car_data[i].dtypes, car_overview[i])


# pd.DataFrame.to_csv(car_data, 'input/without_mixed_type.csv', index=None)
