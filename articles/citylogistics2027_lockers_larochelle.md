---
title: "From convenience asset to network lever: siting automated parcel lockers and its impact on the local urban logistics scheme — the case of La Rochelle (France)"
authors:
  - Corwin Fevre (EIGSI La Rochelle)
  - Tatiana Graindorge (EIGSI La Rochelle)
  - Robin David (EIGSI La Rochelle)
  - Jean-Philippe Samier (EIGSI La Rochelle)
event: "14th International Conference on City Logistics (City Logistics 2027), Algarve, Portugal"
type: "Extended abstract (3 pages)"
target_proceedings: "Transportation Research Procedia (Elsevier)"
date: "2026-07-01 (draft v3 — 3-page, verified citations)"
---

<!--
  3-page EXTENDED ABSTRACT for City Logistics 2027 (deadline 15 July 2026).
  English. Produced via the ARS academic-paper pipeline. Condensed to fit 3 pages.
  Integrity: La Rochelle figures from the supplied corpus (refs 1-5); external
  refs 6-9 verified with DOIs. Exact pagination to be confirmed in the Elsevier
  Procedia template.
-->

## Abstract

Automated parcel lockers (APLs) are widely deployed to relieve the externalities of e-commerce last-mile delivery, yet their value to the wider freight system is decided less by the technology than by **where lockers are placed**. This paper asks how locker siting reshapes the *local* urban logistics scheme of a mid-sized, geographically peripheral city, and pairs a state-of-the-art review, grounded in two professional freight diagnostics of La Rochelle (France), with a multi-year field experimentation from three engineering projects (2021–2026). A reproducible GIS multicriteria workflow, applied to 148 surveyed collection points, the public-transport network and population data, yields ten public-transport-anchored locker sites and exposes a gap between locker supply and demand density. A companion survey classifies 95 public car parks and finds 74 suitable for micro-hub installation, showing that the land to anchor consolidation near demand already exists. Coupling locker siting with this consolidation and cyclo-logistics gives an estimated 40% CO₂ reduction over five years and a 44% cut in truck-kilometres on a real carrier perimeter. For "end-of-line" cities, locker networks deliver system value only when co-designed with consolidation, not as stand-alone amenities.

**Keywords:** city logistics; automated parcel lockers; last-mile delivery; facility location; collection-and-delivery points; La Rochelle

## 1. Introduction

E-commerce has pushed business-to-consumer parcel flows into city centres faster than urban freight systems have adapted, concentrating congestion, emissions, kerbside conflict and failed deliveries in the streets least able to absorb them. Automated parcel lockers answer part of this problem: as unattended, out-of-home collection-and-delivery points, they consolidate many drops into one secured stop and let recipients collect along trips they already make.

The value a locker network returns to the system, however, is fixed at the siting stage. A locker placed for real-estate convenience adds an asset without changing flows; one placed where demand, accessibility and the carrier network coincide restructures rounds and creates the volume that makes consolidated, low-emission distribution viable. Evidence on this link comes mostly from large metropolises, while mid-sized "end-of-line" cities — peripheral to national corridors, served by few national operators — remain thinly documented. We therefore ask: **how does locker siting reshape the local urban logistics scheme of a mid-sized city?** We answer it for La Rochelle (~170,000 inhabitants), whose authority targets carbon neutrality by 2040 and regulates city-centre delivery (06:00–11:00 windows; a goal of fully low-emission vehicles). The contribution is a transferable, low-data siting method and evidence that public-transport-anchored siting plus consolidation reshapes — not merely supplements — the local scheme.

## 2. State of the art and local context

**Locker siting.** Locker location is a facility-location problem balancing coverage, demand density and multimodal accessibility against capital cost and cannibalisation of existing collection points [7]. Two solution families dominate: exact optimisation of locker number, size and location [7], and GIS-based multicriteria decision-making that ranks candidate sites on accessibility and demand [9]. Both converge on a compact set of criteria — proximity to public-transport (PT) nodes and soft modes, residential and footfall density, insertion into daily trips — and report re-delivery cuts near 30% and lower per-parcel emissions than van home delivery [6, 8]. Empirical studies warn that lockers are often sited for car rather than transit access, limiting reach [8]; PT-anchored pilots (Valencia, SPROUT; Paris, RATP–Pickup) are the corrective [refs 3–5]. We extend this logic in two rarely-combined ways: a low-data, reproducible workflow for mid-sized cities, and the joint siting of lockers *and* the upstream consolidation land that makes them effective.

**The La Rochelle freight system.** A 2018 FRETURB diagnostic quantified ~101,300 goods movements/week across the agglomeration, ~2,290/day in the historic centre, with e-commerce at 0.31 parcels/household/week (~25,300/week, ~20% of movements) concentrated on two poles — a dense historic core and a large social-housing district [ref 1]. The territory relied on an electric consolidation centre (Elcidis, 2001–2018) and 72 delivery bays, ~80% undersized. A 2024 study typologised logistics objects (urban delivery/service spaces including lockers; distribution spaces; platforms; regional gateways) and characterised La Rochelle as an "end-of-line" market with few resident national operators [ref 2].

## 3. Case study and method

Three EIGSI field projects form one line of inquiry:

- **P1 (2021), cargo-bike last mile** — hyper-centre flow analysis (633 shops, 38 streets, ~31% pedestrian) and comparative CO₂ accounting (cargo-bike ≈ 13 vs. thermal van ≈ 220 g/km) [ref 3].
- **P2 (2024), locker siting** — a reproducible GIS multicriteria workflow (Python/GeoPandas): inventory of 148 collection points (relays, agencies, 9 lockers); enrichment with PT stops (Yélo, 1,414 stops), bike-share and car parks; 5-minute walk buffers; selection ranking PT proximity first, then non-cannibalisation of relays, then demand density. Output: ten PT-anchored locker sites [ref 4].
- **P3 (2025–2026), VerDelivery + foncier survey** — a consolidation scenario (peripheral car-park nano-hubs fed by light goods vehicles, cargo-bikes for the final leg) on a real carrier perimeter (Aunis Messagerie); and a classification of 95 public car parks by goods-vehicle compatibility (surface ≥ 3 m = candidate; surface < 3 m = conditional; structured = excluded) [ref 5].

![Figure 1. Two field experiments on the local urban logistics scheme of La Rochelle, on a common extent and population backdrop. **(a) Locker siting:** 120 relay points/agencies, 9 existing lockers and the Yélo bus network (1,414 stops) — lockers are few and weakly aligned with the densest quartiers, whereas the PT network offers dense candidate anchors. **(b) Micro-hub foncier:** 95 car parks by light-goods-vehicle compatibility (74 surface ≥ 3 m = candidates, 9 conditional, 12 excluded; marker size ∝ capacity), with the Espace Encan pilot. Field data, EIGSI 2024–2026.](../figures/png/larochelle_two_experiments.png)

## 4. Results

**A visible coverage gap.** The surveyed network (Fig. 1a) has 120 relay points but only 9 automated lockers, clustered on the centre and eastern axis and weakly aligned with the densest quartiers; the Yélo network instead offers 1,414 candidate anchor nodes across the demand surface.

**Siting.** The multicriteria analysis returns ten PT-integrated, high-footfall, under-served locations (railway station, Place de Verdun, university campus/residences, Yélo interchanges), complementary to existing relays and to candidate micro-hubs. Corpus benchmarks: 24/7 access and fewer failed deliveries; ~6,200 parcels/yr per unit; ~12 g CO₂/parcel versus ~50 g for a van [refs 4–5].

**Land for consolidation.** The foncier survey (Fig. 1b) classifies 95 car parks: 74 surface sites meet the ≥ 3 m clearance light goods vehicles need (micro-hub candidates), 9 are conditional, 12 are excluded; the Espace Encan car park (~420 spaces) is the VerDelivery pilot. The recurring "no available land" objection to consolidation does not hold here.

**System-level impact.** Coupling locker siting with this consolidation and cyclo-logistics (P3) yields ≈ **40% CO₂ reduction over five years** (236 → 128 tCO₂e), a **44% cut in truck-kilometres**, and ~€5,505/yr fuel savings on the studied perimeter [ref 5]. Mechanistically, lockers act as demand anchors that pull dispersed home deliveries into off-peak, consolidated provisioning and create the volume that justifies micro-/nano-hub and cargo-bike distribution; anchoring them to the Yélo network materialises a passenger–freight interface.

## 5. Discussion

Siting is the decisive lever: PT-anchored, density-aware placement maximises utilisation and modal-shift potential, whereas sites chosen for availability alone risk cannibalising relay points (~30% of host-shop turnover) without net gain. Barriers persist — a durable home-delivery preference, insufficient network density, capital cost (~€1,000/yr installed; €3,000–30,000/unit), accessibility for reduced-mobility users, and governance. The lesson for "end-of-line" cities is integration: with few resident national operators, a locker network returns system benefits only when co-designed with consolidation and local cyclo-logistics. With 74 compatible car parks, the land to host that consolidation already exists — the binding constraint is institutional, not spatial.

## 6. Conclusion

The work links locker **siting** to **system-level impact** in a real mid-sized case, bridging professional diagnostics and field experimentation, and shows that PT-anchored siting plus consolidation reshapes the local scheme rather than merely adding capacity. Planned extensions include a capacitated coverage / p-median optimisation of the candidate lockers and car parks [7], post-deployment utilisation monitoring, and integration into the agglomeration's logistics roadmap and delivery-bay master plan.

## Statements

**Data availability.** La Rochelle figures derive from the supplied corpus (refs 1–5); the collection-point, car-park, bus-network and population datasets and the figure scripts are available from the authors. **Author contributions (CRediT):** conceptualisation T. Graindorge, C. Fevre; data/software R. David, C. Fevre; analysis all; draft C. Fevre; supervision T. Graindorge, J.-P. Samier (to be confirmed). **AI-usage disclosure:** drafting/editing were AI-assisted under author supervision; all data, analysis and conclusions are the authors' own. **Conflicts of interest:** none.

## References

*(Corpus items 1–5 are primary sources supplied for this study. External references 6–9 were verified against bibliographic databases; DOIs given.)*

1. Interface Transport (2018). *Base de connaissances marchandises — CdA de La Rochelle.* [corpus]
2. Interface Transport (2024). *Étude sur les besoins en foncier logistique — CdA de La Rochelle.* [corpus]
3. EIGSI (2021). *Projet I&E n°1 — Cargo-Vélo La Rochelle.* [corpus]
4. EIGSI (2024). *Projet IE 49 — LOG_URB_ROCHELLE (lockers & micro-hubs).* [corpus]
5. EIGSI (2025–2026). *Projet PIE 26-38 — VerDelivery.* [corpus]
6. Iwan, S., Kijewska, K., Lemke, J. (2016). Analysis of parcel lockers' efficiency as the last-mile delivery solution — the results of the research in Poland. *Transportation Research Procedia*, 12, 644–655. https://doi.org/10.1016/j.trpro.2016.02.018
7. Deutsch, Y., Golany, B. (2018). A parcel locker network as a solution to the logistics last-mile problem. *International Journal of Production Research*, 56(1–2), 251–261. https://doi.org/10.1080/00207543.2017.1395490
8. Lachapelle, U., Burke, M., Brotherton, A., Leung, A. (2018). Parcel locker systems in a car-dominant city: location, characterisation and potential impacts on city planning and consumer travel access. *Journal of Transport Geography*, 71, 1–14. https://doi.org/10.1016/j.jtrangeo.2018.06.022
9. Bovkir, R., Moslem, S., Pilla, F. (2025). GIS-based fuzzy multi-criteria decision-making for selecting optimal parcel lockers location: a case study in Dublin, Ireland. *Land Use Policy*, 158, 107771. https://doi.org/10.1016/j.landusepol.2025.107771
