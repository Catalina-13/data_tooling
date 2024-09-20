# World Happiness Report Analysis

## Overview

This project provides an interactive web application for analyzing the World Happiness Report data from 2015, 2016, and 2019. Users can explore happiness scores of various countries, compare scores across different years, and visualize the influence of various factors on happiness.

## Features

- **Year Selection**: Choose between the years 2015, 2016, and 2019 to view happiness data.
- **Country Comparison**: Select multiple countries to compare their happiness scores and other metrics.
- **Visualizations**: View bar charts and line plots to visualize happiness scores and various factors affecting happiness.
- **Factor Analysis**: Analyze how different factors, such as GDP per capita, social support, and freedom to make life choices, influence happiness scores.

## Requirements

To run this application, you need the following:

- Python 3.11
- Streamlit
- Pandas
- Matplotlib
- Seaborn

You can install the required packages using pip:

```bash
pip install streamlit pandas matplotlib seaborn
```

## Dataset

The application uses the World Happiness Report data for the years 2015, 2016, and 2019. Ensure the datasets are in CSV format and stored in a folder named `data`. The expected file names are:

- `2015.csv`
- `2016.csv`
- `2019.csv`

### Example Data Structure

For 2019, the dataset should contain the following columns:
- `Country or region`
- `Score`
- `GDP per capita`
- `Social support`
- `Healthy life expectancy`
- `Freedom to make life choices`
- `Generosity`
- `Perceptions of corruption`

For 2015 and 2016, the datasets should contain:
- `Country`
- `Happiness Rank`
- `Happiness Score`
- `Economy (GDP per Capita)`
- `Family`
- `Health (Life Expectancy)`
- `Freedom`
- `Trust (Government Corruption)`
- `Generosity`
- `Dystopia Residual`

## Running the Application

To start the application, navigate to the project directory in your terminal and run:

```bash
streamlit run app.py
```

This will launch the Streamlit app in your web browser.

## User Input

- `Year Selection`: Use the dropdown menu to select the year of interest (2015, 2016, or 2019).
- `Country Selection`: Use the multiselect widget to choose one or more countries for comparison.
- `Metric Selection`: After selecting countries, choose a metric (e.g., GDP per capita, health) for factor analysis.

## Output

- `Happiness Scores`: Displays the happiness scores of the selected countries for the chosen year.
- `Comparative Visualization`: Shows a bar chart of happiness scores and a line plot comparing scores across selected years (2015 to 2019).
- `Factor Analysis`: Visualizes the selected metric for the chosen countries.
