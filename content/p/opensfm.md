+++
title = "OpenSfM"
description = "Open source Structure-from-Motion pipeline that reconstructs camera poses, dense point clouds, meshes, and georeferenced DSM and orthophoto maps from images."
weight = 15

[extra]
summary = "OpenSfM is a free, open source Structure-from-Motion library that reconstructs 3D scenes from image collections and produces dense point clouds, meshes, and georeferenced 2D maps (DSM, orthophoto)."
developer = "OpenSfM contributors"
license = "BSD-2-Clause"
open_source = true
price_model = "Free / open source"
price_detail = "Distributed free of charge under a BSD 2-Clause license. No pricing is stated."
platforms = [
  "Linux",
  "MacOS (Apple Silicon)",
  "Windows",
]
deployment = [
  "Desktop / CLI",
  "Self-hosted",
]
primary_outputs = [
  "Orthomosaic",
  "DSM",
  "Point cloud",
  "3D mesh",
]
target_use_cases = [
  "Surveying & mapping",
  "Research & education",
]
latest_version = "1.0"
first_release_year = "2014"
official_url = "https://github.com/OpenSfM/OpenSfM"
key_features = [
  "Structure-from-Motion pipeline (feature detection, GPU OpenCL matching, track building, incremental and direct aerotriangulation reconstruction) with Ceres-based bundle adjustment",
  "Feature detectors including SIFT, HAHOG, DSP-SIFT, AKAZE, SURF, and ORB, with pair selection by GPS, capture time, file order, or image similarity (BoW / VLAD)",
  "Camera models for perspective, Brown, fisheye (OpenCV and custom 62 / 624 parameters), spherical / equirectangular, and dual, with rolling-shutter correction and multi-camera rig support",
  "Georeferencing with GPS from EXIF or text file, ground control points and checkpoints in any CRS, and horizontal plus vertical coordinate systems via EPSG codes, compound EPSG, or PROJ strings",
  "Dense reconstruction via GPU PatchMatch (OpenCL), TSDF fusion, and a Surface Nets mesh, exported as PLY / LAS / LAZ point clouds and Potree-style octree tiles",
  "Direct TSDF-based Digital Surface Model and orthophoto rendering exported as GeoTIFF",
  "Exporters for COLMAP, Bundler, OpenMVS, PMVS, VisualSFM, PLY, LAS/LAZ, GeoJSON, and GeoTIFF",
  "Quality report (PDF) with SfM metrics and GPS/GCP/checkpoint error tables, plus a built-in JavaScript 3D viewer and a Potree-fed web point-cloud viewer",
]
pros = [
  "Free and open source under a permissive BSD 2-Clause license",
  "Covers the full pipeline from sparse SfM through dense point clouds, meshes, and georeferenced DSM and orthophoto outputs",
  "Runs on Linux, macOS (Apple Silicon), and Windows",
  "Scriptable Python library with C++ core and command-line pipeline commands",
  "GPU (OpenCL) acceleration for matching and dense depth estimation",
]
cons = [
  "Installation relies on conda lock files and a source build rather than a packaged desktop installer",
  "No vendor-hosted cloud processing service",
  "No DTM, contour, or CAD (DXF/DWG/LandXML) export",
]
typical_workflow = [
  "Prepare a dataset folder of images and (optionally) copy a workflow preset config.yaml (aerial, terrestrial, object)",
  "Feature detection and GPU matching with geometric verification, followed by track building",
  "Incremental or direct aerotriangulation reconstruction with Ceres bundle adjustment to recover camera poses and a sparse point cloud",
  "Georeference the reconstruction using GPS, ground control points, and the target coordinate system (EPSG / PROJ)",
  "Dense reconstruction (GPU PatchMatch, TSDF fusion, Surface Nets mesh) exporting dense point clouds and meshes",
  "Render georeferenced DSM and orthophoto GeoTIFFs, produce the PDF quality report, and export to other formats as needed",
]
sources = [
  "https://github.com/OpenSfM/OpenSfM",
  "https://opensfm.org/docs/",
]

[extra.features]
image_input = "yes"
multispectral = "unknown"
thermal = "unknown"
lidar = "unknown"
video = "unknown"
gcp = "yes"
rtk_ppk = "yes"
accuracy_report = "yes"
coordinate_systems = "yes"
orthomosaic = "yes"
dsm = "yes"
dtm = "unknown"
point_cloud = "yes"
mesh_3d = "yes"
contours = "unknown"
tiles_3d = "unknown"
gaussian_splatting = "unknown"
cad_export = "unknown"
desktop = "yes"
cloud = "unknown"
self_hosted = "unknown"
api = "yes"
gpu = "yes"
web_viewer = "yes"
flight_planning = "unknown"
measurements = "unknown"
volume = "unknown"
veg_indices = "unknown"
change_detection = "unknown"
classification = "unknown"
annotations = "unknown"

[extra.feature_notes]
rtk_ppk = "Accepts per-image GPS positions with accuracy values, supporting RTK/PPK-corrected coordinates."
gcp = "Ground control points and checkpoints (with per-point standard deviation) in any CRS, plus a control points annotation tool."
accuracy_report = "A PDF quality report with SfM metrics and GPS/GCP and checkpoint error tables."
coordinate_systems = "Horizontal plus vertical coordinate systems via EPSG codes, compound EPSG, or PROJ strings, with geoids fetched on demand from the PROJ CDN."
orthomosaic = "Direct TSDF-based orthophoto rendering exported as GeoTIFF."
dsm = "Direct TSDF-based Digital Surface Model rendering exported as GeoTIFF."
mesh_3d = "A Surface Nets (dual-contouring) mesh exported as PLY, with robust multi-view color baking; a texture-atlas workflow is not explicitly described."
api = "Python library with performance-critical C++ code, plus command-line pipeline commands."
gpu = "GPU acceleration via OpenCL for matching and multi-view depth estimation (PatchMatch)."
web_viewer = "Built-in JavaScript viewer for interactive 3D preview plus a web point-cloud viewer fed by Potree octree tiles."
+++

OpenSfM is an open source Structure-from-Motion (SfM) library written in Python with performance-critical code in C++. This repository continues the original OpenSfM project created at Mapillary, which is no longer in active development, and its 1.0 release focuses on the GIS and geospatial workflows of its largest users, OpenDroneMap and WebODM. It reconstructs camera poses and sparse 3D points from unordered image collections and extends the pipeline to dense point clouds, meshes, and georeferenced 2D maps. It runs on Linux, macOS (Apple Silicon), and Windows, and is distributed under a BSD 2-Clause license.

The pipeline performs feature detection (SIFT, HAHOG, DSP-SIFT, AKAZE, SURF, ORB), GPU (OpenCL) matching with geometric verification, track building, and incremental or direct aerotriangulation reconstruction, with Ceres-based bundle adjustment that switches to a stochastic solver for very large scenes. It supports multiple camera models (perspective, Brown, fisheye, spherical/equirectangular, and dual) with rolling-shutter correction and multi-camera rigs. Georeferencing uses GPS positions from EXIF or a text file plus ground control points and checkpoints in any coordinate reference system, with horizontal and vertical systems defined by EPSG codes, compound EPSG, or PROJ strings.

Dense reconstruction uses GPU PatchMatch depth estimation, sparse-voxel-octree TSDF fusion, and a Surface Nets mesh, exporting dense clouds as PLY, LAS, or LAZ, meshes as PLY, and Potree-style octree tiles for streaming web viewers. Direct TSDF-based Digital Surface Model and orthophoto rendering are exported as GeoTIFF. OpenSfM can export to COLMAP, Bundler, OpenMVS, PMVS, VisualSFM, PLY, LAS/LAZ, GeoJSON, and GeoTIFF, produce a localized PDF quality report with SfM metrics and error tables, and provides a built-in JavaScript 3D viewer, a Potree-fed web point-cloud viewer, and a Rerun export. It is driven through pipeline commands and a Python API, and supports out-of-core submodel splitting and merging for large scenes.
