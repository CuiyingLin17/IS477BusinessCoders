# Task updates
We have completed a couple of our tasks to find and prepare our datasets, but all other tasks have not been started; details for the tasks that we completed are as follows:
### Identify and describe specific storage and organization strategy
<p> My strategy for organizing and storing our datasets and work was to have different folders for different types of files. Notebooks will contain all the coding work, the acquired notebooks include the code to retrieve the data. Future notebooks will be named according to their purpose and added to this folder. Other folders that are needed to organize and document our process include results, to explain our process and findings, references, data, to hold cleaned and merged data, and any future work done on other software. The reason for me to organize the files in this way is because having all the notebooks in one place for my members to look at will be helpful in the future of this project. In case we face errors in our code, back tracking will be easy if our files are stored and named based on their functions. <br>
For our future work the contents in the results folder should include all and only files that help explain and showcase the final product of our project. These most likely will be text files. References will include all of the websites and softwares that were used to make this project possible. Finally, we will need to make readme and contribution files to make this project more accessible to new users. </p>

### Collect & Prepare Data
<p> We acquired the datasets that were described in our Project Plan, and we checked for integrity by using SHA-256 to be prepared to download for future usage. Because our data is easily accessible online, there was not too much extra work needed to prepare the data. The hash will help the data be consistent in the future when the data set gets updated. Hash will help future users access the same data we are using currently to achieve the same results. </p>

# Updated Timeline
| Tasks | Description | Requirement Addressing | Complete by | Responsible Party | Status |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Relate project workflow with lifecycle models | Lifecycle models were discussed in class. The responsible party will review these models and relate the project to one or more models. | Data lifecycle | May 3 | Yelin | Not yet started |
| Identify and describe file and data types | The responsible party will describe 1) the file types and 2) the datasets used (i.e. structure and schema). | Files storage and organization | March 25 | Cuiying | Completed |
| Identify and describe specific storage and organization strategy | The responsible party will determine how files and data will be stored and organized to better suit project needs. The responsible party will also determine file naming conventions and document the strategy. | Files storage and organization | March 11 | Cindy | Completed |
| Identify and handle constraints | There may be ethical, legal, and/or policy constraints to data usage. The responsible party will identify all relevant constraints and describe how these constraints were addressed. Examples of constraints include consent, privacy/confidentiality, copyright, licenses, and terms of use. | Ethical data handling | Ongoing until submission | Yelin | Ongoing |
| Collect data | The responsible party will find and retrieve datasets on unemployment, inflation, income, and retail sales from trustworthy sources (e.g. FRED). | Data collection and acquisition | March 8 | Team | Completed |
| Prepare data | The responsible party will extract relevant information/columns from the raw datasets and add any columns calculated from existing columns (e.g. inflation rate). | Extraction and enrichment | March 15 | Cindy | Completed |
| Integrate data | The responsible party will combine all the datasets into one dataset using either Pandas from Python or SQL. | Data integration | April 26 | Cuiying | Not yet started |
| Assess and document data quality | The responsible party will assess the quality of the data and document the results. | Data quality | March 20 | Yelin | Completed |
| Clean data and describe methods used | The responsible party will clean the dataset for any missing values, outliers, or syntactic or semantic differences between datasets. | Data cleaning | April 19 | Team | Not yet started |
| Create automated workflow | The responsible party will create an automated end-to-end workflow for data handling. | Workflow automation and provenance | April 26? | Cindy | Not yet started |
| Analyze datasets | The responsible party will analyze the integrated dataset to answer the research question. | N/A | May 2 | Team | Not yet started |
| Document workflow | The responsible party will document the work performed in detail to allow for reproduction. For example, clear instructions for the workflow, description of data sources, and describe analysis steps. | Reproducibility and provenance | Ongoing until submission | Team | Ongoing |
| Document relevant information of data used | The responsible party will document descriptions of the datasets (e.g. data source, variable definitions, data types, etc.) | Metadata and data documentation | May 2 | Cuiying | Not yet started |

# Changes to Project Plan
<p> We pushed the Complete By dates for all the other tasks to later dates because we realized that we will not meet the original deadlines with our current progress. We changed the date for identifying and describing constraints to "Ongoing until submission" because we believe that the constraints apply to data extraction, usage, and distribution which would make more sense for this task to be completed as an ongoing process. We also changed the date for data lifecycle relation to May 3 because we believe that such relation can be better made when the whole process is completed. </p>

# Challenges & Problems
<p>We identified a challenge which is practical. The datasets we used are from different sources, so they need careful documentation of links/ agency origin. We addressed this by recording the source information for each dataset in the project materials. Besides, because these datasets are maintained and updated over time, the values may change if downloaded at different dates. This creates a reproducibility concern for later project stages, so we planned to keep a stable copy of the downloaded files in the repository and document retrieval details.

What’s more, we also found an analytical limitation in the current dataset selection. All four variables are measured at the U.S. national level, which means our analysis will focus on broad macroeconomic relationships rather than regional or state-level differences. In addition, although the datasets can be aligned by date, they represent different economic concepts and may require preprocessing before direct comparison. This means the data cannot simply be combined without checking consistency in time coverage and interpretation.</p>


# Team Member Contribution
<p>Cindy started setting up the folders needed to organize notebooks and future files that will be made. She also uploaded the data acquisition Google Co-lab files to acquire all 4 files and also found the hash of all the files. </p>

<p>Yelin worked on the Identify and Handle Constraints, Assess and Document Data Quality, and Challenges & Problems sections. She did the data quality check and reviewed the selected datasets and summarized the main data quality and project constraints identified during this milestone.
</p>

# Identify and handle constraints
<p>We discovered a number of limitations pertaining to data consumption and analysis after examining the four datasets (UNRATE, CPIAUCSL/CUSR0000SA0, RSAFS, and DSPI) that we had chosen for this study. All datasets are free of sensitive or private data because they are sourced from public sources including FRED, BLS, the U.S. Census Bureau, and the U.S. Bureau of Economic Analysis. As a result, we found no issues with confidentiality or privacy.</p>

# Assess and document data quality
<p>During this milestone, we conducted an initial data quality assessment of the four selected datasets: UNRATE, CPIAUCSL, RSAFS, and DSPI. We reviewed each dataset for structure, missing values, duplicate rows, and time coverage.

The datasets are generally well-structured and suitable for later analysis. Each file contains one date column (`observation_date`) and one numeric variable column. UNRATE has 939 rows, CPIAUCSL has 950 rows, RSAFS has 410 rows, and DSPI has 805 rows. This consistent structure will make later preprocessing and integration more manageable.

The assessment also showed that data completeness is generally strong. RSAFS and DSPI contain no missing values, while UNRATE and CPIAUCSL each contain one missing value in the indicator column. No duplicate rows were found in any of the four datasets. In addition, all four datasets cover a sufficiently broad time range for the project, although their starting dates differ. UNRATE spans from 1948-01-01 to 2026-03-01, CPIAUCSL spans from 1947-01-01 to 2026-02-01, RSAFS spans from 1992-01-01 to 2026-02-01, and DSPI spans from 1959-01-01 to 2026-01-01.

Based on this review, we concluded that the selected datasets are appropriate for the project, but further preprocessing will still be required. In particular, the datasets will need to be aligned by time period, and the small number of missing values in UNRATE and CPIAUCSL will need to be handled before merging and analysis.</p>












