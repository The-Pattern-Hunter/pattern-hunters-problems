# Python Code for Chapter 3

## Scripts Overview

### 1. hardy_weinberg_calculator.py
Calculate Hardy-Weinberg equilibrium frequencies and test for deviations.

**Usage:**
```bash
python hardy_weinberg_calculator.py --p 0.6
python hardy_weinberg_calculator.py --p 0.6 --observed "AA:360,Aa:480,aa:160"
2. population_simulator.py
Simulate random mating across multiple generations.
python population_simulator.py --p 0.6 --generations 20 --pop_size 1000
3. selection_model.py
Model natural selection effects on allele frequencies.
python selection_model.py --p 0.5 --selection 0.3 --generations 100
pip install -r requirements.txt
Requirements

numpy >= 1.20.0
pandas >= 1.3.0
matplotlib >= 3.4.0
scipy >= 1.7.0
