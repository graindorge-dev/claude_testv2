import json, math, warnings; warnings.filterwarnings("ignore")
import geopandas as gpd, pandas as pd, openpyxl, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
REPO="/home/user/claude_testv2"
def fnum(v):
    try: return float(v)
    except: return None

# --- population backdrop ---
pop=gpd.read_file("DATA/population.geojson").set_crs(4326,allow_override=True)
cands={c:pd.to_numeric(pop[c],errors="coerce").notna().sum() for c in ["pop_rp_2009","pop_rp_2007","pop_rp_1999"] if c in pop.columns}
popcol=max(cands,key=cands.get); pop[popcol]=pd.to_numeric(pop[popcol],errors="coerce")
vmin,vmax=pop[popcol].min(),pop[popcol].max(); norm=Normalize(vmin,vmax)

# --- collection points ---
wb=openpyxl.load_workbook("Donn#U00e9es points de collecte.xlsx",read_only=True,data_only=True); ws=wb.active
rows=list(ws.iter_rows(values_only=True))
hi=[i for i,r in enumerate(rows) if r and 'Latitude' in [str(c) for c in r]][0]
hdr=[str(c) for c in rows[hi]]; cp=[dict(zip(hdr,r)) for r in rows[hi+1:] if r and any(r)]
relay=[];lock=[]
for d in cp:
    la,lo=fnum(d.get("Latitude")),fnum(d.get("Longitude"))
    if la is None or lo is None or not(46.05<la<46.40 and -1.45<lo<-1.00): continue
    (lock if str(d.get("locker")).lower()=="yes" else relay).append((lo,la))
# --- bus ---
import openpyxl as _ox
_wbb=_ox.load_workbook("bus_stop.xlsx",read_only=True,data_only=True); _wsb=_wbb.active
_rb=list(_wsb.iter_rows(values_only=True)); _hb=[str(c) for c in _rb[0]]
bx,by=[],[]
for _r in _rb[1:]:
    if not _r: continue
    _d=dict(zip(_hb,_r)); la,lo=fnum(_d.get("stop_lat")),fnum(_d.get("stop_lon"))
    if la and lo and 46.05<la<46.40 and -1.45<lo<-1.00: bx.append(lo); by.append(la)
# --- parkings ---
wb2=openpyxl.load_workbook("DATA/Parkings.xlsx",read_only=True,data_only=True); ws2=wb2.active
r2=list(ws2.iter_rows(values_only=True)); h2=[str(c) for c in r2[0]]
def cat(h,t):
    s='surface' in (t or '')
    if s and (h or 0)>=300: return 'green'
    if s and (h or 0)<300: return 'yellow'
    return 'other'
P=[]
for r in r2[1:]:
    if not r or not r[0]: continue
    d=dict(zip(h2,r)); x,y=fnum(d.get('Xlong')),fnum(d.get('Ylat'))
    if x is None or y is None: continue
    P.append({'nom':d.get('nom'),'x':x,'y':y,'h':fnum(d.get('hauteur_max')),
              'places':fnum(d.get('nb_places')),'cat':cat(fnum(d.get('hauteur_max')),str(d.get('type_ouvrage') or ''))})
def sub(c): return [r for r in P if r['cat']==c]
def sz(r): return 16+(r['places'] or 50)/9.0

EXT=dict(xlim=(-1.20,-1.085),ylim=(46.137,46.193))
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(15,7.6),sharex=True,sharey=True)
for ax in (ax1,ax2):
    pop.plot(column=popcol,cmap="Greys",ax=ax,edgecolor="#b0b4ba",linewidth=0.4,alpha=0.45,norm=norm,zorder=1)
    ax.set_xlim(*EXT['xlim']); ax.set_ylim(*EXT['ylim'])
    ax.set_aspect(1/math.cos(math.radians(46.16))); ax.set_xlabel("Longitude")
ax1.set_ylabel("Latitude")

# Panel (a): lockers experiment
ax1.scatter(bx,by,s=4,c="#9aa0a6",alpha=0.55,marker=".",zorder=2)
ax1.scatter([p[0] for p in relay],[p[1] for p in relay],s=30,facecolor="#1a73e8",edgecolor="white",linewidth=0.5,zorder=4)
ax1.scatter([p[0] for p in lock],[p[1] for p in lock],s=150,marker="*",facecolor="#e8710a",edgecolor="black",linewidth=0.7,zorder=5)
ax1.set_title("(a) Experiment 1 — parcel-locker siting\n(collection network vs. demand & public transport)",fontsize=11,fontweight="bold")
leg1=[Line2D([],[],marker='.',color='w',markerfacecolor="#9aa0a6",markersize=9,label=f"Yélo bus stops (n={len(bx)})"),
      Line2D([],[],marker='o',color='w',markerfacecolor="#1a73e8",markeredgecolor='white',markersize=9,label=f"Relay points / agencies (n={len(relay)})"),
      Line2D([],[],marker='*',color='w',markerfacecolor="#e8710a",markeredgecolor='black',markersize=15,label=f"Existing automated lockers (n={len(lock)})")]
ax1.legend(handles=leg1,loc="lower left",fontsize=8.5,framealpha=0.93,title="Last-mile collection points")

# Panel (b): micro-hub foncier
for c,face,z in [('other','#c2c2c2',2),('yellow','#f4b400',3),('green','#2e7d32',4)]:
    S=sub(c); ax2.scatter([r['x'] for r in S],[r['y'] for r in S],s=[sz(r) for r in S],facecolor=face,edgecolor="white",linewidth=0.5,alpha=0.9,zorder=z)
enc=[r for r in P if 'ncan' in str(r['nom'])]
if enc: ax2.scatter([r['x'] for r in enc],[r['y'] for r in enc],s=250,marker="*",facecolor="#e8710a",edgecolor="black",linewidth=0.8,zorder=6)
ax2.set_title("(b) Experiment 2 — candidate land for micro-hubs\n(car parks by goods-vehicle compatibility)",fontsize=11,fontweight="bold")
leg2=[Line2D([],[],marker='o',color='w',markerfacecolor="#2e7d32",markeredgecolor='white',markersize=10,label=f"Surface ≥ 3 m — candidate (n={len(sub('green'))})"),
      Line2D([],[],marker='o',color='w',markerfacecolor="#f4b400",markeredgecolor='white',markersize=9,label=f"Surface < 3 m — conditional (n={len(sub('yellow'))})"),
      Line2D([],[],marker='o',color='w',markerfacecolor="#c2c2c2",markeredgecolor='white',markersize=8,label=f"Structured — excluded (n={len(sub('other'))})"),
      Line2D([],[],marker='*',color='w',markerfacecolor="#e8710a",markeredgecolor='black',markersize=15,label="Espace Encan — VerDelivery pilot")]
ax2.legend(handles=leg2,loc="upper left",fontsize=8.5,framealpha=0.93,title="Micro-hub foncier (size ∝ capacity)")

fig.suptitle("La Rochelle — two field experiments on the local urban logistics scheme (EIGSI, 2024–2026)",
             fontsize=13.5,fontweight="bold",y=0.99)
# shared population colorbar
sm=ScalarMappable(cmap="Greys",norm=norm); sm.set_array([])
cb=fig.colorbar(sm,ax=[ax1,ax2],orientation="vertical",fraction=0.025,pad=0.02,shrink=0.7)
cb.set_label(f"Population density by quartier — INSEE ({popcol[-4:]})",fontsize=9)
fig.text(0.5,0.005,"Sources : OpenStreetMap, INSEE (RP), réseau Yélo, relevés étudiants EIGSI (2024–2026)",ha="center",fontsize=7,color="#555")
fig.savefig(f"{REPO}/figures/png/larochelle_two_experiments.png",dpi=300,bbox_inches="tight")
fig.savefig(f"{REPO}/figures/svg/larochelle_two_experiments.svg",bbox_inches="tight")
print("saved two-panel | relays",len(relay),"lockers",len(lock),"bus",len(bx),"| parkings g/y/o",len(sub('green')),len(sub('yellow')),len(sub('other')))
