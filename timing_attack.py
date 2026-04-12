import time
import string

# Secret password (unknown to attacker)
SECRET = "s3cur312e"

# Vulnerable password check function
def check_password(user_input):
    for i in range(len(SECRET)):
        if i >= len(user_input) or user_input[i] != SECRET[i]:
            return False
        time.sleep(0.05)  # Delay for each correct character
    return len(user_input) == len(SECRET)

# Measure execution time
def measure_time(guess, trials=3):
    total = 0
    for _ in range(trials):
        start = time.perf_counter()
        check_password(guess)
        end = time.perf_counter()
        total += (end - start)
    return total / trials

# Attack logic
def timing_attack():
    chars = string.ascii_lowercase + string.digits
    guessed = ""

    print("Starting Timing Attack...\n")

    for i in range(len(SECRET)):
        timings = {}

        for c in chars:
            guess = guessed + c
            t = measure_time(guess)
            timings[c] = t

        # Choose character with maximum time
        best_char = max(timings, key=timings.get)
        guessed += best_char

        print(f"Guessed so far: {guessed}")

    print("\nFinal guessed password:", guessed)

# Run attack
if __name__ == "__main__":
    timing_attack()
