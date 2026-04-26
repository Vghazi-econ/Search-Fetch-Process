import wbgapi as wb
import matplotlib.pyplot as plt

# 1. Search for GDP )
print("--- Results for GDP ---")
wb.series.info(q="gdp")

# 2. Search for CPI
print("\n--- Results for cpi ---")
wb.series.info(q="consumer price")
# 3. Search for EXPORT
print("\n--- Results for exp ---")
wb.series.info(q="export")

indicators = ["NY.GDP.MKTP.KD.ZG", "FP.CPI.TOTL.ZG", "NE.EXP.GNFS.ZS"]
countries = ["SAU", "EGY"]

df = wb.data.DataFrame(indicators, countries, mrv=5)

df.columns = [col.replace("YR", "") for col in df.columns]
df_final = df.T

print(df_final)

# 1. Plot the data
# kind='line' is best for showing trends over time
ax = df_final.plot(kind="line", marker="o", figsize=(10, 6))

# 2. Add titles and labels
plt.title(" Indicators Comparison: SAU vs EGY", fontsize=14, fontweight="light")
plt.ylabel("Percentage Change (%)", fontsize=12)
plt.xlabel("Year", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)

# 3. Clean up the legend
plt.legend(title="Country & Indicator", bbox_to_anchor=(1.05, 1), loc="upper left")

# 4. Display the chart
plt.tight_layout()
plt.show()
