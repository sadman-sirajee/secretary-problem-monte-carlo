import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Parameters
n = 100
num_runs = 200_000
rng = np.random.default_rng(42)

# Generate random permutations efficiently.
# Each row is one independent interview order.
orders = np.empty((num_runs, n), dtype=np.int16)
for i in range(num_runs):
    orders[i] = rng.permutation(np.arange(1, n + 1))

def simulate_success_rates(orders, s):
    num_runs, n = orders.shape
    rates = []

    # m = 0,...,n-1
    for m in range(n):
        if m == 0:
            # No sample: accept the first candidate.
            selected = orders[:, 0]
        else:
            # Best (lowest numerical rank) among first m candidates.
            sample_best = orders[:, :m].min(axis=1)

            # Find first post-sample candidate better than sample_best.
            later = orders[:, m:]
            better = later < sample_best[:, None]

            has_better = better.any(axis=1)
            first_idx = better.argmax(axis=1)

            # If none is better, the strategy is forced to take the last candidate.
            selected = np.where(
                has_better,
                later[np.arange(num_runs), first_idx],
                orders[:, -1]
            )

        success = selected <= s
        rates.append(success.mean())

    return np.array(rates)

criteria = [1, 3, 5, 10]
results = {}

for s in criteria:
    results[s] = simulate_success_rates(orders, s)

# Create result table
df = pd.DataFrame({"m": np.arange(n)})
for s in criteria:
    df[f"P_success_s={s}"] = results[s]

# Save CSV
csv_path = "/mnt/data/secretary_problem_results.csv"
df.to_csv(csv_path, index=False)

# Find empirical optima
summary = []
for s in criteria:
    rates = results[s]
    m_opt = int(np.argmax(rates))
    summary.append({
        "s": s,
        "optimal_m": m_opt,
        "max_empirical_success_rate": rates[m_opt],
        "success_percent": rates[m_opt] * 100
    })

summary_df = pd.DataFrame(summary)
summary_path = "/mnt/data/secretary_problem_optima.csv"
summary_df.to_csv(summary_path, index=False)

# Plot all four curves together
plt.figure(figsize=(11, 6))
for s in criteria:
    plt.plot(np.arange(n), results[s], label=f"s = {s}")
    m_opt = int(np.argmax(results[s]))
    plt.scatter([m_opt], [results[s][m_opt]])

plt.xlabel("Sample size m")
plt.ylabel("Estimated success probability")
plt.title("Secretary Problem: Success Rate vs. Sample Size (n = 100)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plot_path = "/mnt/data/secretary_problem_success_rates.png"
plt.savefig(plot_path, dpi=200)
plt.show()

print(summary_df.to_string(index=False))
print(f"\nFiles created:\n{plot_path}\n{csv_path}\n{summary_path}")
