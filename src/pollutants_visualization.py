import os
import pandas as pd
import matplotlib.pyplot as plt
from paths import POLLUTANTS_GRAPHS_DIR

# Create subdirectories for organization
YEARLY_PLOTS_DIR = os.path.join(POLLUTANTS_GRAPHS_DIR, "yearly_plots")
MONTHLY_PLOTS_DIR = os.path.join(POLLUTANTS_GRAPHS_DIR, "monthly_plots")
TREND_PLOTS_DIR = os.path.join(POLLUTANTS_GRAPHS_DIR, "trend_analysis")

for directory in [YEARLY_PLOTS_DIR, MONTHLY_PLOTS_DIR, TREND_PLOTS_DIR]:
    os.makedirs(directory, exist_ok=True)

# Load dataset
data_path = os.path.join(os.path.dirname(__file__), "..", "data", "raw", "Pollutants_Parameters.xlsx")
df = pd.read_excel(data_path)

# Ensure proper month ordering
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
df["Month"] = pd.Categorical(df["Month"], categories=month_order, ordered=True)
df = df.sort_values(["Year", "Month"])

# Year descriptions for annotations
year_descriptions = {
    2021: "2021 shows a clear seasonal cycle with winter pollution peaks.\n"
          "PM2.5 strongly influences AQI throughout the year.\n"
          "Lowest pollution occurs during monsoon months.\n"
          "Winter stagnation dominates air quality.",

    2022: "2022 exhibits sharper winter peaks than 2021.\n"
          "PM10 variability increases, indicating dust influence.\n"
          "Post-monsoon rise begins earlier.\n"
          "Pollution recovery is slower.",

    2023: "2023 records extreme winter AQI values.\n"
          "PM2.5 rises faster than PM10.\n"
          "Combustion sources dominate pollution.\n"
          "Overall variability increases significantly.",

    2024: "2024 shows prolonged winter pollution episodes.\n"
          "AQI remains high even after PM decline.\n"
          "Pollution persistence is evident.\n"
          "Seasonal dispersion weakens.",

    2025: "2025 maintains elevated baseline pollution.\n"
          "AQI closely mirrors PM2.5 trends.\n"
          "Clean months show reduced recovery.\n"
          "Structural air quality issues emerge."
}

# ==============================
# PART A: MONTHLY PLOTS (YEAR-WISE)
# ==============================

print("Generating monthly plots...")

for year in sorted(df["Year"].unique()):
    data_year = df[df["Year"] == year]

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data_year["Month"], data_year["AQI (IN)"], marker='o', label="AQI", linewidth=2)
    ax.plot(data_year["Month"], data_year["PM2.5"], marker='s', label="PM2.5", linewidth=2)
    ax.plot(data_year["Month"], data_year["PM10"], marker='^', label="PM10", linewidth=2)

    ax.set_xlabel("Month", fontsize=11)
    ax.set_ylabel("Concentration / AQI", fontsize=11)
    ax.set_title(f"Monthly Air Quality Trend – {year}", fontsize=13, fontweight='bold')
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)

    # Add description inside plot
    ax.text(
        0.01, 0.02,
        year_descriptions.get(year, ""),
        transform=ax.transAxes,
        fontsize=9,
        verticalalignment="bottom",
        bbox=dict(boxstyle="round", alpha=0.8, facecolor='wheat')
    )

    plt.tight_layout()
    
    # Save figure
    output_path = os.path.join(MONTHLY_PLOTS_DIR, f"monthly_trend_{year}.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {output_path}")
    plt.close()

# ==============================
# PART B: YEARLY AVERAGE TREND
# ==============================

print("\nGenerating yearly trend analysis...")

yearly_avg = df.groupby("Year")[["AQI (IN)", "PM2.5", "PM10"]].mean()

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(yearly_avg.index, yearly_avg["AQI (IN)"], marker='o', label="AQI", linewidth=2.5, markersize=8)
ax.plot(yearly_avg.index, yearly_avg["PM2.5"], marker='s', label="PM2.5", linewidth=2.5, markersize=8)
ax.plot(yearly_avg.index, yearly_avg["PM10"], marker='^', label="PM10", linewidth=2.5, markersize=8)

ax.set_xlabel("Year", fontsize=11)
ax.set_ylabel("Average Concentration / AQI", fontsize=11)
ax.set_title("Year-wise Average Air Quality Trend", fontsize=13, fontweight='bold')
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3)

# Add description
ax.text(
    0.01, 0.02,
    "Yearly averages indicate rising pollution severity over time.\n"
    "PM2.5 shows the strongest upward trend.\n"
    "AQI closely follows particulate matter levels.\n"
    "Peaks increase more than baseline values.",
    transform=ax.transAxes,
    fontsize=9,
    verticalalignment="bottom",
    bbox=dict(boxstyle="round", alpha=0.8, facecolor='wheat')
)

plt.tight_layout()

# Save figure
output_path = os.path.join(TREND_PLOTS_DIR, "yearly_average_trend.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"✓ Saved: {output_path}")
plt.close()

# ==============================
# PART C: MONTHLY COMPARISON (ALL YEARS)
# ==============================

print("\nGenerating monthly comparison across years...")

fig, ax = plt.subplots(figsize=(14, 7))

for year in sorted(df["Year"].unique()):
    data_year = df[df["Year"] == year]
    ax.plot(data_year["Month"], data_year["AQI (IN)"], marker='o', label=f"{year}", linewidth=2)

ax.set_xlabel("Month", fontsize=11)
ax.set_ylabel("AQI", fontsize=11)
ax.set_title("AQI Comparison Across All Years (Monthly)", fontsize=13, fontweight='bold')
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3)

plt.tight_layout()

output_path = os.path.join(TREND_PLOTS_DIR, "aqi_monthly_comparison.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"✓ Saved: {output_path}")
plt.close()

print("\n✓ All plots generated successfully!")
print(f"\nPlots saved to: {POLLUTANTS_GRAPHS_DIR}")
