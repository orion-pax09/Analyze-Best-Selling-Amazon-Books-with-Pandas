# Amazon Best Sellers Analysis with Pandas

## About the Project

This project uses a dataset of Amazon's top 50 bestselling books from **2009–2019** to practice practical, real-world data analysis with Pandas.

The purpose of the project is to demonstrate how Pandas can be used to take a raw CSV dataset, explore it, clean it, analyze it, and export useful results — a workflow common to most real-world data analysis tasks.

## Project Goals

The main goals of this project are to learn and demonstrate:

- Loading CSV data with Pandas
- Exploring a dataset
- Understanding columns and data types
- Removing duplicate records
- Renaming columns
- Converting data types
- Filtering rows
- Selecting columns
- Sorting data
- Counting values with `value_counts()`
- Grouping data with `groupby()`
- Calculating averages with `mean()`
- Finding highly rated books
- Comparing Fiction vs Non-Fiction
- Exporting analysis results to CSV
- Creating basic visualizations with Matplotlib

## Dataset

The dataset used in this project is the [**Amazon Top 50 Bestselling Books (2009–2019)**](https://www.kaggle.com/datasets/sootersaalu/amazon-top-50-bestselling-books-2009-2019) dataset from Kaggle. If you're a beginner, feel free to download it from the link above and follow along with this project.

It contains **550 records and 7 columns**:

| Column      | Description                        |
| ----------- | ----------------------------------- |
| Name        | Book name                          |
| Author      | Book author                        |
| User Rating | Amazon user rating                 |
| Reviews     | Number of user reviews             |
| Price       | Book price                         |
| Year        | Year the book appeared on the list |
| Genre       | Fiction or Non Fiction             |

## What I Did

The project follows a simple workflow:

**Load → Explore → Clean → Analyze → Export**

### 1. Load

Used Pandas to read the CSV file into a DataFrame.

### 2. Explore

Used methods such as:

- `head()`
- `shape`
- `columns`
- `describe()`

to understand the structure, size, and content of the dataset.

### 3. Clean

Performed basic data cleaning:

- Removed duplicate rows with `drop_duplicates()`
- Renamed columns using `rename()`
- Converted `Price` to a numeric type using `astype(float)`

### 4. Analyze

Performed the following analyses:

- Found the authors appearing most frequently on the bestseller list using `value_counts()`
- Found books with ratings of 4.8 or higher
- Found the top books based on number of reviews
- Calculated the average rating for each genre using `groupby()` and `mean()`
- Compared Fiction and Non-Fiction performance

### 5. Export

Exported analysis results to CSV files using `to_csv()`, including:

- `top_authors.csv`
- `avg_rating_by_genre.csv`
- `genre_performance.csv`

## Key Pandas Concepts Learned

| Method                | Purpose                          |
| --------------------- | --------------------------------- |
| `pd.read_csv()`        | Load CSV data                    |
| `.head()`              | View first rows                  |
| `.shape`               | Check rows and columns           |
| `.columns`             | View column names                |
| `.drop_duplicates()`   | Remove duplicate rows            |
| `.rename()`            | Rename columns                   |
| `.astype()`            | Change data type                 |
| `.value_counts()`      | Count occurrences                |
| `.loc[]`               | Select/filter rows and columns   |
| `.sort_values()`       | Sort data                        |
| `.groupby()`           | Group data                       |
| `.mean()`              | Calculate averages               |
| `.to_csv()`            | Export results                   |

## Example Questions Answered

This project uses Pandas to answer questions such as:

- Which authors appear most often?
- Which books have ratings of 4.8 or higher?
- Which books have the most reviews?
- Which genre has the higher average rating?
- How can the cleaned and analyzed data be exported for further use?

## Learning Purpose

This repository is a **hands-on Pandas practice project**.

The goal is not simply to produce the final answers, but to demonstrate the *process* of taking a real dataset and working through it step by step:

```text
Raw CSV
   ↓
Explore the data
   ↓
Clean the data
   ↓
Filter & transform
   ↓
Analyze
   ↓
Visualize
   ↓
Export results
```

This workflow represents a basic real-world data analysis process and provides practice for working with larger, more complex datasets in the future.

## Tools Used

- Python
- Pandas
- CSV

## Repository Structure

```text
amazon-best-sellers-analysis/
│
├── bestsellers.csv
├── main.py
├── top_authors.csv
├── avg_rating_by_genre.csv
├── genre_performance.csv
└── README.md
```

## Goal

The goal of this project is to become comfortable using Pandas to **load, clean, explore, analyze, visualize, and export data from a real-world dataset**.
