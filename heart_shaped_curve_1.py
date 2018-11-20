#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from geomdl import BSpline
from geomdl import utilities
from geomdl import exchange

from geomdl.visualization import VisMPL


# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a B-Spline curve instance
curve = BSpline.Curve()

# Set up the curve
curve.degree = 4
curve.ctrlpts = exchange.import_txt("heart_shaped_control_points_1.cpt")

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Set evaluation delta
curve.delta = 0.01

# Evaluate curve
curve.evaluate()

# Plot the control point polygon and the evaluated curve
vis_comp = VisMPL.VisCurve2D()
curve.vis = vis_comp
curve.render()


# Good to have something here to put a breakpoint
pass