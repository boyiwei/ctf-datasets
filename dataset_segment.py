import json
import math

# Load JSON data from file

json_name = "Intercode_CTF/intercode_dataset"
with open(f"{json_name}.json", 'r') as f:
    data = json.load(f)

# Assuming data is a list, determine the size of each segment
n = len(data)
segment_size = math.ceil(n /5)
keys = list(data.keys())
# Split and save each segment
num_segments = (len(keys) + segment_size - 1) // segment_size

# Split and save each segment
for i in range(num_segments):
    segment_keys = keys[i * segment_size:(i + 1) * segment_size]
    segment = {k: data[k] for k in segment_keys}
    with open(f'{json_name}_segment{num_segments}_{i+1}.json', 'w') as out_file:
        json.dump(segment, out_file, indent=2)