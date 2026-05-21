Data Cleaning & Visualization Project
A data science project that cleans and visualizes the Titanic dataset using Python.
Dataset

Source: Titanic Dataset
URL: https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

Libraries Used

pandas — Data manipulation and cleaning
numpy — Numerical operations
matplotlib — Data visualization
seaborn — Statistical data visualization

Project Steps
Step 1: Load Dataset

Loaded Titanic dataset directly from GitHub URL using pandas

Step 2: Data Cleaning

Handled missing values in Age column (filled with median)
Handled missing values in Embarked column (filled with mode)
Dropped Cabin column (too many missing values)
Removed duplicate rows
Removed outliers from Age using IQR method

Step 3: Visualizations

Survival Count — Bar chart showing survived vs not survived
Age Distribution — Histogram with KDE curve
Survival by Gender — Grouped bar chart
Passenger Class Distribution — Bar chart
Fare Distribution by Class — Box plot
Correlation Heatmap — Heatmap of feature correlations

Step 4: Key Insights

Overall survival rate of passengers
Female vs Male survival rate comparison
Average age and fare of passengers

How to Run

Clone the repository:

bashgit clone https://github.com/Mr-Prasan-2008/data-cleanind-visualization.git

Install required libraries:

bashpip install pandas matplotlib seaborn

Run the script:

bashpython data_cleaning_visualization.py
Output

Charts displayed on screen
Visualization saved as titanic_visualization.png
