+++
title = "DJI Terra"
description = "Windows photogrammetry and LiDAR software that turns DJI drone imagery into 2D orthomosaics, DSMs, point clouds, and 3D models."
weight = 7

[extra]
summary = "DJI Terra is DJI's Windows desktop software for processing drone imagery and LiDAR into 2D maps, point clouds, and 3D models."
developer = "DJI (SZ DJI Technology Co., Ltd.)"
country = "China"
license = "Proprietary"
open_source = false
price_model = "Paid (commercial license, free trial available)"
price_detail = "Sold as Standard and Flagship versions (and additional editions) through official DJI dealers. Standard, Flagship, and Education versions are perpetual; the Agriculture version is a 1-year (365-day) license. From v5.0.0 onward, no upgrade or maintenance fees are required and paid users can upgrade to v5.0.0 free of charge. A one-month free trial is offered, limited to reconstruction from no more than 500 photos and LiDAR reconstruction data of no more than 8 GB. License activation is tied to a single computer and cannot be transferred between devices."
platforms = [
  "Windows 10 or later (64-bit)",
]
deployment = [
  "Desktop application (Windows)",
  "On-premise cluster computation across networked worker devices with NAS",
]
primary_outputs = [
  "Orthomosaic",
  "DSM",
  "Point cloud",
  "3D mesh",
  "3D tiles",
  "Gaussian splats",
  "Index maps",
]
target_use_cases = [
  "Surveying & mapping",
  "Agriculture",
  "Inspection & infrastructure",
]
latest_version = "V5.3.0 (released 2026-07-23)"
first_release_year = "unknown"
official_url = "https://enterprise.dji.com/dji-terra"
key_features = [
  "2D reconstruction producing digital orthophoto maps (DOM) and digital surface models (DSM) in GeoTIFF format using UTM projection",
  "3D reconstruction producing LOD models (.osgb,.b3dm,.s3mb), textured meshes (.ply,.obj,.fbx,.i3s), and point clouds (.pnts,.las,.laz,.s3mb)",
  "LiDAR reconstruction from Zenmuse L1 and L2 data, output as.pnts,.las,.s3mb,.ply, and.pcd",
  "3D Gaussian Splatting reconstruction (v5.0.0 and later)",
  "2D multispectral reconstruction with calculated vegetation indices",
  "Support for Ground Control Points (GCPs) and aerotriangulation with reprojection-error and 3D-error reporting",
  "RTK/POS geotag support (e.g. Phantom 4 RTK)",
  "Cluster computation for large datasets across multiple networked devices",
  "Mission types including Mapping, Oblique, Corridor, Waypoints, and Detailed Inspection",
]
pros = [
  "Processes multiple input types: nadir, oblique, multispectral, and LiDAR data",
  "Exports a range of 2D, 3D, and LiDAR formats (GeoTIFF,.osgb,.b3dm,.obj,.fbx,.las,.laz,.ply,.pcd)",
  "Supports GCPs, RTK geotags, and aerotriangulation with an accuracy/quality report",
  "Cluster computation option for large datasets",
  "Standard, Flagship, and Education versions are perpetual, with no upgrade or maintenance fees from v5.0.0 onward",
]
cons = [
  "Runs only on Windows; not compatible with operating systems other than Windows, such as macOS",
  "Stated as not compatible with non-NVIDIA graphics cards, such as AMD",
  "License activation is limited to a single computer and cannot be transferred between devices",
  "Free trial is capped at 500 photos and 8 GB of LiDAR data",
]
typical_workflow = [
  "Plan and fly a capture mission (Mapping, Oblique, Corridor, Waypoints, or Detailed Inspection) with a supported DJI aircraft",
  "Import the captured visible-light, multispectral, or LiDAR data into DJI Terra on a Windows machine",
  "Run aerotriangulation, optionally adding Ground Control Points and using RTK/POS data for absolute orientation and accuracy",
  "Reconstruct 2D maps, 3D models, or LiDAR point clouds (optionally across a compute cluster)",
  "Export deliverables such as DOM/DSM GeoTIFFs, point clouds, textured meshes, LOD tiled models, or vegetation index maps",
]
sources = [
  "https://www.dji.com/dji-terra",
]

[extra.features]
image_input = "yes"
multispectral = "yes"
thermal = "yes"
lidar = "yes"
video = "yes"
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
gaussian_splatting = "yes"
cad_export = "yes"
desktop = "yes"
cloud = "unknown"
self_hosted = "unknown"
api = "unknown"
gpu = "yes"
web_viewer = "unknown"
flight_planning = "yes"
measurements = "yes"
volume = "yes"
veg_indices = "yes"
change_detection = "unknown"
classification = "yes"
annotations = "yes"

[extra.feature_notes]
multispectral = "2D multispectral reconstruction from DJI Mavic 3 Multispectral / Phantom 4 Multispectral data."
thermal = "Added in DJI Terra V5.3.0 (July 2026): Thermal Infrared 2D Reconstruction for temperature mapping/hotspot analysis (2D only)."
lidar = "Processes Zenmuse L-series (L1/L2/L3) LiDAR data into LAS point clouds."
video = "Added in DJI Terra V5.3.0 (July 2026): video frame extraction for visible-light 2D/3D reconstruction. Earlier versions explicitly did not accept video."
gcp = "Ground Control Points supported for photogrammetry reconstruction (one DJI FAQ notes GCPs are not used for LiDAR)."
accuracy_report = "Reconstruction quality / accuracy report output; LiDAR quality reports include flight-strip accuracy."
coordinate_systems = "Over 8500 built-in coordinate systems selectable by name or EPSG code, with seven-parameter transformation support."
dtm = "Bare-ground DEM generated via LiDAR ground-point classification (excludes buildings/vegetation)."
contours = "Contour lines generated from DEM/DSM (LiDAR point cloud missions); exportable as DXF."
tiles_3d = "Outputs LOD/tiled model formats: b3dm and pnts (Cesium 3D Tiles), i3s, osgb, s3mb."
gaussian_splatting = "The official DJI Terra product page (enterprise.dji.com/dji-terra, redirected from dji.com/dji-terra) explicitly states: \"DJI Terra is 3D modeling software equipped with next-generation reconstruction technologies, including 3D Gaussian Splatting,\" and features a \"Photorealistic Gaussian Splatting\" section. It also notes the capability arrived in version 5.0.0 and invites prior trial users to reap"
cad_export = "Exports DXF (contours, point grid); LandXML supported from V4.2 (GeoJSON also added)."
desktop = "Windows desktop application (Windows 10 64-bit or newer)."
gpu = "GPU-accelerated reconstruction; requires an NVIDIA GPU (system requirements)."
flight_planning = "Includes mission planning to capture data: Mapping, Oblique, Corridor, Waypoint, and Detailed Inspection missions."
measurements = "In-viewer distance (horizontal/straight/vertical/slope), area (projection/fitted), and volume measurements."
volume = "Cut/fill volume calculation using lowest-point or mean-plane base plane."
veg_indices = "Multispectral reconstruction generates vegetation index maps: NDVI, GNDVI, NDRE, LCI, OSAVI (plus reflectance maps)."
classification = "LiDAR point cloud ground-point classification (and other classes) for terrain/DEM."
annotations = "Annotation function in the reconstructed-model viewer (also used to extract geoid/coordinate info)."
+++

DJI Terra is a Windows desktop application from DJI for reconstructing drone-captured data into mapping and modeling outputs. It supports 2D reconstruction of nadir imagery into digital orthophoto maps (DOM) and digital surface models (DSM) in GeoTIFF/UTM format, 3D reconstruction of oblique imagery into textured meshes and level-of-detail (LOD) tiled models, LiDAR reconstruction from Zenmuse L1 and L2 sensors, and 2D multispectral reconstruction with calculated vegetation indices. Version 5.0.0 and later add 3D Gaussian Splatting reconstruction.

The software handles georeferencing through Ground Control Points (GCPs) and RTK/POS geotags, and its aerotriangulation workflow reports GCP reprojection errors, GCP 3D errors, and camera calibration information. Output formats include GeoTIFF for 2D maps; .osgb, .b3dm, and .s3mb for LOD models; .ply, .obj, .fbx, and .i3s for textured meshes; and .pnts, .las, .laz, .s3mb, .ply, and .pcd for point clouds. Missions supported include Mapping, Oblique, Corridor, Waypoints, and Detailed Inspection.

DJI Terra runs on Windows 10 or later (64-bit) and requires an NVIDIA GPU; it is not compatible with macOS or with non-NVIDIA graphics cards. It offers single-machine and cluster computation across networked worker devices. It is sold in multiple editions through DJI dealers, with Standard, Flagship, and Education versions being perpetual and the Agriculture version a 1-year license; a one-month free trial is limited to 500 photos and 8 GB of LiDAR data. The latest version listed is V5.3.0 (released 2026-07-23).
