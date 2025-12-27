import csv

input_file = "data.txt"
output_file = "data.csv"

f = open(input_file, "r", encoding="utf-8", errors="ignore")
g = open(output_file, "w", newline="", encoding="utf-8")
writer = csv.writer(g)

# write header
writer.writerow([
    "freq",
    "stage1_db", "stage1_deg",
    "stage2_db", "stage2_deg",
    "stage3_db", "stage3_deg"
])


f.readline()

for line in f:
    clean = line.replace("dB", "").replace("(", "").replace(")", "")
    clean = ",".join(clean.split())
    parts = clean.split(",")
    writer.writerow(parts)

f.close()
g.close()

