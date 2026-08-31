# COVID-19 Data Analysis
# Step 2: Exploratory Data Analysis (EDA)
import pandas as pd

file_path = r"C:\Users\likit\OneDrive\Documents\covid 19\data\covid19_cleaned.csv"

df = pd.read_csv(file_path)

print("Column names in your dataset:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("COVID-19 Data Analysis")
print("=" * 60)

# --------------------------------------------------
# 2. Basic information
# --------------------------------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

# --------------------------------------------------
# 3. Statistical summary
# --------------------------------------------------

print("\nStatistical Summary:")
print(df.describe())

# --------------------------------------------------
# 4. Total COVID-19 cases
# --------------------------------------------------

total_confirmed = df["Confirmed"].sum()

print("\nTotal Confirmed Cases:")
print(total_confirmed)

# --------------------------------------------------
# 5. Total recovered cases
# --------------------------------------------------

total_recovered = df["Recovered"].sum()

print("\nTotal Recovered Cases:")
print(total_recovered)

# --------------------------------------------------
# 6. Total deaths
# --------------------------------------------------

total_deaths = df["Deaths"].sum()

print("\nTotal Deaths:")
print(total_deaths)

# --------------------------------------------------
# 7. Total active cases
# --------------------------------------------------

total_active = df["Active"].sum()

print("\nTotal Active Cases:")
print(total_active)

# --------------------------------------------------
# 8. Recovery rate
# --------------------------------------------------

if total_confirmed > 0:
    recovery_rate = (total_recovered / total_confirmed) * 100
else:
    recovery_rate = 0

print("\nRecovery Rate:")
print(round(recovery_rate, 2), "%")

# --------------------------------------------------
# 9. Death rate
# --------------------------------------------------

if total_confirmed > 0:
    death_rate = (total_deaths / total_confirmed) * 100
else:
    death_rate = 0

print("\nDeath Rate:")
print(round(death_rate, 2), "%")

# --------------------------------------------------
# 10. State-wise confirmed cases
# --------------------------------------------------

state_cases = df.groupby("State")["Confirmed"].sum()

print("\nState-wise Confirmed Cases:")
print(state_cases.sort_values(ascending=False))

# --------------------------------------------------
# 11. Top 10 states by confirmed cases
# --------------------------------------------------

top_cases = state_cases.sort_values(ascending=False).head(10)

print("\nTop 10 States by Confirmed Cases:")
print(top_cases)

# --------------------------------------------------
# 12. State-wise deaths
# --------------------------------------------------

state_deaths = df.groupby("State")["Deaths"].sum()

print("\nState-wise Deaths:")
print(state_deaths.sort_values(ascending=False))

# --------------------------------------------------
# 13. Top 10 states by deaths
# --------------------------------------------------

top_deaths = state_deaths.sort_values(ascending=False).head(10)

print("\nTop 10 States by Deaths:")
print(top_deaths)

# --------------------------------------------------
# 14. State-wise recoveries
# --------------------------------------------------

state_recovered = df.groupby("State")["Recovered"].sum()

print("\nState-wise Recoveries:")
print(state_recovered.sort_values(ascending=False))

# --------------------------------------------------
# 15. Top 10 states by recovery
# --------------------------------------------------

top_recovered = state_recovered.sort_values(ascending=False).head(10)

print("\nTop 10 States by Recoveries:")
print(top_recovered)

# --------------------------------------------------
# 16. State-wise active cases
# --------------------------------------------------

state_active = df.groupby("State")["Active"].sum()

print("\nState-wise Active Cases:")
print(state_active.sort_values(ascending=False))

# --------------------------------------------------
# 17. Find state with highest confirmed cases
# --------------------------------------------------

highest_case_state = state_cases.idxmax()
highest_case_value = state_cases.max()

print("\nState with Highest Confirmed Cases:")
print(highest_case_state, "-", highest_case_value)

# --------------------------------------------------
# 18. Find state with highest deaths
# --------------------------------------------------

highest_death_state = state_deaths.idxmax()
highest_death_value = state_deaths.max()

print("\nState with Highest Deaths:")
print(highest_death_state, "-", highest_death_value)

# --------------------------------------------------
# 19. Find state with highest recoveries
# --------------------------------------------------

highest_recovery_state = state_recovered.idxmax()
highest_recovery_value = state_recovered.max()

print("\nState with Highest Recoveries:")
print(highest_recovery_state, "-", highest_recovery_value)

# --------------------------------------------------
# 20. Final message
# --------------------------------------------------

print("\n" + "=" * 60)
print("EDA completed successfully!")
print("=" * 60)