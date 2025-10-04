# Chapter 3: Exercises and Problems

## Problem Set 1: Hardy-Weinberg Equilibrium

### Problem 1.1: Basic Calculations
A population has the following genotype frequencies:
- AA: 360 individuals
- Aa: 480 individuals  
- aa: 160 individuals

**Tasks:**
1. Calculate the frequency of each genotype
2. Calculate the allele frequencies (p and q)
3. Calculate expected genotype frequencies under Hardy-Weinberg equilibrium
4. Is this population in Hardy-Weinberg equilibrium?

**Use the Hardy-Weinberg calculator:**
```bash
python code/python/hardy_weinberg_calculator.py --observed "AA:360,Aa:480,aa:160"
```

---

### Problem 1.2: Carrier Frequency
A recessive genetic disease affects 1 in 10,000 individuals in a population.

**Tasks:**
1. What is the frequency of the disease allele (q)?
2. What proportion of the population are carriers (heterozygotes)?
3. In a city of 1 million people, how many carriers would you expect?

**Hint:** If disease frequency (q²) = 0.0001, then q = √0.0001

---

### Problem 1.3: Blood Type Analysis
Using the `blood_types.csv` dataset:

**Tasks:**
1. Calculate ABO allele frequencies for Delhi population
2. Calculate expected blood type frequencies
3. Compare observed vs. expected using chi-square test
4. Is the Delhi population in Hardy-Weinberg equilibrium?

**Code template:**
```python
import pandas as pd
df = pd.read_csv('datasets/blood_types.csv')
# Your analysis here
```

---

## Problem Set 2: Population Simulation

### Problem 2.1: Genetic Drift in Small Populations
Simulate genetic drift in populations of different sizes.

**Tasks:**
1. Run simulation with N=50, p=0.5, 100 generations
2. Run simulation with N=1000, p=0.5, 100 generations  
3. Compare the variance in allele frequencies
4. Which population shows more genetic drift?

**Commands:**
```bash
python code/python/population_simulator.py --p 0.5 --pop_size 50 --generations 100 --plot
python code/python/population_simulator.py --p 0.5 --pop_size 1000 --generations 100 --plot
```

---

### Problem 2.2: Multiple Starting Frequencies
How does starting frequency affect drift?

**Tasks:**
1. Simulate populations with p₀ = 0.1, 0.5, 0.9
2. Use N=200, run for 200 generations
3. Which starting frequency is most stable?
4. Explain your observations

**Command:**
```bash
python code/python/population_simulator.py --p 0.1,0.5,0.9 --pop_size 200 --generations 200 --plot
```

---

### Problem 2.3: Loss of Genetic Diversity
The Asiatic lion population bottleneck reduced numbers to ~20 individuals around 1900.

**Tasks:**
1. Simulate this bottleneck: N=20, starting p=0.5
2. Run for 50 generations
3. Calculate probability of allele loss
4. What are conservation implications?

---

## Problem Set 3: Natural Selection

### Problem 3.1: Selection Against Recessive
A lethal recessive allele (aa individuals die before reproduction).

**Tasks:**
1. Model selection with s=1.0 (complete selection), h=0.0 (recessive)
2. Starting frequency p=0.5
3. How many generations until q < 0.01?
4. Why doesn't the allele disappear completely?

**Command:**
```bash
python code/python/selection_model.py --p 0.5 --selection 1.0 --dominance 0.0 --generations 100 --plot
```

---

### Problem 3.2: Heterozygote Advantage (Sickle Cell)
Sickle cell allele shows heterozygote advantage in malaria regions.

**Fitness values:**
- AA (normal): w=0.9 (susceptible to malaria)
- AS (carrier): w=1.0 (protected from malaria)
- SS (sickle cell): w=0.2 (severe anemia)

**Tasks:**
1. Model this selection scenario
2. Find the equilibrium frequency
3. Why does the harmful S allele persist?

**Command:**
```bash
python code/python/selection_model.py --wAA 0.9 --wAa 1.0 --waa 0.2 --p 0.1 --generations 200 --plot
```

---

### Problem 3.3: Comparing Selection Strengths
How does selection strength affect evolutionary rate?

**Tasks:**
1. Compare s = 0.01, 0.05, 0.1, 0.3, 0.5
2. All with h=0.0 (recessive), starting p=0.5
3. How long until p < 0.1 for each?
4. Plot all trajectories on one graph

**Command:**
```bash
python code/python/selection_model.py --p 0.5 --dominance 0.0 --compare 0.01,0.05,0.1,0.3,0.5 --generations 200
```

---

## Problem Set 4: Conservation Genetics

### Problem 4.1: Asiatic Lion Genetic Diversity
Using `lion_genetics.csv`:

**Tasks:**
1. Calculate average heterozygosity across all loci
2. Calculate average inbreeding coefficient (F)
3. Which loci show strongest inbreeding signal?
4. What does this mean for conservation?

**Analysis template:**
```python
import pandas as pd
df = pd.read_csv('datasets/lion_genetics.csv')

# Calculate metrics
avg_Ho = df['observed_heterozygosity'].mean()
avg_F = df['inbreeding_coefficient'].mean()

# Identify problematic loci
high_F = df[df['inbreeding_coefficient'] > 0.2]
```

---

### Problem 4.2: Minimum Viable Population
Estimate minimum viable population size to maintain genetic diversity.

**Tasks:**
1. Simulate populations of size N=25, 50, 100, 200
2. Run each for 100 generations
3. Calculate genetic diversity loss
4. What is minimum N to maintain >90% diversity?

---

### Problem 4.3: Genetic Rescue Design
Design a genetic rescue program for Asiatic lions.

**Scenario:** Introduce lions from African populations (different allele frequencies).

**Tasks:**
1. Current Gir population: N=675, p=0.3
2. Introduce 25 African lions with p=0.7
3. Calculate new allele frequencies
4. Predict heterozygosity gain

**Formula:** p_new = (N₁p₁ + N₂p₂)/(N₁ + N₂)

---

## Problem Set 5: Darwin's Finches

### Problem 5.1: Beak Size and Natural Selection
Using `finch_beaks.csv`:

**Tasks:**
1. Compare beak depth distributions across islands
2. Test if mean beak depth differs significantly
3. Calculate selection differential if large-beaked birds survive better
4. Predict evolutionary response

**Analysis hints:**
- Use t-tests to compare islands
- Selection differential: S = mean(survivors) - mean(population)
- Response to selection: R = h² × S

---

### Problem 5.2: Adaptive Radiation
How many finch species evolved from one ancestor?

**Tasks:**
1. Count distinct species in dataset
2. Calculate morphological divergence
3. Estimate selection strength needed
4. Compare to observed time since colonization

---

## Problem Set 6: Mendel's Experiments

### Problem 6.1: Chi-Square Test
Using `mendel_peas.csv`:

**Tasks:**
1. Test seed shape F2 ratio against expected 3:1
2. Test seed color F2 ratio against expected 3:1
3. Test plant height F2 ratio against expected 3:1
4. Are Mendel's results "too good to be true"? (all p > 0.05?)

**Analysis template:**
```python
from scipy.stats import chisquare
import pandas as pd

df = pd.read_csv('datasets/mendel_peas.csv')
f2_data = df[df['generation'] == 'F2']

# For seed shape
seed_shape = f2_data[f2_data['trait'] == 'Seed Shape']
observed = seed_shape['count'].values
expected = [sum(observed) * 0.75, sum(observed) * 0.25]

chi2, p = chisquare(observed, expected)
```

---

### Problem 6.2: Dihybrid Cross Prediction
If Mendel crossed RrYy × RrYy (round yellow × round yellow):

**Tasks:**
1. Predict the 9:3:3:1 ratio for F2 generation
2. For 556 offspring, calculate expected counts
3. Generate hypothetical data and test fit
4. What would deviation suggest?

---

## Problem Set 7: Integration Problems

### Problem 7.1: Evolution in Action
The peppered moth (Biston betularia) evolved dark coloration during industrial revolution.

**Scenario:**
- Initial frequency of dark allele: p = 0.01
- Industrial pollution favors dark moths
- Fitness: light moths w=0.7, dark moths w=1.0
- Assume dominance of dark allele (h=1.0)

**Tasks:**
1. Model selection over 50 generations
2. How long until dark moths are >90%?
3. What happens when pollution clears (reverse selection)?
4. Model return to light coloration

---

### Problem 7.2: Population Structure
Compare genetic diversity between:
- Large continuous population (N=10000)
- Fragmented populations (10 populations of N=100)

**Tasks:**
1. Simulate both scenarios for 100 generations
2. Compare heterozygosity loss
3. Calculate FST (population differentiation)
4. Which scenario better preserves diversity?

---

### Problem 7.3: Medical Genetics Application
Cystic fibrosis (CF) allele frequency in European populations: q ≈ 0.02

**Tasks:**
1. Calculate carrier frequency
2. Calculate probability both parents are carriers
3. Calculate risk for affected child if both carriers
4. Design genetic screening strategy

**Calculations:**
```python
q = 0.02  # CF allele frequency
p = 1 - q

# Carrier frequency (2pq)
carrier_freq = 2 * p * q

# Probability both parents are carriers
both_carriers = carrier_freq ** 2

# Risk of affected child (1/4 if both carriers)
risk = both_carriers * 0.25
```

---

## Challenge Problems

### Challenge 1: Evolutionary Rescue
An endangered species (N=100) faces environmental change.

**Current situation:**
- Allele A confers 20% advantage in new environment
- Current frequency: p = 0.1
- Extinction occurs if N < 50

**Tasks:**
1. Model population size AND allele frequency changes
2. Will population survive or go extinct?
3. What initial p is needed for rescue?
4. How does population size affect outcome?

---

### Challenge 2: Mutation-Selection Balance
Deleterious mutations arise at rate μ = 10⁻⁵ per generation.

**Tasks:**
1. Calculate equilibrium frequency under selection (s=0.01)
2. Formula: q_eq = √(μ/s) for recessive
3. Verify by simulation
4. How does dominance affect equilibrium?

---

### Challenge 3: Complex Selection
Model industrial melanism with:
- Multiple alleles (light, medium, dark)
- Environment-dependent fitness
- Migration between polluted and clean areas

**Tasks:**
1. Design multi-allele model
2. Implement frequency-dependent selection
3. Add migration parameter
4. Find equilibrium frequencies

---

## Computational Exercises

### Exercise 1: Optimize Parameter Estimation
Given observed genotype frequencies, find best-fit p value.

**Tasks:**
1. Write function to calculate HW chi-square for any p
2. Use optimization to find p that minimizes chi-square
3. Compare to direct calculation from data
4. Plot chi-square landscape

---

### Exercise 2: Stochastic Simulation
Implement Wright-Fisher model with random sampling.

**Tasks:**
1. Write simulator for finite population
2. Compare to deterministic model
3. Calculate fixation probabilities
4. Validate against theoretical predictions

---

### Exercise 3: Visualization Dashboard
Create interactive visualization tool.

**Features:**
- Sliders for p, s, h, N
- Real-time plot updates
- Multiple scenarios comparison
- Export results

**Tools:** Use plotly or bokeh for interactivity

---

## Data Analysis Projects

### Project 1: Real Population Analysis
Find real genetic data online (e.g., 1000 Genomes Project).

**Tasks:**
1. Download SNP data for one population
2. Calculate allele frequencies for 100 SNPs
3. Test HW equilibrium for each
4. Identify loci under selection

---

### Project 2: Meta-Analysis
Compare genetic diversity across multiple species.

**Tasks:**
1. Compile data for 10 endangered species
2. Calculate heterozygosity for each
3. Correlate with population size
4. Identify conservation priorities

---

### Project 3: Historical DNA Analysis
Ancient DNA reveals past genetic diversity.

**Tasks:**
1. Find ancient DNA study (e.g., mammoths, Neanderthals)
2. Compare past vs. present diversity
3. Quantify genetic diversity loss
4. Model demographic history

---

## Submission Guidelines

For each problem, submit:
1. **Code:** Well-commented Python scripts
2. **Results:** Output tables and figures
3. **Interpretation:** Biological meaning (2-3 paragraphs)
4. **Conclusions:** Key findings and implications

**Format:**
```
problem_1_1_yourname.py
problem_1_1_results.csv
problem_1_1_plot.png
problem_1_1_interpretation.md
```

---

## Assessment Rubric

| Criterion | Excellent (4) | Good (3) | Satisfactory (2) | Needs Work (1) |
|-----------|---------------|----------|------------------|----------------|
| **Accuracy** | All calculations correct | 1-2 minor errors | 3-4 errors | Multiple errors |
| **Code Quality** | Clean, well-documented | Mostly clear | Basic functionality | Poor structure |
| **Interpretation** | Deep biological insight | Good understanding | Basic explanation | Misses key points |
| **Visualization** | Publication-quality plots | Clear figures | Basic plots | Unclear/missing |

---

## Hints and Tips

### General Tips
1. Always check allele frequencies sum to 1.0
2. Verify genotype frequencies sum to 1.0
3. Use large sample sizes for stable estimates
4. Compare results to theoretical predictions

### Debugging Common Errors
- **"AlleleFrequencyError"**: Check 0 ≤ p ≤ 1
- **Chi-square warning**: Need expected counts ≥ 5
- **Plotting issues**: Check data dimensions match

### Computational Efficiency
- Vectorize operations with numpy
- Use pandas for data manipulation
- Cache expensive calculations
- Profile code to find bottlenecks

---

## Additional Resources

### Online Tools
- [Hardy-Weinberg Calculator](https://www.example.com)
- [Population Genetics Simulator](https://www.example.com)
- [Chi-Square Calculator](https://www.example.com)

### Datasets
- 1000 Genomes Project: https://www.internationalgenome.org/
- ALFRED (Allele Frequency Database): https://alfred.med.yale.edu/
- AnAge Database: https://genomics.senescence.info/species/

### Further Reading
- Hartl & Clark (2007). *Principles of Population Genetics*
- Hedrick (2011). *Genetics of Populations*
- Futuyma & Kirkpatrick (2017). *Evolution*

---

## Questions and Support

- **GitHub Issues**: Post questions as issues
- **Discussion Forum**: https://github.com/yourusername/discussions
- **Office Hours**: See syllabus for times
- **Email**: instructor@example.com

Good luck with the exercises! Remember: understanding concepts matters more than getting perfect numerical answers. Focus on biological interpretation! 🧬
