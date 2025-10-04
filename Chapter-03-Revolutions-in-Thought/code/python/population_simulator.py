"""
Population Genetics Simulator
Chapter 3: Revolutions in Thought - Darwin to DNA

Simulates random mating and genetic drift across generations.

Usage:
    python population_simulator.py --p 0.6 --generations 20 --pop_size 1000
    python population_simulator.py --p 0.3,0.5,0.7 --generations 50 --pop_size 100
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse
from typing import List, Tuple, Dict


def simulate_population(p0: float, population_size: int, generations: int) -> pd.DataFrame:
    """
    Simulate random mating across generations.
    
    Parameters
    ----------
    p0 : float
        Initial frequency of A allele
    population_size : int
        Number of individuals in population
    generations : int
        Number of generations to simulate
        
    Returns
    -------
    pd.DataFrame
        Simulation results with columns: generation, p, AA, Aa, aa
    """
    results = []
    p = p0
    
    for gen in range(generations + 1):
        q = 1 - p
        
        # Create gamete pool based on current allele frequencies
        gametes = np.random.choice(['A', 'a'], 
                                  size=population_size * 2,
                                  p=[p, q])
        
        # Random fertilization
        genotypes = []
        for i in range(0, len(gametes), 2):
            genotype = ''.join(sorted([gametes[i], gametes[i+1]]))
            genotypes.append(genotype)
        
        # Count genotypes
        AA = genotypes.count('AA')
        Aa = genotypes.count('Aa')
        aa = genotypes.count('aa')
        
        # Calculate new allele frequency for next generation
        p = (2 * AA + Aa) / (2 * population_size)
        
        results.append({
            'generation': gen,
            'p': p,
            'q': 1 - p,
            'AA': AA,
            'Aa': Aa,
            'aa': aa,
            'AA_freq': AA / population_size,
            'Aa_freq': Aa / population_size,
            'aa_freq': aa / population_size
        })
    
    return pd.DataFrame(results)


def simulate_multiple_populations(p_values: List[float], 
                                  population_size: int, 
                                  generations: int) -> Dict[float, pd.DataFrame]:
    """
    Simulate multiple populations with different starting frequencies.
    
    Parameters
    ----------
    p_values : list of float
        List of initial allele frequencies
    population_size : int
        Population size for each simulation
    generations : int
        Number of generations
        
    Returns
    -------
    dict
        Dictionary mapping p values to simulation DataFrames
    """
    results = {}
    for p in p_values:
        results[p] = simulate_population(p, population_size, generations)
    return results


def plot_allele_frequencies(sim_results: pd.DataFrame, 
                            p0: float,
                            save_path: str = None):
    """
    Plot allele frequency changes over generations.
    
    Parameters
    ----------
    sim_results : pd.DataFrame
        Simulation results
    p0 : float
        Initial allele frequency
    save_path : str, optional
        Path to save plot
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Plot 1: Allele frequencies
    ax1.plot(sim_results['generation'], sim_results['p'], 
            'o-', label='p (freq A)', color='steelblue', linewidth=2)
    ax1.plot(sim_results['generation'], sim_results['q'], 
            's-', label='q (freq a)', color='coral', linewidth=2)
    ax1.axhline(y=p0, linestyle='--', color='steelblue', alpha=0.5, 
               label=f'Initial p = {p0}')
    ax1.axhline(y=1-p0, linestyle='--', color='coral', alpha=0.5, 
               label=f'Initial q = {1-p0}')
    
    ax1.set_xlabel('Generation', fontsize=12)
    ax1.set_ylabel('Allele Frequency', fontsize=12)
    ax1.set_title('Allele Frequency Changes Across Generations', 
                 fontsize=14, fontweight='bold')
    ax1.legend(loc='best')
    ax1.grid(alpha=0.3)
    ax1.set_ylim(0, 1)
    
    # Plot 2: Genotype frequencies
    ax2.plot(sim_results['generation'], sim_results['AA_freq'], 
            'o-', label='AA', color='blue', linewidth=2)
    ax2.plot(sim_results['generation'], sim_results['Aa_freq'], 
            's-', label='Aa', color='green', linewidth=2)
    ax2.plot(sim_results['generation'], sim_results['aa_freq'], 
            '^-', label='aa', color='red', linewidth=2)
    
    # Expected HW frequencies (dashed lines)
    expected_AA = p0**2
    expected_Aa = 2*p0*(1-p0)
    expected_aa = (1-p0)**2
    
    ax2.axhline(y=expected_AA, linestyle='--', color='blue', alpha=0.5)
    ax2.axhline(y=expected_Aa, linestyle='--', color='green', alpha=0.5)
    ax2.axhline(y=expected_aa, linestyle='--', color='red', alpha=0.5)
    
    ax2.set_xlabel('Generation', fontsize=12)
    ax2.set_ylabel('Genotype Frequency', fontsize=12)
    ax2.set_title('Genotype Frequency Changes Across Generations', 
                 fontsize=14, fontweight='bold')
    ax2.legend(loc='best')
    ax2.grid(alpha=0.3)
    ax2.set_ylim(0, max(expected_AA, expected_Aa, expected_aa) * 1.2)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    
    plt.show()


def plot_multiple_populations(results_dict: Dict[float, pd.DataFrame],
                              save_path: str = None):
    """
    Plot allele frequency trajectories for multiple populations.
    
    Parameters
    ----------
    results_dict : dict
        Dictionary mapping initial p values to simulation results
    save_path : str, optional
        Path to save plot
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    
    colors = plt.cm.viridis(np.linspace(0, 1, len(results_dict)))
    
    for (p0, df), color in zip(results_dict.items(), colors):
        ax.plot(df['generation'], df['p'], 
               'o-', label=f'p₀ = {p0}', color=color, 
               linewidth=2, markersize=4, alpha=0.7)
    
    ax.set_xlabel('Generation', fontsize=12)
    ax.set_ylabel('Frequency of A allele (p)', fontsize=12)
    ax.set_title('Genetic Drift: Multiple Starting Frequencies', 
                fontsize=14, fontweight='bold')
    ax.legend(loc='best', ncol=2)
    ax.grid(alpha=0.3)
    ax.set_ylim(0, 1)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    
    plt.show()


def calculate_drift_variance(p: float, N: int, t: int) -> float:
    """
    Calculate expected variance in allele frequency due to drift.
    
    Variance after t generations: Var(p_t) = p(1-p)[1 - (1-1/2N)^t]
    
    Parameters
    ----------
    p : float
        Initial allele frequency
    N : int
        Population size
    t : int
        Number of generations
        
    Returns
    -------
    float
        Expected variance
    """
    return p * (1 - p) * (1 - (1 - 1/(2*N))**t)


def print_summary_statistics(sim_results: pd.DataFrame):
    """
    Print summary statistics from simulation.
    
    Parameters
    ----------
    sim_results : pd.DataFrame
        Simulation results
    """
    print("\n" + "="*60)
    print("SIMULATION SUMMARY STATISTICS")
    print("="*60)
    
    print(f"\nInitial allele frequency (p₀): {sim_results.iloc[0]['p']:.4f}")
    print(f"Final allele frequency (p_t): {sim_results.iloc[-1]['p']:.4f}")
    print(f"Change in p: {sim_results.iloc[-1]['p'] - sim_results.iloc[0]['p']:.4f}")
    
    print(f"\nMean p across generations: {sim_results['p'].mean():.4f}")
    print(f"Variance in p: {sim_results['p'].var():.6f}")
    print(f"Standard deviation in p: {sim_results['p'].std():.6f}")
    
    print(f"\nFinal genotype frequencies:")
    print(f"  AA: {sim_results.iloc[-1]['AA_freq']:.4f}")
    print(f"  Aa: {sim_results.iloc[-1]['Aa_freq']:.4f}")
    print(f"  aa: {sim_results.iloc[-1]['aa_freq']:.4f}")
    
    # Expected HW frequencies based on final p
    p_final = sim_results.iloc[-1]['p']
    print(f"\nExpected HW frequencies (based on final p = {p_final:.4f}):")
    print(f"  AA: {p_final**2:.4f}")
    print(f"  Aa: {2*p_final*(1-p_final):.4f}")
    print(f"  aa: {(1-p_final)**2:.4f}")


def main():
    parser = argparse.ArgumentParser(
        description='Population Genetics Simulator - Random Mating and Genetic Drift'
    )
    
    parser.add_argument('--p', type=str, required=True,
                       help='Initial allele frequency (single value or comma-separated list: 0.3,0.5,0.7)')
    parser.add_argument('--pop_size', '--N', type=int, default=1000,
                       help='Population size (default: 1000)')
    parser.add_argument('--generations', '--t', type=int, default=20,
                       help='Number of generations (default: 20)')
    parser.add_argument('--output', '-o', type=str, default=None,
                       help='Output CSV file path')
    parser.add_argument('--plot', action='store_true',
                       help='Generate plots')
    parser.add_argument('--save_plot', type=str, default=None,
                       help='Save plot to file')
    
    args = parser.parse_args()
    
    # Parse p values
    p_values = [float(x.strip()) for x in args.p.split(',')]
    
    # Validate p values
    for p in p_values:
        if not 0 <= p <= 1:
            raise ValueError(f"Allele frequency must be between 0 and 1. Got: {p}")
    
    print("="*60)
    print("POPULATION GENETICS SIMULATOR")
    print("="*60)
    print(f"\nParameters:")
    print(f"  Population size: {args.pop_size}")
    print(f"  Generations: {args.generations}")
    print(f"  Initial p value(s): {', '.join(map(str, p_values))}")
    
    # Single population simulation
    if len(p_values) == 1:
        p0 = p_values[0]
        print(f"\nRunning simulation with p₀ = {p0}...")
        
        results = simulate_population(p0, args.pop_size, args.generations)
        
        # Display results
        print("\nFirst 10 generations:")
        print(results.head(10).to_string(index=False))
        
        if args.generations > 10:
            print(f"\n... (showing first 10 of {args.generations} generations)")
        
        print_summary_statistics(results)
        
        # Save to CSV
        if args.output:
            results.to_csv(args.output, index=False)
            print(f"\nResults saved to {args.output}")
        
        # Plot
        if args.plot or args.save_plot:
            plot_allele_frequencies(results, p0, args.save_plot)
    
    # Multiple population simulation
    else:
        print(f"\nRunning {len(p_values)} parallel simulations...")
        
        results_dict = simulate_multiple_populations(
            p_values, args.pop_size, args.generations
        )
        
        # Display summary for each population
        for p0, results in results_dict.items():
            print(f"\n--- Population with p₀ = {p0} ---")
            print(f"Final p: {results.iloc[-1]['p']:.4f}")
            print(f"Change: {results.iloc[-1]['p'] - p0:.4f}")
        
        # Save combined results
        if args.output:
            combined = pd.concat([
                df.assign(initial_p=p0) for p0, df in results_dict.items()
            ])
            combined.to_csv(args.output, index=False)
            print(f"\nCombined results saved to {args.output}")
        
        # Plot
        if args.plot or args.save_plot:
            plot_multiple_populations(results_dict, args.save_plot)
    
    print("\n" + "="*60)


if __name__ == "__main__":
    main()
