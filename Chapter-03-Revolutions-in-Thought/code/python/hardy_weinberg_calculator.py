"""
Hardy-Weinberg Equilibrium Calculator
Chapter 3: Revolutions in Thought - Darwin to DNA

This script calculates genotype frequencies under Hardy-Weinberg equilibrium
and tests whether observed data fits expected equilibrium proportions.

Usage:
    python hardy_weinberg_calculator.py --p 0.6 --population_size 1000
    python hardy_weinberg_calculator.py --observed AA:360,Aa:480,aa:160
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chisquare
import argparse


class HardyWeinbergCalculator:
    """Class for Hardy-Weinberg equilibrium calculations and simulations."""
    
    def __init__(self, p=None, q=None):
        """
        Initialize with allele frequencies.
        
        Parameters:
        -----------
        p : float
            Frequency of dominant allele (A)
        q : float
            Frequency of recessive allele (a)
        """
        if p is not None and q is not None:
            if not np.isclose(p + q, 1.0):
                raise ValueError("Allele frequencies must sum to 1")
            self.p = p
            self.q = q
        elif p is not None:
            self.p = p
            self.q = 1 - p
        elif q is not None:
            self.q = q
            self.p = 1 - q
        else:
            raise ValueError("Must provide at least one allele frequency")
    
    def calculate_genotype_frequencies(self):
        """
        Calculate expected genotype frequencies under HW equilibrium.
        
        Returns:
        --------
        dict : Genotype frequencies {AA, Aa, aa}
        """
        return {
            'AA': self.p ** 2,
            'Aa': 2 * self.p * self.q,
            'aa': self.q ** 2
        }
    
    def calculate_expected_counts(self, population_size):
        """
        Calculate expected genotype counts for a given population size.
        
        Parameters:
        -----------
        population_size : int
            Total number of individuals
            
        Returns:
        --------
        dict : Expected counts for each genotype
        """
        freqs = self.calculate_genotype_frequencies()
        return {
            genotype: freq * population_size 
            for genotype, freq in freqs.items()
        }
    
    def simulate_population(self, population_size, generations=1):
        """
        Simulate random mating under HW conditions.
        
        Parameters:
        -----------
        population_size : int
            Number of individuals
        generations : int
            Number of generations to simulate
            
        Returns:
        --------
        pd.DataFrame : Genotype counts across generations
        """
        results = []
        
        for gen in range(generations):
            # Create gamete pool based on allele frequencies
            gametes = np.random.choice(['A', 'a'], 
                                      size=population_size * 2,
                                      p=[self.p, self.q])
            
            # Random fertilization
            offspring = []
            for i in range(0, len(gametes), 2):
                genotype = ''.join(sorted([gametes[i], gametes[i+1]]))
                offspring.append(genotype)
            
            # Count genotypes
            counts = pd.Series(offspring).value_counts()
            results.append({
                'generation': gen + 1,
                'AA': counts.get('AA', 0),
                'Aa': counts.get('Aa', 0),
                'aa': counts.get('aa', 0)
            })
        
        return pd.DataFrame(results)
    
    @staticmethod
    def allele_frequencies_from_genotypes(AA, Aa, aa):
        """
        Calculate allele frequencies from genotype counts.
        
        Parameters:
        -----------
        AA, Aa, aa : int
            Counts of each genotype
            
        Returns:
        --------
        tuple : (p, q) allele frequencies
        """
        total = AA + Aa + aa
        p = (2 * AA + Aa) / (2 * total)
        q = 1 - p
        return p, q
    
    def chi_square_test(self, observed):
        """
        Test if observed genotype frequencies fit HW equilibrium.
        
        Parameters:
        -----------
        observed : dict
            Observed counts {AA: n1, Aa: n2, aa: n3}
            
        Returns:
        --------
        dict : Test results including chi-square statistic and p-value
        """
        total = sum(observed.values())
        expected = self.calculate_expected_counts(total)
        
        obs_array = [observed['AA'], observed['Aa'], observed['aa']]
        exp_array = [expected['AA'], expected['Aa'], expected['aa']]
        
        chi2, p_value = chisquare(obs_array, exp_array, ddof=1)
        
        return {
            'chi_square': chi2,
            'p_value': p_value,
            'degrees_of_freedom': 1,
            'significant': p_value < 0.05,
            'observed': observed,
            'expected': expected
        }
    
    def plot_comparison(self, observed=None, population_size=1000):
        """
        Visualize expected vs observed genotype frequencies.
        
        Parameters:
        -----------
        observed : dict, optional
            Observed genotype counts
        population_size : int
            Population size for expected counts
        """
        expected = self.calculate_expected_counts(population_size)
        
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Plot frequencies
        genotypes = ['AA', 'Aa', 'aa']
        expected_freqs = [expected[g] / population_size for g in genotypes]
        
        axes[0].bar(genotypes, expected_freqs, alpha=0.7, color='steelblue', 
                   label='Expected (HW)')
        
        if observed:
            obs_total = sum(observed.values())
            observed_freqs = [observed[g] / obs_total for g in genotypes]
            axes[0].bar(genotypes, observed_freqs, alpha=0.5, color='coral',
                       label='Observed')
        
        axes[0].set_ylabel('Frequency')
        axes[0].set_xlabel('Genotype')
        axes[0].set_title('Hardy-Weinberg Genotype Frequencies')
        axes[0].legend()
        axes[0].set_ylim(0, max(expected_freqs) * 1.2)
        
        # Plot allele frequencies
        allele_freqs = {'A': self.p, 'a': self.q}
        axes[1].bar(allele_freqs.keys(), allele_freqs.values(), 
                   color=['green', 'orange'], alpha=0.7)
        axes[1].set_ylabel('Frequency')
        axes[1].set_xlabel('Allele')
        axes[1].set_title('Allele Frequencies')
        axes[1].set_ylim(0, 1)
        
        # Add text annotations
        for i, (genotype, freq) in enumerate(zip(genotypes, expected_freqs)):
            axes[0].text(i, freq + 0.02, f'{freq:.3f}', 
                        ha='center', va='bottom')
        
        plt.tight_layout()
        plt.savefig('hardy_weinberg_comparison.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        return fig


def main():
    parser = argparse.ArgumentParser(
        description='Hardy-Weinberg Equilibrium Calculator'
    )
    
    parser.add_argument('--p', type=float, help='Frequency of A allele')
    parser.add_argument('--q', type=float, help='Frequency of a allele')
    parser.add_argument('--population_size', type=int, default=1000,
                       help='Population size for simulation')
    parser.add_argument('--observed', type=str,
                       help='Observed genotype counts (format: AA:n1,Aa:n2,aa:n3)')
    parser.add_argument('--simulate', action='store_true',
                       help='Run population simulation')
    parser.add_argument('--generations', type=int, default=10,
                       help='Number of generations to simulate')
    
    args = parser.parse_args()
    
    # Initialize calculator
    if args.p:
        calc = HardyWeinbergCalculator(p=args.p)
    elif args.q:
        calc = HardyWeinbergCalculator(q=args.q)
    else:
        # Default example
        calc = HardyWeinbergCalculator(p=0.6)
    
    print("=" * 60)
    print("HARDY-WEINBERG EQUILIBRIUM CALCULATOR")
    print("=" * 60)
    print(f"\nAllele frequencies:")
    print(f"  p (A allele) = {calc.p:.4f}")
    print(f"  q (a allele) = {calc.q:.4f}")
    print(f"  Verify: p + q = {calc.p + calc.q:.4f}")
    
    # Calculate expected genotype frequencies
    genotypes = calc.calculate_genotype_frequencies()
    print(f"\nExpected genotype frequencies under HW equilibrium:")
    print(f"  AA (p²) = {genotypes['AA']:.4f}")
    print(f"  Aa (2pq) = {genotypes['Aa']:.4f}")
    print(f"  aa (q²) = {genotypes['aa']:.4f}")
    print(f"  Verify sum = {sum(genotypes.values()):.4f}")
    
    # Calculate expected counts
    expected_counts = calc.calculate_expected_counts(args.population_size)
    print(f"\nExpected counts in population of {args.population_size}:")
    for genotype, count in expected_counts.items():
        print(f"  {genotype}: {count:.1f}")
    
    # Chi-square test if observed data provided
    if args.observed:
        obs_parts = args.observed.split(',')
        observed = {}
        for part in obs_parts:
            genotype, count = part.split(':')
            observed[genotype] = int(count)
        
        print(f"\nChi-square goodness of fit test:")
        test_results = calc.chi_square_test(observed)
        print(f"  Chi-square statistic: {test_results['chi_square']:.4f}")
        print(f"  P-value: {test_results['p_value']:.4f}")
        print(f"  Degrees of freedom: {test_results['degrees_of_freedom']}")
        
        if test_results['significant']:
            print(f"  ❌ Reject HW equilibrium (p < 0.05)")
        else:
            print(f"  ✓ Consistent with HW equilibrium (p ≥ 0.05)")
        
        calc.plot_comparison(observed, args.population_size)
    
    # Run simulation if requested
    if args.simulate:
        print(f"\nSimulating {args.generations} generations...")
        sim_results = calc.simulate_population(args.population_size, 
                                               args.generations)
        print(sim_results.to_string(index=False))
        
        # Plot simulation results
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(sim_results['generation'], sim_results['AA'] / args.population_size, 
               'o-', label='AA', color='blue')
        ax.plot(sim_results['generation'], sim_results['Aa'] / args.population_size,
               's-', label='Aa', color='green')
        ax.plot(sim_results['generation'], sim_results['aa'] / args.population_size,
               '^-', label='aa', color='red')
        
        # Add expected frequencies as horizontal lines
        ax.axhline(y=genotypes['AA'], linestyle='--', color='blue', alpha=0.5)
        ax.axhline(y=genotypes['Aa'], linestyle='--', color='green', alpha=0.5)
        ax.axhline(y=genotypes['aa'], linestyle='--', color='red', alpha=0.5)
        
        ax.set_xlabel('Generation')
        ax.set_ylabel('Genotype Frequency')
        ax.set_title('Hardy-Weinberg Equilibrium Across Generations')
        ax.legend()
        ax.grid(alpha=0.3)
        
        plt.savefig('hw_simulation.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    import sys
    
    # Check if running in notebook
    try:
        get_ipython()
        # In notebook - don't run main()
        print("✓ Script loaded successfully!")
        print("\nExample usage:")
        print("  calc = HardyWeinbergCalculator(p=0.6)")
        print("  genotypes = calc.calculate_genotype_frequencies()")
        print("  print(genotypes)")
    except NameError:
        # In command line - run main()
        main()
