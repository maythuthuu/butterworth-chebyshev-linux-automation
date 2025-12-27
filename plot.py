import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data.csv")

freq = df["freq"]

stage1_deg = np.unwrap(np.deg2rad(df["stage1_deg"])) * 180 / np.pi
stage2_deg = np.unwrap(np.deg2rad(df["stage2_deg"])) * 180 / np.pi
stage3_deg = np.unwrap(np.deg2rad(df["stage3_deg"])) * 180 / np.pi

stage1_db = df["stage1_db"]
stage2_db = df["stage2_db"]
stage3_db = df["stage3_db"]

total_db = stage1_db + stage2_db + stage3_db

plt.semilogx(freq, stage1_db, label="Stage 1", linewidth=2)
plt.semilogx(freq, stage2_db, label="Stage 2", linewidth=2)
plt.semilogx(freq, stage3_db, label="Stage 3", linewidth=2)
plt.grid(True, which="both")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.title("6th-Order Butterworth – Magnitude Response")
plt.legend()
plt.tight_layout()
plt.savefig("magnitude.png", dpi=300)
plt.close()

plt.semilogx(freq, stage1_deg, label="Stage 1", linewidth=2)
plt.semilogx(freq, stage2_deg, label="Stage 2", linewidth=2)
plt.semilogx(freq, stage3_deg, label="Stage 3", linewidth=2)
plt.grid(True, which="both")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (degrees)")
plt.title("6th-Order Butterworth – Phase Response")
plt.legend()
plt.tight_layout()
plt.savefig("phase.png", dpi=300)
plt.close()
