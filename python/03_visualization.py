# COVID-19 Data Analysis
# Step 3: Data Visualization

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# 1. Load cleaned dataset
# --------------------------------------------------

df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\covid 19\data\covid19_cleaned.csv")

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Create images folder if required
import os
os.makedirs("images", exist_ok=True)

# --------------------------------------------------
# 2. Set visualization style
# --------------------------------------------------

sns.set_style("whitegrid")

# --------------------------------------------------
# 3. COVID-19 Confirmed Cases Over Time
# --------------------------------------------------

daily_cases = df.groupby("Date")["Confirmed"].sum()

plt.figure(figsize=(12, 6))

plt.plot(
    daily_cases.index,
    daily_cases.values,
    linewidth=2
)

plt.title("COVID-19 Confirmed Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("images/covid_cases_over_time.png")
plt.show()

# --------------------------------------------------
# 4. COVID-19 Deaths Over Time
# --------------------------------------------------

daily_deaths = df.groupby("Date")["Deaths"].sum()

plt.figure(figsize=(12, 6))

plt.plot(
    daily_deaths.index,
    daily_deaths.values,
    linewidth=2
)

plt.title("COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Deaths")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("images/covid_deaths_over_time.png")
plt.show()

# --------------------------------------------------
# 5. Top 10 States by Confirmed Cases
# --------------------------------------------------

top_cases = (
    df.groupby("State")["Confirmed"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_cases.values,
    y=top_cases.index
)

plt.title("Top 10 States by Confirmed COVID-19 Cases")
plt.xlabel("Confirmed Cases")
plt.ylabel("State")

plt.tight_layout()

plt.savefig("images/top_states_cases.png")
plt.show()

# --------------------------------------------------
# 6. Top 10 States by Deaths
# --------------------------------------------------

top_deaths = (
    df.groupby("State")["Deaths"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_deaths.values,
    y=top_deaths.index
)

plt.title("Top 10 States by COVID-19 Deaths")
plt.xlabel("Deaths")
plt.ylabel("State")

plt.tight_layout()

plt.savefig("images/top_states_deaths.png")
plt.show()

# --------------------------------------------------
# 7. Top 10 States by Recoveries
# --------------------------------------------------

top_recovered = (
    df.groupby("State")["Recovered"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_recovered.values,
    y=top_recovered.index
)

plt.title("Top 10 States by COVID-19 Recoveries")
plt.xlabel("Recovered Cases")
plt.ylabel("State")

plt.tight_layout()

plt.savefig("images/top_states_recovered.png")
plt.show()

# --------------------------------------------------
# 8. Active Cases by State
# --------------------------------------------------

top_active = (
    df.groupby("State")["Active"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_active.values,
    y=top_active.index
)

plt.title("Top 10 States by Active COVID-19 Cases")
plt.xlabel("Active Cases")
plt.ylabel("State")

plt.tight_layout()

plt.savefig("images/top_states_active.png")
plt.show()

# --------------------------------------------------
# 9. Recovery vs Deaths
# --------------------------------------------------

total_recovered = df["Recovered"].sum()
total_deaths = df["Deaths"].sum()

comparison = pd.Series({
    "Recovered": total_recovered,
    "Deaths": total_deaths
})

plt.figure(figsize=(8, 6))

plt.pie(
    comparison.values,
    labels=comparison.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("COVID-19 Recoveries vs Deaths")

plt.tight_layout()

plt.savefig("images/recovery_vs_deaths.png")
plt.show()

# --------------------------------------------------
# 10. Confirmed vs Deaths
# --------------------------------------------------

state_data = (
    df.groupby("State")[["Confirmed", "Deaths"]]
    .sum()
    .reset_index()
)

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=state_data,
    x="Confirmed",
    y="Deaths",
    s=100
)

plt.title("Confirmed Cases vs Deaths")
plt.xlabel("Confirmed Cases")
plt.ylabel("Deaths")

plt.tight_layout()

plt.savefig("images/cases_vs_deaths.png")
plt.show()

# --------------------------------------------------
# 11. Final message
# --------------------------------------------------

print("=" * 60)
print("All visualizations created successfully!")
print("=" * 60)

print("\nCharts saved inside the 'images' folder:")
print("1. covid_cases_over_time.png")
print("2. covid_deaths_over_time.png")
print("3. top_states_cases.png")
print("4. top_states_deaths.png")
print("5. top_states_recovered.png")
print("6. top_states_active.png")
print("7. recovery_vs_deaths.png")
print("8. cases_vs_deaths.png")