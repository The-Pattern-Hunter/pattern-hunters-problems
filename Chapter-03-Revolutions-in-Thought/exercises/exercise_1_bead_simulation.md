# Exercise 1: Hardy-Weinberg Bead Simulation

## Learning Objectives

- Understand how random mating maintains allele frequencies
- Visualize the relationship between allele and genotype frequencies
- Experience the principle of statistical predictability in genetics

## Materials Needed

- 100 beads (or small objects) in two colors:
  - 60 red beads (representing A allele)
  - 40 blue beads (representing a allele)
- A container to mix the beads
- Data recording sheet

## Background

Hardy-Weinberg equilibrium demonstrates that allele frequencies remain constant across generations under random mating. This simulation helps you experience this principle hands-on.

**Key Concept:** Individual mating events are unpredictable, but population-level patterns are mathematically precise.

## Procedure

### Part A: Setup and Initial Frequencies

1. **Count your alleles:**
   - Red beads (A allele): 60
   - Blue beads (a allele): 40
   - Total alleles: 100

2. **Calculate initial allele frequencies:**
   - p (freq of A) = 60/100 = 0.60
   - q (freq of a) = 40/100 = 0.40
   - Verify: p + q = 1.00 ✓

3. **Predict genotype frequencies using Hardy-Weinberg:**
   - AA (p²) = (0.60)² = 0.36
   - Aa (2pq) = 2(0.60)(0.40) = 0.48
   - aa (q²) = (0.40)² = 0.16
   - Verify: 0.36 + 0.48 + 0.16 = 1.00 ✓

### Part B: Simulating Random Mating

**Round 1: Creating Offspring**

1. Mix all 100 beads thoroughly in your container
2. Without looking, draw 2 beads to represent one offspring
3. Record the genotype:
   - 2 red = AA
   - 1 red + 1 blue = Aa
   - 2 blue = aa
4. **Important:** Return the beads to the container
5. Repeat steps 2-4 for 50 offspring

**Recording Template:**

```
Offspring #  | Bead 1 | Bead 2 | Genotype
-------------|--------|--------|----------
1            | Red    | Red    | AA
2            | Red    | Blue   | Aa
3            | Blue   | Blue   | aa
...          | ...    | ...    | ...
```

### Part C: Data Analysis

1. **Count your results:**
   - Number of AA: _____
   - Number of Aa: _____
   - Number of aa: _____
   - Total: 50

2. **Calculate observed frequencies:**
   - Observed AA frequency = (# of AA) / 50 = _____
   - Observed Aa frequency = (# of Aa) / 50 = _____
   - Observed aa frequency = (# of aa) / 50 = _____

3. **Compare to predicted frequencies:**

   | Genotype | Predicted | Observed | Difference |
   |----------|-----------|----------|------------|
   | AA       | 0.36      | _____    | _____      |
   | Aa       | 0.48      | _____    | _____      |
   | aa       | 0.16      | _____    | _____      |

### Part D: Multiple Generations (Optional)

To see equilibrium across generations:

1. Use your 50 offspring to create a new gene pool:
   - AA individuals contribute 2 red beads each
   - Aa individuals contribute 1 red and 1 blue bead each
   - aa individuals contribute 2 blue beads each

2. Count total beads of each color
3. Calculate new allele frequencies
4. Compare to original frequencies (should be very similar!)
5. Repeat the mating process

## Questions for Reflection

### Basic Understanding

1. **How close were your observed frequencies to the predicted Hardy-Weinberg frequencies?**
   
   Expected answer: Should be reasonably close, with small differences due to sampling variation.

2. **Did your allele frequencies change from generation to generation?**
   
   Expected answer: No, they should remain approximately constant (around p=0.6, q=0.4).

3. **Why do we return the beads to the container after each draw?**
   
   Expected answer: To maintain constant allele frequencies and simulate an infinite population where each individual can potentially mate multiple times.

### Deeper Analysis

4. **If you started with different initial frequencies (e.g., p=0.8, q=0.2), would Hardy-Weinberg still work?**
   
   Expected answer: Yes! Hardy-Weinberg works for any starting frequencies as long as assumptions are met.

5. **What would happen if you didn't return the beads (sampling without replacement)?**
   
   Expected answer: Allele frequencies would change randomly - this simulates genetic drift in small populations.

6. **How does this simulation relate to real populations?**
   
   Expected answer: Real populations face the same mathematical principles, but may violate HW assumptions through selection, mutation, migration, or small population size.

## Connection to Real Biology

### Medical Application: Carrier Frequency

If this simulation represented a genetic disease where:
- A = normal allele (p = 0.6)
- a = disease allele (q = 0.4)
- Disease is recessive (only aa individuals affected)

**Calculate:**
1. What percentage of the population has the disease? 
   - aa frequency = q² = 0.16 = **16%**

2. What percentage are carriers (healthy but carry one disease allele)?
   - Aa frequency = 2pq = 0.48 = **48%**

3. In a population of 10,000, how many carriers would you expect?
   - 10,000 × 0.48 = **4,800 carriers**

### Conservation Application: Genetic Diversity

If these were Asiatic lions with:
- Allele frequencies p = 0.6, q = 0.4
- Expected heterozygosity (He) = 2pq = 0.48

This means 48% of individuals should be heterozygous, indicating moderate genetic diversity.

**Conservation question:** What if you observed only 30% heterozygosity instead of 48%?
- This suggests inbreeding (non-random mating)
- Calculate inbreeding coefficient: F = (He - Ho)/He = (0.48 - 0.30)/0.48 = 0.375
- This indicates significant inbreeding that threatens population viability!

## Extensions and Modifications

### Easy Modifications

1. **Different starting frequencies:** Try p = 0.2, 0.5, 0.8
2. **Larger sample size:** Use 100 offspring instead of 50
3. **Three allele system:** Add yellow beads for a third allele

### Advanced Modifications

1. **Selection simulation:** 
   - Remove some aa individuals before reproduction (selection against recessive)
   - Observe how frequencies change over generations

2. **Migration simulation:**
   - Add 10 beads from a "different population" each generation
   - See how gene flow affects frequencies

3. **Bottleneck simulation:**
   - Randomly select only 10 beads to found next generation
   - Experience genetic drift in small populations

## Common Student Questions

**Q: Why don't my results exactly match the predictions?**

A: Sampling variation! With 50 offspring, you'll see small random deviations. Try 500 offspring - results get closer to predictions with larger samples. This is the law of large numbers.

**Q: In real life, do populations really follow Hardy-Weinberg?**

A: Rarely perfectly, because real populations experience selection, mutation, migration, and finite size. But HW provides the null hypothesis - deviations tell us which evolutionary forces are acting!

**Q: Why is this important for medicine?**

A: It helps calculate carrier frequencies for genetic diseases, predict disease prevalence, and design genetic screening programs. Essential for genetic counseling!

## Data Recording Sheet

### Trial 1

| Offspring | Bead 1 Color | Bead 2 Color | Genotype |
|-----------|--------------|--------------|----------|
| 1         |              |              |          |
| 2         |              |              |          |
| ...       |              |              |          |
| 50        |              |              |          |

**Summary:**
- AA count: _____
- Aa count: _____
- aa count: _____

**Frequencies:**
- AA frequency: _____
- Aa frequency: _____
- aa frequency: _____

### Predicted vs Observed

| Genotype | Predicted (HW) | Observed | Difference |
|----------|----------------|----------|------------|
| AA       | 0.36           |          |            |
| Aa       | 0.48           |          |            |
| aa       | 0.16           |          |            |

## Assessment Rubric

| Criterion | Excellent (4) | Good (3) | Satisfactory (2) | Needs Work (1) |
|-----------|---------------|----------|------------------|----------------|
| Data Collection | All 50 trials recorded accurately | 45-49 trials accurate | 40-44 trials accurate | <40 accurate |
| Calculations | All frequencies calculated correctly | 1 minor error | 2 minor errors | Multiple errors |
| Analysis | Insightful comparison with HW predictions | Good comparison | Basic comparison | Limited analysis |
| Understanding | Clearly explains HW principle | Explains most concepts | Partial understanding | Confused |

## Additional Resources

- **Interactive Simulator:** Run this simulation digitally at [link to online tool]
- **Video Tutorial:** Watch the bead simulation in action [link]
- **Real Data:** Compare your results to actual population genetics data [link to datasets]

---

**Instructor Notes:**
- This activity typically takes 30-45 minutes
- Works best in groups of 2-3 students
- Can be adapted for online learning using virtual bead simulators
- Assessment: Focus on understanding principles rather than perfect numerical matches
