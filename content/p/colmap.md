+++
title = "COLMAP"
description = "Open source Structure-from-Motion and Multi-View Stereo pipeline that builds sparse and dense 3D models from image sets."
weight = 15

[extra]
summary = "COLMAP is a free, open source (New BSD) Structure-from-Motion and Multi-View Stereo pipeline that reconstructs sparse and dense 3D models from image collections."
developer = "Johannes Schönberger and the COLMAP contributors"
license = "BSD-3-Clause"
open_source = true
price_model = "Free / open source"
price_detail = "Distributed free of charge under the New BSD license. No pricing is stated."
platforms = [
  "Windows",
  "macOS",
  "Linux",
]
deployment = [
  "Desktop",
]
primary_outputs = [
  "Point cloud",
  "3D mesh",
]
target_use_cases = [
  "Research & education",
]
latest_version = "unknown"
first_release_year = "unknown"
official_url = "https://colmap.github.io"
key_features = [
  "Incremental Structure-from-Motion to recover camera poses and sparse 3D structure from ordered or unordered image collections",
  "Multi-View Stereo dense reconstruction using PatchMatch stereo and stereo fusion",
  "Surface meshing via Poisson, Delaunay, and advancing front reconstruction, plus textured mesh generation with the mesh_texturer command",
  "Graphical user interface and command-line interface",
  "PyCOLMAP Python bindings exposing reconstruction pipelines and geometric estimators",
  "Multiple feature matching modes (exhaustive, sequential, vocabulary tree, spatial, transitive, custom)",
  "Multiple camera models and multi-camera rig support",
  "Optional GPU/CUDA acceleration for feature extraction and matching",
  "Geo-registration via GPS/EXIF pose priors and the model_aligner tool with RANSAC-based similarity transform",
]
pros = [
  "Free and open source under the permissive New BSD license",
  "Provides both a graphical interface and a command-line interface",
  "Runs on Windows, macOS, and Linux with pre-built binaries, Conda, and Docker options",
  "Scriptable and extensible through the PyCOLMAP Python bindings",
  "Supports both sparse (SfM) and dense (MVS) reconstruction including textured meshes",
  "Handles both ordered and unordered image collections",
]
cons = [
  "No orthophoto, DSM, DTM, or contour generation",
  "No hosted cloud processing",
  "Geospatial mapping outputs common to drone-survey tools are not part of the documented pipeline",
]
typical_workflow = [
  "Feature extraction: detect and describe sparse feature points in each image",
  "Feature matching: find correspondences using exhaustive, sequential, vocabulary tree, spatial, transitive, or custom modes",
  "Sparse reconstruction: incremental Structure-from-Motion to recover camera poses and a sparse 3D point cloud",
  "Dense reconstruction: image undistortion, depth/normal map computation via PatchMatch stereo, and fusion into a dense point cloud (fused.ply)",
  "Surface reconstruction: Poisson, Delaunay, or advancing front meshing, optionally textured with the mesh_texturer command",
  "Optional geo-registration using GPS/EXIF pose priors or the model_aligner tool",
]
sources = [
  "https://colmap.github.io",
  "https://github.com/colmap/colmap",
  "https://colmap.github.io/tutorial.html",
]

[extra.features]
image_input = "yes"
multispectral = "unknown"
thermal = "unknown"
lidar = "unknown"
video = "unknown"
gcp = "unknown"
rtk_ppk = "unknown"
accuracy_report = "unknown"
coordinate_systems = "yes"
orthomosaic = "unknown"
dsm = "unknown"
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
web_viewer = "unknown"
flight_planning = "unknown"
measurements = "unknown"
volume = "unknown"
veg_indices = "unknown"
change_detection = "unknown"
classification = "unknown"
annotations = "unknown"

[extra.feature_notes]
image_input = "SfM recovers structure from 'ordered or unordered image collections,' which per the special case confirms both nadir and oblique."
coordinate_systems = "Geo-registration via model_aligner using camera-center coordinates; supports GPS lat/lon/alt with conversion to ECEF or ENU frames. Not a full EPSG catalog reprojection tool."
point_cloud = "Dense point cloud produced by the MVS pipeline (PatchMatch stereo plus stereo fusion)."
mesh_3d = "Surface mesh via Poisson, Delaunay, or advancing-front reconstruction; textured mesh via the mesh_texturer command."
desktop = "Full-featured GUI for interactive reconstruction (plus CLI)."
api = "Scriptable command-line interface and Python bindings (pycolmap) exposing most functionality."
gpu = "CUDA/GPU acceleration for feature extraction and matching; CUDA-enabled Python wheels."
+++

COLMAP is a general-purpose Structure-from-Motion (SfM) and Multi-View Stereo (MVS) pipeline with graphical and command-line interfaces. It was originally created by Johannes Schönberger and is maintained by a group of contributors, and it is distributed as free and open source software under the New BSD license. It reconstructs 3D models from ordered or unordered image collections and runs on Windows, macOS, and Linux via pre-built binaries, Conda, Docker, or source builds.

The pipeline first performs feature extraction and matching, then incremental SfM to recover camera poses and a sparse 3D point cloud. A dense reconstruction stage undistorts images, computes depth and normal maps with PatchMatch stereo, and fuses them into a dense point cloud. Surface reconstruction is available through Poisson, Delaunay, and advancing front meshing, and the mesh_texturer command can produce a textured mesh with a texture atlas and per-face UV coordinates. Outputs include sparse model files (cameras, images, points3D, rigs, frames), dense point clouds (PLY), and meshes.

COLMAP can be automated through its command-line interface and the PyCOLMAP Python bindings, which expose reconstruction pipelines and geometric estimators, with CUDA-enabled wheels available. It supports optional GPU acceleration for feature extraction and matching, multiple camera models, and multi-camera rigs. Geo-registration is supported by extracting GPS/EXIF metadata as pose priors and by the model_aligner tool, which estimates a 3D similarity transformation with a RANSAC estimator and supports GPS, cartesian, ECEF, and ENU coordinate conversions.
