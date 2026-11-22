#!/usr/bin/env python3
"""Generate v2.8 Preregistration PDF: Trimmed Tag Estimator as Default Discriminator."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether, Image
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# --- Font setup ---
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("DejaVu", f"{FONT_DIR}/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", f"{FONT_DIR}/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Oblique", f"{FONT_DIR}/DejaVuSans-Oblique.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-BoldOblique", f"{FONT_DIR}/DejaVuSans-BoldOblique.ttf"))

# --- Colors ---
DARK = HexColor("#1a1a1a")
ACCENT = HexColor("#2c5f8a")
LIGHT_BG = HexColor("#f0f4f8")
BORDER = HexColor("#cccccc")
WHITE = HexColor("#ffffff")
GREY = HexColor("#666666")

# --- Styles ---
sTitle = ParagraphStyle("Title", fontName="DejaVu-Bold", fontSize=14.5, leading=18,
                        alignment=TA_CENTER, textColor=ACCENT, spaceAfter=3*mm)
sSubtitle = ParagraphStyle("Sub", fontName="DejaVu", fontSize=9, leading=12,
                           alignment=TA_CENTER, textColor=DARK, spaceAfter=2*mm)
sAuthor = ParagraphStyle("Auth", fontName="DejaVu-Oblique", fontSize=8.5, leading=11,
                         alignment=TA_CENTER, textColor=DARK, spaceAfter=1.5*mm)
sDate = ParagraphStyle("Date", fontName="DejaVu", fontSize=8, leading=10,
                       alignment=TA_CENTER, textColor=GREY, spaceAfter=1*mm)
sDOILine = ParagraphStyle("DOILine", fontName="DejaVu", fontSize=7.5, leading=10,
                          alignment=TA_CENTER, textColor=GREY, spaceAfter=4*mm)
sDisclaimer = ParagraphStyle("Disc", fontName="DejaVu-Oblique", fontSize=7, leading=9.5,
                             alignment=TA_JUSTIFY, textColor=GREY, leftIndent=10*mm,
                             rightIndent=10*mm, spaceBefore=2*mm, spaceAfter=4*mm)
sH1 = ParagraphStyle("H1", fontName="DejaVu-Bold", fontSize=12, leading=15,
                     textColor=ACCENT, spaceBefore=6*mm, spaceAfter=3*mm)
sH2 = ParagraphStyle("H2", fontName="DejaVu-Bold", fontSize=10, leading=13,
                     textColor=ACCENT, spaceBefore=4*mm, spaceAfter=2*mm)
sBody = ParagraphStyle("Body", fontName="DejaVu", fontSize=8.5, leading=12,
                       alignment=TA_JUSTIFY, textColor=DARK, spaceAfter=2*mm)
sBodyBold = ParagraphStyle("BodyBold", fontName="DejaVu-Bold", fontSize=8.5, leading=12,
                           alignment=TA_JUSTIFY, textColor=DARK, spaceAfter=2*mm)
sBullet = ParagraphStyle("Bullet", fontName="DejaVu", fontSize=8.5, leading=12,
                         leftIndent=12, textColor=DARK, bulletIndent=4,
                         bulletFontName="DejaVu", bulletFontSize=8.5, spaceAfter=1*mm)
sCode = ParagraphStyle("Code", fontName="DejaVu", fontSize=7.5, leading=10,
                       textColor=DARK, leftIndent=8*mm, spaceAfter=2*mm,
                       backColor=LIGHT_BG)
sFooter = ParagraphStyle("Footer", fontName="DejaVu", fontSize=7, leading=9,
                         alignment=TA_CENTER, textColor=GREY, spaceBefore=3*mm)
sCaption = ParagraphStyle("Caption", fontName="DejaVu-Oblique", fontSize=7.5, leading=10,
                          alignment=TA_CENTER, textColor=DARK, spaceBefore=1*mm, spaceAfter=3*mm)
sFigLabel = ParagraphStyle("FigLabel", fontName="DejaVu-Bold", fontSize=8, leading=10,
                           alignment=TA_CENTER, textColor=ACCENT, spaceBefore=2*mm, spaceAfter=0.5*mm)

# Figure paths (relative to this script)
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FIG1_PATH = os.path.join(_SCRIPT_DIR, "fig1_cv_comparison.png")
FIG2_PATH = os.path.join(_SCRIPT_DIR, "fig2_deg_ratio_comparison.png")

# Table styles
sTH = ParagraphStyle("TH", fontName="DejaVu-Bold", fontSize=7.5, leading=10,
                     alignment=TA_CENTER, textColor=WHITE)
sTD = ParagraphStyle("TD", fontName="DejaVu", fontSize=7.5, leading=10,
                     alignment=TA_CENTER, textColor=DARK)
sTDL = ParagraphStyle("TDL", fontName="DejaVu", fontSize=7.5, leading=10,
                      alignment=TA_LEFT, textColor=DARK)
sTDB = ParagraphStyle("TDB", fontName="DejaVu-Bold", fontSize=7.5, leading=10,
                      alignment=TA_CENTER, textColor=DARK)

def make_table(header, rows, col_widths):
    """Create a styled table."""
    all_rows = [header] + rows
    t = Table(all_rows, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), ACCENT),
        ('BACKGROUND', (0, 1), (-1, -1), LIGHT_BG),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))
    return t


# --- Build PDF ---
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PDF = os.path.join(OUT_DIR,
    "ALP-ttbar_Toy-MC_v2.8_Preregistration_Trimmed-Tag-Estimator-as-Default_2026-11-21.pdf")

doc = SimpleDocTemplate(OUT_PDF, pagesize=A4,
                        topMargin=15*mm, bottomMargin=12*mm,
                        leftMargin=18*mm, rightMargin=18*mm)

story = []

# ============================================================
# TITLE PAGE / HEADER
# ============================================================
story.append(Paragraph(
    "ALP-ttbar Toy MC v2.8 — Preregistration:<br/>"
    "Trimmed Tag Estimator as Default Discriminator<br/>"
    "in Displaced Light ALP → e<super>+</super>e<super>−</super>",
    sTitle))
story.append(Paragraph("Won Shik Paik (Independent Researcher, Auckland, New Zealand)", sAuthor))
story.append(Paragraph("2026-11-21", sDate))
story.append(Paragraph(
    "DOI: 10.5281/zenodo.24414960  |  Previous: 10.5281/zenodo.24408990 (v2.7 post-reg)",
    sDOILine))

story.append(HRFlowable(width="100%", thickness=0.8, color=ACCENT))

story.append(Paragraph(
    "<i>Disclaimer.</i> Independent personal toy study, not affiliated with the authors of "
    "arXiv:2610.38932 or arXiv:2306.08686, nor with the CMS, ATLAS, LHCb or ALICE "
    "Collaborations or the FCC study. Detector numbers are assumed; only qualitative "
    "trends and ratios are meaningful.",
    sDisclaimer))

# ============================================================
# 1. MOTIVATION AND CONTEXT
# ============================================================
story.append(Paragraph("1. Motivation and Context", sH1))
story.append(Paragraph(
    "The v2.7 Tag Formula Diagnostics study revealed three central findings that motivate "
    "this preregistration:",
    sBody))

story.append(Paragraph(
    "• <b>Conversion-background dominance.</b> Frozen-seed variance decomposition shows that "
    "99.84% of the Tag discriminator's seed-to-seed variance at 17 MeV originates from "
    "conversion-vertex randomness (σ<sub>S</sub>/σ<sub>F</sub> = 0.9992), not signal-vertex "
    "randomness (σ<sub>C</sub>/σ<sub>F</sub> = 0.0432). This is the opposite direction from "
    "the preregistered expectation.",
    sBullet))
story.append(Paragraph(
    "• <b>Trimming effectiveness.</b> Removing the extreme 1% tails (top and bottom) of "
    "the per-vertex λ distribution reduces the Tag CV from 5.80% to 0.13% — a 45-fold "
    "improvement that nearly matches HV-level stability (CV = 0.13%).",
    sBullet))
story.append(Paragraph(
    "• <b>Winsorising backfires.</b> In contrast, Winsorising (clipping rather than removing) "
    "the same 1% fraction <i>increases</i> the CV to 7.35%, because concentrating vertices "
    "at the boundary λ creates a sharp step in the threshold-scan landscape.",
    sBullet))

story.append(Spacer(1, 2*mm))
story.append(Paragraph(
    "These findings suggest that a small fraction of vertices with extreme λ values carry "
    "disproportionate weight in the Tag computation, and that removing them (trimming) rather "
    "than capping them (Winsorising) could appear advantageous. The mean degradation ratio "
    "improves from 1.5549 (untrimmed) to 1.0644 (trimmed, k = 1%) — closer to the ideal "
    "value of 1.0 — while simultaneously achieving a 45-fold gain in stability.",
    sBody))
story.append(Paragraph(
    "At 200 MeV, the effect of trimming is negligible (|Δ(σ/mean)| &lt; 0.05%), consistent "
    "with the finding that extreme-λ leverage is confined to the low-mass regime where "
    "the vertex z distribution is broader.",
    sBody))
story.append(Paragraph(
    "This preregistration formally adopts the trimmed Tag (k = 1%) as the <b>primary "
    "discriminator</b> and tests whether the stability and degradation-ratio improvements "
    "observed in v2.7 are robust across the full 50-seed ensemble at both focus masses.",
    sBody))

# --- Figures from v2.7 results ---
story.append(Spacer(1, 3*mm))
story.append(Paragraph("<b>Figure 1.</b> Tag CV Comparison (v2.7 Results)", sFigLabel))

# Calculate image width to fit within margins (A4 width - left - right margins)
fig_width = 140*mm
fig_height = fig_width * (3.8 / 5.8)  # maintain aspect ratio from figsize

story.append(Image(FIG1_PATH, width=fig_width, height=fig_height))
story.append(Paragraph(
    "<b>Figure 1.</b> Coefficient of variation (CV = σ/mean) of the Tag discriminator across "
    "the 50-seed ensemble at m<sub>a</sub> = 17 MeV, measured in the v2.7 post-registration "
    "study [I1]. The untrimmed Tag exhibits CV = 5.80%, reflecting the strong influence of "
    "conversion-vertex randomness. Trimming the extreme 1% tails (k = 1%) reduces the CV "
    "45-fold to 0.13%, matching the stability of the material-veto discriminator HV "
    "(CV = 0.13%). Winsorising the same fraction backfires, increasing the CV to 7.35% "
    "(+27% relative to untrimmed), because clipping vertices to boundary λ values creates "
    "a step discontinuity in the threshold-scan landscape. "
    "Source: DOI 10.5281/zenodo.24408990.",
    sCaption))

story.append(Spacer(1, 3*mm))
story.append(Paragraph("<b>Figure 2.</b> Degradation Ratio Comparison (v2.7 Results)", sFigLabel))
story.append(Image(FIG2_PATH, width=fig_width, height=fig_height))
story.append(Paragraph(
    "<b>Figure 2.</b> Mean degradation ratio at m<sub>a</sub> = 17 MeV across the 50-seed "
    "ensemble (v2.7). The degradation ratio deg = lim/lim<sub>0</sub> measures how much the "
    "discriminator's sensitivity worsens relative to the ideal case (deg = 1.0, dashed line). "
    "Trimming reduces the mean degradation ratio from 1.5549 (untrimmed) to 1.0644 — a 31.5% "
    "improvement toward ideal — bringing it much closer to the HV reference (1.0576). "
    "This suggests that extreme-λ vertices were distorting the threshold optimisation, and "
    "that their removal could allow the scan to find a more efficient operating point. "
    "The v2.8 study tests whether this improvement is robust. "
    "Source: DOI 10.5281/zenodo.24408990.",
    sCaption))

story.append(Spacer(1, 2*mm))

# ============================================================
# 2. REVIEW: THE TRIMMED TAG ESTIMATOR
# ============================================================
story.append(Paragraph("2. Review: The Trimmed Tag Estimator", sH1))

story.append(Paragraph("2.1 Standard Tag Computation", sH2))
story.append(Paragraph(
    "The standard Tag is an upper-limit degradation ratio computed by scan_tag_endcap in "
    "endcap_sim.py. For a given hypothesis mass m<sub>a</sub>, the code scans a grid of "
    "λ thresholds and mass windows to find the combination that minimises "
    "lim = upper_limit(S, B) = max(3, 2√B)/S, where S and B are the signal yield and "
    "conversion background surviving the λ ≥ t cut and mass-window selection. The "
    "selected minimum lim is then divided by the zero-background reference "
    "lim<sub>0</sub> = 3/S<sub>0</sub> (the ideal expected 95% CL limit computed from "
    "the full signal yield before any λ or mass-window cut) to obtain the Tag "
    "degradation ratio deg = lim/lim<sub>0</sub>. A lower deg means better discrimination.",
    sBody))

story.append(Paragraph("2.2 Trimming Procedure", sH2))
story.append(Paragraph(
    "The trimmed Tag applies a <b>boolean removal mask</b> before the threshold scan. "
    "For each population (signal and conversion separately):",
    sBody))
story.append(Paragraph(
    "• Sort the signed λ values and identify n<sub>rem</sub> = ⌊k × N / 100⌋ vertices "
    "from each tail (the n<sub>rem</sub> smallest and the n<sub>rem</sub> largest).",
    sBullet))
story.append(Paragraph(
    "• Construct boolean masks keep<sub>sig</sub> and keep<sub>conv</sub> that are False "
    "for removed vertices.",
    sBullet))
story.append(Paragraph(
    "• Apply these masks to <i>all</i> candidates in scan_tag_endcap: for every "
    "(t, mass-window) combination, the selection becomes cs = sig['base'] &amp; "
    "keep<sub>sig</sub> &amp; ts &amp; ms, and similarly for conversion.",
    sBullet))
story.append(Paragraph(
    "• The baseline S<sub>0</sub> and lim<sub>0</sub> are computed from the "
    "<i>pre-removal</i> population (unchanged from the standard Tag), so the degradation "
    "ratio remains comparable.",
    sBullet))
story.append(Spacer(1, 1*mm))
story.append(Paragraph(
    "At k = 0, the trimmed Tag reproduces the standard Tag exactly (verified at "
    "floating-point precision in v2.7). The trim fraction k = 1% removes approximately "
    "2% of vertices in total (top + bottom 1% from each of signal and conversion).",
    sBody))

story.append(Paragraph("2.3 Why Trimming May Appear Advantageous Over Winsorising", sH2))
story.append(Paragraph(
    "Both trimming and Winsorising target the same ⌊k × N / 100⌋ vertices from each tail. "
    "Trimming removes them entirely; Winsorising replaces their λ with the nearest retained "
    "boundary value. The v2.7 results show that Winsorising concentrates vertices at the "
    "boundary λ, creating a sharp step in the threshold-scan landscape that amplifies "
    "sensitivity to seed-to-seed fluctuations. Trimming avoids this by removing the vertices "
    "altogether, so they never contribute to S or B regardless of the λ threshold.",
    sBody))

# ============================================================
# 3. EXPERIMENTAL DESIGN
# ============================================================
story.append(Paragraph("3. Experimental Design", sH1))

story.append(Paragraph("3.1 Configuration", sH2))
story.append(Paragraph(
    "All experiments use configuration E3 (material scale f = 0.25; z resolution assigned "
    "per vertex based on the nearest of the 9 sensor disks in SENSOR_DISK_Z, i.e. 'all-disk "
    "z precision') at η = 2.0, consistent with v2.5, v2.6 and v2.7. The generation pipeline "
    "follows v2.6: endcap_signal generates 300,000 signal vertices and endcap_conversions "
    "generates 1,500,000 conversion-photon candidates per seed. After basic-cut selection "
    "(fiducial z range, minimum p<sub>T</sub>), up to N<sub>sig</sub> = 50,000 signal "
    "and up to N<sub>conv</sub> = 100,000 conversion vertices passing cuts are retained via "
    "subsample(); vertex weights are rescaled to preserve the total cross-section.",
    sBody))
story.append(Paragraph(
    "Focus masses: m<sub>a</sub> = 17 MeV (largest observed variation) and m<sub>a</sub> = "
    "200 MeV (comparison baseline where σ/mean is negligible).",
    sBody))

story.append(Paragraph("3.2 Trimmed Tag as Primary Discriminator", sH2))
story.append(Paragraph(
    "The trimmed Tag at k = 1% replaces the standard (untrimmed) Tag as the <b>primary "
    "discriminator</b> for evaluating ALP sensitivity. This means:",
    sBody))
story.append(Paragraph(
    "• The trimmed Tag degradation ratio is the primary metric reported for each seed.",
    sBullet))
story.append(Paragraph(
    "• The untrimmed Tag (k = 0) is retained as a <b>reference baseline</b> for comparison.",
    sBullet))
story.append(Paragraph(
    "• HV degradation ratio continues to be reported alongside both Tag variants.",
    sBullet))
story.append(Paragraph(
    "• The trim fraction k = 1% is fixed for all seeds and both masses. No per-seed "
    "optimisation of k is performed.",
    sBullet))

story.append(Paragraph("3.3 Ensemble Structure", sH2))
story.append(Paragraph(
    "The 50-seed ensemble uses the same seed formulae as v2.6 and v2.7 Group F, "
    "but with a <b>new index range</b> i = 50, 51, …, 99 to ensure independent "
    "validation (the v2.7 study used i = 0, 1, …, 49):",
    sBody))

seed_header = [Paragraph("Parameter", sTH), Paragraph("Formula", sTH)]
seed_rows = [
    [Paragraph("SEED_CONV", sTDL), Paragraph("100i + 5  for i = 50, 51, …, 99", sTDL)],
    [Paragraph("SEED_SIG", sTDL), Paragraph("100i + 11  for i = 50, 51, …, 99", sTDL)],
]
story.append(make_table(seed_header, seed_rows, [50*mm, 120*mm]))
story.append(Spacer(1, 2*mm))
story.append(Paragraph(
    "Using i = 50–99 (rather than repeating i = 0–49) ensures that the v2.8 ensemble "
    "is statistically independent from v2.7 Group F. If the v2.8 results confirm the "
    "trimmed Tag's advantages on fresh pseudo-data, the evidence is substantially "
    "stronger than a replication on the same seeds.",
    sBody))

# ============================================================
# 4. ANALYSIS PLAN
# ============================================================
story.append(Paragraph("4. Analysis Plan", sH1))

story.append(Paragraph("4.1 Primary Outputs", sH2))
story.append(Paragraph(
    "For each of the 50 seeds and both focus masses (17 MeV and 200 MeV), the code computes:",
    sBody))
story.append(Paragraph(
    "• <b>Trimmed Tag degradation ratio</b> (k = 1%) — the primary discriminator.",
    sBullet))
story.append(Paragraph(
    "• <b>Untrimmed Tag degradation ratio</b> (k = 0) — the reference baseline.",
    sBullet))
story.append(Paragraph(
    "• <b>HV degradation ratio</b> — the material-veto comparator.",
    sBullet))
story.append(Spacer(1, 1*mm))
story.append(Paragraph(
    "Ensemble statistics (mean, standard deviation, CV = σ/mean) are computed across the "
    "50 seeds for each quantity. Confidence intervals use 1.96 × SE (normal approximation "
    "for N<sub>seeds</sub> = 50 ≥ 30), consistent with v2.6 and v2.7.",
    sBody))

story.append(Paragraph("4.2 Degradation Ratio Comparison", sH2))
story.append(Paragraph(
    "The central comparison is between the trimmed and untrimmed Tag across the ensemble:",
    sBody))
story.append(Paragraph(
    "• <b>Mean degradation ratio:</b> Does the trimmed Tag yield a lower (better) mean "
    "degradation ratio than the untrimmed Tag? The v2.7 result suggests improvement from "
    "1.5549 to 1.0644 at 17 MeV.",
    sBullet))
story.append(Paragraph(
    "• <b>Stability (CV):</b> Does the trimmed Tag achieve substantially lower CV than the "
    "untrimmed Tag? The v2.7 result suggests improvement from 5.80% to 0.13%.",
    sBullet))
story.append(Paragraph(
    "• <b>Seed-level dominance:</b> In what fraction of the 50 seeds does the trimmed Tag "
    "yield a lower degradation ratio than the untrimmed Tag?",
    sBullet))

story.append(Paragraph("4.3 Seed-0 Cross-Check (v2.7 Seed)", sH2))
story.append(Paragraph(
    "Before running the main i = 50–99 ensemble, a single verification run is performed "
    "using v2.7's seed i = 0 (SEED_CONV = 5, SEED_SIG = 11). This seed is <b>not</b> "
    "part of the v2.8 ensemble; it serves solely as a code-consistency check. "
    "The following must hold:",
    sBody))
story.append(Paragraph(
    "• The untrimmed Tag (k = 0) at seed i = 0 must match the v2.7 Group F seed-0 result "
    "to floating-point precision.",
    sBullet))
story.append(Paragraph(
    "• The trimmed Tag at k = 1% at seed i = 0 must match the v2.7 Approach C result for "
    "the same seed.",
    sBullet))
story.append(Paragraph(
    "• HV at seed i = 0 must match the v2.7 Group F seed-0 HV result.",
    sBullet))
story.append(Spacer(1, 1*mm))
story.append(Paragraph(
    "This confirms that the v2.8 code uses the same frozen components and seed structure "
    "as v2.7, before proceeding to the independent seed range.",
    sBody))

story.append(Paragraph("4.4 Additional Diagnostics", sH2))
story.append(Paragraph(
    "To understand <i>why</i> trimming could improve the degradation ratio (not just the CV), "
    "the following are recorded per seed:",
    sBody))
story.append(Paragraph(
    "• <b>Optimal threshold shift:</b> Does trimming change the optimal λ threshold and/or "
    "mass window chosen by scan_tag_endcap? A shift would indicate that extreme-λ vertices "
    "were distorting the optimisation landscape.",
    sBullet))
story.append(Paragraph(
    "• <b>Signal and background yields:</b> S and B at the optimal cut for both trimmed "
    "and untrimmed, to determine whether the improvement arises from better signal "
    "retention, better background rejection, or both.",
    sBullet))
story.append(Paragraph(
    "• <b>Per-seed Δ(deg):</b> The difference deg(k=0) − deg(k=1%) for each seed, to "
    "assess whether the improvement is uniform or concentrated in a subset of seeds.",
    sBullet))

# ============================================================
# 5. PREDICTIONS
# ============================================================
story.append(Paragraph("5. Predictions", sH1))
story.append(Paragraph(
    "All predictions are for the E3 configuration (f = 0.25, η = 2.0, 17-band geometry), "
    "unless otherwise stated. Predictions are labelled CONFIRMED if the stated inequality "
    "or threshold is met; otherwise REFUTED.",
    sBody))

story.append(Paragraph("5.1 Stability Predictions", sH2))

pred_s_header = [Paragraph("ID", sTH), Paragraph("Prediction", sTH),
                 Paragraph("Threshold", sTH), Paragraph("Mass", sTH),
                 Paragraph("Rationale", sTH)]
pred_s_rows = [
    [Paragraph("S1", sTDB),
     Paragraph("Trimmed Tag (k=1%)<br/>CV substantially<br/>lower than untrimmed", sTDL),
     Paragraph("CV(trimmed) &lt;<br/>CV(untrimmed) / 10<br/>at 17 MeV", sTDL),
     Paragraph("17 MeV", sTD),
     Paragraph("v2.7 found 45-fold<br/>reduction; threshold<br/>is conservative 10×", sTDL)],
    [Paragraph("S2", sTDB),
     Paragraph("Trimmed Tag CV<br/>approaches HV-level<br/>stability", sTDL),
     Paragraph("CV(trimmed) &lt; 1%<br/>at 17 MeV", sTDL),
     Paragraph("17 MeV", sTD),
     Paragraph("v2.7: CV = 0.13%<br/>for trimmed vs<br/>0.13% for HV", sTDL)],
    [Paragraph("S3", sTDB),
     Paragraph("Trimming negligible<br/>at 200 MeV", sTDL),
     Paragraph("|CV(trimmed) −<br/>CV(untrimmed)|<br/>&lt; 0.1% at 200 MeV", sTDL),
     Paragraph("200 MeV", sTD),
     Paragraph("v2.7: |Δ(σ/mean)|<br/>&lt; 0.05% at 200 MeV;<br/>leverage confined<br/>to low mass", sTDL)],
]
story.append(make_table(pred_s_header, pred_s_rows, [14*mm, 38*mm, 38*mm, 18*mm, 38*mm]))

story.append(Spacer(1, 3*mm))
story.append(Paragraph("5.2 Degradation Ratio Predictions", sH2))

pred_d_header = [Paragraph("ID", sTH), Paragraph("Prediction", sTH),
                 Paragraph("Threshold", sTH), Paragraph("Mass", sTH),
                 Paragraph("Rationale", sTH)]
pred_d_rows = [
    [Paragraph("D1", sTDB),
     Paragraph("Trimmed Tag has<br/>lower mean deg ratio<br/>than untrimmed", sTDL),
     Paragraph("mean(deg<sub>trim</sub>) &lt;<br/>mean(deg<sub>untrim</sub>)<br/>at 17 MeV", sTDL),
     Paragraph("17 MeV", sTD),
     Paragraph("v2.7: 1.0644 vs<br/>1.5549; removing<br/>extreme-λ vertices<br/>may improve<br/>optimisation", sTDL)],
    [Paragraph("D2", sTDB),
     Paragraph("Trimmed Tag closer<br/>to ideal (1.0)", sTDL),
     Paragraph("mean(deg<sub>trim</sub>) &lt; 1.2<br/>at 17 MeV", sTDL),
     Paragraph("17 MeV", sTD),
     Paragraph("v2.7: 1.0644;<br/>threshold set at<br/>1.2 to allow for<br/>ensemble variation", sTDL)],
    [Paragraph("D3", sTDB),
     Paragraph("Trimmed Tag<br/>improves majority<br/>of seeds", sTDL),
     Paragraph("Fraction of seeds<br/>where deg<sub>trim</sub> &lt;<br/>deg<sub>untrim</sub> &gt; 0.8", sTDL),
     Paragraph("17 MeV", sTD),
     Paragraph("If trimming is<br/>broadly beneficial,<br/>&gt;80% of seeds<br/>should improve", sTDL)],
    [Paragraph("D4", sTDB),
     Paragraph("Degradation ratio<br/>unchanged at<br/>200 MeV", sTDL),
     Paragraph("|mean(deg<sub>trim</sub>) −<br/>mean(deg<sub>untrim</sub>)|<br/>&lt; 0.05 at 200 MeV", sTDL),
     Paragraph("200 MeV", sTD),
     Paragraph("At 200 MeV the<br/>extreme-λ leverage<br/>is negligible; trim<br/>should be inert", sTDL)],
]
story.append(make_table(pred_d_header, pred_d_rows, [14*mm, 36*mm, 38*mm, 18*mm, 40*mm]))

story.append(Spacer(1, 3*mm))
story.append(Paragraph("5.3 Diagnostic Predictions", sH2))

pred_x_header = [Paragraph("ID", sTH), Paragraph("Prediction", sTH),
                 Paragraph("Threshold", sTH), Paragraph("Mass", sTH),
                 Paragraph("Rationale", sTH)]
pred_x_rows = [
    [Paragraph("X1", sTDB),
     Paragraph("Optimal threshold<br/>shifts under<br/>trimming", sTDL),
     Paragraph("Median |Δt<sub>opt</sub>| &gt; 0<br/>across 50 seeds<br/>at 17 MeV", sTDL),
     Paragraph("17 MeV", sTD),
     Paragraph("Removing extreme-λ<br/>vertices could alter<br/>the threshold<br/>landscape", sTDL)],
    [Paragraph("X2", sTDB),
     Paragraph("Improvement is<br/>uniform across seeds", sTDL),
     Paragraph("CV of Δ(deg) &lt; 50%<br/>at 17 MeV", sTDL),
     Paragraph("17 MeV", sTD),
     Paragraph("If a few seeds drive<br/>the mean improvement,<br/>CV of Δ(deg) will<br/>be large", sTDL)],
]
story.append(make_table(pred_x_header, pred_x_rows, [14*mm, 36*mm, 38*mm, 18*mm, 40*mm]))

# ============================================================
# 6. IMPLEMENTATION NOTES
# ============================================================
story.append(Paragraph("6. Implementation Notes", sH1))

story.append(Paragraph("6.1 Code Structure", sH2))
story.append(Paragraph(
    "The post-registration code will consist of:",
    sBody))
story.append(Paragraph(
    "<b>run_v28_trimmed_tag.py</b> — Orchestrator that runs the trimmed and untrimmed Tag "
    "and HV across 50 seeds at both focus masses. Imports endcap_sim.py and mtag_v24.py "
    "(frozen). Outputs a JSON file with per-seed results and a NumPy archive (.npz) with "
    "arrays.",
    sBullet))
story.append(Paragraph(
    "<b>generate_v28_report.py</b> — Generates the post-registration PDF from the saved "
    "results, including tables and figures for all predictions.",
    sBullet))

story.append(Paragraph("6.2 Frozen Components", sH2))
story.append(Paragraph(
    "The following modules are frozen from previous versions and must not be modified:",
    sBody))
story.append(Paragraph(
    "• mtag_v24.py (tag formula, 17-band geometry) — frozen since v2.4 preregistration",
    sBullet))
story.append(Paragraph(
    "• mtag_v22.py (9-band baseline for endcap_sim import) — frozen since v2.2",
    sBullet))
story.append(Paragraph(
    "• endcap_sim.py (simulation engine) — frozen since v2.5. Generates 300,000 signal and "
    "1,500,000 conversion-photon candidates; after basic cuts, subsample() retains up to "
    "N<sub>sig</sub> = 50,000 signal and up to N<sub>conv</sub> = 100,000 conversion vertices",
    sBullet))

story.append(Paragraph("6.3 Computational Requirements", sH2))
story.append(Paragraph(
    "The v2.8 computation reuses the v2.7 Group F ensemble infrastructure with a fresh "
    "seed range (i = 50–99). For each seed, scan_tag_endcap runs twice (once with k = 0, "
    "once with k = 1%) at two masses, yielding 50 × 2 × 2 = 200 scan_tag_endcap calls "
    "plus 50 × 2 HV computations. The trimming mask is computed once per seed per mass "
    "and applied within scan_tag_endcap. All 50 seeds require fresh simulation because "
    "the seed range is new (no cached outputs from v2.7). Total computation: ~100 "
    "simulation runs (50 seeds × 2 masses), comparable to v2.7 Group F.",
    sBody))

# ============================================================
# 7. SUCCESS CRITERIA AND INTERPRETATION GUIDE
# ============================================================
story.append(Paragraph("7. Success Criteria and Interpretation Guide", sH1))

story.append(Paragraph(
    "<b>Strong evidence for trimmed Tag as default:</b> All 5 of {S1, S2, D1, D2, D3} "
    "CONFIRMED at 17 MeV, <b>and</b> both cross-mass predictions {S3, D4} CONFIRMED at "
    "200 MeV. This would indicate that the trimmed Tag is both more stable and closer "
    "to ideal sensitivity than the untrimmed Tag, with the improvement broadly distributed "
    "across seeds and safe at higher mass. The trimmed Tag could then be formally adopted "
    "as the default discriminator across both masses for all subsequent studies and the "
    "future directions outlined in §9 below.",
    sBody))
story.append(Spacer(1, 1*mm))
story.append(Paragraph(
    "<b>Moderate evidence:</b> 3 or 4 of {S1, S2, D1, D2, D3} CONFIRMED. The trimmed "
    "Tag appears advantageous but with caveats — perhaps the improvement is concentrated "
    "in a subset of seeds, or the mean degradation ratio, while improved, does not reach "
    "the 1.2 threshold. Adoption is conditional on identifying and explaining the "
    "REFUTED prediction(s).",
    sBody))
story.append(Spacer(1, 1*mm))
story.append(Paragraph(
    "<b>Weak or no evidence:</b> 2 or fewer of {S1, S2, D1, D2, D3} CONFIRMED. The v2.7 "
    "result may not generalise, and the standard Tag may remain preferable as the primary "
    "discriminator. Alternative approaches (e.g., signal-side λ regularisation per §9.2) "
    "would become higher priority.",
    sBody))
story.append(Spacer(1, 1*mm))
story.append(Paragraph(
    "<b>Cross-mass safety:</b> {S3, D4} test whether trimming is safe at 200 MeV. If "
    "either is REFUTED, a mass-dependent trim strategy would be needed, and adoption "
    "would be restricted to the 17 MeV regime pending further study.",
    sBody))
story.append(Spacer(1, 1*mm))
story.append(Paragraph(
    "<b>Diagnostic predictions:</b> {X1, X2} provide mechanistic insight but do not "
    "affect the adoption decision. <b>X1 edge case:</b> In the scan_tag_endcap code, "
    "a None optimal threshold means no λ cut is applied — this is a valid scan candidate, "
    "not an error. If either the trimmed or untrimmed method returns None for a given seed, "
    "that seed is excluded from the numeric |Δt<sub>opt</sub>| calculation. The count of "
    "such excluded seeds and the count of None ↔ numeric transitions (where one method "
    "selects a finite cut and the other does not) are reported separately. If zero seeds "
    "yield a numeric pair, X1 is marked N/A. When multiple (threshold, mass-window) "
    "combinations tie for the minimum lim, the first candidate in scan order is retained, "
    "consistent with the existing code. <b>X2 contingency:</b> X2 (uniformity of "
    "improvement) is evaluated only if D1 is CONFIRMED; if D1 is REFUTED (i.e., trimming "
    "does not improve the mean degradation ratio), the uniformity of a non-existent "
    "improvement is undefined.",
    sBody))

# ============================================================
# 8. SUMMARY OF PREDICTIONS
# ============================================================
story.append(Paragraph("8. Summary of Predictions", sH1))

sum_header = [Paragraph("ID", sTH), Paragraph("Short Description", sTH),
              Paragraph("Criterion", sTH), Paragraph("Mass", sTH)]
sum_rows = [
    [Paragraph("S1", sTD), Paragraph("Trimmed CV ≪ untrimmed CV", sTDL),
     Paragraph("CV(trim) &lt; CV(untrim) / 10", sTDL), Paragraph("17 MeV", sTD)],
    [Paragraph("S2", sTD), Paragraph("Trimmed CV near HV level", sTDL),
     Paragraph("CV(trim) &lt; 1%", sTDL), Paragraph("17 MeV", sTD)],
    [Paragraph("S3", sTD), Paragraph("Trim negligible at 200 MeV", sTDL),
     Paragraph("|ΔCV| &lt; 0.1%", sTDL), Paragraph("200 MeV", sTD)],
    [Paragraph("D1", sTD), Paragraph("Trimmed mean deg &lt; untrimmed", sTDL),
     Paragraph("mean(deg<sub>T</sub>) &lt; mean(deg<sub>U</sub>)", sTDL), Paragraph("17 MeV", sTD)],
    [Paragraph("D2", sTD), Paragraph("Trimmed mean deg near ideal", sTDL),
     Paragraph("mean(deg<sub>T</sub>) &lt; 1.2", sTDL), Paragraph("17 MeV", sTD)],
    [Paragraph("D3", sTD), Paragraph("Trimming improves &gt;80% seeds", sTDL),
     Paragraph("frac(deg<sub>T</sub>&lt;deg<sub>U</sub>) &gt; 0.8", sTDL), Paragraph("17 MeV", sTD)],
    [Paragraph("D4", sTD), Paragraph("Deg ratio unchanged at 200 MeV", sTDL),
     Paragraph("|Δmean(deg)| &lt; 0.05", sTDL), Paragraph("200 MeV", sTD)],
    [Paragraph("X1", sTD), Paragraph("Optimal threshold shifts", sTDL),
     Paragraph("median |Δt<sub>opt</sub>| &gt; 0", sTDL), Paragraph("17 MeV", sTD)],
    [Paragraph("X2", sTD), Paragraph("Improvement uniform across seeds", sTDL),
     Paragraph("CV(Δdeg) &lt; 50%", sTDL), Paragraph("17 MeV", sTD)],
]
story.append(make_table(sum_header, sum_rows, [14*mm, 50*mm, 55*mm, 22*mm]))
story.append(Spacer(1, 2*mm))
story.append(Paragraph(
    "<b>Total: 9 predictions.</b> 3 stability (S1–S3), 4 degradation ratio (D1–D4), "
    "2 diagnostic (X1–X2). Core predictions: {S1, S2, D1, D2, D3}.",
    sBody))

# ============================================================
# 9. FUTURE DIRECTIONS
# ============================================================
story.append(Paragraph("9. Future Directions", sH1))

story.append(Paragraph(
    "Beyond validating trimmed Tag as the default discriminator (the subject of this "
    "preregistration), several follow-up directions remain from the v2.7 post-registration "
    "roadmap (§9.2–§9.6 of [I1]), plus two newly identified studies. All items below are "
    "listed in approximate order of implementation feasibility, from studies achievable "
    "within the current framework to those requiring substantial architectural extensions.",
    sBody))

# --- 9.1 Background-Focused Diagnostics (from v2.7 §9.3) ---
story.append(Paragraph("9.1 Background-Focused Diagnostics", sH2))
story.append(Paragraph(
    "The finding that Tag variability is primarily a question of background modelling, not "
    "signal efficiency, opens new diagnostic directions. Future studies could investigate: "
    "(a) the per-seed breakdown of the optimised background yield B at the Tag's chosen "
    "threshold, to quantify how many conversion vertices cross the threshold boundary from "
    "seed to seed; (b) a decomposition of B into contributions from near-band and inter-band "
    "conversion vertices, to identify whether the instability is dominated by a few vertices "
    "at extreme λ or by a broad shift in the λ distribution; and (c) the effect of increasing "
    "N<sub>conv</sub> beyond 100,000, to test whether the variance diminishes as "
    "√N<sub>conv</sub> (suggesting independent vertex contributions) or more slowly "
    "(suggesting correlated effects). These analyses could be performed on existing simulation "
    "outputs with minimal additional code.",
    sBody))

# --- 9.2 Signal-Side λ Regularisation (from v2.7 §9.2) ---
story.append(Paragraph("9.2 Signal-Side λ Regularisation", sH2))
story.append(Paragraph(
    "For <i>signal</i> vertices, the inter-band p<sub>conv</sub> floor produces extremely "
    "large λ values in the 17-band geometry. A regularised p<sub>conv</sub> that imposes a "
    "physical minimum (e.g., a constant floor above 10<super>−12</super>, matching the ε "
    "used in Approach B's inter-band classification) could reduce the extreme signal-vertex "
    "λ tail. However, since Approach A shows that signal-vertex randomness contributes only "
    "0.19% of Tag variance, such a signal-side change alone may not substantially improve "
    "Tag stability. Identifying and regularising the conversion-side mechanism (§7.1(c) of "
    "[I1]) would be a higher priority for future work. Either modification would change the "
    "tag formula itself and require a fresh preregistration.",
    sBody))

# --- 9.3 Extension to Other Configurations (from v2.7 §9.5) ---
story.append(Paragraph("9.3 Extension to Other Configurations", sH2))
story.append(Paragraph(
    "This study used the E3 configuration (f = 0.25) and two masses (17 MeV, 200 MeV). "
    "The conversion-dominance finding may depend on the material scale factor f: at higher f "
    "(denser material), more conversions occur near bands and fewer in gaps, potentially "
    "shifting the balance between σ<sub>C</sub> and σ<sub>S</sub>. A systematic scan over "
    "f ∈ {0.10, 0.25, 0.50, 1.00} and a broader mass grid (5–500 MeV) could map the "
    "boundary of the conversion-dominated regime and determine whether it extends to the "
    "full mass range of the ALP → e<super>+</super>e<super>−</super> search.",
    sBody))

# --- 9.4 Alternative Discriminator Architectures (from v2.7 §9.4) ---
story.append(Paragraph("9.4 Alternative Discriminator Architectures", sH2))
story.append(Paragraph(
    "The contrast between the Tag and HV discriminators is instructive. HV achieves "
    "CV = 0.13% at 17 MeV — roughly 44× more stable than the Tag — because it uses a "
    "material-veto approach that is binary (vertex passes or fails based on proximity to "
    "material) rather than continuous (the Tag's λ threshold scan over a 14-element TGRID). "
    "Future work could explore hybrid discriminators that combine the Tag's mass-dependent "
    "sensitivity with the HV's stability, for example by using the HV as a pre-filter to "
    "remove conversion-dominated vertices before applying a simplified Tag cut.",
    sBody))

# --- 9.5 Dimuon Control Sample (NEW) ---
story.append(Paragraph(
    "9.5 Dimuon Control Sample (ALP → μ<super>+</super>μ<super>−</super>)", sH2))
story.append(Paragraph(
    "Unlike electrons, muons traverse tracker material with minimal Bremsstrahlung or "
    "electromagnetic showering. For ALP masses above the dimuon threshold (m<sub>a</sub> > "
    "2m<sub>μ</sub> ≈ 211 MeV), the decay channel ALP → μ<super>+</super>μ<super>−</super> "
    "could serve as a control sample within the same geometric configuration.",
    sBody))
story.append(Paragraph(
    "By running the existing simulation with muon-like daughters — where conversion-photon "
    "background and material-interaction effects are largely absent — it may become possible "
    "to isolate the contribution of material interactions to the observed efficiency "
    "degradation. If the degradation ratio approaches 1.0 in the dimuon channel under "
    "identical geometry, this would confirm that the signal loss arises primarily from "
    "material interactions and reconstruction bias, not from the kinematic properties of "
    "displaced vertices. This approach mirrors the control-region validation technique used "
    "in experimental searches.",
    sBody))

# --- 9.6 Gaussian-Sum Filter (GSF) Tracking (NEW) ---
story.append(Paragraph("9.6 Gaussian-Sum Filter (GSF) Tracking", sH2))
story.append(Paragraph(
    "The current toy model assumes that vertex positions are reconstructed with Gaussian "
    "resolution assigned from the nearest sensor disk. In a real tracker, electron tracks "
    "suffer non-Gaussian energy loss from Bremsstrahlung, which degrades standard Kalman "
    "filter performance. The ATLAS and CMS experiments address this by employing "
    "Gaussian-Sum Filters (GSF), which model the track state as a mixture of Gaussian "
    "components to accommodate the asymmetric energy-loss distribution.",
    sBody))
story.append(Paragraph(
    "Incorporating a simplified GSF-like reconstruction layer into the toy MC could test "
    "whether the resolution conflation bias identified in v2.5 and the conversion-background "
    "dominance found in v2.7 could be partially mitigated by improved track reconstruction. "
    "This would require extending the simulation from its current 'vertex-level' abstraction "
    "to a 'hit → track → vertex' pipeline — a substantial but well-motivated extension "
    "that would bring the toy model closer to the reconstruction chain used in real "
    "displaced-vertex analyses.",
    sBody))
story.append(Paragraph(
    "Together with the dimuon control study (§9.5), these two directions form a "
    "complementary validation programme: the dimuon channel isolates the cause of the "
    "observed degradation (material-interaction bias), while GSF tracking could offer a "
    "reconstruction-level mitigation strategy.",
    sBody))

# --- 9.7 Preregistration Lessons (from v2.7 §9.6) ---
story.append(Paragraph("9.7 Preregistration Lessons", sH2))
story.append(Paragraph(
    "The v2.7 diagnostics demonstrate that preregistration is valuable even in exploratory "
    "toy MC studies. The 2/4 core score nominally indicates 'weak' diagnostic evidence, but "
    "the REFUTED predictions are arguably more valuable than the CONFIRMED ones: they reveal "
    "a mechanism (conversion-background dominance) that was not anticipated and that has "
    "clear implications for discriminator design. Future preregistrations in this series "
    "could benefit from (a) explicitly listing 'direction-agnostic' predictions that are "
    "informative regardless of which way they go, and (b) defining success criteria that "
    "account for the information content of refutations, not just confirmations.",
    sBody))

# ============================================================
# 10. DOI CHAIN
# ============================================================
story.append(Paragraph("10. DOI Chain", sH1))

doi_header = [Paragraph("Version", sTH), Paragraph("DOI", sTH),
              Paragraph("Description", sTH)]
doi_rows = [
    [Paragraph("v2.8 prereg (this)", sTD),
     Paragraph("10.5281/zenodo.24414960", sTDL),
     Paragraph("Trimmed Tag Estimator prereg", sTDL)],
    [Paragraph("v2.7 post-reg", sTD),
     Paragraph("10.5281/zenodo.24408990", sTDL),
     Paragraph("Tag Formula Diagnostics results", sTDL)],
    [Paragraph("v2.7 prereg", sTD),
     Paragraph("10.5281/zenodo.24388228", sTDL),
     Paragraph("Tag Formula Diagnostics prereg", sTDL)],
    [Paragraph("v2.6 post-reg", sTD),
     Paragraph("10.5281/zenodo.24373115", sTDL),
     Paragraph("Multi-Seed Ensemble results", sTDL)],
    [Paragraph("v2.6 prereg", sTD),
     Paragraph("10.5281/zenodo.24361872", sTDL),
     Paragraph("Multi-Seed Ensemble prereg", sTDL)],
    [Paragraph("v2.5 results", sTD),
     Paragraph("10.5281/zenodo.24341050", sTDL),
     Paragraph("Deconflation post-reg", sTDL)],
    [Paragraph("v2.5 prereg", sTD),
     Paragraph("10.5281/zenodo.24329044", sTDL),
     Paragraph("Deconflation prereg", sTDL)],
    [Paragraph("v2.4 results", sTD),
     Paragraph("10.5281/zenodo.24302619", sTDL),
     Paragraph("17-band geometry post-reg", sTDL)],
    [Paragraph("v2.4 prereg", sTD),
     Paragraph("10.5281/zenodo.24296796", sTDL),
     Paragraph("17-band geometry prereg", sTDL)],
    [Paragraph("v2.3 results", sTD),
     Paragraph("10.5281/zenodo.24273586", sTDL),
     Paragraph("Endcap tag post-reg", sTDL)],
    [Paragraph("v2.3 prereg", sTD),
     Paragraph("10.5281/zenodo.24244893", sTDL),
     Paragraph("Endcap tag prereg", sTDL)],
    [Paragraph("v2.2 results", sTD),
     Paragraph("10.5281/zenodo.24238224", sTDL),
     Paragraph("Barrel → endcap post-reg", sTDL)],
    [Paragraph("v2.2 prereg", sTD),
     Paragraph("10.5281/zenodo.24189990", sTDL),
     Paragraph("Barrel → endcap prereg", sTDL)],
    [Paragraph("v2.1 results", sTD),
     Paragraph("10.5281/zenodo.24136462", sTDL),
     Paragraph("Barrel material-veto post-reg", sTDL)],
    [Paragraph("v2.1 prereg", sTD),
     Paragraph("10.5281/zenodo.24063091", sTDL),
     Paragraph("Barrel material-veto prereg", sTDL)],
    [Paragraph("v2.0", sTD),
     Paragraph("10.5281/zenodo.24056097", sTDL),
     Paragraph("Initial barrel study", sTDL)],
]
story.append(make_table(doi_header, doi_rows, [30*mm, 55*mm, 60*mm]))

# ============================================================
# 11. REFERENCES
# ============================================================
story.append(Paragraph("11. References", sH1))

story.append(Paragraph("11.1 External References", sH2))

refs_ext = [
    "[E1] J. Alimena, F. Blekman, C. Cazzaniga, X. Cid Vidal, J. Niedziela, L. Rygaard, "
    "R. Soto Rey, \"Hunting for Long-Lived ALPs in Top Events via Displaced Dielectron "
    "Pairs at the LHC,\" arXiv:2610.38932 [hep-ph] (2026) (motivating analysis: "
    "generator-level sensitivity study for displaced ALP → e<super>+</super>e<super>−</super> "
    "in tt̄ events at the CMS detector).",

    "[E2] L. Rygaard, J. Niedziela, R. Schäfer, S. Bruggisser, J. Alimena, S. Westhoff, "
    "F. Blekman, \"Top Secrets: Long-Lived ALPs in Top Production,\" arXiv:2306.08686 "
    "[hep-ph] (2023) (predecessor analysis: displaced di-muon ALP search strategy in "
    "tt̄ production at the LHC and HL-LHC).",

    "[E3] A. L. Read, \"Presentation of search results: the CL<sub>s</sub> technique,\" "
    "J. Phys. G <b>28</b> (2002) 2693 (upper-limit methodology background).",

    "[E4] D. Curtin et al., \"Long-Lived Particles at the Energy Frontier: The MATHUSLA "
    "Physics Case,\" Rep. Prog. Phys. <b>82</b> (2019) 116201, arXiv:1806.07396 "
    "(displaced-vertex physics context).",

    "[E5] NumPy v1.26, numpy.org (pseudo-random number generation, array operations).",
    "[E6] ReportLab v5.0.1, reportlab.com (PDF generation).",
    "[E7] SciPy v1.14, scipy.org (Pearson correlation, scipy.stats.pearsonr).",
]

for ref in refs_ext:
    story.append(Paragraph(ref, ParagraphStyle("Ref", fontName="DejaVu", fontSize=7.5,
                                                leading=10, textColor=DARK,
                                                leftIndent=8*mm, firstLineIndent=-8*mm,
                                                spaceAfter=1.5*mm)))

story.append(Paragraph("11.2 Internal References (ALP-ttbar Toy MC Series)", sH2))

refs_int = [
    "[I1] W. S. Paik, \"ALP-ttbar Toy MC v2.7 — Post-Registration: Tag Formula Diagnostics "
    "Results,\" DOI: 10.5281/zenodo.24408990 (identified conversion-background dominance, "
    "trimming effectiveness, and Winsorising failure that motivate this study).",

    "[I2] W. S. Paik, \"ALP-ttbar Toy MC v2.7 — Preregistration: Tag Formula Diagnostics,\" "
    "DOI: 10.5281/zenodo.24388228 (preregistered analysis plan for the diagnostic study).",

    "[I3] W. S. Paik, \"ALP-ttbar Toy MC v2.6 — Post-Registration: Multi-Seed Ensemble "
    "Results,\" DOI: 10.5281/zenodo.24373115 (50-seed ensemble, identified Tag CV ≈ 7.4%).",

    "[I4] W. S. Paik, \"ALP-ttbar Toy MC v2.6 — Preregistration: Multi-Seed Ensemble,\" "
    "DOI: 10.5281/zenodo.24361872.",

    "[I5] W. S. Paik, \"ALP-ttbar Toy MC v2.5 — Post-Registration: Deconflation,\" "
    "DOI: 10.5281/zenodo.24341050.",

    "[I6] W. S. Paik, \"ALP-ttbar Toy MC v2.5 — Preregistration: Deconflation,\" "
    "DOI: 10.5281/zenodo.24329044.",

    "[I7] W. S. Paik, \"ALP-ttbar Toy MC v2.4 — Post-Registration: 17-Band Geometry,\" "
    "DOI: 10.5281/zenodo.24302619 (introduced the 17-band geometry used here).",

    "[I8] W. S. Paik, \"ALP-ttbar Toy MC v2.4 — Preregistration: 17-Band Geometry,\" "
    "DOI: 10.5281/zenodo.24296796.",
]

for ref in refs_int:
    story.append(Paragraph(ref, ParagraphStyle("RefInt", fontName="DejaVu", fontSize=7.5,
                                                leading=10, textColor=DARK,
                                                leftIndent=8*mm, firstLineIndent=-8*mm,
                                                spaceAfter=1.5*mm)))

# --- Build ---
doc.build(story)

from pypdf import PdfReader
reader = PdfReader(OUT_PDF)
n_pages = len(reader.pages)
size_mb = os.path.getsize(OUT_PDF) / (1024 * 1024)
print(f"PDF generated: {n_pages} pages, {size_mb:.2f} MB")
print(f"  → {OUT_PDF}")
