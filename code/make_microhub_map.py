#!/usr/bin/env python3
"""
Map candidate land for micro-hubs in La Rochelle: public car parks classified by
light-goods-vehicle (LGV) compatibility, from the EIGSI "VerDelivery" foncier survey.

Classification (report logic = surface + clearance):
    green  : surface car park AND hauteur_max >= 300 cm  -> micro-hub candidate
    yellow : surface car park AND hauteur_max <  300 cm  -> conditional (adjustable portico)
    other  : structured (en ouvrage)                     -> excluded

Inputs:
    DATA/Parkings.xlsx      cols: nom, adresse, nb_places, hauteur_max (cm),
                            Xlong, Ylat, type_ouvrage
    DATA/population.geojson INSEE population by quartier (context backdrop)

Outputs:
    figures/png/larochelle_microhub_parkings.png  (300 dpi)
    figures/svg/larochelle_microhub_parkings.svg

Deps: geopandas, matplotlib, pandas, openpyxl. Adjust paths before running.
"""
import math, warnings
warnings.filterwarnings("ignore")
import geopandas as gpd, pandas as pd, openpyxl
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PARKINGS = "DATA/Parkings.xlsx"
POP      = "DATA/population.geojson"
OUT_PNG  = "figures/png/larochelle_microhub_parkings.png"
OUT_SVG  = "figures/svg/larochelle_microhub_parkings.svg"


def fnum(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def category(htmax_cm, type_ouvrage):
    surface = "surface" in (type_ouvrage or "")
    if surface and (htmax_cm or 0) >= 300:
        return "green"
    if surface and (htmax_cm or 0) < 300:
        return "yellow"
    return "other"


def main():
    wb = openpyxl.load_workbook(PARKINGS, read_only=True, data_only=True)
    rows = list(wb.active.iter_rows(values_only=True))
    hdr = [str(c) for c in rows[0]]
    recs = []
    for r in rows[1:]:
        if not r or not r[0]:
            continue
        d = dict(zip(hdr, r))
        x, y = fnum(d.get("Xlong")), fnum(d.get("Ylat"))
        if x is None or y is None:
            continue
        recs.append({"nom": d.get("nom"), "x": x, "y": y,
                     "h": fnum(d.get("hauteur_max")), "places": fnum(d.get("nb_places")),
                     "cat": category(fnum(d.get("hauteur_max")), str(d.get("type_ouvrage") or ""))})

    pop = gpd.read_file(POP).set_crs(4326, allow_override=True)
    cands = {c: pd.to_numeric(pop[c], errors="coerce").notna().sum()
             for c in ["pop_rp_2009", "pop_rp_2007", "pop_rp_1999"] if c in pop.columns}
    popcol = max(cands, key=cands.get)
    pop[popcol] = pd.to_numeric(pop[popcol], errors="coerce")

    def sub(c):
        return [r for r in recs if r["cat"] == c]

    def sz(r):
        return 18 + (r["places"] or 50) / 8.0

    fig, ax = plt.subplots(figsize=(9, 8))
    pop.plot(column=popcol, cmap="Greys", ax=ax, edgecolor="#b8bcc2",
             linewidth=0.4, alpha=0.45, zorder=1)
    styles = [("other", "#c2c2c2", 2, "Structured (en ouvrage) — excluded"),
              ("yellow", "#f4b400", 3, f"Surface, < 3 m — conditional (n={len(sub('yellow'))})"),
              ("green", "#2e7d32", 4, f"Surface ≥ 3 m — micro-hub candidate (n={len(sub('green'))})")]
    for c, face, z, lab in styles:
        S = sub(c)
        ax.scatter([r["x"] for r in S], [r["y"] for r in S], s=[sz(r) for r in S],
                   facecolor=face, edgecolor="white", linewidth=0.5, alpha=0.9, zorder=z, label=lab)
    enc = [r for r in recs if "ncan" in str(r["nom"])]
    if enc:
        ax.scatter([r["x"] for r in enc], [r["y"] for r in enc], s=260, marker="*",
                   facecolor="#e8710a", edgecolor="black", linewidth=0.8, zorder=6,
                   label="Espace Encan — VerDelivery pilot")

    ax.set_xlim(-1.20, -1.085); ax.set_ylim(46.135, 46.195)
    ax.set_aspect(1 / math.cos(math.radians(46.16)))
    ax.set_title("Candidate land for micro-hubs: La Rochelle car parks by LGV compatibility\n"
                 "(foncier survey, EIGSI VerDelivery 2025–26; marker size ∝ capacity)",
                 fontsize=11.5, fontweight="bold")
    ax.set_xlabel("Longitude"); ax.set_ylabel("Latitude")
    ax.legend(loc="lower left", fontsize=8, framealpha=0.92)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=300, bbox_inches="tight")
    fig.savefig(OUT_SVG, bbox_inches="tight")
    print(f"saved {OUT_PNG} | green/yellow/other: "
          f"{len(sub('green'))}/{len(sub('yellow'))}/{len(sub('other'))}")


if __name__ == "__main__":
    main()
