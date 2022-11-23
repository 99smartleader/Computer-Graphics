# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 20:01:28 2022

@author: 99smartleader/smartwolf99
"""

# Import NURBS-Python and the visualization component
from geomdl import BSpline
from geomdl import utilities
# from geomdl.visualization import VisPlotly as vis
from geomdl.visualization import VisMPL as vis
# Create a BSpline surface instance
surf = BSpline.Surface()
# Set evaluation delta
surf.delta = 0.05
# Set degrees
surf.degree_u = 3
surf.degree_v = 2
# Set control points
control_points = [[0, 0, 0], [0, 4, 0], [1, 8, 3],
                  [2, 0, 6], [2, 4, 0], [2, 8, 0],
                  [4, 0, 0], [4, 4, 0], [4, 8, 6],
                  [6, 0, 0], [6, 4, -3], [6, 8, 3]]
surf.set_ctrlpts(control_points, 4, 3)
# Auto generate knot vectors
surf.knotvector_u = utilities.generate_knot_vector(surf.degree_u, 4)
surf.knotvector_v = utilities.generate_knot_vector(surf.degree_v, 3)
# Evaluate surface
surf.evaluate()
# Visualization config
vis_config = vis.VisConfig(figure_size=[10.5,10])
# Visualization component
vis_comp = vis.VisSurface(vis_config)
# Set visualization component of the surface
surf.vis = vis_comp
# Render the surface
surf.render()
