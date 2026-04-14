import pandas as pd

# Load the raw astronomical dataset
df = pd.read_csv("data/raw/exoplanets.csv")

print("First 5 rows:")
print(df.head())
print()

print("Column names:")
print(df.columns.tolist())
print()

print("Dataset shape (rows, columns):")
print(df.shape)
print()

print("Missing values in each column:")
print(df.isnull().sum())
print()

print("Invalid value checks:")
print("Orbital period <= 0:", (df["pl_orbper"] <= 0).sum())
print("Radius <= 0:", (df["pl_rade"] <= 0).sum())
print("Mass <= 0:", (df["pl_bmasse"] <= 0).sum())
print("Stellar temperature <= 0:", (df["st_teff"] <= 0).sum())
print("Distance < 0:", (df["sy_dist"] < 0).sum())
print()

# Clean the dataset by removing rows missing key analysis variables
clean_df = df.dropna(subset=["pl_name", "pl_orbper", "pl_rade", "pl_bmasse"])

print("Cleaned dataset shape (rows, columns):")
print(clean_df.shape)
print()

print("Rows removed during cleaning:")
print(len(df) - len(clean_df))
print()

# Save cleaned dataset
clean_df.to_csv("data/processed/exoplanets_cleaned.csv", index=False)

print("Cleaned dataset saved to data/processed/exoplanets_cleaned.csv")
import matplotlib.pyplot as plt

# Load cleaned dataset
clean_df = pd.read_csv("data/processed/exoplanets_cleaned.csv")

# Remove any remaining missing values for plotting
plot_df = clean_df[["pl_orbper", "pl_bmasse"]].dropna()

# Create scatter plot
plt.figure()
plt.scatter(plot_df["pl_orbper"], plot_df["pl_bmasse"])

# Log scale (important for astronomical data)
plt.xscale("log")
plt.yscale("log")

# Labels
plt.xlabel("Orbital Period (days)")
plt.ylabel("Planet Mass (Earth masses)")
plt.title("Planet Mass vs Orbital Period")

# Save plot
plt.savefig("outputs/plots/mass_vs_orbital_period.png")

print("Plot saved to outputs/plots/mass_vs_orbital_period.png")
