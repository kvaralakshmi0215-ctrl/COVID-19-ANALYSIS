# COVID-19 Data Analysis
# Step 4: Statistical Analysis

import pandas as pd
import numpy as np

# --------------------------------------------------
# 1. Load cleaned dataset
# --------------------------------------------------

df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\covid 19\data\covid19_cleaned.csv")

print("=" * 70)
print("COVID-19 STATISTICAL ANALYSIS")
print("=" * 70)

# --------------------------------------------------
# 2. Convert Date column
# --------------------------------------------------

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# --------------------------------------------------
# 3. Calculate total cases, recoveries, deaths
# --------------------------------------------------

total_cases = df["Confirmed"].sum()
total_recovered = df["Recovered"].sum()
total_deaths = df["Deaths"].sum()
total_active = df["Active"].sum()

print("\nOVERALL STATISTICS")
print("-" * 50)

print(f"Total Confirmed Cases : {total_cases:,}")
print(f"Total Recovered       : {total_recovered:,}")
print(f"Total Deaths          : {total_deaths:,}")
print(f"Total Active Cases    : {total_active:,}")

# --------------------------------------------------
# 4. Recovery Rate
# --------------------------------------------------

if total_cases > 0:
    recovery_rate = (total_recovered / total_cases) * 100
else:
    recovery_rate = 0

print(f"\nRecovery Rate         : {recovery_rate:.2f}%")

# --------------------------------------------------
# 5. Death Rate
# --------------------------------------------------

if total_cases > 0:
    death_rate = (total_deaths / total_cases) * 100
else:
    death_rate = 0

print(f"Death Rate            : {death_rate:.2f}%")

# --------------------------------------------------
# 6. Active Case Rate
# --------------------------------------------------

if total_cases > 0:
    active_rate = (total_active / total_cases) * 100
else:
    active_rate = 0

print(f"Active Case Rate      : {active_rate:.2f}%")

# --------------------------------------------------
# 7. State-wise statistics
# --------------------------------------------------

state_analysis = df.groupby("State").agg({
    "Confirmed": "sum",
    "Recovered": "sum",
    "Deaths": "sum",
    "Active": "sum"
}).reset_index()

# --------------------------------------------------
# 8. Calculate recovery rate by state
# --------------------------------------------------

state_analysis["Recovery_Rate"] = (
    state_analysis["Recovered"] /
    state_analysis["Confirmed"].replace(0, np.nan)
) * 100

# --------------------------------------------------
# 9. Calculate death rate by state
# --------------------------------------------------

state_analysis["Death_Rate"] = (
    state_analysis["Deaths"] /
    state_analysis["Confirmed"].replace(0, np.nan)
) * 100

# Replace infinite/missing values
state_analysis = state_analysis.replace(
    [np.inf, -np.inf],
    np.nan
)

state_analysis = state_analysis.fillna(0)

# --------------------------------------------------
# 10. Display state statistics
# --------------------------------------------------

print("\nSTATE-WISE ANALYSIS")
print("-" * 50)

print(state_analysis.to_string(index=False))

# --------------------------------------------------
# 11. Top 10 states by cases
# --------------------------------------------------

top_cases = state_analysis.sort_values(
    "Confirmed",
    ascending=False
).head(10)

print("\nTOP 10 STATES BY CONFIRMED CASES")
print("-" * 50)

print(
    top_cases[
        ["State", "Confirmed"]
    ].to_string(index=False)
)

# --------------------------------------------------
# 12. Top 10 states by deaths
# --------------------------------------------------

top_deaths = state_analysis.sort_values(
    "Deaths",
    ascending=False
).head(10)

print("\nTOP 10 STATES BY DEATHS")
print("-" * 50)

print(
    top_deaths[
        ["State", "Deaths"]
    ].to_string(index=False)
)

# --------------------------------------------------
# 13. Top 10 states by recovery rate
# --------------------------------------------------

top_recovery_rate = state_analysis.sort_values(
    "Recovery_Rate",
    ascending=False
).head(10)

print("\nTOP 10 STATES BY RECOVERY RATE")
print("-" * 50)

print(
    top_recovery_rate[
        ["State", "Recovery_Rate"]
    ].to_string(index=False)
)

# --------------------------------------------------
# 14. Top 10 states by death rate
# --------------------------------------------------

top_death_rate = state_analysis.sort_values(
    "Death_Rate",
    ascending=False
).head(10)

print("\nTOP 10 STATES BY DEATH RATE")
print("-" * 50)

print(
    top_death_rate[
        ["State", "Death_Rate"]
    ].to_string(index=False)
)

# --------------------------------------------------
# 15. Mean and median
# --------------------------------------------------

print("\nSTATISTICAL MEASURES")
print("-" * 50)

print(
    f"Mean Confirmed Cases per Record : "
    f"{df['Confirmed'].mean():,.2f}"
)

print(
    f"Median Confirmed Cases          : "
    f"{df['Confirmed'].median():,.2f}"
)

print(
    f"Mean Deaths per Record          : "
    f"{df['Deaths'].mean():,.2f}"
)

print(
    f"Median Deaths                   : "
    f"{df['Deaths'].median():,.2f}"
)

# --------------------------------------------------
# 16. Standard deviation
# --------------------------------------------------

print(
    f"Standard Deviation of Cases     : "
    f"{df['Confirmed'].std():,.2f}"
)

print(
    f"Standard Deviation of Deaths    : "
    f"{df['Deaths'].std():,.2f}"
)

# --------------------------------------------------
# 17. Correlation analysis
# --------------------------------------------------

correlation = df[
    ["Confirmed", "Recovered", "Deaths", "Active"]
].corr()

print("\nCORRELATION MATRIX")
print("-" * 50)

print(correlation)

# --------------------------------------------------
# 18. Strongest correlation with confirmed cases
# --------------------------------------------------

confirmed_correlations = correlation["Confirmed"].drop(
    "Confirmed"
)

strongest_relationship = confirmed_correlations.abs().idxmax()

print(
    "\nStrongest relationship with confirmed cases:"
)

print(
    strongest_relationship,
    "Correlation =",
    round(
        confirmed_correlations[strongest_relationship],
        3
    )
)

# --------------------------------------------------
# 19. Save state analysis
# --------------------------------------------------

state_analysis.to_csv(
    "data/state_wise_covid_analysis.csv",
    index=False
)

print("\nState-wise analysis saved successfully!")

# --------------------------------------------------
# 20. Final message
# --------------------------------------------------

print("\n" + "=" * 70)
print("STATISTICAL ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 70)