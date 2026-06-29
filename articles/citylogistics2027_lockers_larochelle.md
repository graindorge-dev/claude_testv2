---
title: "Siting automated parcel lockers and its impact on the local urban logistics scheme: an extended case study of La Rochelle (France)"
author:
  - Corwin Fevre (EIGSI La Rochelle)
  - Tatiana Graindorge (EIGSI La Rochelle)
  - Robin David
  - Jean-Philippe Samier
event: "14th International Conference on City Logistics (City Logistics 2027), Algarve, Portugal"
type: "Extended abstract (3 pages)"
date: "2026-06-29 (draft)"
---

<!--
  DRAFT extended abstract for City Logistics 2027 (Institute for City Logistics).
  Target: 3 pages, English. Candidate for Transportation Research Procedia (Elsevier).
  Status note: La Rochelle figures are sourced from the supplied corpus (see References).
  External academic citations marked [verify] still need database verification before submission.
-->

## Abstract

Automated parcel lockers (APLs) are increasingly promoted as a city-logistics scheme to mitigate the externalities of e-commerce last-mile delivery. Their effectiveness, however, depends critically on **where they are sited**. This paper examines how locker location decisions reshape the *local* urban logistics scheme, using La Rochelle (France) — a mid-sized Atlantic city pursuing carbon neutrality by 2040 — as a case study. We combine (i) a state-of-the-art review of locker siting and last-mile consolidation, grounded in two professional freight diagnostics of the territory (2018, 2024), and (ii) a real-world experimentation drawing on three field-based engineering projects (2021–2026) that mapped relay points, applied multicriteria GIS analysis to propose ten locker sites anchored to the public-transport network, and quantified the effects of coupling lockers with micro-/nano-hubs and cyclo-logistics. Results indicate that demand- and accessibility-driven siting, integrated with upstream consolidation, can cut last-mile vehicle movements and CO₂ emissions while improving service quality, and that mid-sized "end-of-line" cities require locker networks co-designed with local consolidation rather than stand-alone deployments.

**Keywords:** city logistics; automated parcel lockers; last-mile delivery; facility location; e-commerce; collection-and-delivery points; La Rochelle

## 1. Introduction

The growth of e-commerce has intensified business-to-consumer (B2C) parcel flows in city centres, amplifying the well-known externalities of the last mile: congestion, local emissions, noise, kerbside competition and failed first-attempt deliveries. Automated parcel lockers — a form of out-of-home, unattended collection-and-delivery point (CDP) — are now a mainstream city-logistics scheme: by consolidating many drops into a single secured stop with 24/7 customer access, they reduce delivery rounds and failed deliveries while shifting the final leg from the carrier to the consumer's existing mobility patterns.

Yet the benefit of a locker network is largely determined at the **siting** stage. A poorly located locker is under-used and merely adds an asset; a well-located one captures latent demand, integrates with public transport (PT) and soft modes, and restructures local flows. Most empirical evidence comes from large metropolitan areas; mid-sized, "end-of-line" cities — geographically peripheral to national logistics corridors and dependent on local subcontractors — remain under-studied.

This paper addresses that gap. Its **objective** is to assess how locker siting reshapes the local urban logistics scheme of a mid-sized French city, La Rochelle, by combining a structured state of the art with a real, multi-year field experimentation. La Rochelle is an instructive testbed: the *Communauté d'Agglomération* (CdA) targets carbon neutrality by 2040, regulates city-centre access (deliveries 06:00–11:00; a stated objective of 100 % low-emission delivery vehicles), hosts ~14,000 students, and has a dense, constrained historic core.

## 2. State of the art and local context

### 2.1 Locker siting as a city-logistics lever

Locker location is a facility-location problem in which coverage, demand density and multimodal accessibility must be balanced against capital cost and cannibalisation of existing CDPs. The literature converges on a small set of siting criteria — proximity to PT nodes and soft-mode networks, residential and footfall density, and integration into daily mobility chains — and reports that out-of-home delivery can cut re-deliveries by ~30 % and substantially lower per-parcel emissions relative to van home delivery [verify: Iwan et al. 2016; Deutsch & Golany 2018; Lachapelle et al. 2018]. PT-anchored deployments are particularly promising: pilots placing connected lockers in metro/bus stations (e.g. Valencia, SPROUT; Paris, RATP–Pickup) let travellers collect parcels along existing trips, concentrating carrier drops at a single node [corpus].

### 2.2 The La Rochelle freight system

Two professional diagnostics frame the local scheme. The 2018 FRETURB-based study quantified ~101,300 goods movements/week across the CdA, of which ~2,290/day occur in the city centre; e-commerce was estimated at 0.31 parcels/household/week (~25,300 deliveries/week, ~20 % of all movements), with two generator poles (dense historic core; large collective-housing district). The territory has historically relied on an electric urban consolidation centre (Elcidis, 2001; public-service delegation ended 2018) and on 72 city-centre delivery bays, ~80 % of them undersized against national guidelines. The 2024 logistics-real-estate study added an object typology — *urban delivery & service spaces* (including lockers and relay points), *urban distribution spaces* (EUD), *urban distribution platforms*, and *regional gateways* — and characterised La Rochelle as an "end-of-line" market with few national operators and dependence on local last-mile specialists. Together these establish both the demand for out-of-home delivery and the spatial constraints any locker network must respect.

## 3. Case study and method

The experimentation draws on three EIGSI–CdA field projects forming a coherent line of inquiry:

- **P1 (2021) — Cargo-bike last mile.** Partnership with a local cyclo-logistics operator; hyper-centre flow analysis (633 shops over 38 streets, ~31 % in pedestrian zones) and comparative CO₂ accounting (cargo-bike ≈ 13 g/km vs. thermal van ≈ 220 g/km).
- **P2 (2024) — Locker & micro-hub siting.** A reproducible multicriteria GIS workflow (Python/GeoPandas/Folium): (1) inventory of existing relay points and lockers; (2) enrichment with PT stops (Yélo network), bike-share stations and car parks; (3) 5-minute walking-distance buffers; (4) multicriteria selection prioritising PT proximity, avoidance of relay-point cannibalisation, and population/footfall density (including the student population). This yields **ten priority locker sites**, each anchored to a bus stop, plus candidate micro-hub locations.
- **P3 (2025–2026) — VerDelivery.** A consolidation scenario inspired by the OVO model: peripheral car-park *nano-hubs* fed by light goods vehicles, with cargo-bikes performing the final leg; assessed on the Aunis Messagerie city-centre perimeter.

Impacts are evaluated with per-mode CO₂ factors, vehicle-movement and vehicle-kilometre reductions, and a consolidation logic linking siting to the wider scheme.

## 4. Results

**Siting.** The multicriteria analysis (P2) returns ten PT-integrated, high-footfall, currently under-served candidate locations (e.g. the railway station, Place de Verdun, university residences/campus and Yélo interchanges), explicitly complementary to existing relay points and to candidate micro-hubs. Siting criteria are ranked: PT proximity first, then non-cannibalisation of relays, then demand density.

**Locker performance (corpus benchmarks).** Out-of-home lockers offer 24/7 access and fewer failed deliveries; an installed unit can process on the order of 6,200 parcels/yr; PT-station lockers in the Valencia pilot saved ≈ 3,937 kg CO₂/yr each, with a per-parcel footprint of ~12 g CO₂ versus ~50 g for a van delivery.

**System-level impact.** When siting is coupled with upstream consolidation and cyclo-logistics (P3), the modelled OVO scenario yields ≈ **−40 % CO₂ over five years** (236 → 128 tCO₂e), **−44 % truck-kilometres**, and ~€5,505/yr in fuel savings on the studied perimeter. Crucially, lockers act as **demand anchors**: they pull B2C drops out of dispersed home-delivery rounds and into off-peak, consolidated provisioning, and they create the volume needed to justify micro-/nano-hub + cargo-bike distribution. Anchoring lockers to the Yélo network also materialises a **passenger–freight interface**, a recognised city-logistics topic.

## 5. Discussion

Siting is the decisive lever. PT-anchored, density-driven placement maximises utilisation and modal-shift potential, whereas locations that cannibalise relay points erode a revenue stream (~30 % of host-shop turnover, per local surveys) without net system gain. Barriers remain: a persistent home-delivery preference, insufficient network density (*maillage*), capital cost (≈ €1,000/yr installed; €3–30k per unit), accessibility for reduced-mobility users, and governance/land-pressure questions requiring public–private coordination.

For mid-sized "end-of-line" cities the central lesson is **integration**: with few national operators and a reliance on local subcontractors, a locker network delivers system-level benefits only when co-designed with consolidation (UCC/micro-hubs) and local cyclo-logistics — not as a stand-alone retail amenity. This reframes lockers from a convenience product into a structuring component of the local urban logistics scheme.

## 6. Conclusion and perspectives

The paper links locker **siting** to **system-level impact** in a real mid-sized case, bridging two professional freight diagnostics and three years of field experimentation. The contribution is twofold: a transferable, GIS-based multicriteria siting workflow, and evidence that PT-anchored siting plus consolidation reshapes — rather than merely supplements — the local scheme. Perspectives include a capacitated coverage/p-median optimisation model, post-deployment utilisation monitoring, a full-territory simulation, and formal integration into the CdA logistics roadmap and the *Schéma Directeur des Aires de Livraison*.

## References

*(Provisional. Corpus items are primary sources supplied for this study; items marked [verify] are well-known works to be confirmed against bibliographic databases before submission.)*

1. Interface Transport (2018). *Mission d'accompagnement à l'élaboration d'une politique de transport de marchandises sur le territoire de la CdA de La Rochelle — Base de connaissances marchandises.* [corpus]
2. Interface Transport (2024). *Étude sur les besoins en foncier logistique pour le territoire de la CdA de La Rochelle.* [corpus]
3. EIGSI (2021). *Projet I&E n°1 — Cargo-Vélo La Rochelle, rapport final.* [corpus]
4. EIGSI (2024). *Projet IE Groupe 49 — LOG_URB_ROCHELLE (lockers & micro-hubs), rapport final.* [corpus]
5. EIGSI (2025–2026). *Projet PIE 26-38 — VerDelivery, rapport final.* [corpus]
6. Iwan, S., Kijewska, K., Lemke, J. (2016). Analysis of parcel lockers' efficiency as the last mile delivery solution. *Transportation Research Procedia.* [verify]
7. Deutsch, Y., Golany, B. (2018). A parcel locker network as a solution to the logistics last-mile problem. *Int. J. of Production Research.* [verify]
8. Lachapelle, U., Burke, M., Brotherton, A., Leung, A. (2018). Parcel lockers and CDPs in a car-dominant city. *Journal of Transport Geography.* [verify]
9. Dablanc, L. (2007). Goods transport in large European cities. *Transportation Research Part A.* [verify]
10. Taniguchi, E., Thompson, R.G., Yamada, T. — modelling city logistics. [verify]
