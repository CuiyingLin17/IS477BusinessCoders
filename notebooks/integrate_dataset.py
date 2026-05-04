#load datasets
import pandas as pd

cpi = pd.read_csv('data/filtered_10yrs/CPIAUCSL_filtered.csv')
income = pd.read_csv('data/filtered_10yrs/DSPI_filtered.csv')
retail_sales = pd.read_csv('data/filtered_10yrs/RSAFS_filtered.csv')
unemployment = pd.read_csv('data/filtered_10yrs/UNRATE_filtered.csv')

#merge dataset
merged_dataset = (
    cpi.merge(income, on = 'observation_date', how = 'outer')
    .merge(retail_sales, on = 'observation_date', how = 'outer')
    .merge(unemployment, on = 'observation_date', how = 'outer')
)

#check if merged_dataset contains same rows as the datasets
assert len(merged_dataset) == len(cpi), 'merged_dataset must contain same rows as cpi'
assert len(merged_dataset) == len(income), 'merged_dataset must contain same rows as income'
assert len(merged_dataset) == len(retail_sales), 'merged_dataset must contain same rows as retail_sales'
assert len(merged_dataset) == len(unemployment), 'merged_dataset must contain same rows as unemployment'

#reorder columns
merged_dataset = merged_dataset[['observation_date', 'UNRATE', 'Inflation_Rate', 'DSPI', 'RSAFS']]
#rename columns
merged_dataset.columns = ['observation_date', 'unemployment_rate', 'inflation_rate', 'disposable_personal_income', 'retail_sales']

#save dataset as csv file
merged_dataset.to_csv('data/merged_dataset.csv', index = False)
