# Chapter 2 - Datasets

This folder contains all datasets used in Chapter 2 problems and solutions.

---

## 📁 Available Datasets

| File | Description | Used In | Rows |
|------|-------------|---------|------|
| `rajesh_weekly_sales.csv` | One week of tea stall data | Problem 2.1 | 7 |
| `study_scores.csv` | Study hours vs test scores | Problem 2.2 | 7 |
| `rajesh_two_weeks.csv` | Two weeks combined data | Problem 2.3 | 14 |
| `kamala_pricing.csv` | Vegetable pricing by time | Problem 2.4 | 5 |
| `rajesh_week3_validation.csv` | Week 3 validation data | Problem 2.5 | 7 |
| `rajesh_complete_data.csv` | Full dataset with all variables | Problem 2.6 | 20 |

---

## 📊 Dataset Descriptions

### rajesh_weekly_sales.csv

**Description:** Rajesh's tea stall sales for one week

**Columns:**
- `Day` (string): Day of week (Mon, Tue, Wed, ...)
- `Temperature` (float): Daily temperature in °C
- `Sales` (int): Daily sales in rupees (₹)

**Sample Data:**
```csv
Day,Temperature,Sales
Mon,35,450
Tue,33,520
Wed,30,580
```

**Use Case:** Basic pattern recognition and simple linear modeling

---

### study_scores.csv

**Description:** Student study hours and corresponding test scores

**Columns:**
- `StudyHours` (int): Hours studied before test
- `TestScore` (int): Score achieved (out of 100)

**Sample Data:**
```csv
StudyHours,TestScore
2,65
3,70
4,75
```

**Use Case:** Building first linear model, understanding slope and intercept

---

### rajesh_two_weeks.csv

**Description:** Extended dataset combining Week 1 and Week 2

**Columns:**
- `Day` (string): Day identifier (W1-Mon, W1-Tue, ..., W2-Mon, ...)
- `Temperature` (float): Daily temperature in °C
- `Sales` (int): Daily sales in rupees (₹)

**Sample Data:**
```csv
Day,Temperature,Sales
W1-Mon,35,450
W1-Tue,33,520
...
W2-Mon,37,440
```

**Use Case:** Least squares calculation with more data points

---

### kamala_pricing.csv

**Description:** Kamala's vegetable pricing strategy throughout the day

**Columns:**
- `Time` (string): Time of day (7 AM, 10 AM, ...)
- `Price` (int): Price per kg in rupees (₹/kg)
- `DemandFactor` (float): Customer demand multiplier
- `QualityFactor` (float): Freshness/quality factor

**Sample Data:**
```csv
Time,Price,DemandFactor,QualityFactor
7 AM,40,1.2,1.0
10 AM,38,1.0,0.95
1 PM,35,1.0,0.9
```

**Use Case:** Multi-factor modeling, business optimization

---

### rajesh_week3_validation.csv

**Description:** Week 3 data for model validation and error analysis

**Columns:**
- `Day` (string): Day of week
- `Temperature` (float): Daily temperature in °C
- `ActualSales` (int): Actual sales in rupees (₹)
- `Weather` (string): Weather condition (Sunny, Cloudy, Light Rain, Heavy Rain)

**Sample Data:**
```csv
Day,Temperature,ActualSales,Weather
Mon,34,510,Sunny
Tue,32,580,Cloudy
Wed,29,650,Light Rain
```

**Use Case:** Model validation, residual analysis, weather effect discovery

---

### rajesh_complete_data.csv

**Description:** Complete dataset with all variables for multi-factor modeling

**Columns:**
- `Day` (int): Day number (1-20)
- `Temperature` (float): Daily temperature in °C
- `DayOfWeek` (int): Day of week (1=Monday, 7=Sunday)
- `Weather` (int): Weather code (0=Sunny, 1=Cloudy, 2=Rainy)
- `Sales` (int): Daily sales in rupees (₹)

**Sample Data:**
```csv
Day,Temperature,DayOfWeek,Weather,Sales
1,35,1,0,450
2,33,2,0,520
3,30,3,1,580
```

**Use Case:** Model comparison, multi-variable regression, feature importance

---

## 🔍 Data Characteristics

### Temperature Range
- **Minimum:** 25°C (cool day)
- **Maximum:** 38°C (hot day)
- **Mean:** ~31°C
- **Range:** Typical Odisha summer temperatures

### Sales Range
- **Minimum:** ₹420 (very hot Friday)
- **Maximum:** ₹800 (cool rainy Sunday)
- **Mean:** ~₹594
- **Pattern:** Negative correlation with temperature

### Weather Distribution
- **Sunny days:** ~50% (Weather = 0)
- **Cloudy days:** ~30% (Weather = 1)
- **Rainy days:** ~20% (Weather = 2)

### Day of Week Pattern
- **Weekdays (Mon-Fri):** Variable, work-driven
- **Saturday:** Higher (market day)
- **Sunday:** Highest (leisure time)

---

## 💾 Loading Data in Python

### Using Pandas (Recommended)

```python
import pandas as pd

# Load data
df = pd.read_csv('data/rajesh_weekly_sales.csv')

# View first few rows
print(df.head())

# Access columns
temperature = df['Temperature']
sales = df['Sales']

# Basic statistics
print(df.describe())
```

### Using NumPy

```python
import numpy as np

# Load data (skip header)
data = np.loadtxt('data/rajesh_weekly_sales.csv', 
                  delimiter=',', 
                  skiprows=1,
                  usecols=(1,2))  # Temperature and Sales columns

temperature = data[:, 0]
sales = data[:, 1]
```

### Using Base Python

```python
import csv

# Load data
with open('data/rajesh_weekly_sales.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Access data
for row in data:
    temp = float(row['Temperature'])
    sales = int(row['Sales'])
    print(f"{temp}°C → ₹{sales}")
```

---

## 📈 Data Visualization Examples

### Quick Scatter Plot

```python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/rajesh_weekly_sales.csv')

plt.scatter(df['Temperature'], df['Sales'])
plt.xlabel('Temperature (°C)')
plt.ylabel('Sales (₹)')
plt.title('Temperature vs Sales')
plt.show()
```

### Multiple Subplots

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Temperature vs Sales
axes[0].scatter(df['Temperature'], df['Sales'])
axes[0].set_title('Temperature Effect')

# Day vs Sales (if available)
axes[1].bar(range(len(df)), df['Sales'])
axes[1].set_title('Daily Sales')

plt.tight_layout()
plt.show()
```

---

## 🔧 Data Preprocessing Tips

### Handle Missing Values

```python
# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values
df_clean = df.dropna()

# Or fill with mean
df['Sales'].fillna(df['Sales'].mean(), inplace=True)
```

### Normalize Temperature

```python
# Standardize (mean=0, std=1)
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df['Temperature_normalized'] = scaler.fit_transform(df[['Temperature']])
```

### Create Derived Features

```python
# Add temperature categories
df['TempCategory'] = pd.cut(df['Temperature'], 
                             bins=[0, 28, 33, 40],
                             labels=['Cool', 'Moderate', 'Hot'])

# Add sales categories
df['SalesCategory'] = pd.cut(df['Sales'],
                              bins=[0, 500, 650, 1000],
                              labels=['Low', 'Medium', 'High'])
```

---

## 🧪 Data Validation

### Check Data Integrity

```python
# Temperature should be realistic
assert df['Temperature'].min() >= 20, "Temperature too low!"
assert df['Temperature'].max() <= 45, "Temperature too high!"

# Sales should be positive
assert (df['Sales'] > 0).all(), "Sales must be positive!"

# No duplicates
assert df.duplicated().sum() == 0, "Duplicate rows found!"
```

### Statistical Checks

```python
# Check correlation
corr = df['Temperature'].corr(df['Sales'])
print(f"Correlation: {corr:.3f}")
assert corr < 0, "Expected negative correlation!"

# Check variance
print(f"Temperature variance: {df['Temperature'].var():.2f}")
print(f"Sales variance: {df['Sales'].var():.2f}")
```

---

## 📚 Creating Your Own Dataset

### Template CSV Structure

```csv
Temperature,Sales
[your_temp_1],[your_sales_1]
[your_temp_2],[your_sales_2]
...
```

### Example: Create Custom Data

```python
import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
temperature = np.random.uniform(25, 38, 20)
sales = 1550 - 30*temperature + np.random.normal(0, 20, 20)

# Create DataFrame
df = pd.DataFrame({
    'Temperature': temperature,
    'Sales': sales.astype(int)
})

# Save to CSV
df.to_csv('data/my_custom_data.csv', index=False)
```

---

## 🔗 Related Resources

**Data Sources:**
- Original observations from Bhubaneswar tea stalls
- Simulated based on real weather patterns
- Educational dataset for learning purposes

**Similar Datasets:**
- UCI Machine Learning Repository
- Kaggle Datasets
- Real-world business data (anonymized)

**Tools for Data Analysis:**
- Pandas: Data manipulation
- NumPy: Numerical computing
- Matplotlib: Visualization
- Scikit-learn: Machine learning

---

## ⚠️ Data Usage Notes

### Academic Use
✅ Free to use for learning and education  
✅ Cite as: "Pattern Hunters Chapter 2 Dataset"  
✅ Modify for your own exercises

### Limitations
- Simplified for educational purposes
- Real business data has more complexity
- Some values rounded for clarity
- Weather categories simplified

### Real-World Application
When using similar data in real projects:
- Collect more data points (50+ recommended)
- Include more variables (customer demographics, etc.)
- Account for seasonal changes
- Validate with actual business outcomes

---

## 🤝 Contributing Data

Have real tea stall or business data to share?
1. Anonymize sensitive information
2. Format as CSV following our structure
3. Submit via pull request
4. Help others learn from real data!

---

**Questions about the data?** Open an issue or ask in [Discussions](../../discussions)

**Back to:** [Chapter 2 Home](../../README.md) | [Repository Home](../../../../README.md)
