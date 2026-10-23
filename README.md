# Monte Carlo Simulation: Secretary Problem

A Python-based Monte Carlo simulation that studies the classical Secretary Problem and estimates the probability of selecting one of the top-ranked candidates under different selection strategies.

## 📌 Assignment Overview

The Secretary Problem is a decision-making problem in which candidates are evaluated one at a time. The goal is to select a strong candidate without being able to return to previously rejected candidates.

This project uses Monte Carlo simulation to investigate how the initial observation period affects the probability of selecting one of the top-ranked candidates.

## 🎯 Objectives

- Simulate random candidate interview orders.
- Estimate selection success probabilities for different sample sizes.
- Identify the sample size that produces the highest empirical success rate.
- Compare results for different values of `s`.
- Visualize the simulation results using Python.

## ⚙️ Simulation Setup

| Parameter | Value |
|---|---|
| Total candidates (`n`) | 100 |
| Simulation runs | 200,000 |
| Random seed | 42 |
| Values of `s` | 1, 3, 5, 10 |
| Sample size (`m`) | 0–99 |

Here, `s` represents the number of top-ranked candidates counted as a successful selection, while `m` represents the number of candidates observed before making a selection.

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib

## 📊 Results

The simulation estimates the following best sample sizes:

| `s` | Best sample size (`m`) | Success rate |
|---:|---:|---:|
| 1 | 35 | 36.978% |
| 3 | 26 | 60.561% |
| 5 | 21 | 70.512% |
| 10 | 14 | 81.561% |

These are empirical estimates obtained from the simulation.

## 📈 Visualization

The project generates a graph comparing estimated success probabilities across sample sizes for all four values of `s`.

**Graph:** `secretary_problem_success_rates.png`

## 📁 Project Structure

```text
secretary-problem-monte-carlo/
│
├── assignment2.py
├── README.md
├── requirements.txt
├── secretary_problem_results.csv
├── secretary_problem_optima.csv
└── secretary_problem_success_rates.png
```

- `assignment2.py` — Python simulation script.
- `requirements.txt` — Required Python libraries.
- `secretary_problem_results.csv` — Estimated success rates for different sample sizes.
- `secretary_problem_optima.csv` — Best sample size and corresponding success rate for each `s`.
- `secretary_problem_success_rates.png` — Visualization of the simulation results.

## 🚀 How to Run

### 1. Install Python

Install Python 3 from the official website:

https://www.python.org/downloads/

### 2. Clone or Download the Repository

Clone the repository using Git:

```bash
git clone https://github.com/sadman-sirajee/secretary-problem-monte-carlo.git
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

### 3. Open the Project Folder

Open a terminal or command prompt inside the project folder.

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the Simulation

```bash
python assignment2.py
```

The script runs the simulation, prints the summary results, and generates the output files.

## 🧠 Key Takeaway

Monte Carlo simulation helps estimate the performance of decision-making strategies through repeated random experiments. The results illustrate how the definition of a successful selection and the size of the initial observation period influence the estimated success probability.

## 👨‍💻 Author

**Sadman Sirajee**

GitHub: https://github.com/sadman-sirajee

