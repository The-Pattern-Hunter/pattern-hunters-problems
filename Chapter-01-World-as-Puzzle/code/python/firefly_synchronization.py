"""
Chapter 1: Firefly Synchronization Simulator - FIXED VERSION
Demonstrates emergence of synchrony using Kuramoto model
"""

import numpy as np
import matplotlib.pyplot as plt

class FireflySwarm:
    def __init__(self, n_fireflies=20, coupling_strength=0.1):
        self.n = n_fireflies
        self.K = coupling_strength
        self.phases = np.random.uniform(0, 2*np.pi, n_fireflies)
        base_freq = 1.0
        freq_variation = 0.1
        self.frequencies = np.random.normal(base_freq, freq_variation, n_fireflies)
        self.phase_history = []
        self.sync_history = []
        
    def update(self, dt=0.01):
        coupling = np.zeros(self.n)
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    coupling[i] += np.sin(self.phases[j] - self.phases[i])
        coupling *= (self.K / self.n)
        self.phases += (self.frequencies + coupling) * dt
        self.phases = self.phases % (2 * np.pi)
        sync = self.measure_synchronization()
        return sync
    
    def measure_synchronization(self):
        z = np.exp(1j * self.phases)
        r = np.abs(np.mean(z))
        return r
    
    def simulate(self, duration=50, dt=0.01):
        steps = int(duration / dt)
        for _ in range(steps):
            self.phase_history.append(self.phases.copy())
            sync = self.update(dt)
            self.sync_history.append(sync)
        return np.array(self.phase_history), np.array(self.sync_history)

def main():
    print("="*60)
    print("FIREFLY SYNCHRONIZATION SIMULATOR")
    print("="*60)
    print("\nInitializing firefly swarm...")
    
    n_fireflies = 30
    coupling = 0.3
    swarm = FireflySwarm(n_fireflies=n_fireflies, coupling_strength=coupling)
    
    print(f"Number of fireflies: {n_fireflies}")
    print(f"Coupling strength: {coupling}")
    print("\nRunning simulation...")
    
    phases, synchronization = swarm.simulate(duration=50)
    
    print("✓ Simulation complete!")
    print("\nCreating visualizations...")
    
    fig, axes = plt.subplots(3, 1, figsize=(12, 10))
    
    # FIXED: Match time array length to data
    time = np.arange(len(phases)) * 0.01
    
    # Plot 1: Phase evolution
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
        x = np.cos(phase_dist)
        y = np.sin(phase_dist)
        axes[2].scatter(x, y, s=100, alpha=0.6, color=color, label=label)
    
    theta = np.linspace(0, 2*np.pi, 100)
    axes[2].plot(np.cos(theta), np.sin(theta), 'k--', alpha=0.3)
    axes[2].set_xlabel('cos(phase)')
    axes[2].set_ylabel('sin(phase)')
    axes[2].set_title('Phase Distribution on Unit Circle')
    axes[2].legend()
    axes[2].set_aspect('equal')
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
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
    print("\nKey Insight:")
    print("Even without a leader, fireflies synchronize through")
    print("local interactions - a beautiful example of EMERGENCE!")
    print("="*60)

if __name__ == "__main__":
    main()
