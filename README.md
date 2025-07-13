# basic-stats


BasicStats is a lightweight pure Python class for calculating fundamental statistical measures from a list of numbers.

It requires no external dependencies and supports:
	•	Mean
	•	Median
	•	Mode
	•	Min / Max
	•	Range
	•	Sample Variance
	•	Sample Standard Deviation

```python
from basic_stats.utils import BasicStats

data = [2, 4, 4, 4, 5, 5, 7, 9]
stats = BasicStats(data)

print("Mean:", stats.mean())
print("Median:", stats.median())
print("Mode:", stats.mode())
print("Min:", stats.min())
print("Max:", stats.max())
print("Range:", stats.rn())
print("Variance:", stats.variance())
print("Standard Deviation:", stats.std_deviation())
```