"""
Chapter 1: Firefly Synchronization Simulator
Demonstrates emergence of synchrony using Kuramoto model

Problem: Challenge C2
Author: Dr. Alok Patel
Repository: github.com/The-Pattern-Hunter/pattern-hunters-problems
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class FireflySwarm:
    """
    Simulates firefly synchronization using the Kuramoto model
    
    Parameters:
    -----------
    n_fireflies : int
        Number of fireflies in the swarm
    coupling_strength : float (0-1)
        How strongly fireflies influence each other
    """
    
    def __init__(self, n_fireflies=20, coupling_strength=0.1):
        self.n = n_fireflies
        self.K = coupling_strength
        
        # Initialize random phases (0 to 2π)
        self.phases = np.random.uniform(0, 2*np.pi, n_fireflies)
        
        # Natural frequencies (slightly different for each firefly)
        base_freq = 1.0  # Average frequency
        freq_variation = 0.1  # How much they vary
        self.frequencies = np.random.normal(base_freq, freq_variation, n_fireflies)
        
        # History for plotting
        self.phase_history = [self.phases.copy()]
        self.sync_history = []
        
    def update(self, dt=0.01):
        """Update firefly phases using Kuramoto model"""
        
        # Calculate coupling term (how fireflies influence each other)
        coupling = np.zeros(self.n)
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    coupling[i] += np.sin(self.phases[j] - self.phases[i])
        
        coupling *= (self.K / self.n)
        
        # Update phases
        self.phases += (self.frequencies + coupling) * dt
        self.phases = self.phases % (2 * np.pi)  # Keep phases in [0, 2π]
        
        # Store history
        self.phase_history.append(self.phases.copy())
        
        # Calculate synchronization measure
        sync = self.measure_synchronization()
        self.sync_history.append(sync)
        
        return sync
    
    def measure_synchronization(self):
        """
        Measure synchronization using order parameter
        Returns value from 0 (no sync) to 1 (perfect sync)
        """
        # Convert phases to complex numbers
        z = np.exp(1j * self.phases)
        
        # Order parameter is magnitude of mean
        r = np.abs(np.mean(z))
        
        return r
    
    def is_flashing(self, threshold=np.pi/4):
        """Determine which fireflies are currently flashing"""
        # Flash when phase is near 0 or 2π
        return (self.phases < threshold) | (self.phases > (2*np.pi - threshold))
    
    def simulate(self, duration=50, dt=0.01):
        """Run simulation for specified duration"""
        steps = int(duration / dt)
        
        for _ in range(steps):
            self.update(dt)
        
        return np.array(self.phase_history), np.array(self.sync_history)


def main():
    """Run firefly synchronization simulation and create visualizations"""
    
    print("="*60)
    print("FIREFLY SYNCHRONIZATION SIMULATOR")
    print("="*60)
    print("\nInitializing firefly swarm...")
    
    # Create firefly swarm
    n_fireflies = 30
    coupling = 0.3
    swarm = FireflySwarm(n_fireflies=n_fireflies, coupling_strength=coupling)
    
    print(f"Number of fireflies: {n_fireflies}")
    print(f"Coupling strength: {coupling}")
    print("\nRunning simulation...")
    
    # Run simulation
    phases, synchronization = swarm.simulate(duration=50)
    
    print("✓ Simulation complete!")
    print("\nCreating visualizations...")
    
    # Create visualization
    fig, axes = plt.subplots(3, 1, figsize=(12, 10))
    
    # Plot 1: Phase evolution over time
    time = np.arange(len(phases)) * 0.01
    for i in range(swarm.n):
        axes[0].plot(time, phases[:, i], alpha=0.3, linewidth=0.5)
    
    axes[0].set_xlabel('Time')
    axes[0].set_ylabel('Phase (radians)')
    axes[0].set_title('Firefly Phases Over Time (Convergence to Synchrony)')
    axes[0].grid(True, alpha=0.3)
    axes[0].set_ylim([0, 2*np.pi])
    
    # Plot 2: Synchronization measure
    axes[1].plot(time, synchronization, linewidth=2, color='red')
    axes[1].set_xlabel('Time')
    axes[1].set_ylabel('Synchronization (0=none, 1=perfect)')
    axes[1].set_title('Synchronization Measure Over Time')
    axes[1].grid(True, alpha=0.3)
    axes[1].set_ylim([0, 1.05])
    axes[1].axhline(y=0.9, color='green', linestyle='--', label='High sync threshold')
    axes[1].legend()
    
    # Plot 3: Phase distribution at different times
    time_points = [0, len(phases)//4, len(phases)//2, len(phases)-1]
    colors = ['blue', 'orange', 'green', 'red']
    labels = ['Start', '25%', '50%', 'End']
    
    for tp, color, label in zip(time_points, colors, labels):
        phase_dist = phases[tp, :]
        # Convert to unit circle coordinates
        x = np.cos(phase_dist)
        y = np.sin(phase_dist)
        axes[2].scatter(x, y, s=100, alpha=0.6, color=color, label=label)
    
    # Draw unit circle
    theta = np.linspace(0, 2*np.pi, 100)
    axes[2].plot(np.cos(theta), np.sin(theta), 'k--', alpha=0.3)
    axes[2].set_xlabel('cos(phase)')
    axes[2].set_ylabel('sin(phase)')
    axes[2].set_title('Phase Distribution on Unit Circle')
    axes[2].legend()
    axes[2].set_aspect('equal')
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('firefly_synchronization.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Print summary
    print("\n" + "="*60)
    print("ANALYSIS RESULTS")
    print("="*60)
    print(f"\nInitial synchronization: {synchronization[0]:.3f}")
    print(f"Final synchronization: {synchronization[-1]:.3f}")
    print(f"Improvement: {(synchronization[-1] - synchronization[0]):.3f}")
    
    if any(synchronization > 0.9):
        time_to_sync = time[synchronization > 0.9][0]
        print(f"\n✓ Reached 90% synchronization at t = {time_to_sync:.1f}s")
    else:
        print("\n✗ Did not reach 90% synchronization")
        print(f"  Maximum synchronization: {synchronization.max():.3f}")
    
    print("\n" + "="*60)
    print("\nVisualization saved as 'firefly_synchronization.png'")
    print("\nKey Insight:")
    print("Even without a leader, fireflies synchronize through")
    print("local interactions - a beautiful example of EMERGENCE!")
    print("="*60)


if __name__ == "__main__":
    main()
    
    print("\n" + "="*60)
    print("EXPERIMENT IDEAS:")
    print("="*60)
    print("\n1. Try different coupling strengths:")
    print("   swarm = FireflySwarm(n_fireflies=30, coupling_strength=0.1)")
    print("   swarm = FireflySwarm(n_fireflies=30, coupling_strength=0.5)")
    print("\n2. Vary the number of fireflies:")
    print("   swarm = FireflySwarm(n_fireflies=10, coupling_strength=0.3)")
    print("   swarm = FireflySwarm(n_fireflies=100, coupling_strength=0.3)")
    print("\n3. Modify frequency variation in __init__:")
    print("   freq_variation = 0.05  # More similar")
    print("   freq_variation = 0.20  # More diverse")
    print("\n" + "="*60)