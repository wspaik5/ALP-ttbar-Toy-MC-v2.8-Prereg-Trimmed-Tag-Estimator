#!/usr/bin/env python3
"""Generate motivational figures for v2.8 Preregistration from v2.7 results."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import os

# --- Style setup ---
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.linewidth': 0.8,
    'axes.edgecolor': '#444444',
    'axes.labelcolor': '#1a1a1a',
    'xtick.color': '#444444',
    'ytick.color': '#444444',
    'grid.color': '#e0e0e0',
    'grid.linewidth': 0.5,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'savefig.dpi': 220,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.15,
})

# Categorical palette (3 colors: validated visually distinct + CVD safe)
C_UNTRIM = '#2c5f8a'   # blue - untrimmed
C_TRIM   = '#2a9d4e'   # green - trimmed
C_WINSOR = '#d94f3d'   # red - winsorised
C_HV     = '#7b68ae'   # purple - HV reference
C_IDEAL  = '#888888'   # grey - ideal line

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# FIGURE 1: Tag CV Comparison (v2.7 results)
# ============================================================
fig1, ax1 = plt.subplots(figsize=(5.8, 3.8))

methods = ['Untrimmed\nTag', 'Trimmed Tag\n(k = 1%)', 'Winsorised\nTag (k = 1%)', 'HV\n(reference)']
cvs = [5.80, 0.13, 7.35, 0.13]
colors = [C_UNTRIM, C_TRIM, C_WINSOR, C_HV]
bar_width = 0.55

bars = ax1.bar(range(len(methods)), cvs, width=bar_width, color=colors,
               edgecolor='white', linewidth=1.5, zorder=3)

# Direct labels on bars
for bar, cv in zip(bars, cvs):
    h = bar.get_height()
    label = f'{cv:.2f}%'
    if cv < 1:
        # Put label above short bars
        ax1.text(bar.get_x() + bar.get_width()/2, h + 0.25, label,
                ha='center', va='bottom', fontsize=10, fontweight='bold', color='#1a1a1a')
    else:
        # Put label inside tall bars
        ax1.text(bar.get_x() + bar.get_width()/2, h - 0.3, label,
                ha='center', va='top', fontsize=10, fontweight='bold', color='white')

# Annotation: 45× improvement arrow
ax1.annotate('45× reduction',
            xy=(1, 0.13), xytext=(0.3, 3.5),
            fontsize=9, fontweight='bold', color=C_TRIM,
            arrowprops=dict(arrowstyle='->', color=C_TRIM, lw=1.5),
            ha='center')

# Annotation: Winsorising backfires
ax1.annotate('Backfires\n(+27%)',
            xy=(2, 7.35), xytext=(2.7, 6.0),
            fontsize=8, fontstyle='italic', color=C_WINSOR,
            arrowprops=dict(arrowstyle='->', color=C_WINSOR, lw=1.2),
            ha='center')

ax1.set_xticks(range(len(methods)))
ax1.set_xticklabels(methods, fontsize=9)
ax1.set_ylabel('Coefficient of Variation (%)', fontsize=10)
ax1.set_title('Tag CV Across 50-Seed Ensemble at 17 MeV\n(v2.7 Post-Registration Results)',
              fontsize=11, fontweight='bold', color='#1a1a1a', pad=10)

ax1.set_ylim(0, 9)
ax1.yaxis.set_major_locator(mticker.MultipleLocator(1))
ax1.grid(axis='y', zorder=0, alpha=0.7)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Source note
ax1.text(0.5, -0.18, 'Source: v2.7 Post-Registration (DOI: 10.5281/zenodo.24408990)',
         transform=ax1.transAxes, fontsize=7, color='#888888', ha='center', style='italic')

fig1.tight_layout()
fig1.savefig(f'{OUT_DIR}/fig1_cv_comparison.png')
plt.close(fig1)
print("Figure 1 saved: fig1_cv_comparison.png")


# ============================================================
# FIGURE 2: Degradation Ratio Comparison (v2.7 results)
# ============================================================
fig2, ax2 = plt.subplots(figsize=(5.8, 3.8))

methods2 = ['Untrimmed Tag', 'Trimmed Tag\n(k = 1%)', 'HV\n(reference)']
deg_ratios = [1.5549, 1.0644, 1.0576]
colors2 = [C_UNTRIM, C_TRIM, C_HV]

bars2 = ax2.bar(range(len(methods2)), deg_ratios, width=0.50, color=colors2,
                edgecolor='white', linewidth=1.5, zorder=3)

# Ideal line at 1.0
ax2.axhline(y=1.0, color=C_IDEAL, linestyle='--', linewidth=1.2, zorder=2, label='Ideal (no degradation)')
ax2.text(len(methods2) - 0.3, 1.015, 'Ideal = 1.0', fontsize=8, color=C_IDEAL,
         ha='right', va='bottom', style='italic')

# Direct labels
for bar, deg in zip(bars2, deg_ratios):
    h = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, h + 0.015, f'{deg:.4f}',
            ha='center', va='bottom', fontsize=10, fontweight='bold', color='#1a1a1a')

# Annotation: improvement
ax2.annotate('',
            xy=(1, 1.0644), xycoords='data',
            xytext=(0, 1.5549), textcoords='data',
            arrowprops=dict(arrowstyle='<->', color='#333333', lw=1.2))
ax2.text(-0.15, 1.31, '−31.5%', fontsize=9, fontweight='bold', color='#333333',
         ha='center', rotation=90)

ax2.set_xticks(range(len(methods2)))
ax2.set_xticklabels(methods2, fontsize=9.5)
ax2.set_ylabel('Mean Degradation Ratio', fontsize=10)
ax2.set_title('Mean Degradation Ratio at 17 MeV\n(v2.7 Post-Registration Results)',
              fontsize=11, fontweight='bold', color='#1a1a1a', pad=10)

ax2.set_ylim(0.9, 1.7)
ax2.yaxis.set_major_locator(mticker.MultipleLocator(0.1))
ax2.grid(axis='y', zorder=0, alpha=0.7)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# Source note (positioned below x-labels to avoid overlap)
ax2.text(0.5, -0.22, 'Source: v2.7 Post-Registration (DOI: 10.5281/zenodo.24408990)',
         transform=ax2.transAxes, fontsize=7, color='#888888', ha='center', style='italic')

fig2.tight_layout()
fig2.savefig(f'{OUT_DIR}/fig2_deg_ratio_comparison.png')
plt.close(fig2)
print("Figure 2 saved: fig2_deg_ratio_comparison.png")

print("\nBoth figures generated successfully.")
