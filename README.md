# Budget Optimizer App

Welcome to the **Budget Optimizer**, an interactive Streamlit application designed to help you compare your actual financial allocations with your ideal budgeting plan. This tool assists both individuals and organizations in identifying spending gaps, optimizing resource allocation, and visualizing the balance between planned and real-world expenditures.

## Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Author](#author)
- [References](#references)

## Project Overview

This application offers a streamlined way to **upload, compare, and analyze ideal and actual budget spreadsheets**. Users can visually compare category-wise allocations, spot excesses and shortfalls, and receive actionable summaries for better financial decision-making.

- Upload an *ideal* and an *actual* budget (in `.xlsx` format)
- Instantly visualize differences in amounts and proportions
- Highlight over/under-spending for each budget category
- Simple, browser-based access via Streamlit

## Key Features

- **File Uploader:** Drag-and-drop interface for uploading two budget files.
- **Automated Comparison:** Merges categories for alignment and analysis.
- **Interactive Tables:** View ideal vs. actual distribution side-by-side.
- **Bar Chart Visualization:** Instantly shows over and under spending by category.
- **Summary Metrics:** Total planned vs. actual amounts and surplus/deficit calculation.
- **Modern UI:** Intuitive, clean design for easy interaction.
- **Modular Structure:** Each app function is contained in a dedicated script for easy extension and maintenance.

## How It Works

1. **Upload** your ideal and actual budget spreadsheets.
2. **Compare**: The app aligns categories, calculates differences, and fills any missing values with zeros to prevent analysis breakdown.
3. **Visualize**: See your financial standing through comparative tables and interactive bar charts.
4. **Interpret**: Instantly understand where your spending deviates from the plan and by how much.




### Project Files

- `main.py`: Entry point for the app UI
- `1_Compare.py`: Core logic for file uploads, comparison, and visualization
- `2_actual.py`: Component for viewing/analyzing only the actual budget
- `3_Ideal.py`: Component for viewing/analyzing only the ideal budget

Ensure your Excel files match the expected column names:  
For **ideal budget**: `"Category"`, `"Proportion"`  
For **actual budget**: `"Category"`, `"Amount"`
Two demo files are also available on the main page.

## Usage

1. Place all application files in the same directory.
2. Open a terminal in that directory and run:

    ```bash
    streamlit run main.py
    ```

3. Follow the Streamlit sidebar to access comparison or individual analysis pages.
4. Upload your `ideal` and `actual` budget Excel files.
5. Review the output, tables, and interactive charts for quick insights.


## Author

- **Lead Developer:** Jozy Fatima

Special thanks to the open-source community for Streamlit and supporting libraries that make rapid application development accessible.

## References

- Streamlit Documentation
- pandas, matplotlib, seaborn official documentation

*Last updated: July 26, 2025. Feedback and contributions are welcome!*
