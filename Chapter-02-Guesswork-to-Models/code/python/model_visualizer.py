"""
Interactive Model Visualizer
Creates 4-panel visualization and interactive prediction tool

Chapter 2: From Guesswork to Models
The Pattern Hunters - Dr. Alok Patel
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_data(filename='../../data/rajesh_weekly_sales.csv'):
    """Load tea stall data from CSV"""
    try:
        df = pd.read_csv(filename)
        return df['Temperature'].values, df['Sales'].values
    except FileNotFoundError:
        print(f"⚠️  File not found: {filename}")
        print("Using sample data instead...")
        temp = np.array([35, 33, 30, 28, 36, 29, 26])
        sales = np.array([450, 520, 580, 720, 480, 650, 780])
        return temp, sales

def calculate_least_squares(x, y):
    """
    Calculate least squares regression manually
    Returns model parameters and metrics
    """
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    # Calculate slope
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)
    slope = numerator / denominator
    
    # Calculate intercept
    intercept = y_mean - slope * x_mean
    
    # Make predictions
    y_pred = intercept + slope * x
    
    # Calculate residuals
    residuals = y - y_pred
    
    # Calculate R²
    ss_res = np.sum(residuals ** 2)
    ss_tot = np.sum((y - y_mean) ** 2)
    r_squared = 1 - (ss_res / ss_tot)
    
    # Calculate MAE
    mae = np.mean(np.abs(residuals))
    
    return {
        'slope': slope,
        'intercept': intercept,
        'predictions': y_pred,
        'residuals': residuals,
        'r_squared': r_squared,
        'mae': mae
    }

def create_visualization(x, y, model_results):
    """Create 4-panel visualization"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Rajesh's Tea Stall - Model Analysis", 
                 fontsize=16, fontweight='bold')
    
    slope = model_results['slope']
    intercept = model_results['intercept']
    y_pred = model_results['predictions']
    residuals = model_results['residuals']
    r_squared = model_results['r_squared']
    mae = model_results['mae']
    
    # Panel 1: Scatter plot with regression line
    ax1 = axes[0, 0]
    ax1.scatter(x, y, color='steelblue', s=100, alpha=0.6, 
                edgecolors='black', label='Actual')
    
    # Plot regression line
    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = intercept + slope * x_line
    ax1.plot(x_line, y_line, 'r-', linewidth=2, label='Model')
    
    ax1.set_xlabel('Temperature (°C)', fontsize=12)
    ax1.set_ylabel('Sales (₹)', fontsize=12)
    ax1.set_title('Temperature vs Sales with Best-Fit Line', fontsize=13)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Add equation
    equation = f"Sales = {intercept:.0f} - {abs(slope):.1f} × Temp"
    ax1.text(0.05, 0.95, equation, transform=ax1.transAxes,
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5),
             verticalalignment='top', fontsize=10)
    
    # Panel 2: Residual plot
    ax2 = axes[0, 1]
    ax2.scatter(y_pred, residuals, color='green', s=100, 
                alpha=0.6, edgecolors='black')
    ax2.axhline(y=0, color='r', linestyle='--', linewidth=2)
    ax2.set_xlabel('Predicted Sales (₹)', fontsize=12)
    ax2.set_ylabel('Residuals (₹)', fontsize=12)
    ax2.set_title('Residual Plot (Error Analysis)', fontsize=13)
    ax2.grid(True, alpha=0.3)
    
    # Add MAE reference lines
    ax2.axhline(y=mae, color='orange', linestyle=':', linewidth=1, 
                label=f'±MAE (±₹{mae:.0f})')
    ax2.axhline(y=-mae, color='orange', linestyle=':', linewidth=1)
    ax2.legend()
    
    # Panel 3: Actual vs Predicted
    ax3 = axes[1, 0]
    ax3.scatter(y, y_pred, color='purple', s=100, alpha=0.6, 
                edgecolors='black')
    
    # Perfect prediction line
    min_val = min(y.min(), y_pred.min())
    max_val = max(y.max(), y_pred.max())
    ax3.plot([min_val, max_val], [min_val, max_val], 'r--', 
             linewidth=2, label='Perfect Prediction')
    
    ax3.set_xlabel('Actual Sales (₹)', fontsize=12)
    ax3.set_ylabel('Predicted Sales (₹)', fontsize=12)
    ax3.set_title('Actual vs Predicted Values', fontsize=13)
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Panel 4: Model statistics
    ax4 = axes[1, 1]
    ax4.axis('off')
    
    stats_text = f"""
MODEL STATISTICS
================

Equation:
Sales = {intercept:.2f} + ({slope:.2f}) × Temperature

Or simplified:
Sales = {intercept:.0f} - {abs(slope):.1f} × Temp

Model Quality:
• R² = {r_squared:.4f} ({r_squared*100:.2f}%)
• Mean Absolute Error = ₹{mae:.2f}
• Slope = {slope:.2f} ₹/°C

Interpretation:
• For every 1°C temperature increase,
  sales decrease by ₹{abs(slope):.2f}

• Model explains {r_squared*100:.1f}% of variation

• Average prediction error: ±₹{mae:.0f}

Data Summary:
• Sample size: {len(x)} days
• Temperature: {x.min():.1f}°C - {x.max():.1f}°C
• Sales: ₹{y.min():.0f} - ₹{y.max():.0f}
"""
    
    ax4.text(0.1, 0.9, stats_text, transform=ax4.transAxes,
             fontsize=10, verticalalignment='top', family='monospace',
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))
    
    plt.tight_layout()
    return fig

def interactive_predictor(slope, intercept):
    """Interactive prediction tool"""
    MIN_SALES = 300
    MAX_SALES = 900
    
    print("\n" + "="*50)
    print("INTERACTIVE SALES PREDICTOR")
    print("="*50)
    print(f"\nModel: Sales = {intercept:.0f} + ({slope:.2f}) × Temperature\n")
    
    while True:
        try:
            temp_input = input("\nEnter temperature (°C) or 'q' to quit: ")
            if temp_input.lower() == 'q':
                break
            
            temp = float(temp_input)
            predicted_sales = intercept + slope * temp
            
            # Apply bounds
            bounded_sales = max(MIN_SALES, min(MAX_SALES, predicted_sales))
            
            print(f"\n📊 Prediction for {temp}°C:")
            print(f"   Raw prediction: ₹{predicted_sales:.0f}")
            if bounded_sales != predicted_sales:
                print(f"   Bounded prediction: ₹{bounded_sales:.0f}")
                print(f"   (Applied ₹{MIN_SALES}-₹{MAX_SALES} bounds)")
            else:
                print(f"   Expected sales: ₹{bounded_sales:.0f}")
            
            # Add interpretation
            if temp < 28:
                print("   💡 Cool day - expect high sales!")
            elif temp < 33:
                print("   💡 Moderate temperature - normal sales")
            else:
                print("   💡 Hot day - expect lower sales")
                
        except ValueError:
            print("❌ Please enter a valid number or 'q'")
    
    print("\n👋 Thanks for using the predictor!")

def main():
    """Main program"""
    print("\n🍵 Rajesh's Tea Stall Model Visualizer")
    print("="*50)
    
    # Load data
    print("\nLoading data...")
    temperature, sales = load_data()
    
    print(f"✓ Loaded {len(temperature)} days of data")
    print(f"  Temperature range: {temperature.min():.1f}°C - {temperature.max():.1f}°C")
    print(f"  Sales range: ₹{sales.min():.0f} - ₹{sales.max():.0f}")
    
    # Calculate model
    print("\nCalculating least squares regression...")
    model_results = calculate_least_squares(temperature, sales)
    
    print(f"✓ Model fitted!")
    print(f"  R² = {model_results['r_squared']:.4f}")
    print(f"  MAE = ₹{model_results['mae']:.2f}")
    
    # Create visualization
    print("\nGenerating visualization...")
    fig = create_visualization(temperature, sales, model_results)
    
    # Save figure
    output_file = 'tea_stall_analysis.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Saved visualization as '{output_file}'")
    
    # Show plot
    print("\n📊 Displaying visualization...")
    print("   (Close the plot window to continue)")
    plt.show()
    
    # Interactive predictor
    response = input("\nWould you like to make predictions? (y/n): ")
    if response.lower() == 'y':
        interactive_predictor(model_results['slope'], model_results['intercept'])
    
    print("\n✅ Analysis complete!")
    print("\n📚 Next steps:")
    print("   - Try model_comparison.py to compare multiple models")
    print("   - Modify the code to use your own data")
    print("   - Experiment with different visualization styles")

if __name__ == "__main__":
    main()
