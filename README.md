# ALP-ttbar Toy MC v2.8 — Preregistration: Trimmed Tag Estimator as Default

Preregistration for v2.8 of the ALP-ttbar Toy MC series: adopting trimmed Tag (k=1%) as the default discriminator. Tests whether the 45-fold CV reduction found in v2.7 translates to improved degradation ratios across the 50-seed ensemble at 17 and 200 MeV.

**DOI:** [10.5281/zenodo.24414960](https://doi.org/10.5281/zenodo.24414960)

## Context

The v2.7 Tag Formula Diagnostics study revealed that:
- 99.84% of Tag variance originates from conversion-vertex randomness, not signal
- Trimming the extreme 1% tails of the per-vertex λ distribution reduces Tag CV from 5.80% to 0.13% (a 45-fold improvement)
- Winsorising the same fraction backfires (CV → 7.35%)
- The mean degradation ratio improves from 1.5549 (untrimmed) to 1.0644 (trimmed k=1%)

This preregistration formally adopts trimmed Tag (k=1%) as the primary discriminator and tests the robustness of these improvements.

## Predictions (9 total)

| ID | Description | Criterion | Mass |
|----|-------------|-----------|------|
| S1 | Trimmed CV ≪ untrimmed | CV(trim) < CV(untrim)/10 | 17 MeV |
| S2 | Trimmed CV near HV level | CV(trim) < 1% | 17 MeV |
| S3 | Trim negligible at 200 MeV | \|ΔCV\| < 0.1% | 200 MeV |
| D1 | Trimmed mean deg < untrimmed | mean(deg_T) < mean(deg_U) | 17 MeV |
| D2 | Trimmed mean deg near ideal | mean(deg_T) < 1.2 | 17 MeV |
| D3 | Trimming improves >80% seeds | frac(deg_T<deg_U) > 0.8 | 17 MeV |
| D4 | Deg ratio unchanged at 200 MeV | \|Δmean(deg)\| < 0.05 | 200 MeV |
| X1 | Optimal threshold shifts | median \|Δt_opt\| > 0 | 17 MeV |
| X2 | Improvement uniform across seeds | CV(Δdeg) < 50% | 17 MeV |

Core predictions: {S1, S2, D1, D2, D3}.

## Future Directions (§9, ordered by feasibility)

Seven follow-up directions from the v2.7 roadmap plus two newly identified studies:

1. **§9.1 Background-Focused Diagnostics** — Per-seed B breakdown, near-band vs inter-band decomposition, N_conv scaling test. Achievable on existing outputs with minimal code.
2. **§9.2 Signal-Side λ Regularisation** — Regularise p_conv floor to reduce extreme signal-vertex λ tail. Code changes within current framework.
3. **§9.3 Extension to Other Configurations** — Scan f ∈ {0.10, 0.25, 0.50, 1.00} and broader mass grid (5–500 MeV) to map conversion-dominated regime.
4. **§9.4 Alternative Discriminator Architectures** — Hybrid discriminators combining Tag sensitivity with HV stability.
5. **§9.5 Dimuon Control Sample** *(new)* — ALP → μ⁺μ⁻ as control channel; muons traverse material without Bremsstrahlung, isolating material-interaction bias from kinematic effects.
6. **§9.6 GSF Tracking** *(new)* — Extend to hit → track → vertex pipeline with Gaussian-Sum Filter reconstruction; substantial extension.
7. **§9.7 Preregistration Lessons** — Direction-agnostic predictions and refutation-aware success criteria.

## Configuration

- E3: f = 0.25, η = 2.0, 17-band geometry (9 sensor disks + 8 service bands)
- 50-seed ensemble, i = 50–99 (SEED_CONV = 100i+5, SEED_SIG = 100i+11); independent from v2.7's i = 0–49
- Up to N_sig = 50,000 signal vertices, up to N_conv = 100,000 conversion vertices per seed
- Focus masses: 17 MeV and 200 MeV

## Reproduction

### Dependencies

```
pip install matplotlib numpy reportlab pypdf
```

The PDF generation script requires **DejaVu Sans** TrueType fonts (Regular, Bold, Oblique, BoldOblique) installed on the system. On Debian/Ubuntu:

```
sudo apt install fonts-dejavu-core
```

### Execution Order

```bash
# 1. Generate motivational figures from v2.7 data
python generate_figures.py

# 2. Generate the preregistration PDF (requires the PNGs from step 1)
python generate_v28_prereg.py
```

All paths are relative to the script directory — no hardcoded absolute paths.

## Files

- `ALP-ttbar_Toy-MC_v2.8_Preregistration_Trimmed-Tag-Estimator-as-Default_2026-11-21.pdf` — Preregistration document (8 pages, with figures)
- `generate_v28_prereg.py` — PDF generation script (ReportLab)
- `generate_figures.py` — Matplotlib script for v2.7 motivational figures
- `fig1_cv_comparison.png` — Figure 1: Tag CV comparison across methods (v2.7 data)
- `fig2_deg_ratio_comparison.png` — Figure 2: Mean degradation ratio comparison (v2.7 data)
- `frozen/endcap_sim.py` — Simulation engine (frozen since v2.5)
- `frozen/mtag_v24.py` — Tag formula, 17-band (frozen since v2.4)
- `frozen/mtag_v22.py` — 9-band baseline (frozen since v2.2)

### Frozen File Provenance

The `frozen/` directory contains simulation modules carried forward from earlier versions. These files are identical to the versions archived in the v2.7 post-registration repository (DOI: [10.5281/zenodo.24408990](https://doi.org/10.5281/zenodo.24408990)).

| File | MD5 | Frozen Since |
|------|-----|-------------|
| `frozen/endcap_sim.py` | `7daa81b2723a1c13df68ee69b428c2d0` | v2.5 |
| `frozen/mtag_v24.py` | `39451a2189d71ec4a9d5990eacb54c6e` | v2.4 |
| `frozen/mtag_v22.py` | `a687701efe4476a999e27b32341c8c39` | v2.2 |

## File Hashes

**PDF:**
- SHA-256: `30623edbd06a28e1d13a4577823dc94e4e86345dd31c4a0ec75228d7cab3fd82`
- MD5: `592d1b9b1c3b77c4c060bf7d1b90f042`

## DOI Chain

| Version | DOI | Description |
|---------|-----|-------------|
| v2.8 prereg (this) | 10.5281/zenodo.24414960 | Trimmed Tag Estimator prereg |
| v2.7 post-reg | 10.5281/zenodo.24408990 | Tag Formula Diagnostics results |
| v2.7 prereg | 10.5281/zenodo.24388228 | Tag Formula Diagnostics prereg |
| v2.6 post-reg | 10.5281/zenodo.24373115 | Multi-Seed Ensemble results |
| v2.6 prereg | 10.5281/zenodo.24361872 | Multi-Seed Ensemble prereg |
| v2.5 results | 10.5281/zenodo.24341050 | Deconflation post-reg |
| v2.5 prereg | 10.5281/zenodo.24329044 | Deconflation prereg |
| v2.4 results | 10.5281/zenodo.24302619 | 17-band geometry post-reg |
| v2.4 prereg | 10.5281/zenodo.24296796 | 17-band geometry prereg |

## Disclaimer

Independent personal toy study, not affiliated with the authors of arXiv:2610.38932 (Alimena et al., 2026) or arXiv:2306.08686 (Rygaard et al., 2023), nor with the CMS, ATLAS, LHCb or ALICE Collaborations or the FCC study. Detector numbers are assumed; only qualitative trends and ratios are meaningful.

## Author

Won Shik Paik (Independent Researcher, Auckland, New Zealand)
