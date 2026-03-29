import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import marching_cubes
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# =========================
# PARAMETRI
# =========================
N = 80              # risoluzione griglia
L = 14.0            # estensione spaziale [-L, L]
iso_fraction = 0.22 # isosuperficie come frazione del massimo
c1 = 1
c2 = 1

# colori fase
POS_COLOR = "#4C72B0"   # blu
NEG_COLOR = "#DD8452"   # arancione

# =========================
# GRIGLIA 3D
# =========================
x = np.linspace(-L, L, N)
y = np.linspace(-L, L, N)
z = np.linspace(-L, L, N)

dx = x[1] - x[0]
dy = y[1] - y[0]
dz = z[1] - z[0]

X, Y, Z = np.meshgrid(x, y, z, indexing="ij")

R = np.sqrt(X**2 + Y**2 + Z**2)
R_safe = np.where(R == 0, 1e-12, R)
cos_theta = Z / R_safe

# =========================
# ORBITALI IDROGENO (a0 = 1)
# =========================
phi_1s = (1 / np.sqrt(np.pi)) * np.exp(-R)

phi_2pz = (1 / (4 * np.sqrt(2 * np.pi))) * R * np.exp(-R / 2) * cos_theta

psi_mix = c1 * phi_1s + c2 * phi_2pz

# =========================
# FUNZIONE PER DISEGNARE UNA ISOSUPERFICIE POS/NEG
# =========================
def add_isosurface(ax, field, level, color, alpha=0.75):
    """
    Disegna la superficie field = level usando marching cubes.
    """
    verts, faces, normals, values = marching_cubes(
        field, level=level, spacing=(dx, dy, dz)
    )

    # marching_cubes usa coordinate a partire dall'indice 0:
    # trasliamo per tornare al sistema fisico [-L, L]
    verts[:, 0] += x[0]
    verts[:, 1] += y[0]
    verts[:, 2] += z[0]

    mesh = Poly3DCollection(verts[faces], alpha=alpha)
    mesh.set_facecolor(color)
    mesh.set_edgecolor("none")
    ax.add_collection3d(mesh)

def plot_orbital(ax, psi, title):
    """
    Mostra fase positiva e negativa con due superfici separate:
      psi = +iso   e   psi = -iso
    """
    max_abs = np.max(np.abs(psi))
    iso = iso_fraction * max_abs

    # parte positiva: psi = +iso
    if np.max(psi) > iso:
        add_isosurface(ax, psi, iso, POS_COLOR, alpha=0.78)

    # parte negativa: psi = -iso
    # Equivalentemente cerco isosuperficie di (-psi) = +iso
    if np.max(-psi) > iso:
        add_isosurface(ax, -psi, iso, NEG_COLOR, alpha=0.78)

    # assi
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_zlim(-6, 6)
    ax.set_box_aspect([1, 1, 1])

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title(title, pad=18)

    # vista
    ax.view_init(elev=18, azim=35)

    # pulizia grafica
    ax.grid(False)
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

# =========================
# FIGURA
# =========================
fig = plt.figure(figsize=(15, 5))

ax1 = fig.add_subplot(131, projection="3d")
plot_orbital(ax1, phi_1s, r"Orbitale $1s$")

ax2 = fig.add_subplot(132, projection="3d")
plot_orbital(ax2, phi_2pz, r"Orbitale $2p_z$")

ax3 = fig.add_subplot(133, projection="3d")
plot_orbital(ax3, psi_mix, rf"Sovrapposizione $\,\psi = {c1}\phi_{{1s}} + {c2}\phi_{{2p_z}}$")

plt.tight_layout()
plt.show()
