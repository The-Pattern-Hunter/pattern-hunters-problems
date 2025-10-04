# Chapter 3 Datasets

## Overview

This directory contains datasets for Hardy-Weinberg equilibrium analysis, population genetics exercises, and evolutionary studies.

## Files

### 1. blood_types.csv
**Description:** ABO blood group frequencies across Indian populations

**Columns:**
- `region`: Geographic region (North, South, East, West, Central India)
- `city`: Specific city sampled
- `blood_type`: A, B, AB, or O
- `count`: Number of individuals with this blood type
- `sample_size`: Total individuals sampled

**Use cases:**
- Calculate ABO allele frequencies (p, q, r)
- Test Hardy-Weinberg equilibrium
- Compare genetic structure across populations

**Example:**
```python
import pandas as pd
df = pd.read_csv('blood_types.csv')
delhi_data = df[df['city'] == 'Delhi']
```

### 2. finch_beaks.csv
**Description:** Beak measurements from Darwin's Galápagos finches

**Columns:**
- `island`: Galápagos island where collected
- `species`: Finch species name
- `beak_depth_mm`: Beak depth in millimeters
- `beak_length_mm`: Beak length in millimeters
- `body_mass_g`: Body mass in grams
- `year_collected`: Year of collection

**Use cases:**
- Analyze natural selection on beak morphology
- Compare trait variation across islands
- Study adaptive radiation

**Example:**
```python
df = pd.read_csv('finch_beaks.csv')
isabela_finches = df[df['island'] == 'Isabela']
```

### 3. mendel_peas.csv
**Description:** Mendel's original pea plant inheritance data

**Columns:**
- `trait`: Trait studied (Seed Shape, Seed Color, Plant Height)
- `parent_cross`: Parental genotypes
- `generation`: F1 or F2
- `phenotype`: Observed phenotype
- `count`: Number of individuals
- `expected_ratio`: Theoretical Mendelian ratio

**Use cases:**
- Chi-square test for Mendelian ratios
- Understand inheritance patterns
- Practice goodness-of-fit tests

**Example:**
```python
df = pd.read_csv('mendel_peas.csv')
seed_shape = df[df['trait'] == 'Seed Shape']
```

### 4. lion_genetics.csv
**Description:** Genetic diversity in Asiatic lion populations

**Columns:**
- `population`: Population name (Gir Forest)
- `locus`: Genetic marker identifier
- `AA`, `Aa`, `aa`: Genotype counts
- `total`: Total individuals sampled
- `year`: Year of sampling
- `observed_heterozygosity`: Proportion of heterozygotes
- `expected_heterozygosity`: Expected under HW equilibrium
- `inbreeding_coefficient`: F statistic (He-Ho)/He

**Use cases:**
- Conservation genetics analysis
- Inbreeding assessment
- Hardy-Weinberg equilibrium testing
- Genetic diversity evaluation

**Example:**
```python
df = pd.read_csv('lion_genetics.csv')
avg_heterozygosity = df['observed_heterozygosity'].mean()
```

## Quick Analysis Examples

### Calculate Allele Frequencies from Blood Type Data

```python
import pandas as pd
import numpy as np

df = pd.read_csv('blood_types.csv')

# Get Delhi data
delhi = df[df['city'] == 'Delhi']

# Extract counts
A = delhi[delhi['blood_type'] == 'A']['count'].values[0]
B = delhi[delhi['blood_type'] == 'B']['count'].values[0]
AB = delhi[delhi['blood_type'] == 'AB']['count'].values[0]
O = delhi[delhi['blood_type'] == 'O']['count'].values[0]
N = A + B + AB + O

# Calculate allele frequencies (maximum likelihood)
r = np.sqrt(O / N)  # freq of O allele
p = 1 - np.sqrt((B + O) / N)  # freq of A allele
q = 1 - p - r  # freq of B allele

print(f"Allele frequencies in Delhi:")
print(f"  p (A) = {p:.3f}")
print(f"  q (B) = {q:.3f}")
print(f"  r (O) = {r:.3f}")
```

### Test Hardy-Weinberg Equilibrium

```python
from scipy.stats import chisquare

df = pd.read_csv('lion_genetics.csv')

# Select one locus
locus_data = df[df['locus'] == 'MHC-DRB1']

# Observed counts
obs_AA = locus_data['AA'].values[0]
obs_Aa = locus_data['Aa'].values[0]
obs_aa = locus_data['aa'].values[0]
total = locus_data['total'].values[0]

# Calculate allele frequencies
p = (2*obs_AA + obs_Aa) / (2*total)
q = 1 - p

# Expected counts under HW
exp_AA = p**2 * total
exp_Aa = 2*p*q * total
exp_aa = q**2 * total

# Chi-square test
chi2, pval = chisquare([obs_AA, obs_Aa, obs_aa], 
                       [exp_AA, exp_Aa, exp_aa], 
                       ddof=1)

print(f"Chi-square test for {locus_data['locus'].values[0]}:")
print(f"  χ² = {chi2:.3f}")
print(f"  p-value = {pval:.4f}")
if pval < 0.05:
    print("  Reject HW equilibrium")
else:
    print("  Accept HW equilibrium")
```

### Analyze Natural Selection in Finches

```python
import matplotlib.pyplot as plt

df = pd.read_csv('finch_beaks.csv')

# Compare beak depths across islands for one species
species_data = df[df['species'] == 'Ground Finch (Large)']

islands = species_data['island'].unique()
for island in islands:
    island_data = species_data[species_data['island'] == island]
    plt.hist(island_data['beak_depth_mm'], alpha=0.5, label=island)

plt.xlabel('Beak Depth (mm)')
plt.ylabel('Frequency')
plt.title('Beak Depth Distribution Across Islands')
plt.legend()
plt.show()
```

## Data Sources

- **blood_types.csv**: Synthesized from multiple Indian population genetics studies
- **finch_beaks.csv**: Based on Grant & Grant long-term finch studies (1973-2020)
- **mendel_peas.csv**: Mendel's original 1866 published data
- **lion_genetics.csv**: Simulated based on published Asiatic lion genetic studies

## Citation

If using these datasets in publications:

```
Chapter 3 datasets from "Mathematical Biology: Pattern Hunting from Darwin to DNA"
Available at: https://github.com/yourusername/chapter3-darwin-to-dna
```

## Data Quality Notes

- All datasets have been quality-checked for consistency
- Missing values are minimal and documented
- Sample sizes are sufficient for statistical analysis
- Data represents realistic biological variation

## License

All datasets provided under CC BY-SA 4.0 license for educational use.
