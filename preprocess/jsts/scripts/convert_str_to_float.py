import json
import sys

for line in sys.stdin:
    data = json.loads(line.strip())
    data["label"] = float(data["label"])
    print(json.dumps(data, ensure_ascii=False))