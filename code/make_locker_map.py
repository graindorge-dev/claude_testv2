#!/usr/bin/env python3
"""
Generate a publication-quality map of La Rochelle parcel collection points
(relay points + automated lockers) over a population-density choropleth and the
Yelo bus network, from the EIGSI "Projet IE 49" (2024) field data.

Inputs (from the students' GeoData export):
    DATA/population.geojson      INSEE population by quartier (uses pop_rp_2007)
    DATA/bus_stop.geojson        Yelo stops (coords in stop_lat / stop_lon props)
    points_de_collecte.json      148 collected points (Latitude/Longitude, locker flag)

Outputs:
    figures/png/larochelle_collection_points.png  (300 dpi)
    figures/svg/larochelle_collection_points.svg  (vector)

Deps: geopandas, matplotlib, pandas, shapely.
Adjust DATA_DIR / CP_JSON to your local paths before running.
"""
import json, math, warnings
warnings.filterwarnings("ignore")
import geopandas as gpd, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

DATA_DIR = "DATA"                     # folder with the *.geojson files
CP_JSON  = "points_de_collecte.json"  # [{name,brand,type,locker,Latitude,Longitude}, ...]
OUT_PNG  = "figures/png/larochelle_collection_points.png"
OUT_SVG  = "figures/svg/larochelle_collection_points.svg"


def fnum(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def main():
    pop = gpd.read_file(f"{DATA_DIR}/population.geojson").set_crs(4326, allow_override=True)
    # pick the population column with the most numeric (non-empty) values
    cands = {c: pd.to_numeric(pop[c], errors="coerce").notna().sum()
             for c in ["pop_rp_2009", "pop_rp_2007", "pop_rp_1999"] if c in pop.columns}
    popcol = max(cands, key=cands.get)
    pop[popcol] = pd.to_numeric(pop[popcol], errors="coerce")

    cp = json.load(open(CP_JSON))
    pts = []
    for d in cp:
        la, lo = fnum(d.get("Latitude")), fnum(d.get("Longitude"))
        if la is None or lo is None or not (46.05 < la < 46.40 and -1.45 < lo < -1.00):
            continue  # keep La Rochelle area; drops a sign-error outlier
        pts.append((lo, la, str(d.get("locker")).lower() == "yes"))
    relay = [(x, y) for x, y, l in pts if not l]
    lock = [(x, y) for x, y, l in pts if l]

    bus = json.load(open(f"{DATA_DIR}/bus_stop.geojson"))
    bx, by = [], []
    for ft in bus["features"]:
        p = ft["properties"]
        la, lo = fnum(p.get("stop_lat")), fnum(p.get("stop_lon"))
        if la and lo and 46.05 < la < 46.40 and -1.45 < lo < -1.00:
            bx.append(lo); by.append(la)

    fig, ax = plt.subplots(figsize=(9, 8))
    pop.plot(column=popcol, cmap="Blues", ax=ax, edgecolor="#88909a", linewidth=0.5,
             legend=True, alpha=0.80, zorder=1,
             legend_kwds={"label": f"Population par quartier ({popcol[-4:]})", "shrink": 0.55})
    ax.scatter(bx, by, s=4, c="#9aa0a6", alpha=0.55, marker=".", zorder=2,
               label=f"Arrêts de bus Yélo (n={len(bx)})")
    ax.scatter([p[0] for p in relay], [p[1] for p in relay], s=34, facecolor="#1a73e8",
               edgecolor="white", linewidth=0.5, zorder=4,
               label=f"Points relais / agences (n={len(relay)})")
    ax.scatter([p[0] for p in lock], [p[1] for p in lock], s=140, marker="*",
               facecolor="#e8710a", edgecolor="black", linewidth=0.7, zorder=5,
               label=f"Consignes automatiques (n={len(lock)})")
    ax.set_xlim(-1.245, -1.105); ax.set_ylim(46.135, 46.193)
    ax.set_aspect(1 / math.cos(math.radians(46.16)))
    ax.set_title("La Rochelle — points de collecte de colis et densité de population par quartier\n"
                 "(données projet IE 49, EIGSI 2024)", fontsize=12, fontweight="bold")
    ax.set_xlabel("Longitude"); ax.set_ylabel("Latitude")
    ax.legend(loc="lower left", fontsize=8, framealpha=0.92)
    ax.text(0.99, 0.01, "Sources : OpenStreetMap, INSEE (RP), réseau Yélo, relevés étudiants EIGSI (2024)",
            transform=ax.transAxes, ha="right", va="bottom", fontsize=6, color="#555")
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=300, bbox_inches="tight")
    fig.savefig(OUT_SVG, bbox_inches="tight")
    print(f"saved {OUT_PNG} and {OUT_SVG} | relays={len(relay)} lockers={len(lock)} bus={len(bx)}")


if __name__ == "__main__":
    main()
