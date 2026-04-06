#!/usr/bin/env python3
import time
import matplotlib.pyplot as plt
from subsequence import hvlcs

charVal = {'a': 2, 'b': 4, 'c': 5, 'd': 3, 'e': 1}

tests = [
    ("abcdeabcde" * 3,    "edcbaedcba" * 3),
    ("abcdeabcde" * 5,    "edcbaedcba" * 5),
    ("abcdeabcde" * 10,   "edcbaedcba" * 10),
    ("abcdeabcde" * 15,   "edcbaedcba" * 15),
    ("abcdeabcde" * 20,   "edcbaedcba" * 20),
    ("abcdeabcde" * 30,   "edcbaedcba" * 30),
    ("abcdeabcde" * 40,   "edcbaedcba" * 40),
    ("abcdeabcde" * 50,   "edcbaedcba" * 50),
    ("abcdeabcde" * 75,   "edcbaedcba" * 75),
    ("abcdeabcde" * 100,  "edcbaedcba" * 100),
]

lengths = []
times = []

print(f"{'Test':<6} {'Length':<10} {'Time (ms)':<10}")
print("-" * 30)

for i, (A, B) in enumerate(tests, 1):
    start = time.perf_counter()
    value, subseq = hvlcs(A, B, charVal)
    elapsed = (time.perf_counter() - start) * 1000
    lengths.append(len(A))
    times.append(elapsed)
    print(f"{i:<6} {len(A):<10} {elapsed:<10.2f}")

# generate graph
plt.plot(lengths, times, 'o-')
plt.xlabel("String Length")
plt.ylabel("Runtime (ms)")
plt.title("HVLCS Runtime vs Input Size")
plt.savefig("data/runtime_chart.png")
print("\nGraph saved to data/runtime_chart.png")