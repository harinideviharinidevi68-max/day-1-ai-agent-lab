"""Day 2: Print the real ReAct agent trace."""

import sys
from pathlib import Path

# Access the agent.py from the Day 1 folder
DAY1_FOLDER = Path(__file__).resolve().parent.parent / "day 1"
sys.path.insert(0, str(DAY1_FOLDER))

from agent import agent


QUESTION = (
    "Which is cheaper: CS101 and AI202 with a 10% scholarship, "
    "or all three courses with a 25% scholarship? By how much?"
)

print("QUESTION:", QUESTION, "\n")
print("--- the agent's actions and observations ---")

answer = agent(QUESTION, max_steps=8)

print("\nFINAL ANSWER:", answer)