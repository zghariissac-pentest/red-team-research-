import random
import string

def mutate_string(s: str, rounds: int = 3) -> str:
    mutated = s
    for _ in range(rounds):
        mutated = "".join(
            chr((ord(c) + random.randint(1, 3)) % 126)
            if c.isalpha()
            else c
            for c in mutated
        )
    return mutated

def add_noise(s: str, strength: int = 2) -> str:
    noise_chars = string.punctuation + string.ascii_letters
    noise = "".join(random.choice(noise_chars) for _ in range(strength))
    return noise + s + noise

def main():
    sample = "ThisIsASampleString"
    print("Original:", sample)

    mutated = mutate_string(sample)
    noisy = add_noise(mutated)

    print("Mutated:", mutated)
    print("With noise:", noisy)
    print("Educational only. No bypass functionality.")

if __name__ == "__main__":
    main()

