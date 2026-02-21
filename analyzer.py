
---

## ✅ Full Safe Working Implementation

### `analyzer.py`
```python
from collections import Counter

def analyze_log(file_path):
    levels = Counter()

    with open(file_path, "r") as f:
        for line in f:
            if "ERROR" in line:
                levels["ERROR"] += 1
            elif "WARNING" in line:
                levels["WARNING"] += 1
            elif "INFO" in line:
                levels["INFO"] += 1

    return levels
