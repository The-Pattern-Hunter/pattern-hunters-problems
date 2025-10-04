# Chapter 3: Revolutions in Thought - Darwin to DNA

## 📚 Overview

This repository contains all code, data, and interactive exercises for **Chapter 3: Revolutions in Thought - Darwin to DNA** from the mathematical biology textbook. This chapter explores how mathematical thinking revolutionized our understanding of evolution and genetics.

## 🎯 Learning Objectives

By working through these materials, you will be able to:

- Explain how Darwin's voyage observations led to evolutionary theory
- Describe Mendel's experimental approach and why it was revolutionary
- Connect Hardy-Weinberg equilibrium to real population genetics
- Analyze how Fisher and Wright unified genetics with evolution
- Evaluate Kimura's neutral theory contribution to evolutionary thinking
- Calculate expected genotype frequencies using Hardy-Weinberg
- Determine equilibrium points in selection models
- Apply Fisher's fundamental theorem to predict evolutionary responses
- Use Wright's F-statistics to analyze population structure
- Distinguish neutral from adaptive molecular evolution

## 📂 Repository Structure

```
chapter3-darwin-to-dna/
├── README.md                          # This file
├── data/                              # Datasets for exercises
│   ├── galapagos_finches.csv         # Darwin's finch beak measurements
│   ├── mendel_pea_plants.csv         # Mendel's original pea plant data
│   ├── blood_type_frequencies.csv    # ABO blood group data
│   ├── tiger_genetics.csv            # Asiatic lion genetic diversity data
│   └── molecular_evolution.csv       # Protein sequence evolution rates
├── notebooks/                         # Jupyter notebooks
│   ├── 01_darwin_finches_analysis.ipynb
│   ├── 02_mendel_ratios.ipynb
│   ├── 03_hardy_weinberg_equilibrium.ipynb
│   ├── 04_fisher_wright_models.ipynb
│   └── 05_neutral_theory.ipynb
├── scripts/                           # Python/R scripts
│   ├── hardy_weinberg_calculator.py
│   ├── selection_simulator.py
│   ├── drift_vs_selection.py
│   └── f_statistics.R
├── exercises/                         # Interactive exercises
│   ├── exercise_1_bead_simulation.md
│   ├── exercise_2_hardy_weinberg_practice.md
│   ├── exercise_3_selection_models.md
│   └── solutions/
├── visualizations/                    # Generated plots and figures
└── tests/                            # Unit tests for code

```

## 🚀 Getting Started

### Prerequisites

**Python Environment:**
```bash
python >= 3.8
numpy >= 1.20
pandas >= 1.3
matplotlib >= 3.4
scipy >= 1.7
jupyter >= 1.0
```

**R Environment (optional):**
```R
R >= 4.0
tidyverse
ggplot2
```

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/mathematical-biology-chapter3.git
cd mathematical-biology-chapter3
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Launch Jupyter:
```bash
jupyter notebook
```

## 📊 Key Datasets

### 1. Galápagos Finches Data
- **File:** `data/galapagos_finches.csv`
- **Description:** Beak measurements from Darwin's finch species
- **Columns:** species, island, beak_depth, beak_length, body_mass
- **Source:** Based on historical measurements and modern studies

### 2. Mendel's Pea Plants
- **File:** `data/mendel_pea_plants.csv`
- **Description:** Original counts from Mendel's pea plant experiments
- **Columns:** trait, parent_cross, offspring_count, phenotype
- **Source:** Mendel (1866)

### 3. Blood Type Frequencies
- **File:** `data/blood_type_frequencies.csv`
- **Description:** ABO blood group frequencies across Indian populations
- **Columns:** population, region, A, B, AB, O, sample_size
- **Use:** Hardy-Weinberg equilibrium calculations

## 💻 Interactive Exercises

### Exercise 1: Hardy-Weinberg Bead Simulation

Simulate genetic inheritance using a simple bead model to understand how allele frequencies remain constant under random mating.

**Run the simulation:**
```python
python scripts/hardy_weinberg_calculator.py --p 0.6 --population_size 1000
```

**Learning outcomes:**
- Understand random mating and genetic equilibrium
- Calculate expected genotype frequencies
- Compare theoretical predictions with simulation results

### Exercise 2: Selection vs. Drift

Explore how natural selection and genetic drift shape allele frequencies in populations of different sizes.

**Interactive notebook:**
```bash
jupyter notebook notebooks/04_fisher_wright_models.ipynb
```

**Parameters to explore:**
- Selection coefficient (s)
- Population size (N)
- Initial allele frequency (p₀)

### Exercise 3: Neutral Theory Analysis

Analyze protein sequence evolution to distinguish neutral mutations from adaptive changes.

**Analysis script:**
```python
python scripts/drift_vs_selection.py --input data/molecular_evolution.csv
```

## 📈 Key Calculations

### Hardy-Weinberg Equilibrium

For a gene with two alleles (A and a):
- Allele frequencies: p (A) + q (a) = 1
- Genotype frequencies: p² (AA) + 2pq (Aa) + q² (aa) = 1

**Example calculation:**
```python
from scripts.hardy_weinberg_calculator import calculate_genotype_frequencies

p = 0.6  # Frequency of A allele
genotypes = calculate_genotype_frequencies(p)
print(f"AA: {genotypes['AA']:.3f}")  # 0.360
print(f"Aa: {genotypes['Aa']:.3f}")  # 0.480
print(f"aa: {genotypes['aa']:.3f}")  # 0.160
```

### Fisher's Fundamental Theorem

Rate of increase in fitness = Genetic variance in fitness

**Simulation:**
```python
python scripts/selection_simulator.py --generations 100 --variance 0.05
```

## 🔬 Case Studies

### 1. Sickle Cell and Malaria (Balancing Selection)

Analyze why harmful sickle cell alleles persist in malaria-endemic regions.

**Notebook:** `notebooks/03_hardy_weinberg_equilibrium.ipynb`

### 2. Asiatic Lion Conservation Genetics

Apply population genetics to conservation of endangered Asiatic lions.

**Data:** `data/tiger_genetics.csv`

### 3. Molecular Clock Analysis

Estimate evolutionary divergence times using neutral theory.

**Script:** `scripts/drift_vs_selection.py`

## 📚 Additional Resources

### Textbook Sections
- Section 3.1: Darwin's Voyage and Natural Selection
- Section 3.2: Mendel's Laws of Inheritance
- Section 3.3: Hardy-Weinberg Equilibrium
- Section 3.4: Fisher and Wright's Mathematical Synthesis
- Section 3.5: Kimura's Neutral Theory

### External Links
- [Hardy-Weinberg Calculator (Online)](https://www.example.com/hw-calc)
- [Evolution Simulator](https://www.example.com/evolution-sim)
- [Population Genetics Primer](https://www.example.com/popgen)

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### How to contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-exercise`)
3. Commit your changes (`git commit -m 'Add new selection exercise'`)
4. Push to the branch (`git push origin feature/new-exercise`)
5. Open a Pull Request

## 📝 Citation

If you use these materials in your research or teaching, please cite:

```bibtex
@book{mathematical_biology_2025,
  author = {Your Name},
  title = {Mathematical Biology: Pattern Hunting from Darwin to DNA},
  year = {2025},
  publisher = {Cambridge University Press},
  chapter = {3},
  pages = {XX-XX}
}
```

## 📄 License

This educational material is licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).

Code is licensed under MIT License - see [LICENSE](LICENSE) file for details.

## 🐛 Issues and Support

- **Bug reports:** [Open an issue](https://github.com/yourusername/repo/issues)
- **Questions:** Use [Discussions](https://github.com/yourusername/repo/discussions)
- **Email:** support@example.com

## 🙏 Acknowledgments

- Charles Darwin for the original finch observations
- Gregor Mendel for experimental genetics
- G.H. Hardy and Wilhelm Weinberg for population genetics theory
- R.A. Fisher and Sewall Wright for the modern synthesis
- Motoo Kimura for neutral theory

## 📅 Version History

- **v1.0.0** (2025-01-15): Initial release
- **v1.1.0** (2025-02-01): Added molecular evolution exercises
- **v1.2.0** (2025-03-15): Interactive visualizations added

---

**Happy Learning! 🧬**

For questions or feedback, please open an issue or contact the maintainers.
