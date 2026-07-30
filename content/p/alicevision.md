+++
title = "AliceVision"
description = "Open-source photogrammetric computer vision framework, used via the node-based Meshroom desktop app for 3D reconstruction and camera tracking."
weight = 13

[extra]
summary = "Open-source photogrammetric computer vision framework (AliceVision) used through the node-based Meshroom desktop application for 3D reconstruction and camera tracking."
developer = "AliceVision"
license = "MPL-2.0"
open_source = true
price_model = "Free / open source"
price_detail = "Meshroom and AliceVision are distributed free of charge under MPLv2, with pre-compiled binaries and full source available."
platforms = [
  "Windows",
  "Linux",
  "macOS",
]
deployment = [
  "Desktop application",
  "Self-hosted distributed processing (render farm)",
]
primary_outputs = [
  "Point cloud",
  "3D mesh",
  "Gaussian splats",
]
target_use_cases = [
  "Surveying & mapping",
  "Film, VFX & games",
  "Research & education",
]
latest_version = "unknown"
first_release_year = "unknown"
official_url = "https://alicevision.org"
key_features = [
  "Structure from Motion (SfM) and Multi-View Stereo (MVS) 3D reconstruction from unordered photographs or videos",
  "Node-based visual programming framework in which each node is an operation whose outputs feed subsequent steps, with caching that invalidates only affected downstream nodes",
  "Point cloud, mesh, and textured model outputs plus recovered camera positions and scene geometry",
  "Camera tracking using natural features and CCTag markers",
  "HDR fusion from bracketed photography and panorama stitching (including fisheye)",
  "Photometric stereo and multi-view photometric stereo",
  "Local and distributed execution on render farms",
  "Extensible via custom nodes written in Python or by integrating external command-line tools; optional plugins add segmentation, monocular depth estimation, RoMa feature matching, 3D Gaussian Splatting, MicMac algorithms, and GPS/geolocation georeferencing",
]
pros = [
  "Free and open source under MPLv2 with published source code",
  "Cross-platform with pre-compiled binaries and buildable",
  "Produces dense point clouds and textured 3D meshes",
  "Automatable and extensible through a Python node API and command-line interface",
  "Supports distributed processing across render farms",
  "Includes additional capabilities beyond basic reconstruction: camera tracking, HDR fusion, and panorama stitching",
]
cons = [
  "Delivered as a node-based framework in which pipelines are built from interconnected nodes, rather than a one-click product",
  "Several capabilities (segmentation, depth estimation, Gaussian splatting, MicMac, geolocation) are provided only through separate add-on plugins rather than the core AliceVision plugin",
  "Georeferencing from GPS relies on the optional Geolocation plugin rather than the built-in AliceVision plugin",
]
typical_workflow = [
  "Import a set of overlapping photographs (or video frames) into Meshroom",
  "Run the AliceVision pipeline nodes for feature detection/matching and Structure from Motion to recover camera poses",
  "Compute depth maps via Multi-View Stereo and generate a dense point cloud",
  "Build and texture the 3D mesh",
  "Visualize results in the interactive 2D/3D viewers and export the models",
]
sources = [
  "https://alicevision.org",
  "https://github.com/alicevision/meshroom",
  "https://meshroom.org/index.php/sample-page/",
  "https://meshroom-manual.readthedocs.io/en/latest/",
]

[extra.features]
image_input = "yes"
multispectral = "unknown"
thermal = "unknown"
lidar = "unknown"
video = "yes"
gcp = "unknown"
rtk_ppk = "unknown"
accuracy_report = "unknown"
coordinate_systems = "unknown"
orthomosaic = "unknown"
dsm = "unknown"
dtm = "unknown"
point_cloud = "yes"
mesh_3d = "yes"
contours = "unknown"
tiles_3d = "unknown"
gaussian_splatting = "yes"
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
image_input = "AliceVision/Meshroom performs incremental Structure-from-Motion from multi-view, effectively unordered image collections; the official capturing guide instructs 'Try to take pictures from all angles', supporting arbitrary viewpoints."
video = "KeyframeSelection node extracts keyframes from video for reconstruction; supported formats include mp4, mov, mkv, avi, etc."
point_cloud = "Dense point cloud produced by DepthMap + Meshing (Output Dense Point Cloud, densePointCloud.abc) and exportable via ExportColoredPointCloud node."
mesh_3d = "Meshing node outputs mesh.obj; Texturing node creates UVs and textures (texturedMesh.obj/.mtl), i.e. a 3D textured mesh."
gaussian_splatting = "A bundled default plugin 'GSplat: 3D Gaussian Splatting reconstruction integrated with photogrammetry' (Meshroom develop/latest)."
desktop = "Meshroom is a free desktop application (GUI) with pre-built binaries per the official manual installation page."
api = "Documented Command Line Features (standalone AliceVision CLI executables) plus a Python node-based framework where users create custom nodes / integrate command-line tools."
gpu = "DepthMap node. 'This node requires CUDA', i.e. GPU (NVIDIA/CUDA) acceleration is required for dense reconstruction."
+++

AliceVision is a photogrammetric computer vision framework that provides 3D reconstruction and camera tracking algorithms, inferring scene geometry from unordered photographs or videos. It originated from collaboration between academic and industrial partners, including the CMP research team at CTU, Toulouse INP, INRIA, Mikros Image, and the IMAGINE team, in the context of projects such as the EU POPART and LADIO efforts. It is distributed under the Mozilla Public License v2.0 (with MIT covering libmv-derived components).

Meshroom is the open-source, node-based visual programming application built on AliceVision. Each node represents an operation whose outputs feed subsequent steps, and a caching system reuses intermediate results while invalidating only affected downstream nodes. Meshroom supports both local and distributed execution on render farms, and users can extend it by creating custom nodes in Python or integrating external command-line tools. Pre-compiled binaries are available and the software can also be built from source on Windows, Linux/Unix, and macOS.

Through the bundled AliceVision plugin, Meshroom offers pipelines for 3D reconstruction, camera tracking, HDR fusion, panorama stitching, and photometric stereo. Typical outputs include dense point clouds, meshes, textured models, and recovered camera positions. Additional optional plugins extend the toolset with AI segmentation, monocular depth estimation, RoMa dense feature matching, 3D Gaussian Splatting, MicMac photogrammetric algorithms, and GPS-based geolocation/georeferencing.
