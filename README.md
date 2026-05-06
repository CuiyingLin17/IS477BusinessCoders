# Macroeconomic Factors and Retail Sales Relationship Analysis - IS477 Final Project

## Contributors
<p>Cindy Chen (cchen280@illinois.edu) <br>
Cuiying Lin (clin230@illinois.edu) <br>
Yelin Zhong (zhongyelin601@gmail.com) </p>

## Summary
<p>As Business + Data Science majors, this was a great opportunity for us to apply our data science skills and knowledge we learned from this class on to something else that is related to our major. By dividing the work between the three of us, we choose reliable sources, prepare and integrate the data to be ready for analysis. The purpose of this project is to analyze how each macroeconomic factor in the United States affects retail sales in the past 10 years. The factors that we choose include inflation, unemployment rate, and personal income. Inflation and personal income directly affects the purchasing power individuals have during a period of time, affecting retail sales. Unemployment rate may not affect everyone, but can determine the state of an economy. Higher unemployment can mean companies are laying off more employees either due to technological improvements or signs of recession. Lower unemployment can be signs of economic growth and usually will fall back to equilibrium. Breaking down changes in retail sales by different factors can help better understand and predict financial valuations on the retail. In order to get representative and accurate data, we found that the Federal Reserve Bank of St. Louis has easily accessible and data that was easy to use for our project. To ensure that our analysis stays relevant to current times, we kept the time frame within the last decade because it is more representative for when we need to predict future patterns of the economy, specifically in retail. If we take into account too many years of data, such as the market crash in 2008, the patterns would not be as relevant and timely. </p>

<p> Our results were that disposable personal income had the highest correlation with retail sales in the past ten years. With a correlation of .96, this means that the amount of disposable income people have highly affects retail sales. This result makes sense because when people have more money to spend, retail sales will increase, and vice versa. Inflation rate has a correlation of 0.36 with retail sales, which is considered moderately weak correlation between the two. Because inflation increases prices, retail sales increasing moderately makes sense. For the same reason, sales volume decreases leading to the moderate weak correlation found here. Finally, the unemployment rate has a -.3 correlation with retail sales. This means that unemployment rate and retail sales move in opposite directions. When retail sales increase, unemployment decreases, when unemployment increases retail sales decreases. Lower unemployment rates boosts consumer confidence because it means the economy is doing better, more people have a job. People feel economically stable and safer in their jobs, therefore they will spend more money. When unemployment is high, the job market is more unstable, people without a job will not have the money to spend, decreasing retail sales. </p>

## Data Profile

<p>The data sets that we acquired from the Federal Reserve Bank of St. Louis all have similar structures and characteristics. For the first dataset, the Consumer Price Index for All Urban Consumers, this data tells us the aggregated price paid by all urban consumers for a typical basket of goods compared to a base period. A basket of goods includes housing, transportation, medical bills, clothing, education, etc. However, this index purposely excludes food and energy because prices for these goods are much more volatile compared to others. The numbers are seasonally adjusted to ensure accurate representation of each month.The content in this dataset is simply the date the index was recorded, and the CPI of that respective date. The data starts from January 1st, 1947, and updates on the first of every single month until February first of 2026 as of the date we collected the data. Originally, the dates were recorded as an object in the data set, and the indexes were recorded as floats.  Of course, in the process of acquiring and preparing the data, we changed the date to date time to make it easier to work with. We also added a third column to the data for inflation rate, as this is the variable of interest. Due to the government shutdown in October 2025, the CPI column has missing value for the observation date of 2025-10-01. As a result, the inflation rate column has missing values for the observation date of 2025-10-01 and 2025-11-01.</p>

<p>The second data set, the Disposable Personal Income Index measures the amount of dollars in disposable income people have in billions of dollars in a month. This index is also seasonally adjusted which means that they used a statistical method to remove predictable fluctuations. These fluctuations include holidays or weather that may have a pattern effect on the data. For example, retail sales would usually rise around Christmas because it is the holiday season, people are buying gifts for each other. In order to see if retail sales are truly rising, or a result of the holiday season, the data adjusts the rate by a seasonal factor. The formula to calculate the adjusted rate is by dividing the unadjusted monthly rate by the seasonal factor, which removes those patterns, then multiplied by twelve. As a result, the data given is easily and more accurate to the rate of a year. If nothing changes, this is what the data expects the DPI to perform for the rest of the year. Similar to the other datasets, the DPI dataset only has two columns, the date and the index of that respective date. The data starts on January 1st 1959 and goes until January 1st 2026 as of the collecting this data. The date was also originally recorded as an object, which we later will convert to date time to be easier to work with. </p>

<p>The third data set, Advance Retail Sales, reports an advance estimate of retail sales from a subsample of firms from the Monthly Retail Trade Survey. An advance estimate is the first calculation of the retail sales in a month that are expected to happen. This estimate will then be replaced by actual performance of that month from the same Monthly Retail Trade Survey. Similarly, to the rest of the data, the numbers are also adjusted seasonally to ensure accurate representation of every month. The actual data also only has two columns, a date column and retails sales in millions column. Because the retail sales column is given in millions, and the disposable personal income index is given in billions, this is something we will need to address later in our analysis. In addition, we will need to again convert the date here as an object to a date time data type to be easier to use. </p>

<p>The final data set, Unemployment Rate, measures the amount of unemployed people over the total amount of people in the labor force. To be considered unemployed, someone would need to be over the age of 16 actively seeking employment, who are not in any institutions, or are not on active duty in the Armed Forces. The labor force only includes people who can legally work. The final number is a percentage of people who are looking for work out of everyone that can and want to work. This percentage is also seasonally adjusted to ensure accurate representation of every month. Similar to the other data sets, this data set is also only 2 columns, one for the date and the other for the percentage of people unemployed on that respective date. The data starts on January 1st of 1948 and goes to March 1st of 2026. We will also need to convert the date column from an object to a date time date type to make it easier for us to use later on. The data has missing value for the observation date of 2025-10-01 due to the government shutdown.</p>

## Data Quality
<p>After cleaning and merging the datasets, we evaluated the overall quality of the final dataset used for analysis. The final dataset contains 133 monthly observations and five variables, including one date column and four numerical indicators: unemployment rate, inflation rate, disposable personal income, and retail sales.
 
In general, the dataset is clean and well-structured. Each row represents one monthly observation, and each column has a clear meaning. Also, the date column has been converted to a proper datetime format, which allows the data to be sorted and analyzed in chronological order. This is especially important because our project focuses on changes in retail sales and macroeconomic conditions over time.

The dataset covers a consistent time period from January 2015 to January 2026, which aligns well with our goal of studying recent economic trends over approximately the past ten years. Although the original datasets had different starting dates, the final merged dataset uses the shared time period needed for analysis. As a result, the variables are easier to compare because they are aligned by the same monthly observation dates.

The data completeness is also strong overall. There are no missing values in the observation date, disposable personal income, or retail sales columns. However, the unemployment rate column has one missing value, and the inflation rate column has two missing values. Compared with the total number of observations, these missing values are limited and do not significantly affect the overall analysis. Still, they are important to acknowledge because missing values can slightly affect calculations such as summary statistics and correlations.
In addition, no duplicate rows were found in the final dataset, which suggests that the merging process did not create repeated observations. This matters because duplicate monthly records could distort the correlation results or make certain time periods appear more important than they actually are. The variables also appear to fall within reasonable ranges. For example, the unemployment rate ranges from 3.4% to 14.8%, which reflects both normal labor market conditions and the unusually high unemployment period during the COVID-19 pandemic. Similarly, retail sales and disposable personal income generally increase over time, which is consistent with broader economic growth patterns.

One limitation is that the final dataset only includes monthly-level national data, so it does not capture regional differences or industry-specific retail patterns. For example, changes in retail sales may vary across states or across different retail categories, but our dataset only reflects the overall national trend. Even so, this level of aggregation is appropriate for our research question because our goal is to examine broad macroeconomic relationships rather than local or sector-level effects.
Overall, the final cleaned dataset is reliable and suitable for our analysis. While there are a few missing values and some extreme observations, these issues are limited and understandable in the context of real-world economic data. Therefore, the dataset provides a strong foundation for analyzing the relationship between macroeconomic factors and retail sales.
</p>

## Data Cleaning
<p>After performing data profiling and data quality assessments, we performed the following data cleaning operations to address specific issues in our dataset:  
  
- The `observation_date` column was converted to a datetime data type in the year-month-day format (e.g., 2015-01-01) using `pd.to_datetime()`. Although the dates were already consistently formatted as strings, this conversion ensures proper handling for time series-analysis and improves the validity of this column.  
- The `disposable_personal_income` column was multiplied by 1,000 to convert values from billions to millions. This standardization addressed inconsistencies in units between `disposable_personal_income` (originally in billions) and `retail_sales` (originally in millions) to ensure comparability between variables.   
- The `retail_sales` column was converted to a float data type from integers since sales are usually recorded as a float and to ensure consistency between variables.  
- The `disposable_personal_income` and `retail_sales` columns were renamed to `disposable_personal_income_millions` and `retail_sales_millions` to clearly indicate their units of measurement. This improves clarity and enhances interpretability for future analysis.  
</p>
<p>Although there were one to two observations with missing values due to the government shutdown in October 2025, we did not perform data cleaning on this observation because we believe that this would not significantly affect our analysis. </p>

## Challenges
<p>While working on the project, the main challenges that we have encountered include the following:
  
- **Time frame selection**: Since we wanted to analyze and better understand future patterns of retail sales, we chose to focus on data from the last ten years, spanning from January 1, 2015 to January 1, 2026. While including more historical data could increase the dataset size and provide more observations for analysis, it could also introduce outdated economic conditions and distort the current trends. For example, the 2008 financial crisis may have little to no impact on present-day consumer behavior and retail sales. However, we also acknowledge that using a shorter time frame could, while ensuring relevance, miss long-term economic cycles or extended effects from major economic events. Therefore, we decided that a ten-year period provides a balanced approach, as it captures recent trends while still maintaining sufficient data variability for meaningful analysis.
- **Data integration from multiple sources**: Although we used reliable data from the FRED and the datasets were generally consistent in structure and format, the datasets for disposable personal income and retails were not reported in the same units, where disposable personal income was reported in billions while retail sales was reported in millions. As mentioned in our Data Profiling section, this discrepancy required us to standardize the units before we could perform any meaningful analysis. We addressed this by converting disposable income into millions to ensure consistency between the two variables. Without this step, any comparison of our results would have been misleading. 
- **Analysis interpretation**: While calculating the correlations between the three macroeconomic factors (inflation, unemployment rate, and disposable personal income) and retail sales was relatively straightforward from a computational perspective, we found that interpretation of the results was more challenging. In addition to analyzing the magnitude and direction of the correlations, we also had to evaluate whether the relationships made sense from an economic and business perspective. For example, the strong positive correlation between disposable personal income and retail sales aligned with economic theory of higher income generally leads to higher consumer spending. However, the weaker correlation between inflation and retail sales led us to reflect on how rising prices as a result of inflation may reduce consumers’ purchasing power if wages do not increase at the same rate, which could potentially lead to lower sales volumes even if nominal revenue appears higher. 
</p>

## Findings
<p>Our analysis shows that U.S. retail sales generally increased from January 2015 to January 2026, but the trend was not completely smooth. From the retail sales over time chart, retail sales grew steadily before 2020, then had a sharp drop around early 2020. This drop was probably related to the economic disruption caused by the COVID-19 pandemic. However, retail sales recovered fairly quickly after that period and continued to increase in the following years. By the end of the dataset, retail sales were much higher than they were in 2015, showing that overall retail activity grew a lot over the past decade.

Among the macroeconomic variables we analyzed, disposable personal income had the strongest relationship with retail sales. The correlation between disposable personal income and retail sales is about 0.96, which shows a very strong positive relationship. This means that when disposable personal income increases, retail sales also tend to increase. The scatter plot supports this finding because most of the points follow a clear upward pattern. This result makes sense because disposable personal income represents the money people have available after taxes. When people have more available income, they are usually able to spend more on goods and services, which can increase retail sales.

The unemployment rate shows a weaker negative relationship with retail sales. The correlation between unemployment rate and retail sales is about -0.30. This means that higher unemployment is generally connected with lower retail sales, but the relationship is not very strong. The scatter plot shows a downward trend overall, but the points are more spread out compared with the income and retail sales relationship. This suggests that unemployment does matter, but it does not explain retail sales changes as clearly as disposable personal income does. One possible reason is that retail sales can also be affected by other factors, such as savings, government support, inflation, and consumer confidence.

The inflation rate has a moderate positive correlation with retail sales, around 0.36. However, this result needs to be interpreted carefully. A positive correlation does not necessarily mean that inflation causes people to buy more goods. Since retail sales are measured in dollar amounts, higher prices may increase the total sales value even if people are not actually buying more products. In other words, some of the increase in retail sales during higher inflation periods may reflect price increases rather than stronger real consumption.

This also shows why it is useful to compare several macroeconomic indicators instead of relying on only one variable. Each factor explains a different part of the economy, but they do not all affect retail sales in the same way.

Overall, our findings suggest that disposable personal income is the most important factor among the variables included in this project. Unemployment and inflation are still useful for understanding the broader economic context, but their relationships with retail sales are weaker and less direct. At the same time, the 2020 drop shows that unexpected external events can temporarily interrupt normal economic patterns. Based on our results, consumer purchasing power seems to play a major role in shaping retail sales trends.
</p>

## Future Work
<p>Through this project, we learned that working with economic data requires both technical preparation and careful interpretation. At first, the datasets looked simple because each dataset mainly included a date column and one numeric variable. However, after working with the data more closely, we realized that even simple datasets still require several important steps before analysis. For example, the dates had to be aligned, the units had to be standardized, and the variables had to be merged into one final dataset. These steps were necessary because small differences in formatting or units could affect the accuracy of the final analysis.
 
One important lesson we learned is that correlation can help identify relationships between variables, but it does not fully explain causation. For example, disposable personal income had a very strong positive correlation with retail sales, which makes sense from an economic perspective. However, this does not mean that income is the only reason retail sales increased. Other factors, such as consumer confidence, interest rates, savings levels, government support, and changes in prices, may also affect retail activity. In future work, we could include more variables to better understand the broader economic environment behind retail sales changes.
 
Another area for future improvement would be to use more advanced statistical methods. In this project, we mainly used visualizations and correlation analysis to explore the relationships between macroeconomic factors and retail sales. This was useful for identifying general patterns, but a future version of the project could use regression analysis or time series models to measure the effect of each variable more directly. For example, a multiple regression model could help estimate how much retail sales change when disposable personal income, unemployment, and inflation change while holding the other factors constant. This would make the analysis more precise and provide stronger evidence than correlation alone.
 
We could also improve the project by separating retail sales into different categories. Our current dataset uses total retail and food services sales, which gives a broad view of the retail market. However, different retail categories may respond differently to macroeconomic changes. For example, grocery stores, clothing stores, electronics stores, and restaurants may not react the same way to inflation or unemployment. In future work, using industry-level retail data could help us understand which parts of the retail sector are more sensitive to changes in income, prices, or labor market conditions.
 
Another possible improvement would be to compare national data with regional or state-level data. Since our current dataset only uses national-level monthly data, it does not capture differences across locations. Economic conditions can vary significantly by region, so regional data could provide a more detailed understanding of how macroeconomic factors affect retail sales in different areas.
 
Overall, this project helped us better understand the full process of working with real-world data, from acquisition and cleaning to visualization and interpretation. If we continued this project, we would expand the dataset, apply more advanced models, and explore more detailed retail categories or regional patterns. These improvements would make the analysis more complete and help us better understand the factors that influence retail sales. </p>

## Reproducing
1. **Data Collection and Acquisition:** We acquired our initial four datasets from the Federal Reserve Bank of St. Louis using `acquire_cpiaucsl.py`, `acquire_dspi.py`, `acquire_rsafs.py`, and `acquire_unrate.py` from the `notebooks` folder. The raw datasets are stored in ‘data/raw’. To ensure integrity of our datasets, we hashed each dataset using SHA-256. The expected hash values of each raw dataset are as follows:
   - CPIAUCSL SHA-256: 4494d9e15555069f0721bf5d18062bd7f88b70e3736ac5da2d5fcaf9ac64cd40
   - DSPI SHA-256: ba1a48acd91c12a92b591cb80bb58413fcbaad89b382fc2830d67145c87540c9
   - RSAFS SHA-256: 0d72fb748168b52997f318e01401cef1c9689a8aa3ce0d384f6b902d705a93c1
   - UNRATE SHA-256: 084d2f0cfe41575534b96bd51b88c6e93ddc8d5f0eca7e470ecfd19f5428c94f
2. **Storage and Organization:** We used different folders for files of different purposes, detailed as follows:
   - `data`: datasets acquired and created for the project
     - `raw`: raw datasets acquired from the FRED
     - `filtered_10yrs`: raw datasets filtered to January 1, 2015 - January 1, 2026
     - `merged_data`: integrated dataset and its cleaned version
   - `notebooks`: all python scripts used for the project
   - `reports`: project plan, status report, and final project report. 
   - `results`: table and graphs generated for analysis
   - `snakemake_files`: files for automating project workflow
3. **Data Integration:** We integrated the four datasets using `pd.merge()`. It was merged on `observation_date` using outer merge because we wanted to keep all the observations. We also filtered our columns to only include the observation date, unemployment rate, inflation rate, disposable personal income, and retail sales. The integrated dataset is stored in `data/merged_data`
4. **Data Quality and Cleaning:** For data profiling, we used `df.info()` to identify any missing values. For data cleaning, we performed the following operations:  
   - converted `observation_date`’s data type to datetime, 
   - standardized the unit of `disposable_personal_income` to millions, 
   - converted `retail_sales`’s data type to float, and
   - renamed `disposable_personal_income` to `disposable_personal_income_millions` and `retail_sales` to `retail_sales_millions`.
   
   The cleaned dataset is stored in `data/merged_data`

5. **Data Analysis and Visualization:** We created a correlation matrix with all the variables and a line plot for retail sales over time. We also created two scatterplots of disposable income versus retail sales and unemployment rate versus retail sales.
The table and graphs are stored in `results`
6. **Workflow automation:** We used Snakemake to create an automated workflow. The Snakemake file and execution script is stored in `snakemake_files`.

## References
- Kluyver, T., Ragan-Kelley, B., Pérez, F., Granger, B., Bussonnier, M., Frederic, J., Kelley, K., Hamrick, J., Grout, J., Corlay, S., Ivanov, P., Avila, D., Abdalla, S., & Willing, C. (2016). Jupyter Notebooks—A publishing format for reproducible computational workflows. In F. Loizides & B. Schmidt (Eds.), Positioning and Power in Academic Publishing: Players, Agents and Agendas (pp. 87–90).
- Python Software Foundation. (2023). Python (Version 3.11) [Computer software]. https://www.python.org/
- U.S. Bureau of Economic Analysis, Disposable Personal Income [DSPI], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/DSPI, May 5, 2026.
- U.S. Bureau of Labor Statistics, Consumer Price Index for All Urban Consumers: All Items in U.S. City Average [CPIAUCSL], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/CPIAUCSL, May 5, 2026.
- U.S. Bureau of Labor Statistics, Unemployment Rate [UNRATE], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/UNRATE, May 5, 2026.
- U.S. Census Bureau, Advance Retail Sales: Retail Trade and Food Services [RSAFS], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/RSAFS, May 5, 2026.

## Descriptive Metadata
```
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "name": "US Retail Sales and Macroeconomics Factors Dataset",
  "creator": [
    {
      "@type": "Person",
      "name": "Cindy Chen"
    },
    {
      "@type": "Person",
      "name": "Cuiying Lin"
    },
    {
      "@type": "Person",
      "name": "Yelin Zhong"
    }
  ],
  "license": "CC0 1.0 Universal",
  "distribution": {
    "@type": "DataDownload",
    "contentUrl": "https://github.com/CuiyingLin17/IS477BusinessCoders/blob/main/data/merged_data/merged_dataset_cleaned.csv",
    "encodingFormat": "CSV"
  },
  "dateCreated": "2026-05-04",
  "keywords": [
    "economics",
    "retail sales",
    "inflation",
    "unemployment",
    "income"
  ]
}
```
