# Chapter 2 - Python Code Examples

This folder contains Python implementations for Chapter 2: From Guesswork to Models.

---

## 📁 Files

| File | Description | Related Problem |
|------|-------------|-----------------|
| `model_visualizer.py` | Interactive least squares visualization | Challenge C1 |
| `least_squares_demo.py` | Step-by-step least squares calculation | Problems 2.3, 2.5 |
| `model_comparison.py` | Compare multiple models | Challenge C2 |
| `requirements.txt` | Required Python packages | All files |

---

## 🚀 Quick Start

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

Or install packages individually:
```bash
pip install numpy pandas matplotlib scipy scikit-learn
```

### 2. Run the Scripts

**Interactive Model Visualizer:**
```bash
python model_visualizer.py
```
- Loads Rajesh's tea stall data
- Calculates least squares fit
- Creates 4-panel visualization
- Interactive prediction tool

**Least Squares Demo:**
```bash
python least_squares_demo.py
```
- Shows manual calculation steps
- Demonstrates the math behind least squares
- Educational step-by-step output

**Model Comparison:**
```bash
python model_comparison.py
```
- Compares Temperature, Day, Weather, and Combined models
- Shows which factors matter most
- Generates comparison charts

---

## 📊 What Each Script Does

### model_visualizer.py

**Purpose:** Visualize Rajesh's tea stall model with least squares

**Outputs:**
- `tea_stall_analysis.png` - 4-panel visualization showing:
  - Scatter plot with regression line
  - Residual plot (error analysis)
  - Actual vs. Predicted comparison
  - Model statistics summary

**Features:**
- Manual least squares calculation
- R² and MAE metrics
- Interactive temperature predictor
- Bounded predictions (₹300-900)

**Example output:**
```
Loading data...
✓ Loaded 7 days of data
✓ Model: Sales = 1546 - 30.5 × Temperature
✓ R² = 0.933, MAE = ₹16

Enter temperature (°C): 30
📊 Prediction: ₹631 (Cool day - expect high sales!)
```

---

### least_squares_demo.py

**Purpose:** Educational demonstration of least squares method

**Outputs:**
- Console output showing each calculation step
- Table of deviations and products
- Final model equation

**Example output:**
```
LEAST SQUARES CALCULATION DEMO
================================

Step 1: Calculate means
Mean Temperature: 31.36°C
Mean Sales: ₹594.29

Step 2: Calculate deviations
Day 1: (35 - 31.36) × (450 - 594.29) = -525.22
[... shows all calculations ...]

Step 3: Calculate slope
Slope = -7000.41 / 229.22 = -30.54

Final Model: Sales = 1552 - 30.5 × Temperature
```

---

### model_comparison.py

**Purpose:** Compare single-factor vs. multi-factor models

**Outputs:**
- `model_comparison.png` - 4-panel comparison chart
- Console report with recommendations

**Models compared:**
1. Temperature only (R² ≈ 0.85)
2. Day of week only (R² ≈ 0.58)
3. Weather only (R² ≈ 0.75)
4. Combined model (R² ≈ 0.92)

**Example output:**
```
MODEL COMPARISON REPORT
========================

Best Model: Combined (Temperature + Day + Weather)
R² = 0.923
MAE = ₹18

Recommendation: Use combined model for 92% accuracy
Temperature is strongest single factor (R² = 0.85)
```

---

## 💡 Learning Exercises

### Exercise 1: Modify Parameters
Edit `model_visualizer.py` to:
- Change the minimum sales bound (currently ₹300)
- Add a weather multiplier
- Test different confidence intervals

### Exercise 2: Add Your Own Data
Create your own CSV file:
```csv
Temperature,Sales
32,560
28,690
...
```
Run on your data!

### Exercise 3: Extend the Model
Modify `model_comparison.py` to:
- Add a 5th model with interaction terms
- Include cross-validation
- Plot learning curves

---

## 📚 Code Structure

### Common Functions (used across files)

**Data Loading:**
```python
def load_data(filename):
    df = pd.read_csv(filename)
    return df['Temperature'], df['Sales']
```

**Least Squares Calculation:**
```python
def calculate_least_squares(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    slope = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)
    intercept = y_mean - slope * x_mean
    return slope, intercept
```

**Model Evaluation:**
```python
def calculate_metrics(actual, predicted):
    mae = np.mean(np.abs(actual - predicted))
    r_squared = 1 - (np.sum((actual - predicted)**2) / 
                      np.sum((actual - np.mean(actual))**2))
    return mae, r_squared
```

---

## 🔧 Customization Guide

### Change Data Source
```python
# In model_visualizer.py, line 15:
filename = 'your_data.csv'  # Change this
```

### Adjust Model Bounds
```python
# In model_visualizer.py, line 78:
MIN_SALES = 300  # Change minimum
MAX_SALES = 900  # Change maximum
```

### Add New Visualizations
```python
# Add to create_visualization() function:
ax5 = axes[2, 0]  # New subplot
ax5.plot(your_data)
ax5.set_title('Your New Plot')
```

---

## 🐛 Troubleshooting

### Error: "No module named 'pandas'"
```bash
pip install pandas
```

### Error: "File not found"
Make sure CSV files are in the `data/` folder:
```
Chapter-02-From-Guesswork-to-Models/
├── code/python/model_visualizer.py
└── data/rajesh_weekly_sales.csv  ← Check this path
```

### Error: "Invalid temperature value"
Temperature must be numeric:
```python
# Good: 
temp = 30

# Bad:
temp = "thirty"  # Will cause error
```

---

## 📖 Further Reading

**On Least Squares:**
- NumPy documentation: Linear algebra operations
- SciPy documentation: Statistical functions
- Sklearn documentation: Linear regression

**On Data Visualization:**
- Matplotlib gallery: Example plots
- Seaborn tutorial: Statistical visualizations

**On Model Validation:**
- Cross-validation guide
- Bias-variance tradeoff
- Overfitting prevention

---

## 🤝 Contributing

Found a bug or have an improvement?
- Open an issue in the main repository
- Submit a pull request with fixes
- Share your modified versions in Discussions

---

## 📄 License

These code examples are part of "The Pattern Hunters" educational materials.
- Code: MIT License (free to use and modify)
- Educational content: © Dr. Alok Patel

---

**Questions?** Open an issue or ask in [Discussions](../../discussions)

**Back to:** [Chapter 2 Home](../../README.md) | [Repository Home](../../../../README.md)
