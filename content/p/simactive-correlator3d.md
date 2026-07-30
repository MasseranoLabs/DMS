+++
title = "SimActive Correlator3D"
description = "Windows photogrammetry software turning drone, aerial, and satellite imagery into orthomosaics, DSM/DTM, point clouds, and 3D models."
weight = 8

[extra]
summary = "SimActive Correlator3D is a Windows photogrammetry package that processes drone, aircraft, and satellite imagery (and LiDAR) into orthomosaics, elevation models, point clouds, and 3D models."
developer = "SimActive Inc."
country = "Canada"
license = "Proprietary"
open_source = false
price_model = "Commercial (subscription or perpetual license)"
price_detail = "Subscription listed at USD 295/month or USD 2,950/year. Perpetual licenses listed at USD 5,900 (standard) and USD 6,400 (floating/network), each including one year of support and updates. Tiers by image size: Standard (up to 61 MP), Medium Format (up to 100 MP), and Large Format & Satellite (unlimited resolution); higher tiers require contacting sales. A trial is offered."
platforms = [
  "Windows",
]
deployment = [
  "Desktop application (Windows)",
  "Distributed processing across networked PCs",
  "Self-managed cloud VMs (AWS, Microsoft Azure)",
]
primary_outputs = [
  "Orthomosaic",
  "DSM",
  "DTM",
  "Point cloud",
  "3D mesh",
  "3D tiles",
  "Gaussian splats",
  "Contours",
  "Index maps",
]
target_use_cases = [
  "Surveying & mapping",
  "Construction",
  "Agriculture",
  "Mining & aggregates",
  "Environmental & forestry",
  "Public safety & emergency response",
  "Inspection & infrastructure",
]
latest_version = "11.1"
first_release_year = "2003"
official_url = "https://www.simactive.com"
key_features = [
  "Aerial triangulation and bundle adjustment for aerial, drone, and satellite imagery",
  "Dense point cloud generation (GPU and multi-core CPU accelerated)",
  "Digital Surface Model (DSM) generation and automatic DTM extraction by filtering the DSM",
  "Orthomosaic and orthophoto generation, including a true ortho workflow",
  "3D model generation by meshing the DSM and texturing it with input imagery, output as tiled level-of-detail models",
  "Gaussian splat model generation",
  "GCP creation and management; import of ground control points in common formats",
  "RTK/PPK-assisted bundle adjustment in the AT module",
  "Survey-grade accuracy with detailed quality reports",
  "Volume calculation, 3D change detection, DEM contour extraction, and NDVI map creation",
  "LiDAR import, registration with imagery, colorization, and orthorectification using LiDAR-derived DEMs",
  "Distributed processing across networked PCs or cloud VMs; scripting and API for automation and batch (script/command-line) mode",
]
pros = [
  "Broad input support: drone, aircraft, and satellite imagery; consumer to large-format cameras; oblique and multi-camera setups; infrared, multispectral, and hyperspectral; plus LiDAR",
  "Wide output range covering orthomosaics, DSM, DTM, point clouds, textured 3D meshes, tiled models, contours, NDVI maps, and Gaussian splats",
  "GPU-accelerated processing that can be distributed across multiple networked PCs or self-managed cloud VMs",
  "Scripting and API with a script/command-line batch mode for workflow automation",
  "RTK/PPK-assisted aerial triangulation and GCP support with detailed accuracy/quality reports",
  "Flexible licensing with both subscription and perpetual (including floating/network) options",
]
cons = [
  "Proprietary commercial software; only a trial is offered beyond paid subscription or perpetual licenses",
  "Cloud processing is customer-managed (install on your own AWS or Azure GPU VM), with no vendor-hosted SaaS",
  "Only Windows system requirements; macOS and Linux are not mentioned",
  "Pricing for the Medium Format, Large Format, and Satellite tiers is not published and requires contacting sales",
  "Vendor materials include comparative speed and accuracy claims that are not independently verifiable from the site",
]
typical_workflow = [
  "Create a project and import imagery with geotags (RTK/PPK supported) and, optionally, ground control points",
  "Run aerial triangulation / bundle adjustment to align and orient the images",
  "Generate the DSM, then extract a DTM by automatic filtering of the DSM",
  "Produce a dense point cloud and colorize it from imagery (or import and register LiDAR)",
  "Orthorectify images and build the orthomosaic (including true ortho with a DSM)",
  "Generate 3D models by meshing and texturing, output as tiled level-of-detail models, or Gaussian splats",
  "Derive products such as contours, NDVI maps, volumes, and 3D change detection, and produce a quality/accuracy report",
]
sources = [
  "https://www.simactive.com",
]

[extra.features]
image_input = "yes"
multispectral = "yes"
thermal = "yes"
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
tiles_3d = "unknown"
gaussian_splatting = "yes"
cad_export = "yes"
desktop = "yes"
cloud = "yes"
self_hosted = "unknown"
api = "yes"
gpu = "yes"
web_viewer = "yes"
flight_planning = "unknown"
measurements = "yes"
volume = "yes"
veg_indices = "yes"
change_detection = "yes"
classification = "unknown"
annotations = "unknown"

[extra.feature_notes]
image_input = "'Multi-camera setups & obliques'. Adding oblique imagery to improve results."
thermal = "User Manual: reads radiometric thermal data from R-JPEG images and offers a Thermal mosaic export format."
lidar = "Imports LiDAR point clouds (LAS/LAZ) and automatically registers imagery with LiDAR; orthorectifies from LiDAR DEMs."
rtk_ppk = "AT module supports RTK/PPK Assisted bundle adjustment with corrected positions from EXIF or text file; v11.1 adds direct georeferencing."
coordinate_systems = "Supports selecting projection by EPSG code, custom projection, or Proj.4 definition; output projection specified."
mesh_3d = "3D model generation creates a mesh and applies texture from input images (photorealistic textured model)."
gaussian_splatting = "Correlator3D produces Gaussian splat models, with 'Gaussian Splat Generation' as a processing module and 'Splat Model Editing' among its editing tools; 'Gaussian Splat Models' is listed among output types."
cad_export = "Contours/vectors export to AutoCAD 2000 DXF (.dxf) and ESRI Shapefile (.shp)."
cloud = "Cloud processing is done by the user installing Correlator3D on their own GPU-enabled AWS/Azure Windows VM, not a vendor-hosted SaaS."
api = "Python API plus script mode / command line for automation."
web_viewer = "Generates a shareable online data viewer link via integrated Cesium (requires a Cesium subscription/account)."
measurements = "In-viewer Profile tool (elevation profile along a path) and Volume tool (measure cut/fill volume over a selection)."
veg_indices = "NDVI Map Creation tool."
change_detection = "3D Change Detection tool."
+++

Correlator3D is an end-to-end photogrammetry application from SimActive Inc., a Montreal, Canada company founded around 2003 by Philippe and Louis Simard. The software processes imagery from drone, aircraft, and satellite platforms and performs aerial triangulation to produce geospatial deliverables. Reported inputs span consumer cameras, medium and large format systems, pushbroom sensors, and infrared, multispectral, and hyperspectral imagery, along with oblique and multi-camera acquisitions.

Core outputs include dense point clouds, Digital Surface Models (DSM), Digital Terrain Models (DTM) extracted by filtering the DSM, orthomosaics (with a true ortho workflow), textured 3D models delivered as tiled level-of-detail meshes, Gaussian splat models, and vectorized 3D features. Additional analysis tools cover GCP creation, RTK/PPK-assisted bundle adjustment, volume calculation, 3D change detection, DEM contour extraction, and NDVI map creation. LiDAR data can be imported, registered with imagery, colorized, and used for orthorectification.

The product runs as a Windows desktop application and supports processing acceleration through GPU and multi-core CPUs. Processing can be distributed across networked PCs or across self-managed virtual machines on AWS or Microsoft Azure, and workflows can be automated through scripting, an API, and a script/command-line batch mode. Licensing is commercial, offered as monthly or yearly subscriptions and as standard or floating perpetual licenses, with image-size tiers (Standard up to 61 MP, Medium Format up to 100 MP, and Large Format & Satellite at unlimited resolution). The latest version referenced is 11.1 (2026).
