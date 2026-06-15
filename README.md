# phishing-diploma-project
Game-theoretic and machine learning models for phishing attack analysis.
# Phishing Diploma Project

This repository contains the implementation modules used in a diploma thesis on phishing attack modeling and analysis.

The project combines two complementary approaches:

1. a game-theoretic attacker–defender simulation;
2. a machine learning phishing email detector.

## Modules

### phishing-game-simulation

Python simulation of a simplified attacker–defender game model for phishing email scenarios.

The module calculates mixed equilibrium probabilities in a reduced 2x2 game and performs sensitivity analysis with respect to key parameters such as:

- `p` – probability that an email is phishing;
- `L` – loss/damage in case of compromise.

### ai-phishing-kaggle

Machine learning phishing email detector based on TF-IDF text representation and Logistic Regression.

The module classifies emails as legitimate or phishing and provides a phishing probability score.

## Purpose

The repository is intended for academic demonstration as part of a diploma thesis.  
The game-theoretic simulation is the main modeling component, while the machine learning module is used as an additional practical demonstration of phishing risk estimation.

## Author

Kalin Gerdzhikov
