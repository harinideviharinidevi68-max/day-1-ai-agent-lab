"""Day 2: Self-Consistency experiment."""

import sys
from pathlib import Path
from collections import Counter

# Use config.py from Day 1
DAY1_FOLDER = Path(__file__).resolve().parent.parent / "day 1"
sys.path.insert(0, str(DAY1_FOLDER))

from config import client, MODEL, banner
from cot_compare import COT_PROMPT, QUESTIONS


RUNS = 5
TEMPERATURE = 0.8


def final_answer(text):
    for line in reversed(text.splitlines()):
        if "final answer" in line.lower():
            return line.split(":", 1)[-1].strip()

    return text.splitlines()[-1].strip() if text.strip() else "(empty)"


def run_many(question):
    answers = []

    for attempt in range(1, RUNS + 1):
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": COT_PROMPT},
                {"role": "user", "content": question},
            ],
            temperature=TEMPERATURE,
        )

        output = response.choices[0].message.content.strip()
        answer = final_answer(output)

        print(f"Run {attempt}: {answer}")
        answers.append(answer)

    return answers


if __name__ == "__main__":
    banner("SELF-CONSISTENCY")

    question = QUESTIONS[0]

    print("QUESTION:")
    print(question)
    print()

    answers = run_many(question)

    winner, count = Counter(answers).most_common(1)[0]

    print()
    print(f"Majority answer ({count} of {RUNS} runs): {winner}")