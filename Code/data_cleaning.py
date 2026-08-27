import pandas as pd
import os

# ==========================================
# 1. LOAD DATASET
# ==========================================

base_path = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(
    base_path, "..", "Dataset", "netflix_titles.csv"
)

df = pd.read_csv(file_path)

print("Original Dataset Shape:", df.shape)


# ==========================================
# 2. CHECK DUPLICATES
# ==========================================

duplicates = df.duplicated().sum()

print("Duplicate rows found:", duplicates)

df = df.drop_duplicates()

print("Shape after removing duplicates:", df.shape)


# ==========================================
# 3. HANDLE MISSING VALUES
# ==========================================

# Replace missing values in text columns
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")
df["duration"] = df["duration"].fillna("Unknown")


# Remove rows where date_added is missing
df = df.dropna(subset=["date_added"])


# ==========================================
# 4. CONVERT DATE FORMAT
# ==========================================

df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)


# ==========================================
# 5. CLEAN TEXT DATA
# ==========================================

text_columns = [
    "type",
    "title",
    "director",
    "cast",
    "country",
    "rating",
    "duration",
    "listed_in",
    "description"
]

for column in text_columns:
    df[column] = df[column].astype(str).str.strip()


# ==========================================
# 6. STANDARDIZE TYPE VALUES
# ==========================================

df["type"] = df["type"].str.title()


# ==========================================
# 7. CHECK CLEANED DATA
# ==========================================

print("\n========== CLEANING RESULTS ==========")

print("Cleaned Dataset Shape:", df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Rows After Cleaning:")
print(df.duplicated().sum())

print("\nData Types After Cleaning:")
print(df.dtypes)


# ==========================================
# 8. SAVE CLEANED DATASET
# ==========================================

output_path = os.path.join(
    base_path, "..", "Dataset", "cleaned_netflix_titles.csv"
)

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
print(output_path)