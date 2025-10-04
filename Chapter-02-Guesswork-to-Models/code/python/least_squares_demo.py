"""
Least Squares Demonstration
Educational script showing step-by-step least squares calculation

Chapter 2: From Guesswork to Models
The Pattern Hunters - Dr. Alok Patel
"""

import numpy as np
import pandas as pd

def load_data(filename='../../data/rajesh_two_weeks.csv'):
    """Load Rajesh's tea stall data"""
    try:
        df = pd.read_csv(filename)
        return df['Temperature'].values, df['Sales'].values
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        print("Using sample data instead...")
        # Sample data if file not found
        temp = np.array([35, 33, 30, 28, 36, 29, 26, 37, 34, 31, 27, 38, 30, 25])
        sales = np.array([450, 520, 580, 720, 480, 650, 780, 440, 500, 600, 750, 420, 630, 800])
        return temp, sales

def demonstrate_least_squares(x, y):
    """
    Demonstrate least squares calculation step-by-step
    
    Parameters:
    x: array of temperature values
    y: array of sales values
    """
    n = len(x)
    
    print("=" * 70)
    print("LEAST SQUARES CALCULATION - STEP BY STEP DEMONSTRATION")
    print("=" * 70)
    
    # Step 1: Calculate means
    print("\n📊 STEP 1: Calculate Means")
    print("-" * 70)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    print(f"Mean Temperature (x̄) = {x_mean:.2f}°C")
    print(f"Mean Sales (ȳ) = ₹{y_mean:.2f}")
    
    # Step 2: Calculate deviations
    print("\n📐 STEP 2: Calculate Deviations from Mean")
    print("-" * 70)
    print(f"{'Day':<6} {'Temp':<8} {'Sales':<8} {'(x-x̄)':<10} {'(y-ȳ)':<10}")
    print("-" * 70)
    
    x_dev = x - x_mean
    y_dev = y - y_mean
    
    for i in range(min(5, n)):  # Show first 5 rows
        print(f"{i+1:<6} {x[i]:<8.1f} {y[i]:<8.0f} {x_dev[i]:<10.2f} {y_dev[i]:<10.2f}")
    if n > 5:
        print(f"... (showing first 5 of {n} rows)")
    
    # Step 3: Calculate products and squares
    print("\n🔢 STEP 3: Calculate Products and Squares")
    print("-" * 70)
    print(f"{'Day':<6} {'(x-x̄)':<10} {'(y-ȳ)':<10} {'(x-x̄)(y-ȳ)':<15} {'(x-x̄)²':<10}")
    print("-" * 70)
    
    xy_products = x_dev * y_dev
    x_squares = x_dev ** 2
    
    for i in range(min(5, n)):
        print(f"{i+1:<6} {x_dev[i]:<10.2f} {y_dev[i]:<10.2f} {xy_products[i]:<15.2f} {x_squares[i]:<10.2f}")
    if n > 5:
        print(f"... (showing first 5 of {n} rows)")
    
    # Step 4: Sum the products and squares
    print("\n➕ STEP 4: Sum the Products and Squares")
    print("-" * 70)
    sum_xy = np.sum(xy_products)
    sum_x_sq = np.sum(x_squares)
    
    print(f"Σ[(x-x̄)(y-ȳ)] = {sum_xy:.2f}")
    print(f"Σ[(x-x̄)²] = {sum_x_sq:.2f}")
    
    # Step 5: Calculate slope
    print("\n📈 STEP 5: Calculate Slope")
    print("-" * 70)
    slope = sum_xy / sum_x_sq
    print(f"Slope (m) = Σ[(x-x̄)(y-ȳ)] / Σ[(x-x̄)²]")
    print(f"Slope (m) = {sum_xy:.2f} / {sum_x_sq:.2f}")
    print(f"Slope (m) = {slope:.2f} ₹/°C")
    
    print(f"\n💡 Interpretation:")
    print(f"   For every 1°C increase in temperature,")
    print(f"   sales {'decrease' if slope < 0 else 'increase'} by ₹{abs(slope):.2f}")
    
    # Step 6: Calculate intercept
    print("\n📍 STEP 6: Calculate Intercept")
    print("-" * 70)
    intercept = y_mean - slope * x_mean
    print(f"Intercept (b) = ȳ - (m × x̄)")
    print(f"Intercept (b) = {y_mean:.2f} - ({slope:.2f} × {x_mean:.2f})")
    print(f"Intercept (b) = {intercept:.2f}")
    
    # Step 7: Final model
    print("\n🎯 STEP 7: Final Linear Model")
    print("=" * 70)
    print(f"\n   Sales = {intercept:.2f} + ({slope:.2f}) × Temperature")
    print(f"\n   Or simplified:")
    if slope < 0:
        print(f"   Sales = {intercept:.0f} - {abs(slope):.1f} × Temperature")
    else:
        print(f"   Sales = {intercept:.0f} + {slope:.1f} × Temperature")
    
    # Step 8: Make predictions
    print("\n🔮 STEP 8: Test Predictions")
    print("-" * 70)
    test_temps = [28, 32, 35]
    
    for temp in test_temps:
        pred_sales = intercept + slope * temp
        print(f"   At {temp}°C: Predicted sales = ₹{pred_sales:.0f}")
    
    # Step 9: Calculate R²
    print("\n📊 STEP 9: Model Quality (R²)")
    print("-" * 70)
    y_pred = intercept + slope * x
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - y_mean) ** 2)
    r_squared = 1 - (ss_res / ss_tot)
    
    print(f"R² = 1 - (SS_residual / SS_total)")
    print(f"R² = 1 - ({ss_res:.2f} / {ss_tot:.2f})")
    print(f"R² = {r_squared:.4f} or {r_squared*100:.2f}%")
    
    print(f"\n💡 Interpretation:")
    print(f"   The model explains {r_squared*100:.1f}% of the variation in sales.")
    if r_squared > 0.9:
        print(f"   This is an EXCELLENT fit!")
    elif r_squared > 0.7:
        print(f"   This is a GOOD fit!")
    else:
        print(f"   This is a MODERATE fit.")
    
    # Step 10: Calculate MAE
    print("\n📏 STEP 10: Average Prediction Error (MAE)")
    print("-" * 70)
    mae = np.mean(np.abs(y - y_pred))
    print(f"Mean Absolute Error = ₹{mae:.2f}")
    print(f"\n💡 On average, predictions are off by ±₹{mae:.0f}")
    
    return slope, intercept, r_squared, mae

def main():
    """Main function"""
    print("\n🍵 Rajesh's Tea Stall - Least Squares Analysis")
    print("=" * 70)
    
    # Load data
    print("\nLoading data...")
    temperature, sales = load_data()
    print(f"✓ Loaded {len(temperature)} days of sales data")
    print(f"  Temperature range: {temperature.min():.1f}°C - {temperature.max():.1f}°C")
    print(f"  Sales range: ₹{sales.min():.0f} - ₹{sales.max():.0f}")
    
    # Demonstrate least squares
    slope, intercept, r_squared, mae = demonstrate_least_squares(temperature, sales)
    
    # Summary
    print("\n" + "=" * 70)
    print("📋 SUMMARY")
    print("=" * 70)
    print(f"\n✓ Model Equation: Sales = {intercept:.0f} + ({slope:.2f}) × Temperature")
    print(f"✓ R² Score: {r_squared:.4f} ({r_squared*100:.1f}% of variation explained)")
    print(f"✓ Mean Absolute Error: ±₹{mae:.0f}")
    print(f"✓ Quality: {'Excellent' if r_squared > 0.9 else 'Good' if r_squared > 0.7 else 'Moderate'}")
    
    print("\n" + "=" * 70)
    print("🎓 Key Learning Points:")
    print("-" * 70)
    print("1. Least squares finds the 'best fit' line mathematically")
    print("2. Negative slope = inverse relationship (hotter → less sales)")
    print("3. R² measures how well the model explains the data")
    print("4. MAE tells us typical prediction error in real units (₹)")
    print("5. This same method works for ANY linear relationship!")
    print("=" * 70)
    
    print("\n✨ Try modifying this code:")
    print("   - Use your own CSV data")
    print("   - Change the temperature values to predict different scenarios")
    print("   - Add visualization using matplotlib")
    
    print("\n📚 Next: Try model_visualizer.py for visual analysis!")
    print()

if __name__ == "__main__":
    main()
