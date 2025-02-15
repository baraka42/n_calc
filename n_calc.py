import numpy as np
import matplotlib.pyplot as plt

def simulate_random_results(target_winrate, num_simulations=1000):
    # Convert the winrate to a probability (between 0 and 1)
    target_winrate /= 100.0  # Convert to a percentage and normalize to [0, 1]
    results = []

    # Simulate random results (1 = win, 0 = loss)
    for _ in range(num_simulations):
        result = 1 if np.random.rand() < target_winrate else 0
        results.append(result)

    # Calculate the cumulative winrate
    winrate_accumulated = np.cumsum(results) / np.arange(1, num_simulations + 1)

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, num_simulations + 1), winrate_accumulated, label="Cumulative Winrate")
    plt.axhline(y=target_winrate, color='r', linestyle='--', label="Target Winrate")
    plt.xlabel("Number of Simulations")
    plt.ylabel("Cumulative Winrate")
    plt.title("Cumulative Winrate Simulation")
    plt.legend()
    plt.grid()
    plt.show()

# Define variables
Winrate = 50
Simulations = 1000

# Example usage
simulate_random_results(target_winrate=Winrate, num_simulations=Simulations)