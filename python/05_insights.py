# COVID-19 Data Analysis
# Step 5: Generate Insights

import pandas as pd
import numpy as np

# --------------------------------------------------
# 1. Load data
# --------------------------------------------------

df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\covid 19\data\covid19_cleaned.csv")

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

print("=" * 70)
print("COVID-19 DATA ANALYSIS - KEY INSIGHTS")
print("=" * 70)

# --------------------------------------------------
# 2. Latest date in dataset
# --------------------------------------------------

latest_date = df["Date"].max()

print("\nLatest Date in Dataset:")
print(latest_date)

# --------------------------------------------------
# 3. Get latest record for each state
# --------------------------------------------------

latest_state_data = (
    df.sort_values("Date")
    .groupby("State")
    .tail(1)
    .copy()
)

# --------------------------------------------------
# 4. Calculate rates
# --------------------------------------------------

latest_state_data["Recovery_Rate"] = (
    latest_state_data["Recovered"] /
    latest_state_data["Confirmed"].replace(0, np.nan)
) * 100

latest_state_data["Death_Rate"] = (
    latest_state_data["Deaths"] /
    latest_state_data["Confirmed"].replace(0, np.nan)
) * 100

latest_state_data["Active_Rate"] = (
    latest_state_data["Active"] /
    latest_state_data["Confirmed"].replace(0, np.nan)
) * 100

latest_state_data = latest_state_data.replace(
    [np.inf, -np.inf],
    np.nan
)

latest_state_data = latest_state_data.fillna(0)

# --------------------------------------------------
# 5. State with highest confirmed cases
# --------------------------------------------------

highest_cases = latest_state_data.loc[
    latest_state_data["Confirmed"].idxmax()
]

print("\n1. STATE WITH HIGHEST CONFIRMED CASES")
print("-" * 50)

print(
    f"State      : {highest_cases['State']}"
)

print(
    f"Cases      : {highest_cases['Confirmed']:,}"
)

# --------------------------------------------------
# 6. State with highest deaths
# --------------------------------------------------

highest_deaths = latest_state_data.loc[
    latest_state_data["Deaths"].idxmax()
]

print("\n2. STATE WITH HIGHEST DEATHS")
print("-" * 50)

print(
    f"State      : {highest_deaths['State']}"
)

print(
    f"Deaths     : {highest_deaths['Deaths']:,}"
)

# --------------------------------------------------
# 7. State with highest recoveries
# --------------------------------------------------

highest_recovered = latest_state_data.loc[
    latest_state_data["Recovered"].idxmax()
]

print("\n3. STATE WITH HIGHEST RECOVERIES")
print("-" * 50)

print(
    f"State      : {highest_recovered['State']}"
)

print(
    f"Recovered  : {highest_recovered['Recovered']:,}"
)

# --------------------------------------------------
# 8. Highest recovery rate
# --------------------------------------------------

highest_recovery_rate = latest_state_data.loc[
    latest_state_data["Recovery_Rate"].idxmax()
]

print("\n4. HIGHEST RECOVERY RATE")
print("-" * 50)

print(
    f"State          : {highest_recovery_rate['State']}"
)

print(
    f"Recovery Rate  : "
    f"{highest_recovery_rate['Recovery_Rate']:.2f}%"
)

# --------------------------------------------------
# 9. Highest death rate
# --------------------------------------------------

highest_death_rate = latest_state_data.loc[
    latest_state_data["Death_Rate"].idxmax()
]

print("\n5. HIGHEST DEATH RATE")
print("-" * 50)

print(
    f"State       : {highest_death_rate['State']}"
)

print(
    f"Death Rate  : "
    f"{highest_death_rate['Death_Rate']:.2f}%"
)

# --------------------------------------------------
# 10. Highest active cases
# --------------------------------------------------

highest_active = latest_state_data.loc[
    latest_state_data["Active"].idxmax()
]

print("\n6. HIGHEST ACTIVE CASES")
print("-" * 50)

print(
    f"State       : {highest_active['State']}"
)

print(
    f"Active      : {highest_active['Active']:,}"
)

# --------------------------------------------------
# 11. Overall totals on latest date
# --------------------------------------------------

total_cases = latest_state_data["Confirmed"].sum()
total_recovered = latest_state_data["Recovered"].sum()
total_deaths = latest_state_data["Deaths"].sum()
total_active = latest_state_data["Active"].sum()

print("\n7. OVERALL COVID-19 STATUS")
print("-" * 50)

print(f"Confirmed Cases : {total_cases:,}")
print(f"Recovered       : {total_recovered:,}")
print(f"Deaths          : {total_deaths:,}")
print(f"Active Cases    : {total_active:,}")

# --------------------------------------------------
# 12. Overall recovery rate
# --------------------------------------------------

overall_recovery_rate = (
    total_recovered / total_cases
) * 100

overall_death_rate = (
    total_deaths / total_cases
) * 100

print(
    f"\nOverall Recovery Rate : "
    f"{overall_recovery_rate:.2f}%"
)

print(
    f"Overall Death Rate    : "
    f"{overall_death_rate:.2f}%"
)

# --------------------------------------------------
# 13. Top 5 affected states
# --------------------------------------------------

top_5 = latest_state_data.sort_values(
    "Confirmed",
    ascending=False
).head(5)

print("\n8. TOP 5 MOST AFFECTED STATES")
print("-" * 50)

for index, row in top_5.iterrows():

    print(
        f"{row['State']}: "
        f"{row['Confirmed']:,} cases"
    )

# --------------------------------------------------
# 14. Lowest recovery rate
# --------------------------------------------------

lowest_recovery = latest_state_data.loc[
    latest_state_data["Recovery_Rate"].idxmin()
]

print("\n9. LOWEST RECOVERY RATE")
print("-" * 50)

print(
    f"State         : {lowest_recovery['State']}"
)

print(
    f"Recovery Rate : "
    f"{lowest_recovery['Recovery_Rate']:.2f}%"
)

# --------------------------------------------------
# 15. Lowest death rate
# --------------------------------------------------

lowest_death = latest_state_data.loc[
    latest_state_data["Death_Rate"].idxmin()
]

print("\n10. LOWEST DEATH RATE")
print("-" * 50)

print(
    f"State      : {lowest_death['State']}"
)

print(
    f"Death Rate : "
    f"{lowest_death['Death_Rate']:.2f}%"
)

# --------------------------------------------------
# 16. Save latest state analysis
# --------------------------------------------------

latest_state_data.to_csv(
    "data/latest_state_analysis.csv",
    index=False
)

print("\nLatest state analysis saved!")

# --------------------------------------------------
# 17. Generate text report
# --------------------------------------------------

with open("COVID_19_Insights.txt", "w") as file:

    file.write("COVID-19 DATA ANALYSIS - KEY INSIGHTS\n")
    file.write("=" * 60 + "\n\n")

    file.write(
        f"Latest Date: {latest_date}\n\n"
    )

    file.write(
        f"Total Confirmed Cases: "
        f"{total_cases:,}\n"
    )

    file.write(
        f"Total Recoveries: "
        f"{total_recovered:,}\n"
    )

    file.write(
        f"Total Deaths: "
        f"{total_deaths:,}\n"
    )

    file.write(
        f"Total Active Cases: "
        f"{total_active:,}\n\n"
    )

    file.write(
        f"Overall Recovery Rate: "
        f"{overall_recovery_rate:.2f}%\n"
    )

    file.write(
        f"Overall Death Rate: "
        f"{overall_death_rate:.2f}%\n\n"
    )

    file.write(
        f"Highest Cases: "
        f"{highest_cases['State']} - "
        f"{highest_cases['Confirmed']:,}\n"
    )

    file.write(
        f"Highest Deaths: "
        f"{highest_deaths['State']} - "
        f"{highest_deaths['Deaths']:,}\n"
    )

    file.write(
        f"Highest Recoveries: "
        f"{highest_recovered['State']} - "
        f"{highest_recovered['Recovered']:,}\n"
    )

    file.write(
        f"Highest Recovery Rate: "
        f"{highest_recovery_rate['State']} - "
        f"{highest_recovery_rate['Recovery_Rate']:.2f}%\n"
    )

    file.write(
        f"Highest Death Rate: "
        f"{highest_death_rate['State']} - "
        f"{highest_death_rate['Death_Rate']:.2f}%\n"
    )

print("\nInsight report created:")
print("COVID_19_Insights.txt")

print("\n" + "=" * 70)
print("INSIGHT GENERATION COMPLETED!")
print("=" * 70)