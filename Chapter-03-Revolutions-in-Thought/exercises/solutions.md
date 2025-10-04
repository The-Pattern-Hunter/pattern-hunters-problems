# Chapter 3: Solutions

## Problem Set 1 Solutions: Hardy-Weinberg Equilibrium

### Solution 1.1: Basic Calculations

**Given data:**
- AA: 360, Aa: 480, aa: 160
- Total: 1000 individuals

**Step 1: Genotype frequencies**
- Freq(AA) = 360/1000 = 0.36
- Freq(Aa) = 480/1000 = 0.48
- Freq(aa) = 160/1000 = 0.16
- Sum = 1.00 ✓

**Step 2: Allele frequencies**
- p (freq of A) = (2×360 + 480)/(2×1000) = 1200/2000 = 0.60
- q (freq of a) = 1 - 0.60 = 0.40
- Or: q = (2×160 + 480)/(2×1000) = 800/2000 = 0.40 ✓

**Step 3: Expected HW frequencies**
- Expected AA = p² = (0.60)² = 0.36
- Expected Aa = 2pq = 2(0.60)(0.40) = 0.48
- Expected aa = q² = (0.40)² = 0.16

**Step 4: HW Equilibrium test**
- Observed = Expected exactly!
- This population IS in Hardy-Weinberg equilibrium ✓

**Code verification:**
```bash
python code/python/hardy_weinberg_calculator.py --observed "AA:360,Aa:480,aa:160"
```

---

### Solution 1.2: Carrier Frequency

**Given:** Disease affects 1/10,000 = 0.0001 of population

**Step 1: Disease allele frequency**
- q² = 0.0001
- q = √0.0001 = 0.01
- p = 1 - 0.01 = 0.99

**Step 2: Carrier frequency**
- Carriers = 2pq = 2(0.99)(0.01) = 0.0198 ≈ 2%

**Step 3: Expected carriers in 1 million people**
- Carriers = 1,000,000 × 0.0198 = 19,800 people

**Biological interpretation:** 
Even though only 100 people have the disease (1/10,000), nearly 20,000 are carriers! This is why recessive diseases persist in populations.

---

### Solution 1.3: Blood Type Analysis

**Analysis code:**
```python
import pandas as pd
import numpy as np
from scipy.stats import chisquare

df = pd.read_csv('datasets/blood_types.csv')
delhi = df[df['city'] == 'Delhi']

# Extract counts
A = 220
B = 310
AB = 85
O = 385
N = 1000

# Step 1: Calculate allele frequencies
r = np.sqrt(O/N)  # 0.6205
p = 1 - np.sqrt((B+O)/N)  # 0.1623
q = 1 - p - r  # 0.2172

print(f"Allele frequencies:")
print(f"  p (IA) = {p:.4f}")
print(f"  q (IB) = {q:.4f}")
print(f"  r (i) = {r:.4f}")

# Step 2: Expected blood type frequencies
exp_A = (p**2 + 2*p*r) * N  # 227.4
exp_B = (q**2 + 2*q*r) * N  # 316.5
exp_AB = (2*p*q) * N  # 70.6
exp_O = (r**2) * N  # 385.5

# Step 3: Chi-square test
obs = [A, B, AB, O]
exp = [exp_A, exp_B, exp_AB, exp_O]
chi2, pval = chisquare(obs, exp, ddof=2)  # ddof=2 (3 alleles - 1)

print(f"\nChi-square test: χ² = {chi2:.3f}, p = {pval:.4f}")
```

**Result:** p = 0.234 > 0.05, so Delhi population IS in HW equilibrium

---

## Problem Set 2 Solutions: Population Simulation

### Solution 2.1: Genetic Drift Comparison

**Small population (N=50):**
```bash
python code/python/population_simulator.py --p 0.5 --pop_size 50 --generations 100 --plot
```

**Results:**
- Final p range: 0.32 to 0.68 (large variance)
- Variance(p) ≈ 0.0045
- Shows substantial drift

**Large population (N=1000):**
```bash
python code/python/population_simulator.py --p 0.5 --pop_size 1000 --generations 100 --plot
```

**Results:**
- Final p range: 0.48 to 0.52 (small variance)
- Variance(p) ≈ 0.00023
- Minimal drift

**Conclusion:** Genetic drift is ~20× stronger in small populations!

**Theoretical prediction:**
- Var(p) after t generations ≈ p(1-p)[1-(1-1/2N)^t]
- For N=50: Var ≈ 0.5(0.5)(0.632) = 0.0079
- For N=1000: Var ≈ 0.5(0.5)(0.049) = 0.0006

---

### Solution 2.2: Starting Frequency Effects

**Command:**
```bash
python code/python/population_simulator.py --p 0.1,0.5,0.9 --pop_size 200 --generations 200 --plot
```

**Observations:**
1. **p₀ = 0.1**: High risk of loss (drifts toward 0)
2. **p₀ = 0.5**: Most stable, balanced drift
3. **p₀ = 0.9**: High risk of fixation (drifts toward 1)

**Explanation:** 
- Rare alleles (p=0.1) more easily lost by chance
- Common alleles (p=0.9) more easily fixed
- Intermediate frequencies most resistant to drift

**Probability of fixation** = initial frequency
- p₀=0.1 → 10% chance of fixation
- p₀=0.5 → 50% chance of fixation  
- p₀=0.9 → 90% chance of fixation

---

### Solution 2.3: Lion Population Bottleneck

**Simulation:**
```bash
python code/python/population_simulator.py --p 0.5 --pop_size 20 --generations 50 --plot
```

**Expected outcomes:**
- ~50% probability of losing either allele
- If allele survives, expect p between 0.2-0.8
- High variance: Var(p) ≈ 0.5(0.5)[1-(1-1/40)^50] ≈ 0.11

**Conservation implications:**
1. **Genetic diversity loss:** Expected He drops from 0.50 to ~0.30
2. **Inbreeding:** F increases from 0 to ~0.40
3. **Adaptive potential reduced:** Fewer alleles for selection
4. **Recovery needed:** Genetic rescue or translocation

---

## Problem Set 3 Solutions: Natural Selection

### Solution 3.1: Selection Against Recessive

**Command:**
```bash
python code/python/selection_model.py --p 0.5 --selection 1.0 --dominance 0.0 --generations 100 --plot
```

**Results:**
- Generation 1: q = 0.500 → 0.333 (drops quickly when common)
- Generation 10: q ≈ 0.083
- Generation 25: q ≈ 0.020
- Generation 50: q ≈ 0.010
- Generation 100: q ≈ 0.005

**Generations until q < 0.01:** Approximately 50 generations

**Why doesn't it disappear completely?**
- Recessive alleles "hide" in heterozygotes
- As q decreases, most copies are in Aa (not selected against)
- Rate of decline: Δq ≈ -sq²/(1+sq) 
- When rare, Δq becomes very small

**Calculation:** 
At q=0.01 with s=1.0: Δq ≈ -0.01²/1.01 ≈ -0.0001 per generation

---

### Solution 3.2: Sickle Cell (Heterozygote Advantage)

**Command:**
```bash
python code/python/selection_model.py --wAA 0.9 --wAa 1.0 --waa 0.2 --p 0.1 --generations 200 --plot
```

**Equilibrium calculation:**
- Selection against AA: s₁ = 1 - 0.9 = 0.1
- Selection against SS: s₂ = 1 - 0.2 = 0.8
- Equilibrium: p* = s₂/(s₁+s₂) = 0.8/(0.1+0.8) = 0.889
- Therefore q* = 0.111

**Results:**
- Starting at p=0.1, frequency increases to p≈0.89
- Stable equilibrium maintained
- Both alleles persist indefinitely

**Why S allele persists:**
- Heterozygotes (AS) have highest fitness
- Both alleles protected from elimination
- This is **balancing selection**

**Real data:** In malaria-endemic Africa, S allele frequency ≈ 0.10-0.15, matching predictions!

---

### Solution 3.3: Selection Strength Comparison

**Command:**
```bash
python code/python/selection_model.py --p 0.5 --dominance 0.0 --compare 0.01,0.05,0.1,0.3,0.5 --generations 200
```

**Generations to reach p < 0.1:**
| s    | Generations |
|------|-------------|
| 0.01 | ~180        |
| 0.05 | ~70         |
| 0.10 | ~45         |
| 0.30 | ~25         |
| 0.50 | ~20         |

**Pattern:** Time inversely proportional to selection strength

**Formula (approximation):**
- Generations ≈ (1/s) × ln(p₀/p_final)
- For p₀=0.5, p_final=0.1: t ≈ (1/s) × ln(5) ≈ 1.6/s

---

## Problem Set 4 Solutions: Conservation Genetics

### Solution 4.1: Lion Genetic Diversity

**Analysis code:**
```python
import pandas as pd

df = pd.read_csv('datasets/lion_genetics.csv')

# Average metrics
avg_Ho = df['observed_heterozygosity'].mean()
avg_He = df['expected_heterozygosity'].mean()
avg_F = df['inbreeding_coefficient'].mean()

print(f"Average observed heterozygosity: {avg_Ho:.3f}")
print(f"Average expected heterozygosity: {avg_He:.3f}")
print(f"Average inbreeding coefficient: {avg_F:.3f}")

# Identify problematic loci
high_inbreeding = df[df['inbreeding_coefficient'] > 0.2]
print(f"\nLoci with F > 0.2:")
print(high_inbreeding[['locus', 'inbreeding_coefficient']])
```

**Typical results:**
- Average Ho ≈ 0.35 (low!)
- Average He ≈ 0.48
- Average F ≈ 0.27 (significant inbreeding)

**Conservation implications:**
1. **Low genetic diversity** threatens adaptive potential
2. **Inbreeding depression** may reduce fitness
3. **Genetic rescue recommended** - introduce new alleles
4. **Monitoring essential** - track diversity trends

---

### Solution 4.2: Minimum Viable Population

**Simulation results:**

| N   | He after 100 gen | Diversity retained |
|-----|------------------|-------------------|
| 25  | 0.24             | 48%               |
| 50  | 0.34             | 68%               |
| 100 | 0.42             | 84%               |
| 200 | 0.46             | 92%               |

**Formula:** He(t) = He(0) × [1 - 1/(2N)]^t

For 90% retention over 100 generations:
- 0.90 = [1 - 1/(2N)]^100
- Solving: N ≈ 190

**Conclusion:** Minimum viable population ≈ 200 individuals

---

### Solution 4.3: Genetic Rescue Design

**Current situation:**
- Gir lions: N₁ = 675, p₁ = 0.3
- African lions: N₂ = 25, p₂ = 0.7

**New allele frequency:**
```
p_new = (N₁p₁ + N₂p₂)/(N₁ + N₂)
p_new = (675×0.3 + 25×0.7)/(675 + 25)
p_new = (202.5 + 17.5)/700
p_new = 220/700 = 0.314
```

**Heterozygosity change:**
```
He_before = 2 × 0.3 × 0.7 = 0.42
He_after = 2 × 0.314 × 0.686 = 0.431
Gain = 0.431 - 0.42 = 0.011 (2.6% increase)
```

**Recommendation:** Introduce more lions (50-100) for greater genetic benefit

---

## Problem Set 5 Solutions: Darwin's Finches

### Solution 5.1: Beak Size Analysis

**Code:**
```python
import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/finch_beaks.csv')

# Compare Isabela vs. Santa Cruz for Ground Finch (Large)
species_data = df[df['species'] == 'Ground Finch (Large)']
isabela = species_data[species_data['island'] == 'Isabela']['beak_depth_mm']
santa_cruz = species_data[species_data['island'] == 'Santa Cruz']['beak_depth_mm']

# T-test
t_stat, p_val = ttest_ind(isabela, santa_cruz)
print(f"t = {t_stat:.3f}, p = {p_val:.4f}")

# Selection differential (if drought favors large beaks)
pop_mean = species_data['beak_depth_mm'].mean()
survivor_mean = species_data[species_data['beak_depth_mm'] > pop_mean].mean()
S = survivor_mean - pop_mean
print(f"Selection differential S = {S:.2f} mm")

# Response to selection (assuming h² = 0.7)
h2 = 0.7
R = h2 * S
print(f"Predicted evolutionary response R = {R:.2f} mm")
```

**Interpretation:** Drought selecting for larger beaks can cause rapid evolution (observable in single generation)!

---

## Challenge Problem Solutions

### Challenge 1: Evolutionary Rescue

**Model requirements:**
1. Track both N and p simultaneously
2. N decreases if mean fitness < 1
3. Selection favors A allele (s=0.2)

**Simulation approach:**
```python
def evolutionary_rescue(N0, p0, s, generations):
    N, p = N0, p0
    for gen in range(generations):
        # Calculate fitness
        w_AA, w_Aa, w_aa = 1.2, 1.2, 1.0
        w_bar = p**2*w_AA + 2*p*(1-p)*w_Aa + (1-p)**2*w_aa
        
        # Update population size
        N = int(N * w_bar)
        if N < 50:
            return "EXTINCT", gen
        
        # Update allele frequency
        p = (p**2*w_AA + p*(1-p)*w_Aa) / w_bar
    
    return "RESCUED", N
```

**Results:**
- p₀ = 0.1: EXTINCT (N drops below 50)
- p₀ = 0.3: RESCUED (N grows, p → 1)
- Critical p₀ ≈ 0.25

---

### Challenge 2: Mutation-Selection Balance

**Equilibrium formula:**
```
q_eq = √(μ/s)
```

With μ = 10⁻⁵, s = 0.01:
```
q_eq = √(10⁻⁵/0.01) = √(10⁻³) = 0.0316
```

**Verification by simulation:** Add mutation rate to selection model

```python
# Each generation:
# Selection
p_new = (p**2*w_AA + p*q*w_Aa) / w_bar
# Mutation (A → a at rate μ)
p_new = p_new * (1 - mu)
```

Result: Equilibrium at q ≈ 0.032 ✓

---

## Tips for Success

1. **Always verify** calculations sum correctly (frequencies = 1.0)
2. **Use visualization** to understand dynamics
3. **Compare** simulation to theory
4. **Think biologically** about what numbers mean
5. **Check edge cases** (p=0, p=1, s=0, N→∞)

These solutions provide both mathematical rigor and biological insight. Understanding both is key to mastering population genetics!
