# Impact-assessment method — quantifying the *apport* of lockers and micro-hubs

**Purpose.** Provide a transparent, reproducible way to estimate the contribution
of automated parcel lockers and micro-hubs *relative to the current baseline*
(dispersed van home/relay delivery), computed from open data and documented
emission factors — independent of the earlier student spreadsheets.

Everything below is implemented in `code/impact_analysis.py`. Each parameter
carries a source tag: `[open]` computed from open data, `[corpus]` from the
supplied reports (to confirm), `[factor]` documented agency/literature factor,
`[assum]` analyst assumption (sensitivity-tested).

---

## Baseline (reference scenario)

The current scheme: business-to-consumer (B2C) parcels delivered to the home or
to a relay point by diesel light goods vehicles (LGV) running dispersed rounds,
plus a residual share of failed first attempts that are re-delivered. This is the
reference against which both levers are measured.

## A. Demand model (open data)

Weekly e-commerce demand per quartier *i*:

> D_i = (P_i / H) · r

with P_i the quartier population `[open, INSEE]`, H persons per household
(≈ 2.0) `[open]`, r = 0.31 parcels/household/week `[corpus, FEVAD 2018]`.

*Validation.* Summed over La Rochelle this gives **≈ 11,900 parcels/week**, within
~8 % of the 2018 professional diagnostic (~12,900/week). The demand model
therefore reproduces an independent source and can be trusted as the denominator
for both levers.

## B. Coverage model (supply vs demand)

Point-in-polygon of the 148 surveyed collection points (incl. 9 lockers) into the
31 quartiers gives, per quartier, supply counts against demand D_i. Two headline
indicators:

- **Population served by ≥ 1 locker: 23 %** (vs 87 % for any collection point).
- **Dense quartiers with zero locker** (priority *apport* targets): Les Minimes–
  Université (752 parcels/wk), La Genette, Laleu, Fétilly, **Mireuil Est** (496),
  **Port Neuf**, **Villeneuve** — several of them the very e-commerce poles named
  in the 2018 diagnostic.

The *apport* of a locker programme is then the demand brought within service by
siting lockers in under-served, PT-accessible, dense quartiers (Fig. 1a).
A finer walking-catchment (population raster + 400 m buffers) is the natural
refinement once a sub-quartier population grid in WGS-84 is available.

## C. Emissions model (baseline vs scenario)

Documented factors: LGV diesel **f_van = 0.27 kgCO₂e/km** `[factor, ADEME Base
Carbone]` (cross-check: 15 L/100 km × 2.5 kgCO₂/L ≈ 0.38 kg/km fuel-only);
e-cargo-bike **f_bike = 0.013 kgCO₂e/km** `[corpus/factor]`; per-parcel out-of-home
vs home **12 vs 50 gCO₂** `[corpus]`.

### C.i Lockers — out-of-home diversion

> ΔCO₂_lockers = α · P · [(e_home − e_locker) + φ · e_home]

α diverted share `[assum, sensitivity]`, P parcels/year (= 52·ΣD_i ≈ 619,000),
φ avoided re-delivery share `[assum ≈ 0.15]`. At α = 15 %: **≈ 3.5 t/yr** from the
per-parcel differential plus **≈ 0.7 t/yr** from fewer failed re-deliveries. The
figure scales linearly with coverage × adoption — hence the value of siting
lockers where demand is (Block B).

### C.ii Micro-hubs — modal shift on the last leg

> ΔCO₂_hub = (KM_van_base − KM_van_stem) · f_van − KM_bike · f_bike

For the Aunis Messagerie perimeter (3 vans): baseline 3 × 80 km/day ⇒ **16.2 t/yr**;
scenario vans run depot→hub stems only (3 × 40 km/day) + cargo-bikes for the last
leg ⇒ **≈ 8.5 t/yr**; **saving ≈ 7.7 t/yr (≈ 48 %)** of the perimeter's last-mile
van emissions. Because f_bike is ~20× smaller than f_van, the result is driven by
the **van-kilometres removed** and is robust to the cargo-bike assumption.

**Honest boundary.** `KM_van_base`, `KM_van_stem` and `KM_bike` are operational
inputs that must be **measured from real tours** (GPS traces or the carrier's TMS),
not assumed. The model makes every input explicit so the carrier can plug in
measured values; the emission factors are documented, not bespoke. This is the
key difference from the earlier spreadsheet: the 48 % is a *method output on
stated inputs*, auditable line by line, not a black-box percentage.

---

## What this buys the paper

1. A **defensible, reproducible** impact figure for each lever, replacing opaque
   numbers.
2. A **demand model validated** against an independent source (±8 %).
3. A **coverage diagnosis** (23 % / zero-locker quartiers) that directly motivates
   the siting.
4. A clear **measurement to-do** (tour lengths, adoption, walking-catchment) that
   becomes the empirical programme of the full paper.
