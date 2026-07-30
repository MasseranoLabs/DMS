+++
title = "Trimble Inpho"
description = "Desktop photogrammetry suite from Trimble that turns aerial frame imagery and lidar into point clouds, orthophotos, and 3D meshes."
weight = 10

[extra]
summary = "Trimble Inpho is a modular desktop photogrammetry software suite for processing aerial frame imagery (and lidar) into point clouds, orthophotos, and 3D meshes."
developer = "Trimble"
country = "United States"
license = "Proprietary"
open_source = false
price_model = "Commercial license"
price_detail = "Pricing is not published on the reviewed pages. The download page states the software runs in non-restricted mode with a valid license, and that a demo/no-license mode is only partially available and restricted regarding output."
platforms = [
  "Desktop",
]
deployment = [
  "Desktop",
]
primary_outputs = [
  "Orthomosaic",
  "Point cloud",
  "3D mesh",
]
target_use_cases = [
  "Surveying & mapping",
]
latest_version = "unknown"
first_release_year = "unknown"
official_url = "https://geospatial.trimble.com/en/products/software/trimble-inpho"
key_features = [
  "Aerial triangulation via the MATCH-AT module",
  "Point cloud generation via the MATCH-3DX and MATCH-T modules",
  "Orthophoto generation via OrthoMaster and OrthoVista (true orthophotos and classical orthophotos)",
  "Point cloud editing via DTMaster Stereo and SCOP++",
  "Full UAV/close-range workflow via the UASMaster module",
  "Supports single-camera or multi-camera aerial frame systems and low- or high-overlap imagery",
  "Combines image and lidar data",
  "Quality/accuracy evaluation with interactive automatic tools and a comprehensive project report file",
]
pros = [
  "Modular suite covering triangulation, point cloud generation, orthophoto production, and editing",
  "Handles single- and multi-camera aerial frame systems and both low- and high-overlap imagery",
  "Can combine image data with lidar data",
  "Includes quality/accuracy evaluation tools and a project report file",
  "Described as a long-standing photogrammetry product (stated as over 40 years)",
]
cons = [
  "Requires a valid commercial license; the no-license demo mode is restricted regarding output (per the download page)",
  "Pricing is not published on the reviewed pages",
  "Reviewed sources describe only desktop/office-based processing and do not document cloud, self-hosted, or API deployment",
  "The reviewed pages do not specify a supported operating system or version number",
]
typical_workflow = [
  "Import aerial frame imagery from single- or multi-camera systems",
  "Run aerial triangulation (MATCH-AT)",
  "Generate dense point clouds (MATCH-3DX / MATCH-T)",
  "Edit point clouds (DTMaster Stereo / SCOP++)",
  "Produce true or classical orthophotos (OrthoMaster / OrthoVista) and 3D textured meshes",
  "Evaluate accuracy and quality using the interactive tools and project report file",
]
sources = [
  "https://geospatial.trimble.com/en/products/software/trimble-inpho",
]

[extra.features]
image_input = "yes"
multispectral = "unknown"
thermal = "unknown"
lidar = "yes"
video = "unknown"
gcp = "yes"
rtk_ppk = "yes"
accuracy_report = "yes"
coordinate_systems = "yes"
orthomosaic = "yes"
dsm = "yes"
dtm = "yes"
point_cloud = "yes"
mesh_3d = "yes"
contours = "yes"
tiles_3d = "yes"
gaussian_splatting = "unknown"
cad_export = "yes"
desktop = "yes"
cloud = "unknown"
self_hosted = "unknown"
api = "unknown"
gpu = "unknown"
web_viewer = "unknown"
flight_planning = "unknown"
measurements = "yes"
volume = "yes"
veg_indices = "unknown"
change_detection = "yes"
classification = "yes"
annotations = "unknown"

[extra.feature_notes]
image_input = "Standard aerial-frame photogrammetry; product page cites 'any aerial frame digital imagery' and aerial/satellite image blocks."
lidar = "Supports importing, filtering, classifying and editing LiDAR/airborne laser-scanning point clouds and combining image + lidar data (SCOP++, DTMaster, 'LiDAR Box'); it does not capture LiDAR."
rtk_ppk = "Documented as GNSS/IMU direct georeferencing ('full GNSS and IMU support', UASMaster 'GPS support and high-quality direct-georeferencing', Applanix DG). Confirms GNSS/IMU camera positions rather than using the exact RTK/PPK wording."
accuracy_report = "'Comprehensive project report file' and QA/QC accuracy-evaluation tools; UASMaster quantitative and visual QC."
coordinate_systems = "Georeferencing via the Inpho Coordinate System database with geoid/datum support; coordinate system carried from Trimble Business Center."
orthomosaic = "True-orthophoto and classical orthophoto generation (OrthoMaster) and large orthomosaics (OrthoVista)."
mesh_3d = "Photorealistic textured 3D meshes via MATCH-3DX / MATCH-3DX Meshing add-on."
contours = "Contouring and contour output via DTMaster, SCOP++ and the Inpho DTM Extension."
tiles_3d = "MATCH-3DX mesh output made compatible with 3D Tiles 1.1 in Inpho version 15.0."
cad_export = "Stereo feature collection directly into AutoCAD/MicroStation/ArcGIS and extraction of CAD objects; DWG/DGN-oriented CAD/GIS output rather than a stated DXF/DWG/LandXML export list."
desktop = "Desktop workstation ('Office Software') suite of modules."
measurements = "Photogrammetric/stereo measurement extraction ('extraction of highly precise measurements'; measure/verify control and tie points; measure DTMs in DTMaster)."
volume = "Volume calculations listed as a DTM analysis capability (SCOP++ / DTM module)."
change_detection = "Stereo module (Summit Evolution) supports superimposing vectors for interactive mapping, change detection and GIS updates; not an automated multi-temporal analytics tool."
classification = "Automatic classification of raw point clouds into terrain vs off-terrain (LiDAR filtering) in SCOP++ / DTMaster."
+++

Trimble Inpho is a desktop photogrammetry software suite from Trimble for processing aerial imagery projects. The product page describes it as generating dense point clouds, true orthophotos, and 3D meshes, and states it has over 40 years of history as a photogrammetry solution. It supports any single-camera or multi-camera aerial frame system and handles low- or high-overlap imagery regardless of project size, and can combine image and lidar data.

The suite is organized into modules: MATCH-AT for aerial triangulation; MATCH-3DX and MATCH-T for point cloud generation; OrthoMaster and OrthoVista for orthophoto generation (true and classical orthophotos); DTMaster Stereo and SCOP++ for point cloud editing; and UASMaster for a full UAV and close-range workflow. Users can evaluate the accuracy of imagery and the quality of results using interactive, automatic tools together with a comprehensive project report file.

The related UASMaster module processes data from any UAS with frame-based cameras, using modern computer-vision image matching, flexible camera calibration, direct georeferencing (with Applanix DG), and quantitative and visual quality control, and produces photorealistic 3D meshes and dense point clouds. Stated target applications include city modeling, rural and topographic mapping, and digital twins. Pricing, operating-system requirements, and version details are not provided on the reviewed pages.
