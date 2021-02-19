import csv
from collections import Counter

with open('data.csv', newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

n = len(new_data)
total = 0
for x in new_data:
    total += x
mean = total / n
print(mean)

new_data.sort()
if (n % 2 == 0):
    f_n = int(n//2)
    s_n = int(n//2 + 1)
    f = float(new_data[f_n])
    s = float(new_data[s_n])
    median = (f + s)/2
    print(str(median))
else:
    num = n//2
    median = float(new_data[num])
    print(str(median))
le = str(len(new_data))
print(le)
lo = new_data[0]
print(lo)
newData = Counter(new_data)
values = newData.values()
data = Counter(new_data)
mode_data_for_range = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0
}
for weight, occourrence in data.items():
    if 50 < float(weight) < 60:
        mode_data_for_range["50-60"] += occourrence
    elif 60 < float(weight) < 70:
        mode_data_for_range["60-70"] += occourrence
    elif 70 < float(weight) < 80:
        mode_data_for_range["70-80"] += occourrence
modeRange, modeOccourence = 0, 0
for range, occourrence in mode_data_for_range.items():
    if(occourrence > modeOccourence):
        modeRange, modeOccourence = [
            int(range.split("-")[0]), int(range.split("-")[1])], occourrence
        mode = float((modeRange[0] + modeRange[1]) / 2)
        print(mode)
