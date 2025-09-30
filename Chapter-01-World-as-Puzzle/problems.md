# Chapter 1: The World as a Puzzle
## Problems

**Pattern Recognition in Biology and Daily Life**

---

## 📝 Problem Set Overview

**Total Problems:** 8  
**Difficulty Range:** ⭐ Easy to ⭐⭐⭐ Challenging  
**Estimated Time:** 3-4 hours total  
**Skills Practiced:** Pattern recognition, correlation vs. causation, complex systems, scientific thinking

---

## ⭐ EASY PROBLEMS (Warm-up)

### Problem 1.1: Daily Pattern Recognition
**Difficulty:** ⭐ Easy  
**Time:** 15 minutes  
**Skills:** Observation, pattern identification

You observe customer patterns at a local tea stall over two weeks:

| Day | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday |
|-----|--------|---------|-----------|----------|--------|----------|--------|
| Week 1 | 42 | 65 | 70 | 68 | 87 | 50 | 35 |
| Week 2 | 48 | 70 | 75 | 72 | 91 | 55 | 40 |

**Questions:**
a) What pattern do you observe across the week?  
b) Calculate the average customers for weekdays vs. weekends  
c) Propose a hypothesis to explain this pattern  
d) What additional data would help test your hypothesis?

**Learning Goals:** Recognize patterns, distinguish signal from noise, propose testable hypotheses

---

### Problem 1.2: Correlation vs. Causation
**Difficulty:** ⭐ Easy  
**Time:** 20 minutes  
**Skills:** Critical thinking, causal reasoning

A news article claims: "Study shows ice cream sales cause drowning deaths - both peak in summer months!"

**Questions:**
a) Is this a correlation or causation? Explain.  
b) What is the actual underlying cause?  
c) Give two other examples of correlation without causation from biology  
d) Design an experiment to test if ice cream truly causes drowning

**Learning Goals:** Distinguish correlation from causation, identify confounding variables

---

### Problem 1.3: The Firefly Mystery
**Difficulty:** ⭐ Easy  
**Time:** 25 minutes  
**Skills:** Time series analysis, synchronization

You observe fireflies flashing at night. Three fireflies show these patterns (in seconds):

```
Firefly A: 0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0
Firefly B: 0, 2.1, 4.2, 6.0, 8.1, 10.0, 12.1
Firefly C: 0, 1.9, 3.9, 6.0, 7.9, 10.0, 11.9
```

**Questions:**
a) Calculate the average period (time between flashes) for each firefly  
b) At what times do all three flash together?  
c) What pattern suggests synchronization is occurring?  
d) Propose a biological mechanism that could cause synchronization

**Learning Goals:** Analyze periodic phenomena, detect synchronization patterns

---

## ⭐⭐ MEDIUM PROBLEMS (Building Skills)

### Problem 1.4: The Green Revolution Impact
**Difficulty:** ⭐⭐ Medium  
**Time:** 45 minutes  
**Skills:** Data analysis, trend detection, inflection point identification  
**Dataset:** `datasets/wheat-yield-india.csv`

Analyze wheat yield data from India (1960-1990):

| Year | Yield (kg/hectare) |
|------|--------------------|
| 1960 | 850 |
| 1965 | 900 |
| 1967 | 950 |
| 1970 | 1,450 |
| 1975 | 1,800 |
| 1980 | 2,100 |
| 1985 | 2,300 |
| 1990 | 2,500 |

**Questions:**
a) Plot yield vs. year. Identify the inflection point (Green Revolution start)  
b) Calculate average growth rate before 1967 and after 1970  
c) If yield continued at pre-1967 rate, what would 1990 yield be?  
d) Estimate how many additional people could be fed due to increased yields  
e) List three confounding variables that might affect this analysis

**Learning Goals:** Identify historical trends, quantify impact, consider confounders

---

### Problem 1.5: Pattern Recognition in Your Life
**Difficulty:** ⭐⭐ Medium  
**Time:** 1 week (15 min/day)  
**Skills:** Self-observation, data collection, model building

**Your Task:** Design your own pattern recognition study:

**Day 1-2:** Choose a daily decision you make (sleep time, social media use, study hours, meal timing)  

**Day 3-7:** Collect data on:
- Your decision/behavior
- Factors you consider
- Outcomes you observe

**Day 8:** Analyze your data:
- What patterns emerged?
- Can you predict your behavior?
- What factors matter most?

**Submit:**
- Data table (5-7 days)
- Pattern analysis (200 words)
- Testable hypothesis
- Proposed improvements to your model

**Learning Goals:** Apply scientific method to personal life, build predictive models

---

### Problem 1.6: Complex Systems and Emergence
**Difficulty:** ⭐⭐ Medium  
**Time:** 30 minutes  
**Skills:** Systems thinking, emergence concepts

Consider three scenarios:

**Scenario A:** Individual ants follow simple rules (follow pheromone trails, avoid obstacles). Yet ant colonies exhibit complex behaviors like farming, warfare, and architecture.

**Scenario B:** Individual brain neurons fire based on simple electrical thresholds. Yet consciousness, memory, and creativity emerge.

**Scenario C:** Individual students choosing courses based on interest. Yet university enrollment patterns become predictable.

**Questions:**
a) What is "emergence"? Define in your own words.  
b) For each scenario, identify: (i) simple rules, (ii) emergent behavior  
c) Give one biological example of emergence not listed above  
d) Why can't we predict emergent behavior from individual rules alone?  
e) How does this relate to chaos theory and sensitive dependence?

**Learning Goals:** Understand emergence, complex systems, unpredictability

---

## ⭐⭐⭐ CHALLENGING PROBLEMS (Deep Thinking)

### Problem 1.7: The Detective's Dilemma
**Difficulty:** ⭐⭐⭐ Challenging  
**Time:** 60 minutes  
**Skills:** Scientific reasoning, hypothesis testing, experimental design

Dr. Kochar notices 5 unusual pneumonia cases in her hospital over 2 weeks, all from the same neighborhood. Normal rate is 1 case per month hospital-wide.

**Given Information:**
- All patients live within 500m radius
- Ages: 34, 45, 52, 28, 61 years
- No common workplace or social connections found
- Symptoms started 3-5 days apart
- Local population: ~5,000 people

**Questions:**
a) Calculate: Is 5 cases in 2 weeks statistically unusual? (Hint: Use Poisson probability if expected = 0.5 cases/2 weeks)  
b) List 5 possible explanations (biological, environmental, random)  
c) Design an investigation: What data would you collect? What order?  
d) How would you distinguish between:
   - Infectious outbreak
   - Environmental exposure
   - Random cluster
e) At what point would you alert public health authorities?  
f) What ethical considerations apply?

**Learning Goals:** Scientific investigation, hypothesis generation, statistical reasoning, ethics

---

### Problem 1.8: Building a Predictive Model
**Difficulty:** ⭐⭐⭐ Challenging  
**Time:** 90 minutes  
**Skills:** Model building, least squares, prediction, validation  
**Dataset:** `datasets/temperature-tea-sales.csv`

A tea vendor collected data on daily temperature and sales:

| Temperature (°C) | Sales (cups) |
|------------------|--------------|
| 25 | 145 |
| 28 | 152 |
| 32 | 168 |
| 35 | 180 |
| 38 | 195 |
| 40 | 205 |
| 42 | 218 |

**Questions:**
a) **Visualize:** Plot temperature vs. sales. Does relationship look linear?  
b) **Model:** Calculate the best-fit line using least squares method:
   - Find slope (m) and intercept (b) for: Sales = m × Temperature + b
   - Show all calculation steps
c) **Interpret:** What does the slope mean in practical terms?  
d) **Predict:** Use your model to predict sales at:
   - 30°C (interpolation)
   - 45°C (extrapolation)
e) **Validate:** Which prediction is more reliable? Why?  
f) **Limitations:** List 3 factors your model ignores  
g) **Improve:** How could you make the model more realistic?

**Advanced:** What if the relationship is NOT linear? Try fitting a quadratic model and compare.

**Learning Goals:** Linear regression, model interpretation, prediction limitations

---

## 💻 Coding Challenges (Optional)

### Challenge C1: Visualize Patterns
**Language:** Python  
**Difficulty:** ⭐⭐ Medium  
**Time:** 30 minutes

Write Python code to:
1. Load the tea stall customer data (Problem 1.1)
2. Create a bar plot showing daily patterns
3. Calculate and display weekly averages
4. Add a trend line

**Starter code provided in:** `code/python/chapter1_visualization.py`

---

### Challenge C2: Firefly Synchronization Simulator
**Language:** Python  
**Difficulty:** ⭐⭐⭐ Challenging  
**Time:** 60 minutes

Create an interactive simulation where:
1. Multiple "fireflies" flash with slightly different periods
2. Each firefly adjusts its timing based on neighbors
3. Visualize synchronization emerging over time
4. Measure synchronization quantitatively

**Starter code provided in:** `code/python/firefly_sync.py`

---

## 📊 Datasets

All datasets available in: `Chapter-01-World-as-Puzzle/datasets/`

- `tea-stall-customers.csv` - Problems 1.1, 1.5
- `wheat-yield-india.csv` - Problem 1.4
- `temperature-tea-sales.csv` - Problem 1.8
- `firefly-flash-times.csv` - Problem 1.3

---

## 🎯 Learning Outcomes Check

After completing these problems, you should be able to:
- ✅ Identify patterns in everyday observations
- ✅ Distinguish correlation from causation
- ✅ Explain complex systems and emergence
- ✅ Apply the scientific method systematically
- ✅ Build simple predictive models
- ✅ Recognize when to question patterns vs. trust them

---

## 📚 Additional Resources

**Before attempting problems:**
- Read Chapter 1 in the book (pages 1-24)
- Review Figures 1.5 and 1.6

**If you're stuck:**
- Check the hints in the solutions file
- Use the discussion forum
- Review the pattern recognition toolkit (Figure 1.5)

**After completing:**
- Compare your solutions with provided answers
- Discuss alternative approaches in the forum
- Try creating your own problems!

---

**Next:** [Solutions →](solutions.md) | [Chapter 2 Problems →](../Chapter-02-Guesswork-to-Models/problems.md)

**Back to:** [Chapter 1 Home](README.md) | [Repository Home](../README.md)
