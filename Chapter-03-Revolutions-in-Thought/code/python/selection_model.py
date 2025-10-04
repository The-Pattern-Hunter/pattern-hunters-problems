"""
Natural Selection Model
Chapter 3: Revolutions in Thought - Darwin to DNA

Models the effects of natural selection on allele frequencies.

Usage:
    python selection_model.py --p 0.5 --selection 0.3 --generations 100
    python selection_model.py --wAA 1.0 --wAa 1.1 --waa 0.9 --p 0.5 --generations 100
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse
from typing import Tuple, List


def selection_model(p0: float, s: float, h: float, generations: int) -> pd.DataFrame:
    """
    Model allele frequency change under natural selection.
    
    Parameters
    ----------
    p0 : float
        Initial frequency of A allele
    s : float
        Selection coefficient (0-1)
    h : float
        Dominance coefficient:
        - h = 0: recessive (selection against aa)
        - h = 0.5: additive
        - h = 1: dominant (selection against AA)
    generations : int
        Number of generations to simulate
        
    Returns
    -------
    pd.DataFrame
        Results with columns: generation, p, q, w_bar, delta_p
    """
    results = []
    p = p0
    
    for gen in range(generations + 1):
        q = 1 - p
        
        # Fitness values
        w_AA = 1.0
        w_Aa = 1 - h * s
        w_aa = 1 - s
        
        # Mean fitness
        w_bar = p**2 * w_AA + 2*p*q * w_Aa + q**2 * w_aa
        
        # Change in allele frequency (delta p)
        delta_p = (p*q / w_bar) * (p * (w_AA - w_Aa) + q * (w_Aa - w_aa))
        
        results.append({
            'generation': gen,
            'p': p,
            'q': q,
            'w_AA': w_AA,
            'w_Aa': w_Aa,
            'w_aa': w_aa,
            'w_bar': w_bar,
            'delta_p': delta_p
        })
        
        # Update allele frequency for next generation
        p_new = (p**2 * w_AA + p*q * w_Aa) / w_bar
        p = p_new
    
    return pd.DataFrame(results)


def calculate_equilibrium(s: float, h: float) -> float:
    """
    Calculate equilibrium allele frequency under selection.
    
    For heterozygote advantage: p_eq = s2 / (s1 + s2)
    For directional selection: p_eq = 0 or 1
    
    Parameters
    ----------
    s : float
        Selection coefficient
    h : float
        Dominance coefficient
        
    Returns
    -------
    float
        Equilibrium allele frequency (or None if no stable equilibrium)
    """
    # Heterozygote advantage (h < 0)
    if h < 0:
        s1 = -h * s  # Selection against AA
        s2 = s + h * s  # Selection against aa
        if s1 > 0 and s2 > 0:
            return s2 / (s1 + s2)
    
    # Directional selection
    if s > 0 and h >= 0:
        return 0.0  # aa eliminated
    elif s < 0:
        return 1.0  # AA eliminated
    
    return None


def plot_selection_dynamics(results: pd.DataFrame, s: float, h: float, 
                            save_path: str = None):
    """
    Plot allele frequency change under selection.
    
    Parameters
    ----------
    results : pd.DataFrame
        Simulation results
    s : float
        Selection coefficient
    h : float
        Dominance coefficient
    save_path : str, optional
        Path to save plot
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Plot 1: Allele frequencies
    axes[0, 0].plot(results['generation'], results['p'], 
                   'o-', label='p (freq A)', color='steelblue', linewidth=2)
    axes[0, 0].plot(results['generation'], results['q'], 
                   's-', label='q (freq a)', color='coral', linewidth=2)
    
    # Add equilibrium line if applicable
    p_eq = calculate_equilibrium(s, h)
    if p_eq is not None:
        axes[0, 0].axhline(y=p_eq, linestyle='--', color='green', 
                          label=f'Equilibrium p = {p_eq:.3f}')
    
    axes[0, 0].set_xlabel('Generation', fontsize=11)
    axes[0, 0].set_ylabel('Allele Frequency', fontsize=11)
    axes[0, 0].set_title(f'Selection Model (s={s}, h={h})', fontweight='bold')
    axes[0, 0].legend()
    axes[0, 0].grid(alpha=0.3)
    axes[0, 0].set_ylim(0, 1)
    
    # Plot 2: Mean fitness
    axes[0, 1].plot(results['generation'], results['w_bar'], 
                   'o-', color='purple', linewidth=2)
    axes[0, 1].set_xlabel('Generation', fontsize=11)
    axes[0, 1].set_ylabel('Mean Fitness (w̄)', fontsize=11)
    axes[0, 1].set_title('Mean Fitness Over Time', fontweight='bold')
    axes[0, 1].grid(alpha=0.3)
    
    # Plot 3: Change in p (delta p)
    axes[1, 0].plot(results['generation'], results['delta_p'], 
                   'o-', color='darkred', linewidth=2)
    axes[1, 0].axhline(y=0, linestyle='--', color='black', alpha=0.5)
    axes[1, 0].set_xlabel('Generation', fontsize=11)
    axes[1, 0].set_ylabel('Δp', fontsize=11)
    axes[1, 0].set_title('Rate of Allele Frequency Change', fontweight='bold')
    axes[1, 0].grid(alpha=0.3)
    
    # Plot 4: Genotype frequencies
    AA_freq = results['p']**2
    Aa_freq = 2 * results['p'] * results['q']
    aa_freq = results['q']**2
    
    axes[1, 1].plot(results['generation'], AA_freq, 
                   'o-', label='AA', color='blue', linewidth=2)
    axes[1, 1].plot(results['generation'], Aa_freq, 
                   's-', label='Aa', color='green', linewidth=2)
    axes[1, 1].plot(results['generation'], aa_freq, 
                   '^-', label='aa', color='red', linewidth=2)
    axes[1, 1].set_xlabel('Generation', fontsize=11)
    axes[1, 1].set_ylabel('Genotype Frequency', fontsize=11)
    axes[1, 1].set_title('Genotype Frequencies', fontweight='bold')
    axes[1, 1].legend()
    axes[1, 1].grid(alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    
    plt.show()


def compare_selection_strengths(p0: float, h: float, s_values: List[float], 
                                generations: int, save_path: str = None):
    """
    Compare different selection strengths.
    
    Parameters
    ----------
    p0 : float
        Initial allele frequency
    h : float
        Dominance coefficient
    s_values : list of float
        Different selection coefficients to compare
    generations : int
        Number of generations
    save_path : str, optional
        Path to save plot
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    
    colors = plt.cm.viridis(np.linspace(0, 1, len(s_values)))
    
    for s, color in zip(s_values, colors):
        results = selection_model(p0, s, h, generations)
        ax.plot(results['generation'], results['p'], 
               'o-', label=f's = {s}', color=color, linewidth=2, markersize=4)
    
    ax.set_xlabel('Generation', fontsize=12)
    ax.set_ylabel('Frequency of A allele (p)', fontsize=12)
    ax.set_title(f'Selection Strength Comparison (h = {h})', 
                fontsize=14, fontweight='bold')
    ax.legend(loc='best')
    ax.grid(alpha=0.3)
    ax.set_ylim(0, 1)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {save_path}")
    
    plt.show()


def print_selection_summary(results: pd.DataFrame, s: float, h: float):
    """
    Print summary of selection simulation.
    
    Parameters
    ----------
    results : pd.DataFrame
        Simulation results
    s : float
        Selection coefficient
    h : float
        Dominance coefficient
    """
    print("\n" + "="*60)
    print("NATURAL SELECTION SIMULATION SUMMARY")
    print("="*60)
    
    print(f"\nSelection parameters:")
    print(f"  Selection coefficient (s): {s}")
    print(f"  Dominance coefficient (h): {h}")
    
    if h == 0:
        print("  Type: Selection against recessive (aa)")
    elif h == 0.5:
        print("  Type: Additive selection")
    elif h == 1:
        print("  Type: Selection against dominant (AA)")
    elif h < 0:
        print("  Type: Heterozygote advantage (balancing selection)")
    
    print(f"\nFitness values:")
    print(f"  w(AA) = {results.iloc[0]['w_AA']:.3f}")
    print(f"  w(Aa) = {results.iloc[0]['w_Aa']:.3f}")
    print(f"  w(aa) = {results.iloc[0]['w_aa']:.3f}")
    
    print(f"\nInitial conditions:")
    print(f"  p₀ = {results.iloc[0]['p']:.4f}")
    print(f"  q₀ = {results.iloc[0]['q']:.4f}")
    print(f"  w̄₀ = {results.iloc[0]['w_bar']:.4f}")
    
    print(f"\nFinal state (generation {len(results)-1}):")
    print(f"  p = {results.iloc[-1]['p']:.4f}")
    print(f"  q = {results.iloc[-1]['q']:.4f}")
    print(f"  w̄ = {results.iloc[-1]['w_bar']:.4f}")
    
    print(f"\nChange in allele frequency:")
    print(f"  Δp (total) = {results.iloc[-1]['p'] - results.iloc[0]['p']:.4f}")
    print(f"  Δp (last generation) = {results.iloc[-1]['delta_p']:.6f}")
    
    # Check for equilibrium
    p_eq = calculate_equilibrium(s, h)
    if p_eq is not None:
        print(f"\nEquilibrium frequency: p* = {p_eq:.4f}")
        if abs(results.iloc[-1]['p'] - p_eq) < 0.01:
            print("  Status: Near equilibrium ✓")
        else:
            print("  Status: Approaching equilibrium...")
    else:
        if results.iloc[-1]['p'] > 0.99:
            print("\nAllele A is approaching fixation (p → 1)")
        elif results.iloc[-1]['p'] < 0.01:
            print("\nAllele A is approaching loss (p → 0)")


def main():
    parser = argparse.ArgumentParser(
        description='Natural Selection Model - Allele Frequency Change Under Selection'
    )
    
    parser.add_argument('--p', type=float, default=0.5,
                       help='Initial allele frequency (default: 0.5)')
    parser.add_argument('--selection', '-s', type=float, default=None,
                       help='Selection coefficient (0-1)')
    parser.add_argument('--dominance', '-h', type=float, default=0.0,
                       help='Dominance coefficient (0=recessive, 0.5=additive, 1=dominant)')
    parser.add_argument('--wAA', type=float, default=None,
                       help='Fitness of AA genotype')
    parser.add_argument('--wAa', type=float, default=None,
                       help='Fitness of Aa genotype')
    parser.add_argument('--waa', type=float, default=None,
                       help='Fitness of aa genotype')
    parser.add_argument('--generations', '-g', type=int, default=100,
                       help='Number of generations (default: 100)')
    parser.add_argument('--compare', type=str, default=None,
                       help='Compare multiple selection coefficients (comma-separated)')
    parser.add_argument('--output', '-o', type=str, default=None,
                       help='Output CSV file')
    parser.add_argument('--plot', action='store_true',
                       help='Generate plots')
    parser.add_argument('--save_plot', type=str, default=None,
                       help='Save plot to file')
    
    args = parser.parse_args()
    
    print("="*60)
    print("NATURAL SELECTION MODEL")
    print("="*60)
    
    # Use direct fitness values if provided
    if args.wAA is not None and args.wAa is not None and args.waa is not None:
        print(f"\nUsing direct fitness values:")
        print(f"  w(AA) = {args.wAA}")
        print(f"  w(Aa) = {args.wAa}")
        print(f"  w(aa) = {args.waa}")
        
        results = selection_from_fitness(
            args.p, args.wAA, args.wAa, args.waa, args.generations
        )
        
        # Calculate equivalent s and h
        s = 1 - args.waa
        if args.wAA != 0:
            h = (1 - args.wAa) / s if s != 0 else 0
        else:
            h = 0
        
        print(f"\nEquivalent selection parameters:")
        print(f"  s ≈ {s:.3f}")
        print(f"  h ≈ {h:.3f}")
    
    # Use selection coefficient and dominance
    else:
        if args.selection is None:
            args.selection = 0.1
            print(f"\nNo selection coefficient provided, using default s = 0.1")
        
        print(f"\nSelection parameters:")
        print(f"  s = {args.selection}")
        print(f"  h = {args.dominance}")
        
        s = args.selection
        h = args.dominance
        
        results = selection_model(args.p, s, h, args.generations)
    
    # Display results
    print(f"\nFirst 10 generations:")
    print(results.head(10)[['generation', 'p', 'q', 'w_bar', 'delta_p']].to_string(index=False))
    
    if args.generations > 10:
        print(f"\n... (showing first 10 of {args.generations} generations)")
        print(f"\nLast 5 generations:")
        print(results.tail(5)[['generation', 'p', 'q', 'w_bar', 'delta_p']].to_string(index=False))
    
    print_selection_summary(results, s, h)
    
    # Save to CSV
    if args.output:
        results.to_csv(args.output, index=False)
        print(f"\nResults saved to {args.output}")
    
    # Compare different selection strengths
    if args.compare:
        s_values = [float(x.strip()) for x in args.compare.split(',')]
        print(f"\nComparing selection coefficients: {s_values}")
        compare_selection_strengths(args.p, h, s_values, args.generations, args.save_plot)
    
    # Plot single simulation
    elif args.plot or args.save_plot:
        plot_selection_dynamics(results, s, h, args.save_plot)
    
    print("\n" + "="*60)


if __name__ == "__main__":
    main()
'w_AA': w_AA,
            'w_Aa': w_Aa,
            'w_aa': w_aa,
            'w_bar': w_bar,
            'delta_p': delta_p
        })
        
        # Update allele frequency for next generation
        p_new = (p**2 * w_AA + p*q * w_Aa) / w_bar
        p = p_new
    
    return pd.DataFrame(results)


def selection_from_fitness(p0: float, w_AA: float, w_Aa: float, 
                           w_aa: float, generations: int) -> pd.DataFrame:
    """
    Model selection using direct fitness values.
    
    Parameters
    ----------
    p0 : float
        Initial frequency of A allele
    w_AA, w_Aa, w_aa : float
        Fitness values for each genotype
    generations : int
        Number of generations
        
    Returns
    -------
    pd.DataFrame
        Results with generation and allele frequencies
    """
    results = []
    p = p0
    
    for gen in range(generations + 1):
        q = 1 - p
        
        # Mean fitness
        w_bar = p**2 * w_AA + 2*p*q * w_Aa + q**2 * w_aa
        
        # Change in allele frequency
        delta_p = (p*q / w_bar) * (p * (w_AA - w_Aa) + q * (w_Aa - w_aa))
        
        results.append({
            'generation': gen,
            'p': p,
            'q': q,
