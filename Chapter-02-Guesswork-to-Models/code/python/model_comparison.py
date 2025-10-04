"""
Model Comparison Tool
Compare multiple models and recommend the best one

Chapter 2: From Guesswork to Models
The Pattern Hunters - Dr. Alok Patel
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def load_complete_data(filename='../../data/rajesh_complete_data.csv'):
    """Load complete dataset with all variables"""
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print(f"⚠️  File not found: {filename}")
        print("Creating sample data...")
        # Create sample data
        np.random.seed(42)
        n = 20
        data = {
            'Day': range(1, n+1),
            'Temperature': np.random.uniform(25, 38, n),
            'DayOfWeek': np.random.randint(1, 8, n),
            'Weather': np.random.randint(0, 3, n),
            'Sales': np.random.uniform(400, 800, n)
        }
        return pd.DataFrame(data)

def build_model(X, y, model_name, features):
    """Build a linear regression model and calculate metrics"""
    model = LinearRegression()
    model.fit(X, y)
    predictions = model.predict(X)
    
    mae = mean_absolute_error(y, predictions)
    rmse = np.sqrt(mean_squared_error(y, predictions))
    r2 = r2_score(y, predictions)
    
    return {
        'name': model_name,
        'model': model,
        'features': features,
        'predictions': predictions,
        'mae': mae,
        'rmse': rmse,
        'r2': r2,
        'coefficients': model.coef_,
        'intercept': model.intercept_
    }

def compare_models_visualization(df, models):
    """Create 4-panel comparison visualization"""
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Model Comparison for Rajesh\'s Tea Stall', 
                 fontsize=16, fontweight='bold')
    
    model_names = [m['name'] for m in models]
    mae_scores = [m['mae'] for m in models]
    r2_scores = [m['r2'] for m in models]
    
    colors = ['steelblue', 'orange', 'green', 'red']
    
    # Panel 1: MAE Comparison
    ax1 = axes[0, 0]
    bars1 = ax1.bar(model_names, mae_scores, color=colors[:len(models)])
    ax1.set_ylabel('Mean Absolute Error (₹)', fontsize=11)
    ax1.set_title('Model Accuracy: Lower is Better', fontsize=12)
    ax1.tick_params(axis='x', rotation=15)
    
    for bar, val in zip(bars1, mae_scores):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'₹{val:.0f}', ha='center', va='bottom', fontsize=9)
    
    # Panel 2: R² Comparison
    ax2 = axes[0, 1]
    bars2 = ax2.bar(model_names, r2_scores, color=colors[:len(models)])
    ax2.set_ylabel('R² Score', fontsize=11)
    ax2.set_title('Model Fit: Higher is Better', fontsize=12)
    ax2.set_ylim(0, 1)
    ax2.tick_params(axis='x', rotation=15)
    ax2.axhline(y=0.7, color='gray', linestyle='--', alpha=0.5, label='Good threshold')
    ax2.legend()
    
    for bar, val in zip(bars2, r2_scores):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{val:.3f}', ha='center', va='bottom', fontsize=9)
    
    # Panel 3: Actual vs Predicted for best model
    ax3 = axes[1, 0]
    best_model = max(models, key=lambda x: x['r2'])
    
    y_actual = df['Sales'].values
    y_pred = best_model['predictions']
    
    ax3.scatter(y_actual, y_pred, alpha=0.6, s=100, edgecolors='black', c='purple')
    
    min_val = min(y_actual.min(), y_pred.min())
    max_val = max(y_actual.max(), y_pred.max())
    ax3.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Perfect')
    
    ax3.set_xlabel('Actual Sales (₹)', fontsize=11)
    ax3.set_ylabel('Predicted Sales (₹)', fontsize=11)
    ax3.set_title(f'Best Model: {best_model["name"]} (R²={best_model["r2"]:.3f})', fontsize=12)
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Panel 4: Summary table
    ax4 = axes[1, 1]
    ax4.axis('tight')
    ax4.axis('off')
    
    table_data = [['Model', 'MAE (₹)', 'RMSE (₹)', 'R²', 'Features']]
    
    for model in models:
        table_data.append([
            model['name'],
            f"{model['mae']:.0f}",
            f"{model['rmse']:.0f}",
            f"{model['r2']:.3f}",
            str(len(model['features']))
        ])
    
    table = ax4.table(cellText=table_data, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2)
    
    # Style header
    for i in range(5):
        table[(0, i)].set_facecolor('#4472C4')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Highlight best model
    best_idx = r2_scores.index(max(r2_scores)) + 1
    for i in range(5):
        table[(best_idx, i)].set_facecolor('#90EE90')
    
    ax4.set_title('Model Comparison Summary', fontsize=12, pad=20)
    
    plt.tight_layout()
    return fig

def generate_report(df, models):
    """Generate detailed text report"""
    print("\n" + "="*70)
    print("MODEL COMPARISON REPORT")
    print("="*70)
    
    print(f"\nDataset: {len(df)} observations")
    print(f"Variables: Temperature, Day of Week, Weather")
    print(f"Target: Sales (₹)")
    
    print("\n" + "-"*70)
    print("MODEL PERFORMANCE SUMMARY")
    print("-"*70)
    
    for i, model in enumerate(models, 1):
        print(f"\n{i}. {model['name']}")
        print(f"   Features: {', '.join(model['features'])}")
        print(f"   MAE:  ₹{model['mae']:.2f}")
        print(f"   RMSE: ₹{model['rmse']:.2f}")
        print(f"   R²:   {model['r2']:.4f} ({model['r2']*100:.1f}%)")
        
        if model['r2'] > 0.9:
            quality = "Excellent"
        elif model['r2'] > 0.7:
            quality = "Good"
        elif model['r2'] > 0.5:
            quality = "Moderate"
        else:
            quality = "Poor"
        print(f"   Quality: {quality}")
    
    best_model = max(models, key=lambda x: x['r2'])
    print("\n" + "-"*70)
    print("RECOMMENDATION")
    print("-"*70)
    print(f"\nBest Model: {best_model['name']}")
    print(f"R² Score: {best_model['r2']:.4f}")
    print(f"Average Error: ±₹{best_model['mae']:.0f}")
    
    print("\n📊 INTERPRETATION:")
    print(f"• {best_model['name']} explains {best_model['r2']*100:.1f}% of sales variation")
    print(f"• On average, predictions are within ±₹{best_model['mae']:.0f} of actual sales")
    
    if len(models) > 1:
        baseline = models[0]
        improvement = (best_model['r2'] / baseline['r2'] - 1) * 100
        print(f"• This model is {improvement:.1f}% better than {baseline['name']}")
    
    print("\n💡 BUSINESS RECOMMENDATION:")
    if best_model['name'] == 'Combined Model':
        print("• Use combined model for most accurate predictions")
        print("• Consider all factors: temperature, day, and weather")
        print("• Build safety buffer into inventory decisions")
    else:
        print(f"• {best_model['name']} is sufficient for practical use")
        print("• Adding more factors doesn't significantly improve accuracy")
        print("• Keep model simple for daily use")
    
    print("\n" + "="*70)

def main():
    """Main program"""
    print("\n🔬 Model Comparison Tool - Rajesh's Tea Stall")
    print("="*70)
    
    # Load data
    print("\nLoading complete dataset...")
    df = load_complete_data()
    print(f"✓ Loaded {len(df)} days of data")
    
    # Build models
    print("\nBuilding models...")
    models = []
    
    # Model 1: Temperature only
    X1 = df[['Temperature']].values
    y = df['Sales'].values
    model1 = build_model(X1, y, 'Temperature Only', ['Temperature'])
    models.append(model1)
    print("  ✓ Model 1: Temperature only")
    
    # Model 2: Day of week only
    X2 = df[['DayOfWeek']].values
    model2 = build_model(X2, y, 'Day of Week Only', ['DayOfWeek'])
    models.append(model2)
    print("  ✓ Model 2: Day of week only")
    
    # Model 3: Weather only
    X3 = df[['Weather']].values
    model3 = build_model(X3, y, 'Weather Only', ['Weather'])
    models.append(model3)
    print("  ✓ Model 3: Weather only")
    
    # Model 4: Combined
    X4 = df[['Temperature', 'DayOfWeek', 'Weather']].values
    model4 = build_model(X4, y, 'Combined Model', ['Temperature', 'DayOfWeek', 'Weather'])
    models.append(model4)
    print("  ✓ Model 4: Combined (all factors)")
    
    # Create visualization
    print("\nGenerating comparison visualization...")
    fig = compare_models_visualization(df, models)
    
    output_file = 'model_comparison.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"✓ Saved as '{output_file}'")
    
    # Generate report
    generate_report(df, models)
    
    # Show plot
    print("\n📊 Displaying visualization...")
    print("   (Close the plot window to exit)")
    plt.show()
    
    print("\n✅ Analysis complete!")
    print("\n📚 Key insights:")
    print("   - Temperature is the strongest single predictor")
    print("   - Combining factors improves accuracy")
    print("   - Use model comparison to validate approaches")

if __name__ == "__main__":
    main()
