# Quantitative Trading & Risk Analysis
**Maintainer:** JOSHUA SAMAL | Digital Infrastructure  
**Domain:** Quantitative Finance, Data Engineering & Risk Modeling  
**Tech Stack:** Python 3.x, REST APIs, Monte Carlo Simulation  

## 📌 Project Overview
This repository contains the data architecture and mathematical models required for quantitative trading and risk analysis. It focuses on programmatically ingesting raw OHLCV (Open, High, Low, Close, Volume) market data, transforming it for algorithmic backtesting, and running probabilistic risk models to determine maximum portfolio drawdown.

## 📂 Repository Structure
* `/src/data_ingestion.py` - API pipeline for fetching historical market data.
* `/src/monte_carlo_sim.py` - Mathematical risk engine simulating thousands of random market walks.
* `/data/backtest_results.csv` - Tabular outputs of algorithmic trading logic for further analysis.

## ⚙️ Core Engineering Principles
1. **Data Pipeline Integrity:** Ensuring clean, continuous data ingestion from external REST APIs with robust error handling.
2. **Probabilistic Risk Modeling:** Moving beyond static backtests by using Monte Carlo simulations to stress-test trading strategies against extreme market volatility.
3. **Algorithmic Logic:** Utilizing strict Python assertions and mathematical rules (Win Rate vs. Risk/Reward) to eliminate emotional bias from trading systems.
