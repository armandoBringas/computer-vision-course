"""
From https://github.com/InsightSoftwareConsortium/SimpleITK-Notebooks/blob/master/Python/myshow.pyS
Credit to:
    Z. Yaniv, B. C. Lowekamp, H. J. Johnson, R. Beare, "SimpleITK Image-Analysis Notebooks: a Collaborative Environment for Education and Reproducible Research", J Digit Imaging., https://doi.org/10.1007/s10278-017-0037-8, 31(3): 290-303, 2018.
"""
import sys, os

download_script_location = os.path.abspath("Utilities")
if not download_script_location in sys.path:
    sys.path.append(download_script_location)