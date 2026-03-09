# Overview
<p> Our goal for this project is to gain a better understanding on retail sales trends based on macroeconomic factors by looking at historic data from the past 10 years. As Business + Data Science majors, this is a good opportunity to apply the knowledge and skillsets learned in this class to broaden our knowledge on the economy. The macroeconomic factors we selected to focus on include the unemployment rate and the inflation rate. With our combined background in Accountancy and Finance, we will be able to analyze the relationship between these trends. </p>
<p> Our first steps include dividing the work, and have each of us focus on finding a representative data set for unemployment rate, CPI, and retail sales from a reliable source. We will communicate with each other on our findings then will use the common attribute, in this case the dates of the rates, to find patterns. By comparing the unemployment rates and CPI changes to the retail trends, we will gain a solid understanding of how the market moves with these rates. </p>
<p> With this understanding, in our future careers as Accountants or Financial advisors, we can make accurate predictions on the market and adjust our work as needed. Outside of using this information for future jobs, we could also apply this knowledge when investing our own portfolio. Overall, we hope this project gives us a chance to practice our coding skills and learn more about the economy to assist our future careers and lives. </p>

# Team
<p>Our team consists of three members with backgrounds in Business and DataScience.
  
Cuiying: Accountancy&DataScience

roles&responsibilities: Identifying and describing the  file types and the datasets used (i.e. structure and schema). Combining all the datasets into one dataset using either Pandas from Python or SQL. Documenting descriptions of the datasets (e.g. data source, variable definitions, data types, etc.) Assist in team collaborative portions of the project and help team members in their parts if needed. 

Cindy: Finance&DataScience

roles&responsibilities: Organizing and describing files in the github repository. Collect and organize the information from the data sets. Create an automated workflow for data handling. Assist in team collaborative portions of the project and help team members in their parts if needed. 

Yelin: Accountancy&DataScience

roles&responsibilities: Relating our project workflow with data lifecycle models discussed in class.Identifying and documenting ethical, legal, and policy constraints related to the datasets we use. Assessing and documenting data quality, including consistency, completeness, and readiness for integration. Assist in team collaborative portions of the project and help team members in their parts if needed. </p>


# Datasets

<p> The data sets our group chooses includes unemployment rate, consumer price index, annual income, and retail sales data for trade and food services. All the data sets can be linked together by the date to make comparing the different variables possible at the same date. We found all of the data sets from the Federal Reserve Bank of St. Louis which updates their data monthly. </p>

<p> The unemployment rate data set only includes the data and the respective rate, making the data easy to analyze and compare with the other data sets. This data was retrieved from the U.S. Bureau of Labor Statistics and includes people over the age of 16 that are unemployed who are not in the military or living in institutions. By comparing the numbers from this data set and the retail sales trend data set, we can observe any possible relationships between the two. </p>

<p>
  
**Unemployment Dataset**
  
This unemployment dataset measures the unemployment condition in the labor market. In this project, the unemployment rate could help us examine whether different labor market conditions lead to the different conditions in U.S. retail sales.
  
https://fred.stlouisfed.org/series/UNRATE#
source: U.S. Bureau of Labor Statistics; public data

**Consumer price index: to download data**

This consumer price index dataset measures the change in the price level paid by consumers for getting good/services. It could reflect the purchasing power of consumers. In our project, this dataset could help us to know whether it is a key variable associated with the changes in retail sales from 2016-2026. (We use the CPIAUCSL series available through FRED, which is originally sourced from the U.S. Bureau of Labor Statistics (BLS).)

https://data.bls.gov/series-report; series id: CUSR0000SA0; bruh this works now
https://fred.stlouisfed.org/series/CPIAUCSL 
U.S. Bureau of Labor Statistics; public data

**retail sales**

This dataset measures the total monthly sales of retail trade and food services in the U.S. since 1992. In our project, it is the key factor which we want to research. The dataset  we picked is from FRED with the series id RSAFS.
            
https://fred.stlouisfed.org/series/RSAFS；series id: RSAFS
U.S. Census Bureau; public data

**Income**

This dataset measures income available to individuals after taxes and reflects consumers’ ability to spend. In this project, it helps us analyze whether changes in income are related to changes in U.S. retail sales.We use the DSPI series from FRED.

https://fred.stlouisfed.org/series/DSPI 
U.S. Bureau of Economic Analysis; public data
</p>

# Timeline
| Tasks | Description | Requirement Addressing | Complete by | Responsible Party |
| ----- | ----- | ----- | ----- | ----- |
| Relate project workflow with lifecycle models | Lifecycle models were discussed in class. The responsible party will review these models and relate the project to one or more models. | Data lifecycle | Ongoing until submission | Yelin |
| Identify and describe file and data types | The responsible party will describe 1) the file types and 2) the datasets used (i.e. structure and schema). | Files storage and organization | March 25 | Cuiying |
| Identify and describe specific storage and organization strategy | The responsible party will determine how files and data will be stored and organized to better suit project needs. The responsible party will also determine file naming conventions and document the strategy. | Files storage and organization | March 11 | Cindy |
| Identify and handle constraints | There may be ethical, legal, and/or policy constraints to data usage. The responsible party will identify all relevant constraints and describe how these constraints were addressed. Examples of constraints include consent, privacy/confidentiality, copyright, licenses, and terms of use. | Ethical data handling | March 11 | Yelin |
| Collect data | The responsible party will find and retrieve datasets on unemployment, inflation, income, and retail sales from trustworthy sources (e.g. FRED). | Data collection and acquisition | March 8 | Team |
| Prepare data | The responsible party will extract relevant information/columns from the raw datasets and add any columns calculated from existing columns (e.g. inflation rate). | Extraction and enrichment | March 15 | Cindy |
| Integrate data | The responsible party will combine all the datasets into one dataset using either Pandas from Python or SQL. | Data integration | March 15 | Cuiying |
| Assess and document data quality | The responsible party will assess the quality of the data and document the results. | Data quality | March 20 | Yelin |
| Clean data and describe methods used | The responsible party will clean the dataset for any missing values, outliers, or syntactic or semantic differences between datasets. | Data cleaning | March 21 | Team |
| Create automated workflow | The responsible party will create an automated end-to-end workflow for data handling. | Workflow automation and provenance | March 22? | Cindy |
| Analyze datasets | The responsible party will analyze the integrated dataset to answer the research question. | N/A | March 23 | Team |
| Document workflow | The responsible party will document the work performed in detail to allow for reproduction. For example, clear instructions for the workflow, description of data sources, and describe analysis steps. | Reproducibility and provenance | Ongoing until submission | Team |
| Document relevant information of data used | The responsible party will document descriptions of the datasets (e.g. data source, variable definitions, data types, etc.) | Metadata and data documentation | March 22 | Cuiying |

# Constraints
The known limitations and challenges with our datasets and approach are as follows:
- All of our datasets contain information at the national level, which limits analysis at the regional or state level. 
- All of the datasets are revised and updated monthly, which could be an issue of reproducibility at a later date. 
- The consumer price index dataset and unemployment dataset is missing data for October 2025 as a result of the government shutdown. 
- Our approach analyzes the effects of macroeconomic factors, specifically unemployment, inflation, and income, on retail sales. However, there are other macroeconomic factors, such as interest rates and gross domestic product, and non-macroeconomic factors, such as change in consumer behavior and disruption in supply chain, that affect retail sales altogether. The three factors of our analysis may not encompass the full image.

# Gaps
Currently, our team needs additional input on automation and data quality assessment. While we have a basic understanding of automation, we do not know how such a process is implemented. We also have various interpretations of data quality, therefore a formal definition would be helpful. 
