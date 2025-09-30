"""
Chapter 1: Pattern Visualization
Visualizes patterns from tea stall customer data

Problem: Challenge C1
Author: Dr. Alok Patel
Repository: github.com/The-Pattern-Hunter/pattern-hunters-problems
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data from Problem 1.1
data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Week1': [42, 65, 70, 68, 87, 50, 35],
    'Week2': [48, 70, 75, 72, 91, 55, 40]
}

df = pd.DataFrame(data)

# Calculate averages
df['Average'] = (df['Week1'] + df['Week2']) / 2

# Create figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Weekly comparison
axes[0, 0].bar(df['Day'], df['Week1'], alpha=0.7, label='Week 1', color='skyblue')
axes[0, 0].bar(df['Day'], df['Week2'], alpha=0.7, label='Week 2', color='orange')
axes[0, 0].set_xlabel('Day of Week')
axes[0, 0].set_ylabel('Customers')
axes[0, 0].set_title('Tea Stall Customers by Day')
axes[0, 0].legend()
axes[0, 0].grid(axis='y', alpha=0.3)

# Plot 2: Average with trend line
x = np.arange(len(df))
y = df['Average']
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

axes[0, 1].plot(df['Day'], df['Average'], 'o-', linewidth=2, 
                markersize=8, color='green', label='Average')
axes[0, 1].plot(df['Day'], p(x), '--', color='red', 
                linewidth=2, label=f'Trend: y={z[0]:.1f}x+{z[1]:.1f}')
axes[0, 1].set_xlabel('Day of Week')
axes[0, 1].set_ylabel('Average Customers')
axes[0, 1].set_title('Weekly Average with Trend')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# Plot 3: Weekday vs Weekend comparison
weekday_avg = df.loc[df['Day'].isin(['Mon', 'Tue', 'Wed', 'Thu', 'Fri']), 'Average'].mean()
weekend_avg = df.loc[df['Day'].isin(['Sat', 'Sun']), 'Average'].mean()

categories = ['Weekdays', 'Weekend']
values = [weekday_avg, weekend_avg]
colors = ['steelblue', 'coral']

axes[1, 0].bar(categories, values, color=colors, alpha=0.8)
axes[1, 0].set_ylabel('Average Customers')
axes[1, 0].set_title('Weekday vs Weekend Comparison')
axes[1, 0].set_ylim([0, max(values) * 1.2])
for i, v in enumerate(values):
    axes[1, 0].text(i, v + 2, f'{v:.1f}', ha='center', fontweight='bold')
axes[1, 0].grid(axis='y', alpha=0.3)

# Plot 4: Percentage change from Monday
monday_avg = df.loc[df['Day'] == 'Mon', 'Average'].values[0]
df['Percent_Change'] = ((df['Average'] - monday_avg) / monday_avg) * 100

axes[1, 1].bar(df['Day'], df['Percent_Change'], 
               color=['red' if x < 0 else 'green' for x in df['Percent_Change']],
               alpha=0.7)
axes[1, 1].axhline(y=0, color='black', linestyle='-', linewidth=0.5)
axes[1, 1].set_xlabel('Day of Week')
axes[1, 1].set_ylabel('% Change from Monday')
axes[1, 1].set_title('Percentage Change from Monday Baseline')
axes[1, 1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('tea_stall_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Print summary statistics
print("="*50)
print("TEA STALL PATTERN ANALYSIS")
print("="*50)
print(f"\nWeekday Average: {weekday_avg:.1f} customers")
print(f"Weekend Average: {weekend_avg:.1f} customers")
print(f"Difference: {weekday_avg - weekend_avg:.1f} customers ({((weekday_avg/weekend_avg - 1)*100):.1f}% increase)")
print(f"\nFriday Peak: {df.loc[df['Day']=='Fri', 'Average'].values[0]:.1f} customers")
print(f"Sunday Low: {df.loc[df['Day']=='Sun', 'Average'].values[0]:.1f} customers")
print(f"Weekly Range: {df['Average'].max() - df['Average'].min():.1f} customers")
print("\n" + "="*50)

# BONUS: Load from CSV file if available
print("\n" + "="*50)
print("BONUS: Loading from CSV file...")
print("="*50)
try:
    df_csv = pd.read_csv('../datasets/tea-stall-customers.csv')
    print("\n✓ Successfully loaded data from CSV!")
    print("\nData preview:")
    print(df_csv.head())
    print(f"\nDataset shape: {df_csv.shape[0]} rows, {df_csv.shape[1]} columns")
except FileNotFoundError:
    print("\n✗ CSV file not found. Make sure 'tea-stall-customers.csv' is in the datasets folder.")
    print("  Run this script from the 'code/python/' directory.")