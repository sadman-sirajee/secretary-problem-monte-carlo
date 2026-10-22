# Monte Carlo Simulation: Secretary Problem

## Overview
This project uses Monte Carlo simulation to study the classical Secretary Problem and estimate the optimal selection threshold for different values of `s`.

## Objectives
- Simulate the Secretary Problem using random permutations.
- Estimate success rates for different selection thresholds.
- Identify the threshold that maximizes the probability of selecting the best candidate.
- Compare results for different values of `s`.

## Simulation Setup
- Number of candidates: 100
- Number of simulation runs: 200,000
- Random seed: 42
- Values of `s`: 1, 3, 5, 10

## Tools
- Python
- NumPy
- Pandas
- Matplotlib

## Results
The simulation estimates the following best thresholds:

| s | Best threshold (m) | Success rate |
|---|---:|---:|
| 1 | 35 | 36.978% |
| 3 | 26 | 60.561% |
| 5 | 21 | 70.512% |
| 10 | 14 | 81.561% |

## Project Files
- Python source code: simulation implementation
- CSV files: simulation results
- PNG files: result visualizations

## How to Run
Install the required libraries:

```bash
pip install numpy pandas matplotlib
```

Run the Python simulation script after downloading the repository.

## Conclusion
The simulation demonstrates how the selection strategy and the value of `s` affect the probability of choosing the best candidate.
