# Data Analyst Internship - Task 1

## Data Cleaning and Preprocessing

### Objective

The objective of this task is to clean and preprocess a raw Netflix Movies and TV Shows dataset using Python and Pandas.

The dataset was checked and cleaned for missing values, duplicate records, inconsistent text formatting, date formats, and data types.

## Dataset

Dataset used: Netflix Movies and TV Shows

Original dataset:
- Rows: 8,807
- Columns: 12

## Tools Used

- Python 3.7
- Pandas
- VS Code

## Data Cleaning Steps

### 1. Missing Values

Missing values were identified using:

`df.isnull().sum()`

Missing values were found in:
- director
- cast
- country
- date_added
- rating
- duration

Missing values in categorical columns were replaced with `Unknown` or `Not Rated`.

Rows with missing `date_added` values were removed.

### 2. Duplicate Records

Duplicate records were checked using:

`df.duplicated().sum()`

The original dataset contained 0 duplicate records.

### 3. Text Cleaning

Extra spaces were removed from text columns using:

`.str.strip()`

The `type` column was standardized.

### 4. Date Conversion

The `date_added` column was converted from object format to datetime format using:

`pd.to_datetime()`

The final data type is:

`datetime64[ns]`

### 5. Data Type Checking

Data types were checked before and after preprocessing.

## Cleaning Results

| Description | Result |
|---|---:|
| Original Rows | 8,807 |
| Original Columns | 12 |
| Duplicate Rows | 0 |
| Rows After Cleaning | 8,797 |
| Columns After Cleaning | 12 |
| Missing Values After Cleaning | 0 |
| Duplicate Rows After Cleaning | 0 |

## Project Files

- `Code/data_cleaning.py` - Python cleaning code
- `Dataset/netflix_titles.csv` - Original dataset
- `Dataset/cleaned_netflix_titles.csv` - Cleaned dataset
- `screenshots/` - Screenshots of code and output

## Conclusion

The Netflix dataset was successfully cleaned and preprocessed using Python and Pandas. Missing values were handled, duplicate records were checked, text values were standardized, and the date column was converted into a proper datetime format.

The final cleaned dataset contains 8,797 rows and 12 columns and is ready for further data analysis and visualization.