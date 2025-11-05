import os
from collections import Counter

label_dir = r"C:\d_drive\traffic_violation\combined\train\labels"

counter = Counter()
for file in os.listdir(label_dir):
    if file.endswith(".txt"):
        with open(os.path.join(label_dir, file)) as f:
            for line in f:
                if line.strip():
                    cls = int(line.split()[0])
                    counter[cls] += 1

print("Class counts in training labels:")
for cls_id, count in sorted(counter.items()):
    print(f"Class {cls_id}: {count} labels")
