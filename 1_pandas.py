import pandas as pd
import matplotlib.pyplot as plt

insurance_data = pd.read_csv('datasets/insurance.csv')
# print(insurance_data)

print(insurance_data.head(10))

# print(insurance_data.head(20))
# insurance_data.tail(10)


insurance_data.info()
insurance_data.describe()

filtered_data = insurance_data[insurance_data['age'] > 45]
filtered_data

age_smoker = insurance_data[(insurance_data['age'] < 20) & (insurance_data['smoker'] == 'yes')
                               & (insurance_data['children'] > 1)]

# print(age_smoker)

# filtered_data = insurance_data[(insurance_data['bmi'] > 30) | (insurance_data['smoker'] == 'yes')]
# filtered_data

# selected_columns = insurance_data[['bmi', 'smoker', 'region', 'charges']]
# print(selected_columns)

# trimmed_data = insurance_data.drop(columns=['children'])
# print(trimmed_data)

average_charges = insurance_data.groupby("smoker")["charges"].mean()
print(average_charges)

print(f"Average charges for smokers are: {average_charges['yes']}")  # Average charges for smokers
print(average_charges['no'])   # Average charges for non-smokers

import matplotlib.pyplot as plt

pip install matplotlib