# Parcel Lockers and Pickup Points in Urban Logistics: Location Criteria and Delivery Scheme Design — A Case Study of La Rochelle, France

**Authors:** [Author names — EIGSI La Rochelle]  
**Conference:** 12th International Conference on City Logistics  
**Format:** Extended Abstract (3 pages)

---

## 1. Introduction

The rapid growth of e-commerce has transformed urban freight distribution, multiplying the number of delivery addresses while fragmenting load sizes. Home delivery failures — estimated between 10 and 30% of first attempts in dense urban areas — generate redundant trips, emissions, and road congestion. Parcel lockers and pickup points (PPPs) have emerged as a structural response: by consolidating deliveries at shared access points, they promise to reduce stops per tour, eliminate failed deliveries, and provide recipients with greater flexibility.

However, the mere installation of a locker does not guarantee urban logistics benefits. The net impact depends on the network design (density, size, location), the supply chain upstream of the device, and — critically — whether recipients access the point on foot, by bicycle, or by car. A locker that generates dedicated car trips may increase overall vehicle-kilometres despite reducing operator kilometres. The question of *where* to locate PPPs, and *how* to integrate them into a coherent delivery scheme, is therefore central.

This paper addresses two interrelated questions: (1) What are the criteria that determine the performance of parcel locker and pickup point locations? (2) How should a multi-tier delivery scheme integrating lockers, micro-hubs, and cargo cycles be designed for a medium-sized French city? We develop an answer grounded in the scientific literature and apply it to La Rochelle (Charente-Maritime, ~80,000 inhabitants), using territorial diagnoses conducted in 2018 and 2024.

---

## 2. State of the Art

### 2.1 Why Parcel Lockers Develop

The consolidation function of PPPs is well established. Morganti et al. (2014), studying French and German networks, showed that relay points and lockers developed as alternatives to home delivery to reduce uncertainty linked to recipient absence. Iwan, Kijewska and Lemke (2016), based on the Polish InPost network, demonstrated improvements in deposit density and last-kilometre productivity. Seghezzi, Siragusa and Mangiaracina (2022) modelled lower delivery costs compared to home delivery for urban contexts, driven by increased stop density and near-elimination of failed deliveries.

### 2.2 Location as a Network Problem

Location decisions cannot be treated site by site. Deutsch and Golany (2018) formalised the network design problem: the number of sites, their locations, and their sizes must be decided jointly. A mesh that is too sparse reduces user attractiveness; one that is too dense increases fixed costs and lowers fill rates. Zhou et al. (2024) extended this framework by distinguishing home-based users from commuters, showing that sites integrated into existing travel chains (public transport hubs, workplaces, supermarkets) generate significantly less additional car traffic than purely residential sites.

Castillo et al. (2024), applying routing-optimisation algorithms to Barcelona, demonstrated that micro-hub location and delivery routing cannot be treated separately: co-optimisation reduces total vehicle-kilometres and allows shared use of existing infrastructures such as parking lots.

### 2.3 User Behaviour and Accessibility

User acceptability depends on proximity, opening hours, security, parking availability, and accessibility from home or workplace (Kedia, Kusumastuti and Nicholson, 2017). Lockers transfer part of the logistics work to the consumer (Vakulenko, Hellström and Hjort, 2018). Mehmood et al. (2022), studying Nanjing, found that over 71% of locker sites were primarily accessible by car, with walking and cycling accessibility being much lower — underscoring the importance of modal analysis beyond simple distance buffers.

### 2.4 Conditional Environmental Benefit

The environmental balance of lockers is sensitive to assumptions. Schnieder, Hinde and West (2021) showed that comparisons with home delivery depend critically on recipient travel mode. Gutenschwager, Rabe and Chicaiza-Vaca (2024) emphasise the need to add operator tour emissions and recipient retrieval trips. Silva, Amaral and Fontes (2023), in a systematic review of 102 publications, confirm that lockers can reduce distances, fuel, and failed deliveries but flag dedicated car trips as a recurrent concern.

Recent empirical studies offer more optimistic results when the full scheme is integrated. Pinchasik, Hovi and Dong (2025) used real shipment data in the Greater Oslo area and found that broader locker network use can reduce costs, traffic, and operator emissions. Ghazal et al. (2025), modelling the Aachen city region, found that a combined scenario (electric vehicles + lockers + relay points) reduced costs by at least 5.4% and CO₂ by at least 61.1% compared to conventional delivery — a finding particularly relevant for medium-sized European cities similar to La Rochelle.

### 2.5 Micro-Hubs and Cargo Cycles

Katsela et al. (2022), analysing 17 micro-hub cases in Europe and North America, show that micro-hubs are not a single model but a family of transhipment interfaces. Their success depends on stakeholder organisation, business model, and local context. They enable delivery in dense zones via cargo cycles or electric light vehicles, but their economics require sufficient volume, suitable premises, and cross-operator cooperation.

---

## 3. Methodology and Case Study: La Rochelle

### 3.1 Territorial Context

La Rochelle (Charente-Maritime, France) is a mid-sized coastal city with a historic city centre, a significant tourism peak in summer, and a Community of Agglomeration (CdA) of approximately 200,000 inhabitants. The city has invested in cycling infrastructure and has a stated objective of reducing urban freight externalities.

### 3.2 Data Sources

This study synthesises two professional diagnostic studies produced by Interface Transport for the CdA:

- **2018 Freight Diagnosis**: Freight flow modelling (FRETURB), vehicle counts, e-commerce estimation, regulatory inventory, and modal distribution.
- **2024 Logistics Land Study**: Spatial needs assessment for logistics objects to 2040 horizon, identification of potential sites for urban distribution spaces (EUD), micro-hubs, and cycle-logistics hubs.

Two student project reports (EIGSI, 2021; 2024) on cargo cycles and the locker–micro-hub combination are used as exploratory illustrations. A multicriteria location grid and a GIS-based site pre-selection method complement these sources.

### 3.3 Key Data from the 2018 Diagnosis

The FRETURB model estimates **101,325 weekly B2B movements** across the CdA, of which **49,898 concern the municipality of La Rochelle** and **12,126 the city centre**. E-commerce generates an additional **25,300 weekly deliveries** across the CdA, with approximately **2,000 per week concentrated in the city centre**. Approximately **950 freight vehicles access the city centre daily**, covering an estimated **8,640 km/day** (780 vehicles under 3.5 t and 170 heavy vehicles). Two demand poles are identified: the dense *Centre Marché* sector and the collective housing zone of *Mireuil-Europe* (Interface Transport, 2018).

### 3.4 Key Insights from the 2024 Land Study

The 2024 study translates these flows into spatial needs. It proposes a hierarchical network of logistics objects: peripheral urban distribution platforms, urban distribution spaces (EUD) in the city core (150 m² to several thousand m²), and cycle-logistics hubs within 2 km of the city centre (150–800 m², ground floor, cycle access, battery charging). Priority sites for investigation include the *Quartier Gare/former SERNAM site*, the Exhibition Centre, and several underutilised industrial premises (Interface Transport, 2024).

---

## 4. Proposed Location Criteria and Delivery Scheme

### 4.1 A Multicriteria Location Framework

Drawing on the literature and territorial data, we propose nine weighted criteria for PPP site selection:

| Criterion | Weight |
|-----------|--------|
| B2C/B2B demand potential | 20% |
| Walking and cycling accessibility | 15% |
| Integration into existing travel chains | 15% |
| Operator supply access | 15% |
| Network complementarity (gap coverage) | 10% |
| Urban integration, safety, and accessibility | 10% |
| Technical feasibility | 5% |
| Land and economic feasibility | 5% |
| Territorial and social equity | 5% |

An eliminating pre-screen removes sites without accessible pedestrian routes, safe unloading, or adequate space. Final scoring combines site-specific field observation, GIS isochrone analysis (walking, cycling, public transport), and operator input.

### 4.2 Typology of Sites for La Rochelle

Five site types are proposed, each addressing different demand segments:

- **Mobility lockers** at the train station, bus hubs, and park-and-ride facilities — capturing existing commuter trips
- **Residential lockers** in dense collective housing zones (Mireuil-Europe) — reducing failed home deliveries
- **Commercial lockers** at supermarkets and markets — combining retail and parcel retrieval
- **Relay points** in proximity shops — handling oversized parcels, returns, and providing human service
- **Workplace lockers** at major employers and campuses — enabling retrieval during working hours

### 4.3 Integrated Delivery Scheme

The proposed scheme operates as a hierarchical chain (Figure 1):

1. Inbound flows are consolidated at a **peripheral urban platform** or carrier depot
2. City-bound goods are transferred to a **micro-hub or EUD** near the city centre (proposed site: Quartier Gare/SERNAM area)
3. The micro-hub sorts by channel (locker, relay, residual home delivery) and dispatches via **cargo cycles or electric light vehicles**
4. **Lockers and relay points** also function as collection points for returns, enabling reverse logistics on return trips

This scheme avoids the core failure mode identified in the literature — deploying lockers without upstream consolidation — which produces dedicated courier runs to individual lockers and negates density gains.

---

## 5. Conclusion

This paper shows that the impact of parcel lockers and pickup points on urban logistics depends less on the technology than on three design choices: *where* to place them (sites that capture existing travel, not generate new car trips), *how* to supply them (consolidated from a micro-hub, not by individual carrier vans), and *how to govern* them (shared infrastructure, interoperable systems, public monitoring). Applied to La Rochelle, the 2018 and 2024 territorial data provide a robust empirical base: flow concentrations in the city centre, potential sites identified through land analysis, and quantified targets (reducing ~8,640 km/day of freight vehicle travel in the city centre) frame a realistic pilot experiment.

The next step is a reversible pilot combining one micro-hub, two to three locker sites, and instrumented cargo-cycle tours, with evaluation metrics covering operator kilometres, user modal split, fill rates, and overall CO₂ balance. This would provide the evidence base for agglomeration-wide deployment.

---

## References

Castillo, C., Panadero, J., Alvarez-Palau, E. J., et al. (2024). Towards greener city logistics. *European Transport Research Review*, 16, 44.

Deutsch, Y., & Golany, B. (2018). A parcel locker network as a solution to the logistics last mile problem. *International Journal of Production Research*, 56(1–2), 251–261.

Ghazal, A., Narayanan, S., Adeniran, I. O., Kehrt, C., & Antoniou, C. (2025). Analysis of logistics measures of CEP service providers for the last-mile delivery in small- and medium-sized cities. *European Transport Research Review*, 17.

Gutenschwager, K., Rabe, M., & Chicaiza-Vaca, J. (2024). Comparing direct deliveries and automated parcel locker systems with respect to overall CO₂ emissions for the last mile. *Algorithms*, 17(1), 4.

Interface Transport. (2018). *Diagnostic marchandises — CdA de La Rochelle*.

Interface Transport. (2024). *Étude sur les besoins en foncier logistique — CdA de La Rochelle*.

Iwan, S., Kijewska, K., & Lemke, J. (2016). Analysis of parcel lockers' efficiency as the last mile delivery solution. *Transportation Research Procedia*, 12, 644–655.

Katsela, K., Güneş, Ş., Fried, T., Goodchild, A., & Browne, M. (2022). Defining urban freight microhubs. *Sustainability*, 14(1), 532.

Kedia, A., Kusumastuti, D., & Nicholson, A. (2017). Acceptability of collection and delivery points from consumers' perspective. *Case Studies on Transport Policy*, 5(4), 587–595.

Mehmood, M. S., Jin, A., Rehman, A., et al. (2022). Spatial variability and accessibility of collection and delivery points in Nanjing, China. *Computational Urban Science*, 2, 27.

Morganti, E., Seidel, S., Blanquart, C., Dablanc, L., & Lenz, B. (2014). The impact of e-commerce on final deliveries. *Transportation Research Procedia*, 4, 178–190.

Pinchasik, D. R., Hovi, I. B., & Dong, B. (2025). Replacing home deliveries by deliveries to parcel lockers. *International Journal of Logistics Research and Applications*, 28(4), 401–426.

Schnieder, M., Hinde, C., & West, A. (2021). Sensitivity analysis of emission models of parcel lockers vs. home delivery. *International Journal of Environmental Research and Public Health*, 18(12), 6325.

Seghezzi, A., Siragusa, C., & Mangiaracina, R. (2022). Parcel lockers vs. home delivery. *International Journal of Physical Distribution & Logistics Management*, 52(3), 213–237.

Silva, V., Amaral, A., & Fontes, T. (2023). Sustainable urban last-mile logistics: A systematic literature review. *Sustainability*, 15(3), 2285.

Vakulenko, Y., Hellström, D., & Hjort, K. (2018). What's in the parcel locker? *Journal of Business Research*, 88, 421–427.

Zhou, L., Li, C., Hu, C., & Du, J. (2024). Parcel locker location problem with selectable volume sizes. *Transportation Letters*, 16(9), 1140–1154.
