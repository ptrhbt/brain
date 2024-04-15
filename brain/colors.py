import numpy as np

# Download and prepare dataset from BrainNet repo
coords = np.loadtxt(
    np.DataSource().open(
        "https://raw.githubusercontent.com/mingruixia/BrainNet-Viewer/master/Data/SurfTemplate/BrainMesh_Ch2_smoothed.nv"
    ),
    skiprows=1,
    max_rows=53469,
)
x, y, z = coords.T

triangles = np.loadtxt(
    np.DataSource().open(
        "https://raw.githubusercontent.com/mingruixia/BrainNet-Viewer/master/Data/SurfTemplate/BrainMesh_Ch2_smoothed.nv"
    ),
    skiprows=53471,
    dtype=int,
)
triangles_zero_offset = triangles - 1
i, j, k = triangles_zero_offset.T

vertexcolor_1 = ["red" if entry > 40 else "yellow" for entry in z]
vertexcolor_2 = ["red" if entry > 40 else "yellow" for entry in x]
