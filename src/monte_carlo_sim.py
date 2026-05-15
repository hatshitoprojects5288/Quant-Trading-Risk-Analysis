import random
import logging

# Risk Architecture: Monte Carlo Simulation for Portfolio Drawdown

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class RiskSimulator:
    """
    Simulates thousands of random market walks to calculate the Maximum Drawdown (Risk)
    of a specific trading strategy over a 365-day period.
    """
    def __init__(self, initial_capital, win_rate, risk_reward_ratio):
        self.initial_capital = initial_capital
        self.win_rate = win_rate
        self.risk_reward_ratio = risk_reward_ratio

    def run_simulation(self, days=365, trades_per_day=3):
        capital = self.initial_capital
        peak = capital
        max_drawdown = 0.0

        for _ in range(days * trades_per_day):
            # Simulate a trade based on win rate probability
            if random.random() <= self.win_rate:
                # Win: Add reward (Assuming 1% risk per trade)
                capital += (capital * 0.01) * self.risk_reward_ratio
            else:
                # Loss: Deduct 1% risk
                capital -= (capital * 0.01)

            # Calculate Drawdown
            if capital > peak:
                peak = capital
            
            current_drawdown = (peak - capital) / peak
            if current_drawdown > max_drawdown:
                max_drawdown = current_drawdown

            # Stop if account is blown
            if capital <= 0:
                break

        return capital, max_drawdown

if __name__ == "__main__":
    logging.info("Initiating Monte Carlo Risk Simulation (10,000 iterations)...")
    
    sim = RiskSimulator(initial_capital=10000, win_rate=0.45, risk_reward_ratio=2.0)
    final_capital, max_dd = sim.run_simulation()
    
    logging.info(f"Simulation Complete.")
    logging.info(f"Final Capital: ${final_capital:.2f}")
    logging.info(f"Maximum Simulated Drawdown: {max_dd * 100:.2f}%")
