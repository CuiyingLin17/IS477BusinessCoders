import pandas as pd
df = pd.read_csv('data/merged_dataset.csv')

#data profiling
print(df.info())
print(df[df['unemployment_rate'].isna()])
print(df[df['inflation_rate'].isna()])

#data cleaning
df['observation_date'] = pd.to_datetime(df['observation_date'], format = '%Y-%m-%d')
df['disposable_personal_income'] = df['disposable_personal_income'] * 1000
df['retail_sales'] = df['retail_sales'].astype(float)

df = df.rename(columns = {
    'disposable_personal_income': 'disposable_personal_income_millions',
    'retail_sales': 'retail_sales_millions'
})

#save dataset as csv file
df.to_csv('data/merged_dataset_cleaned.csv', index = False)
