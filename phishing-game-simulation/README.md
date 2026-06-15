# Phishing Game Simulation

This repository contains a Python simulation for a simplified **attacker–defender game model** applied to phishing email scenarios.

The project is part of a diploma thesis on:

**"Game-theoretic model of phishing attacks: attacker–defender interaction"**

The main goal of the script is to demonstrate how mixed equilibrium probabilities can change when key model parameters are varied.

---

## Overview

The simulation models a phishing interaction between two players:

### Attacker strategies

* **S1 – Mass phishing**
  Low-cost phishing campaign with lower personalization.

* **S3 – Spear-phishing**
  More targeted and costly phishing attack with higher potential effectiveness.

### Defender strategies

* **D2 – Opens the email, but does not click**
  The user reads the email but avoids interacting with suspicious links or forms.

* **D3 – Clicks / submits data**
  The user interacts with the phishing content, which creates a higher risk of compromise.

The implemented simulation focuses on a reduced 2x2 subgame:

[
{S_1, S_3} \times {D_2, D_3}
]

---

## What the script does

The script:

1. Defines payoff functions for the attacker and defender.
2. Calculates mixed equilibrium probabilities for the reduced 2x2 game.
3. Performs sensitivity analysis with respect to:

   * `p` – probability that the email is phishing;
   * `L` – loss/damage for the defender in case of compromise.
4. Prints numerical equilibrium values in the terminal.
5. Generates and saves equilibrium graphs as PNG files.

---

## Model parameters

The script uses normalized parameters for demonstration and analysis:

* `G[i]` – gain for the attacker if strategy `Si` succeeds;
* `C[i]` – cost of preparing attack strategy `Si`;
* `L` – defender loss in case of compromise;
* `c` – small operational cost for checking/opening without clicking;
* `m` – cost of ignoring a legitimate email;
* `alpha[i]` – success probability when the user opens without clicking;
* `beta[i]` – success probability when the user clicks/submits data;
* `p` – probability that the email is phishing.

The values are not intended to represent exact real-world measurements. They are normalized in order to demonstrate the strategic behavior of the model.

---

## Mixed equilibrium calculation

The mixed equilibrium is calculated using indifference conditions.

Let:

[
x = P(S_1), \quad 1-x = P(S_3)
]

and:

[
y = P(D_2), \quad 1-y = P(D_3)
]

The defender's mixed strategy is chosen so that the attacker is indifferent between the active attacker strategies.
The attacker's mixed strategy is chosen so that the defender is indifferent between the active defender strategies.

Only valid equilibrium points are kept, meaning:

[
0 \le x \le 1, \quad 0 \le y \le 1
]

---

## Generated output

When the script is executed, it prints tables similar to:

```text
Sensitivity with respect to p

p      P(S1)    P(S3)    P(D2)    P(D3)
0.20   0.167    0.833    0.800    0.200
0.25   0.500    0.500    0.800    0.200
0.30   0.722    0.278    0.800    0.200
...
```

It also saves the following figures:

* `attacker_equilibrium_vs_p.png`
* `defender_equilibrium_vs_p.png`
* `defender_equilibrium_vs_L.png`
* `attacker_equilibrium_vs_L.png`

---

## Requirements

The script requires:

```bash
numpy
matplotlib
```

Install the required packages with:

```bash
pip install numpy matplotlib
```

or, if a `requirements.txt` file is included:

```bash
pip install -r requirements.txt
```

---

## How to run

Clone the repository or download the script, then run:

```bash
python phishing_sim.py
```

The script will:

1. print the numerical equilibrium results;
2. display the graphs;
3. save the graphs as PNG files in the project folder.

---

## Files

Suggested repository structure:

```text
phishing-game-simulation/
│
├── phishing_sim.py
├── README.md
└── requirements.txt
```

If output graphs are included:

```text
phishing-game-simulation/
│
├── phishing_sim.py
├── README.md
├── requirements.txt
└── outputs/
    ├── attacker_equilibrium_vs_p.png
    ├── defender_equilibrium_vs_p.png
    ├── defender_equilibrium_vs_L.png
    └── attacker_equilibrium_vs_L.png
```

---

## Notes

This project is a simplified academic simulation. The model is intended for analysis and visualization of strategic behavior, not for direct deployment as a real-world phishing detection system.

The main focus is the game-theoretic interpretation of the phishing interaction and the effect of changing parameters on mixed equilibrium strategies.

---

## Author

Kalin Gerdzhikov
