import pandas as pd
import numpy as np


car_data = pd.read_csv('input/without_mixed_type.csv')
all_columns = ['sale_date', 'class_id', 'sale_quantity', 'brand_id', 'compartment',
               'type_id', 'level_id', 'department_id', 'TR', 'gearbox_type',
               'displacement', 'if_charging', 'price_level', 'price', 'driven_type_id',
               'fuel_type_id', 'newenergy_type_id', 'emission_standards_id','if_MPV_id', 'if_luxurious_id',
               'power', 'cylinder_number', 'engine_torque', 'car_length', 'car_width',
               'car_height', 'total_quality', 'equipment_quality', 'rated_passenger', 'wheelbase',
               'front_track', 'rear_track']
total_items = len(car_data)


car_overview = {}
def into_dic(object_name):
    def count_classes(object_name):
        L = []
        L.append(set(car_data[object_name]))
        L.append(len(set(car_data[object_name])))
        return L
    car_overview[object_name] = count_classes(object_name)

for i in all_columns:
    into_dic(i)

print (total_items)
print(car_overview['engine_torque'])