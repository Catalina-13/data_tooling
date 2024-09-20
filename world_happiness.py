import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


# Function to load and clean data
@st.cache_data
def load_data(year):
    if year == 2019:
        df = pd.read_csv(
            f"data/{year}.csv",
            usecols=[
                "Country or region",
                "Score",
                "GDP per capita",
                "Social support",
                "Healthy life expectancy",
                "Freedom to make life choices",
                "Generosity",
                "Perceptions of corruption",
            ],
        )
        df.columns = [
            "Country",
            "Happiness Score",
            "Economy (GDP per Capita)",
            "Family",
            "Health (Life Expectancy)",
            "Freedom",
            "Generosity",
            "Trust (Government Corruption)",
        ]
    else:
        df = pd.read_csv(f"data/{year}.csv")
        df.columns = df.columns.str.strip()  # Remove leading/trailing spaces
        columns_to_keep = [
            "Country",
            "Region",
            "Happiness Rank",
            "Happiness Score",
            "Economy (GDP per Capita)",
            "Family",
            "Health (Life Expectancy)",
            "Freedom",
            "Trust (Government Corruption)",
            "Generosity",
            "Dystopia Residual",
        ]
        df = df[columns_to_keep]

    return df


# Load datasets
all_data = {2015: load_data(2015), 2016: load_data(2016), 2019: load_data(2019)}

st.title("🌍 World Happiness Report (2015, 2016, 2019)")
st.markdown(
    "Explore the happiness scores of countries based on the World Happiness Report."
)

year = st.selectbox("Select Year", [2015, 2016, 2019])

# Country selection for comparison
selected_countries = st.multiselect(
    "Select Countries to Compare",
    options=all_data[year]["Country"].unique(),
    default=[
        "United States",
        "Canada",
        "Germany",
    ],  # Default selection
)

# Filter data for selected countries
comparison_data = all_data[year][all_data[year]["Country"].isin(selected_countries)]
st.write(comparison_data)

# Visualization: horizontal bar chart for Happiness Scores of selected countries
st.subheader(f"Happiness Scores of selected countries in {year}")
if not comparison_data.empty:
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.barplot(
        x="Happiness Score", y="Country", data=comparison_data, palette="Blues", ax=ax
    )
    ax.set_xlabel("Happiness Score")
    ax.set_title(f"Happiness Scores of Selected Countries in {year}")
    st.pyplot(fig)
else:
    st.write("Please select at least one country to visualize.")

st.subheader("Compare Happiness Scores from 2015 to 2019")

# Prepare data for comparison across all years
comparison_scores = []
for country in selected_countries:
    for y in [2015, 2016, 2019]:
        if country in all_data[y]["Country"].values:
            score = all_data[y][all_data[y]["Country"] == country][
                "Happiness Score"
            ].values[0]
            comparison_scores.append(
                {"Country": country, "Year": y, "Happiness Score": score}
            )

comparison_df = pd.DataFrame(comparison_scores)

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(
    data=comparison_df, x="Year", y="Happiness Score", hue="Country", marker="o", ax=ax
)
ax.set_xticks([2015, 2016, 2019])
ax.set_ylabel("Happiness Score")
ax.set_title("Happiness Score Comparison from 2015 to 2019")
st.pyplot(fig)

st.subheader("Explore Factors Influencing Happiness Scores")
st.write("Select countries to visualize how different factors impact happiness scores.")

factor_countries = st.multiselect(
    "Select Countries for Factor Analysis",
    options=all_data[year]["Country"].unique(),
    default=selected_countries,
)

# Ensure at least one country is selected
if factor_countries:
    factor_data = all_data[year][all_data[year]["Country"].isin(factor_countries)]

    # Slider for additional metrics
    metrics = [
        "Economy (GDP per Capita)",
        "Family",
        "Health (Life Expectancy)",
        "Freedom",
        "Generosity",
        "Trust (Government Corruption)",
    ]
    selected_metric = st.selectbox("Select Metric for Visualization", metrics)

    metric_fig, metric_ax = plt.subplots(figsize=(10, 8))
    sns.barplot(
        x=selected_metric,
        y="Country",
        data=factor_data,
        palette="viridis",
        ax=metric_ax,
    )
    metric_ax.set_title(f"{selected_metric} for Selected Countries in {year}")
    st.pyplot(metric_fig)
else:
    st.write("Please select at least one country to visualize the factors.")
