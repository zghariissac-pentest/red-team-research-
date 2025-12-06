"""
phishing-mailer.py

Purpose: Email phishing awareness simulator.
This tool does NOT send real emails.

Focus:
- Teach detection of phishing patterns
- Simulate safe awareness campaigns
"""

class PhishingAwarenessSimulator:
    def __init__(self):
        self.templates = []

    def load_template(self, subject, body):
        """Load simulated phishing template for training."""
        self.templates.append((subject, body))

    def simulate_campaign(self):
        """Display simulated phishing messages safely."""
        for idx, tpl in enumerate(self.templates):
            print(f"\n--- Simulation Email {idx + 1} ---")
            print(f"Subject: {tpl[0]}")
            print(f"Body:\n{tpl[1]}")

if __name__ == "__main__":
    sim = PhishingAwarenessSimulator()
    sim.load_template(
        "Security Awareness Test",
        "This is a simulated phishing example for training purposes."
    )
    sim.simulate_campaign()

