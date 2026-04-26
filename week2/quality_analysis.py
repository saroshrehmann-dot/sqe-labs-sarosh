# week2/quality_analysis.py
"""
ISO 25010 Quality Attribute Analysis
SQE Lab 2 — Comparative Analysis Script
"""

import numpy as np
import matplotlib.pyplot as plt

# ── Configuration ───────────────────────────────────────────────
APP1_NAME = "Google Maps"
APP2_NAME = "Apple Maps"
EVALUATOR = "Sarosh Rehman"

# ── Quality Characteristics ────────────────────────────────────
CHARACTERISTICS = [
    "Functional\nSuitability",
    "Performance\nEfficiency",
    "Compatibility",
    "Usability",
    "Reliability",
    "Security",
    "Maintainability",
    "Portability"
]

# Weight values must total = 1.0
WEIGHTS = [0.15, 0.12, 0.10, 0.15, 0.15, 0.15, 0.08, 0.10]

# ── Ratings (1 to 5 scale) ────────────────────────────────────
# Order:
# Functional Suitability, Performance Efficiency,
# Compatibility, Usability, Reliability,
# Security, Maintainability, Portability

APP1_RATINGS = [5, 5, 5, 5, 5, 5, 4, 5]   # Google Maps
APP2_RATINGS = [3, 3, 4, 3, 5, 5, 2, 4]   # Apple Maps

# ── Validation ────────────────────────────────────────────────
assert len(APP1_RATINGS) == 8, "Must have exactly 8 ratings for App 1"
assert len(APP2_RATINGS) == 8, "Must have exactly 8 ratings for App 2"

assert all(1 <= r <= 5 for r in APP1_RATINGS), "Ratings must be between 1 and 5"
assert all(1 <= r <= 5 for r in APP2_RATINGS), "Ratings must be between 1 and 5"

assert abs(sum(WEIGHTS) - 1.0) < 0.001, "Weights must sum to 1.0"


# ── Score Calculation ─────────────────────────────────────────
def weighted_score(ratings, weights):
    """Calculate weighted score."""
    return sum(r * w for r, w in zip(ratings, weights))


app1_score = weighted_score(APP1_RATINGS, WEIGHTS)
app2_score = weighted_score(APP2_RATINGS, WEIGHTS)


# ── Print Report ──────────────────────────────────────────────
print("=" * 60)
print("ISO 25010 Quality Attribute Analysis Report")
print("=" * 60)
print(f"Evaluator : {EVALUATOR}")
print(f"App 1     : {APP1_NAME}")
print(f"App 2     : {APP2_NAME}")
print("=" * 60)

print(f"{'Characteristic':<30}{APP1_NAME:>12}{APP2_NAME:>12}{'Weight':>10}")
print("-" * 60)

for char, r1, r2, w in zip(CHARACTERISTICS, APP1_RATINGS, APP2_RATINGS, WEIGHTS):
    label = char.replace("\n", " ")
    print(f"{label:<30}{r1:>12}{r2:>12}{w:>9.0%}")

print("-" * 60)
print(f"{'WEIGHTED TOTAL':<30}{app1_score:>12.2f}{app2_score:>12.2f}")
print("=" * 60)

# Winner
winner = APP1_NAME if app1_score > app2_score else APP2_NAME
margin = abs(app1_score - app2_score)

print(f"\nOverall Higher Quality: {winner}")
print(f"Margin Difference     : {margin:.2f}")

# Biggest gaps
gaps = []

for char, r1, r2 in zip(CHARACTERISTICS, APP1_RATINGS, APP2_RATINGS):
    gaps.append((abs(r1 - r2), char.replace("\n", " "), r1, r2))

gaps.sort(reverse=True)

print("\nLargest Quality Gaps:")
for diff, char, r1, r2 in gaps[:3]:
    if r1 > r2:
        better = APP1_NAME
    elif r2 > r1:
        better = APP2_NAME
    else:
        better = "Tied"

    print(f"{char}: Gap = {diff}, Better = {better}")


# ── Radar Chart ───────────────────────────────────────────────
def plot_radar_chart(app1_name, app2_name, app1_ratings, app2_ratings,
                     characteristics, app1_score, app2_score):

    N = len(characteristics)

    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]

    values1 = app1_ratings + [app1_ratings[0]]
    values2 = app2_ratings + [app2_ratings[0]]

    fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))

    # Fill areas
    ax.fill(angles, values1, alpha=0.25, label=app1_name)
    ax.fill(angles, values2, alpha=0.25, label=app2_name)

    # Borders
    ax.plot(angles, values1, linewidth=2,
            label=f"{app1_name} ({app1_score:.2f})")

    ax.plot(angles, values2, linewidth=2,
            label=f"{app2_name} ({app2_score:.2f})")

    # Axis labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(characteristics, fontsize=10)

    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"])
    ax.set_ylim(0, 5)

    # Title
    plt.title(
        f"ISO 25010 Quality Profile Comparison\n{app1_name} vs {app2_name}",
        size=14,
        pad=20
    )

    # Legend
    plt.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))

    # Save chart
    filename = f"quality_radar_{app1_name}_{app2_name}.png".replace(" ", "_")
    plt.savefig(filename, dpi=150, bbox_inches="tight")

    print(f"\nRadar chart saved as: {filename}")

    plt.show()


# Run chart function
plot_radar_chart(
    APP1_NAME,
    APP2_NAME,
    APP1_RATINGS,
    APP2_RATINGS,
    CHARACTERISTICS,
    app1_score,
    app2_score
)