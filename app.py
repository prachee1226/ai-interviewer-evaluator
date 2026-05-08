import json

def calculate_score(accuracy, depth, clarity):
    # This is "Normalization"
    # We give Accuracy 50% of the weight, Depth 30%, and Clarity 20%
    final = (accuracy * 0.5) + (depth * 0.3) + (clarity * 0.2)
    return round(final, 2)

print("--- AI INTERVIEWER EVALUATOR ---")

# Inputs from the terminal
question = input("Question asked: ")
answer = input("Candidate's answer: ")

# Simulated AI Decomposition (We will connect real AI next)
# For now, let's pretend the AI gave us these numbers
acc = 8  # Accuracy
dep = 4  # Depth
cla = 9  # Clarity

total = calculate_score(acc, dep, cla)

print(f"\n--- Results ---")
print(f"Correctness: {acc}/10")
print(f"Depth:       {dep}/10")
print(f"Clarity:     {cla}/10")
print(f"FINAL SCORE: {total}/10")