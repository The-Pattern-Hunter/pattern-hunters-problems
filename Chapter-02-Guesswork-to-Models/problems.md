Chapter 2: From Guesswork to Models
Problems
The Art of Scientific Thinking

📝 Problem Set Overview
Total Problems: 8
Difficulty Range: ⭐ Easy to ⭐⭐⭐ Challenging
Estimated Time: 3-4 hours total
Skills Practiced: Model building, least squares method, data fitting, model validation, prediction

⭐ EASY PROBLEMS (Foundation Building)
Problem 2.1: Rajesh's Basic Model
Difficulty: ⭐ Easy
Time: 15 minutes
Skills: Pattern recognition, basic calculation

Rajesh has collected data on his tea sales over one week:

Day	Temperature (°C)	Sales (₹)
Mon	35	450
Tue	33	520
Wed	30	580
Thu	28	720
Fri	36	480
Sat	29	650
Sun	26	780
Questions: a) Calculate the average temperature and average sales
b) Does sales increase or decrease with temperature?
c) Estimate the change in sales for every 1°C temperature drop
d) Predict sales for a day with 32°C temperature using your intuition

Dataset: rajesh_weekly_sales.csv

Problem 2.2: Building Your First Linear Model
Difficulty: ⭐ Easy
Time: 20 minutes
Skills: Linear relationships, equation formulation

A student tracks study hours vs test scores:

Study Hours	Test Score
2	65
3	70
4	75
5	80
6	82
7	85
8	88
Questions: a) Plot these points on graph paper (or describe the pattern)
b) Does the relationship look linear?
c) Write a simple model: Test Score = a × Study Hours + b
d) What score would you predict for 10 hours of study?
e) What are the limitations of this model?

Dataset: study_scores.csv

⭐⭐ INTERMEDIATE PROBLEMS (Building Skills)
Problem 2.3: Least Squares Calculation
Difficulty: ⭐⭐ Medium
Time: 30 minutes
Skills: Least squares method, mathematical calculation

Using Rajesh's complete 2-week data:

Week 1:

Day	Temp (°C)	Sales (₹)
Mon	35	450
Tue	33	520
Wed	30	580
Thu	28	720
Fri	36	480
Sat	29	650
Sun	26	780
Week 2:

Day	Temp (°C)	Sales (₹)
Mon	37	440
Tue	34	500
Wed	31	600
Thu	27	750
Fri	38	420
Sat	30	630
Sun	25	800
Tasks: a) Calculate mean temperature and mean sales across all 14 days
b) Calculate the slope using least squares:

Slope = Σ[(x - x̄)(y - ȳ)] / Σ[(x - x̄)²]
c) Calculate the intercept: b = ȳ - (slope × x̄)
d) Write the complete model: Sales = ...
e) Test your model: predict sales for 32°C and compare with actual measurement
Dataset: rajesh_two_weeks.csv

Problem 2.4: Kamala's Pricing Model
Difficulty: ⭐⭐ Medium
Time: 25 minutes
Skills: Multi-variable modeling, business optimization

Kamala's tomato prices vary throughout the day:

Time	Price (₹/kg)	Demand Factor	Quality Factor
7 AM	40	High (1.2)	Fresh (1.0)
10 AM	38	Medium (1.0)	Fresh (0.95)
1 PM	35	Medium (1.0)	Good (0.9)
4 PM	30	Low (0.8)	Wilting (0.8)
7 PM	25	Very Low (0.6)	Poor (0.7)
Questions: a) Calculate base price (price at standard demand and quality)
b) Create a pricing model: Price = Base × Demand × Quality
c) What should Kamala charge at 3 PM if demand is medium (1.0) and quality is 0.85?
d) Explain why this model makes business sense
e) What factors are missing from this model?

Dataset: kamala_pricing.csv

⭐⭐⭐ CHALLENGING PROBLEMS (Advanced Application)
Problem 2.5: Model Validation and Error Analysis
Difficulty: ⭐⭐⭐ Challenging
Time: 40 minutes
Skills: Model testing, residual analysis, prediction accuracy

You've built a model for Rajesh: Sales = 1546 - 30.5 × Temperature

Test this model against new data from Week 3:

Day	Temp (°C)	Actual Sales (₹)	Weather Condition
Mon	34	510	Sunny
Tue	32	580	Cloudy
Wed	29	650	Light Rain
Thu	35	490	Sunny
Fri	31	620	Cloudy
Sat	27	780	Heavy Rain
Sun	33	540	Sunny
Tasks: a) Calculate predicted sales for each day using the model
b) Calculate residuals (error): Actual - Predicted for each day
c) Calculate mean absolute error: Average of |residuals|
d) Plot residuals vs. weather condition - do you see a pattern?
e) Propose an improved model that includes weather
f) Calculate R² (coefficient of determination) to measure model fit

Dataset: rajesh_week3_validation.csv

Problem 2.6: Multi-Variable Model Construction
Difficulty: ⭐⭐⭐ Challenging
Time: 45 minutes
Skills: Multiple regression concepts, complex modeling

Expand Rajesh's model to include multiple factors:

Complete dataset (20 days):

Temperature (°C)
Day of week (1=Monday, 7=Sunday)
Weather (Sunny=0, Cloudy=1, Rainy=2)
Sales (₹)
Day	Temp	DayOfWeek	Weather	Sales
1	35	1	0	450
2	33	2	0	520
3	30	3	1	580
4	28	4	2	720
...	...	...	...	...
Questions: a) Build three simple models:

Model 1: Sales vs Temperature only
Model 2: Sales vs Day of Week only
Model 3: Sales vs Weather only
b) Which single factor explains sales best?
c) Conceptually describe a combined model: Sales = α + β₁(Temp) + β₂(Day) + β₃(Weather)
d) Explain why day of week matters for sales
e) How would you validate which model is most useful?
Dataset: rajesh_complete_data.csv

Problem 2.7: Model Limitations and Real-World Constraints
Difficulty: ⭐⭐⭐ Challenging
Time: 30 minutes
Skills: Critical thinking, model interpretation

Rajesh wants to use your model to decide how much milk to order. Your model predicts:

At 20°C: Sales = 1546 - 30.5(20) = ₹936
At 45°C: Sales = 1546 - 30.5(45) = ₹174
Critical Analysis Questions: a) Is the 20°C prediction reasonable? (Note: Odisha rarely sees 20°C in summer)
b) Is the 45°C prediction realistic? (What are minimum sales even on hottest days?)
c) Identify at least 3 limitations of extrapolating beyond data range
d) Propose minimum and maximum bounds for the model
e) How would you advise Rajesh to use this model safely?
f) What happens to model reliability as you move away from mean temperature?

Conceptual dataset: Think through scenarios, no CSV needed

Problem 2.8: Comparing Intuition vs. Mathematics
Difficulty: ⭐⭐⭐ Challenging
Time: 35 minutes
Skills: Meta-analysis, scientific method, synthesis

Scenario: Babulal (traditional farmer) and Dr. Sharma (meteorologist) both predict monsoon arrival:

Babulal's indicators (collected over 30 years):

Peacock calls in morning: Yes/No
Ant mound height: Low/Medium/High
Tree flowering: Early/On-time/Late
Wind direction: East/West/Variable
Dr. Sharma's model (based on satellite data):

Sea surface temperature: °C
Atmospheric pressure: mb
Wind speed: km/h
Historical monsoon dates: Dates
Both predict monsoon for June 8th. Actual arrival: June 6th.

Questions: a) Both were off by 2 days. Does this mean both models are equally good?
b) List 3 advantages of Babulal's approach
c) List 3 advantages of Dr. Sharma's approach
d) How could you combine both approaches?
e) Design an experiment to test which indicators (traditional or modern) are most reliable
f) Explain why "all models are wrong, but some are useful"
g) Which model would you trust more for:

Next week's prediction?
Next year's prediction?
10-year climate trend?
Reflection: This problem has no single right answer - it's about thinking deeply!

💻 CODING CHALLENGES
Challenge C1: Build an Interactive Model Visualizer
Difficulty: ⭐⭐ Medium
Time: 60 minutes
Skills: Python/R programming, data visualization

Task: Create a program that:

Reads Rajesh's sales data from CSV
Calculates least squares fit automatically
Plots actual data points vs. model predictions
Shows residuals (errors) as a separate plot
Calculates and displays:
Mean absolute error
R² coefficient
Model equation
Bonus: Add slider to adjust temperature and show predicted sales in real-time

Starter code provided in: code/python/model_visualizer.py

Challenge C2: Model Comparison Tool
Difficulty: ⭐⭐⭐ Challenging
Time: 90 minutes
Skills: Statistical analysis, model evaluation

Task: Create a program that:

Loads data with multiple variables (temp, day, weather)
Builds multiple competing models
Compares models using:
Mean squared error
R² values
Cross-validation
AIC/BIC (if you know these)
Visualizes model comparison
Recommends best model with justification
Output: Report showing which factors matter most for prediction

Starter code provided in: code/python/model_comparison.py

📊 Datasets Provided
All datasets available in data/ folder:

rajesh_weekly_sales.csv - Problem 2.1
study_scores.csv - Problem 2.2
rajesh_two_weeks.csv - Problem 2.3
kamala_pricing.csv - Problem 2.4
rajesh_week3_validation.csv - Problem 2.5
rajesh_complete_data.csv - Problem 2.6
🎯 Learning Outcomes
After completing these problems, you should be able to:

✅ Build simple linear models from data
✅ Apply least squares method manually
✅ Validate model predictions
✅ Identify model limitations
✅ Compare intuitive vs. mathematical approaches
✅ Think critically about model assumptions
✅ Apply models to real-world decisions
✅ Code basic model fitting and visualization

💡 Tips for Success
Start with easy problems to build confidence
Show your work for calculations - partial credit available
Think conceptually first before diving into math
Check reasonableness of answers against real-world intuition
Use coding challenges to deepen understanding (optional but recommended)
Discuss with classmates - teaching others helps you learn
Connect to Chapter 1 - how does modeling extend pattern recognition?
📖 Related Chapter Sections
Section 2.1: Introduction - Everyday problem-solving
Section 2.2: Intuitive Models - Rajesh, Babulal, Kamala
Section 2.3: Formalization - From intuition to mathematics
Section 2.4: Least Squares Method - Finding best-fit models
Section 2.5: Model Refinement - Testing and improving
✅ Self-Check Questions
Before looking at solutions, test yourself:

Can I explain least squares in my own words?
Can I calculate a simple linear model by hand?
Do I understand why we minimize squared errors?
Can I identify when a model is over-extrapolating?
Do I appreciate both strengths and limitations of mathematical models?
🔗 Navigation
Solutions: View Detailed Solutions →

Code Examples: Browse Code →

Previous Chapter: ← Chapter 1: The World as a Puzzle

Next Chapter: Chapter 3: Revolutions in Thought →

Back to Chapter Home: Chapter 2 README

Repository Home: 🏠 Main Page

These problems are designed to transform your intuition into mathematical precision - the key to scientific thinking!

Ready to build your first models? Start with Problem 2.1 and work your way up! 🚀

Last Updated: October 2025
Part of: The Pattern Hunters - A Mathematical Journey Through Modern Biology
Author: Dr. Alok Patel

