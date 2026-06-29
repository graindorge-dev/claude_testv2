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
date: "2026-06-29 (draft v2, ARS academic-paper pipeline)"
---

<!--
  Extended abstract for City Logistics 2027. Target: 3 pages, English.
  Produced via the ARS academic-paper pipeline (outline + draft mode).
  Integrity: La Rochelle figures are sourced from the supplied corpus (refs 1-5);
  citations marked [verify] are well-known works still to be confirmed against
  bibliographic databases before submission (no DOI fabricated — IRON RULE).
-->

## Abstract

Automated parcel lockers (APLs) are widely deployed to relieve the externalities of e-commerce last-mile delivery, yet their contribution to the wider urban freight system is decided less by the technology than by **where lockers are placed**. This paper asks how locker siting reshapes the *local* urban logistics scheme of a mid-sized, geographically peripheral city. We pair a state-of-the-art review, grounded in two professional freight diagnostics of La Rochelle (France), with a real, multi-year experimentation drawn from three engineering field projects (2021–2026). A reproducible GIS multicriteria workflow, applied to 148 surveyed collection points, the public-transport network and population data, yields ten public-transport-anchored locker sites and exposes a coverage gap between locker supply and demand density. Coupling that siting with upstream consolidation (micro-/nano-hubs) and cyclo-logistics produces an estimated 40% CO₂ reduction over five years and a 44% cut in truck-kilometres on a real carrier perimeter. We conclude that, for "end-of-line" cities, locker networks deliver system value only when co-designed with consolidation rather than deployed as stand-alone retail amenities.

**Keywords:** city logistics; automated parcel lockers; last-mile delivery; facility location; collection-and-delivery points; e-commerce; La Rochelle

## 1. Introduction and objective

E-commerce has pushed business-to-consumer (B2C) parcel flows into city centres faster than urban freight systems have adapted. The resulting last mile concentrates congestion, local emissions, kerbside conflict and failed first deliveries in exactly the streets least able to absorb them. Automated parcel lockers answer part of this problem: as unattended, out-of-home collection-and-delivery points, they consolidate many drops into one secured stop and let recipients collect along trips they already make.

The value a locker network returns to the *system*, however, is fixed at the siting stage. A locker placed for real-estate convenience adds an asset without changing flows; a locker placed where demand, accessibility and the carrier network coincide restructures rounds, shifts collection out of the home, and creates the volume that makes consolidated, low-emission distribution viable. Evidence on this siting–impact link comes mostly from large metropolitan areas. Mid-sized, "end-of-line" cities — peripheral to national corridors, served by few national operators and dependent on local subcontractors — remain thinly documented, even though they face the same regulatory pressure to decarbonise.

This paper addresses that gap with a single guiding question: **how does locker siting reshape the local urban logistics scheme of a mid-sized city?** We answer it for La Rochelle (France), a coastal agglomeration of ~170,000 inhabitants whose authority targets carbon neutrality by 2040, regulates city-centre delivery (06:00–11:00 windows; a stated goal of fully low-emission delivery vehicles), and hosts ~14,000 students. The contribution is twofold: a transferable, data-driven siting method, and evidence that public-transport-anchored siting combined with consolidation reshapes — not merely supplements — the local scheme.

## 2. State of the art and local context

### 2.1 Locker siting as a city-logistics scheme

Locker location is a facility-location problem in which coverage, demand density and multimodal accessibility are balanced against capital cost and the cannibalisation of existing collection points. The literature converges on a compact set of siting criteria: proximity to public-transport (PT) nodes and soft-mode networks, residential and footfall density, and insertion into daily mobility chains. Reported effects include re-delivery reductions of roughly 30% and markedly lower per-parcel emissions than van home delivery [verify: Iwan et al. 2016; Deutsch & Golany 2018; Lachapelle et al. 2018]. PT-anchored pilots are instructive: connected lockers placed in metro or bus stations (Valencia, SPROUT; Paris, RATP–Pickup) concentrate carrier drops at one node while travellers collect en route [ref. 3–5].

### 2.2 The La Rochelle freight system

Two professional diagnostics frame the local scheme. The 2018 FRETURB-based study quantified about 101,300 goods movements per week across the agglomeration, of which roughly 2,290 per day occur in the historic centre; e-commerce alone reached an estimated 0.31 parcels per household per week (~25,300 deliveries weekly, near 20% of all movements), concentrated on two poles — a dense historic core (Centre Marché, ~510 parcels/week) and a large social-housing district (Mireuil, ~285 parcels/week) [ref. 1]. The territory long relied on an electric urban consolidation centre (Elcidis, 2001; public-service delegation ended 2018) and on 72 city-centre delivery bays, about 80% undersized against national guidance. The 2024 logistics-real-estate study added an object typology — urban delivery and service spaces (which explicitly include lockers and relay points), urban distribution spaces, urban distribution platforms, and regional gateways — and characterised La Rochelle as an "end-of-line" market with few resident national operators [ref. 2]. Together the two diagnostics establish both a substantial out-of-home delivery demand and the spatial constraints any locker network must respect.

## 3. Case study and method

The experimentation rests on three EIGSI field projects forming one line of inquiry:

- **P1 (2021), cargo-bike last mile** — partnership with a local cyclo-logistics operator; a hyper-centre flow analysis (633 shops over 38 streets, ~31% in pedestrian zones) and comparative CO₂ accounting (cargo-bike ≈ 13 g/km versus thermal van ≈ 220 g/km) [ref. 3].
- **P2 (2024), locker and micro-hub siting** — a reproducible GIS multicriteria workflow (Python, GeoPandas, Folium): (1) inventory of 148 existing collection points (relay points, agencies and 9 automated lockers); (2) enrichment with PT stops (Yélo network, 1,414 stops), bike-share stations and car parks; (3) five-minute walking-distance buffers; (4) multicriteria selection ranking PT proximity first, then non-cannibalisation of existing relays, then population and footfall density including the student population. The output is ten priority locker sites, each anchored to a bus stop [ref. 4].
- **P3 (2025–2026), VerDelivery** — a consolidation scenario inspired by the OVO model: peripheral car-park *nano-hubs* fed by light goods vehicles, with cargo-bikes performing the final leg, assessed on the real perimeter of a local carrier (Aunis Messagerie) [ref. 5].

Impacts are evaluated with per-mode CO₂ factors, vehicle-movement and vehicle-kilometre changes, and a consolidation logic that links siting decisions to the wider scheme.

![Figure 1. Existing parcel collection points in La Rochelle (120 relay points/agencies, 9 automated lockers), the Yélo bus network and population density by quartier (Projet IE 49 field data, EIGSI 2024). Lockers are few and weakly aligned with the densest quartiers, whereas the PT network offers dense candidate anchors — the siting opportunity this paper exploits.](../figures/png/larochelle_collection_points.png)

## 4. Results

**A visible coverage gap.** Mapping the surveyed network (Fig. 1) shows 120 relay points but only 9 automated lockers, clustered along the centre and the eastern commercial axis and weakly aligned with the densest residential quartiers identified in the 2018 diagnostic. The Yélo network, by contrast, provides 1,414 candidate anchor nodes spread across the demand surface. Supply and demand are therefore spatially mismatched, and the PT network is the obvious lever to close the gap.

**Siting.** The multicriteria analysis returns ten PT-integrated, high-footfall, currently under-served candidate sites (among them the railway station, Place de Verdun, university residences and campus, and Yélo interchanges), each complementary to existing relays and to candidate micro-hubs. Ranking PT proximity ahead of pure density keeps the network legible to users and aligned with daily trips.

**Locker performance benchmarks.** Drawn from the corpus: 24/7 access and fewer failed deliveries; on the order of 6,200 parcels per year per unit; PT-station lockers in the Valencia pilot saved about 3,937 kg CO₂ per year each; roughly 12 g CO₂ per parcel versus about 50 g for a van delivery [ref. 4–5].

**System-level impact.** When siting is coupled with upstream consolidation and cyclo-logistics (P3), the modelled scenario yields about a 40% CO₂ reduction over five years (236 → 128 tCO₂e), a 44% cut in truck-kilometres, and roughly €5,505 per year in fuel savings on the studied perimeter [ref. 5]. The mechanism matters more than the headline figure: lockers act as **demand anchors** that pull dispersed home deliveries into off-peak, consolidated provisioning and create the volume that justifies micro-/nano-hub and cargo-bike distribution. Anchoring lockers to the Yélo network also materialises a passenger–freight interface, a recognised city-logistics topic.

## 5. Discussion

Siting is the decisive lever. PT-anchored, density-aware placement maximises utilisation and modal-shift potential, whereas sites chosen for availability alone risk cannibalising relay points, which contribute close to 30% of host-shop turnover, without net system gain. Real barriers persist: a durable home-delivery preference, insufficient network density, capital cost (around €1,000/year installed; €3,000–30,000 per unit), accessibility for reduced-mobility users, and governance and land-pressure questions that demand public–private coordination.

The central lesson for mid-sized "end-of-line" cities is integration. With few resident national operators and a reliance on local subcontractors, a locker network returns system-level benefits only when co-designed with consolidation (urban consolidation centres, micro- and nano-hubs) and local cyclo-logistics. Siting thus reframes lockers from a convenience product into a structuring component of the local scheme, and links a retail-facing decision to carrier-level emissions and vehicle activity.

## 6. Conclusion and perspectives

This work connects locker **siting** to **system-level impact** in a real mid-sized case, bridging two professional freight diagnostics and three years of field experimentation. It offers a transferable GIS multicriteria siting workflow and evidence that PT-anchored siting plus consolidation reshapes the local scheme rather than merely adding capacity. Planned extensions include a capacitated coverage / p-median optimisation of the ten candidate sites, post-deployment utilisation monitoring, a full-territory simulation, and formal integration into the agglomeration's logistics roadmap and its delivery-bay master plan (*Schéma Directeur des Aires de Livraison*).

## Statements

**Data availability.** The La Rochelle figures derive from the supplied corpus (refs 1–5). The collection-point, bus-network and population datasets and the figure-generation script are available from the authors.

**Author contributions (CRediT).** Conceptualisation: T. Graindorge, C. Fevre. Data curation and software: R. David, C. Fevre. Methodology and formal analysis: all authors. Writing — original draft: C. Fevre. Supervision: T. Graindorge, J.-P. Samier. *(To be confirmed by the team.)*

**AI-usage disclosure.** Drafting and editing of this abstract were assisted by an AI writing tool under author supervision; all data, analysis and conclusions are the authors' own and were verified against the source material.

**Conflicts of interest.** None declared.

## References

*(Provisional. Corpus items (1–5) are primary sources supplied for this study; items marked [verify] are well-known works to be confirmed against bibliographic databases before submission — no DOI has been fabricated.)*

1. Interface Transport (2018). *Mission d'accompagnement à l'élaboration d'une politique de transport de marchandises sur le territoire de la CdA de La Rochelle — Base de connaissances marchandises.* [corpus]
2. Interface Transport (2024). *Étude sur les besoins en foncier logistique pour le territoire de la CdA de La Rochelle.* [corpus]
3. EIGSI (2021). *Projet I&E n°1 — Cargo-Vélo La Rochelle, rapport final.* [corpus]
4. EIGSI (2024). *Projet IE Groupe 49 — LOG_URB_ROCHELLE (lockers & micro-hubs), rapport final.* [corpus]
5. EIGSI (2025–2026). *Projet PIE 26-38 — VerDelivery, rapport final.* [corpus]
6. Iwan, S., Kijewska, K., Lemke, J. (2016). Analysis of parcel lockers' efficiency as the last-mile delivery solution. *Transportation Research Procedia.* [verify]
7. Deutsch, Y., Golany, B. (2018). A parcel locker network as a solution to the logistics last-mile problem. *International Journal of Production Research.* [verify]
8. Lachapelle, U., Burke, M., Brotherton, A., Leung, A. (2018). Parcel lockers and collection-and-delivery points in a car-dominant city. *Journal of Transport Geography.* [verify]
9. Dablanc, L. (2007). Goods transport in large European cities. *Transportation Research Part A.* [verify]
10. Taniguchi, E., Thompson, R.G., Yamada, T. — modelling city logistics schemes. [verify]
