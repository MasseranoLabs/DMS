+++
title = "Metashape"
description = "Agisoft Metashape: standalone photogrammetry software (Standard and Professional). Compare features, outputs and pricing for drone mapping."
weight = 3

[extra]
summary = "Agisoft's standalone photogrammetry software that turns photos, satellite and LiDAR data into dense point clouds, DSMs/DTMs, orthomosaics, textured meshes and tiled 3D models."
developer = "Agisoft"
country = "Russia"
license = "Proprietary"
open_source = false
price_model = "Perpetual license"
price_detail = "Node-locked perpetual licenses: Standard USD179, Professional USD3,499. Educational and floating (network) licenses available; upgrades from PhotoScan are free. No mandatory subscription."
platforms = ["Windows", "macOS", "Linux"]
deployment = ["Desktop", "Cloud", "Network/cluster"]
primary_outputs = [
  "Orthomosaic",
  "DSM",
  "DTM",
  "Point cloud",
  "3D mesh",
  "3D tiles",
  "Contours",
]
target_use_cases = ["Surveying & mapping", "Cultural heritage & archaeology", "Film, VFX & games", "Environmental & forestry", "Agriculture", "Research & education"]
latest_version = "2.3.1"
first_release_year = "2010"
official_url = "https://www.agisoft.com/"
key_features = [
  "Photogrammetric triangulation for aerial (nadir/oblique), close-range and satellite imagery, with automatic camera calibration",
  "Dense point cloud generation, editing and automatic multi-class classification",
  "Georeferenced DSM/DTM generation with breakline and fill DEM editing, plus true and DTM-based orthomosaic",
  "3D model generation and photorealistic texturing (HDR, UDIM) and hierarchical tiled models for city-scale reconstruction",
  "LiDAR data support, multispectral and thermal processing, and user-defined vegetation indices (NDVI)",
  "GCP, check point, marker and scale-bar support with coded and non-coded target detection",
  "Distance, area and volume measurements, contour generation and a detailed processing report",
  "Network (cluster) and cloud processing, batch processing, and Python scripting with Java bindings",
]
pros = [
  "Perpetual license with no mandatory subscription, plus a low-cost Standard edition",
  "Broad input support: aerial, close-range, satellite, multispectral, thermal and LiDAR in one package",
  "Powerful automation via Python scripting and Java bindings, batch and distributed network processing",
  "Runs on Windows, macOS and Linux and produces GIS-compatible georeferenced outputs",
]
cons = [
  "Most survey and GIS capabilities are limited to the pricier Professional edition",
  "Professional edition perpetual license is costly (USD3,499)",
  "Cloud processing is an add-on interface rather than a full SaaS platform",
]
typical_workflow = [
  "Load photos and align them to build a sparse tie-point cloud via photogrammetric triangulation",
  "Import georeferencing from camera positions (including RTK/PPK accuracies) and/or GCPs, then optimize cameras",
  "Build a dense point cloud and, if needed, classify points into ground and other classes",
  "Generate derived products: DSM/DTM, 3D textured mesh or hierarchical tiled model, and orthomosaic",
  "Measure distances, areas and volumes, compute vegetation indices (NDVI) and generate contours",
  "Export georeferenced results (GeoTIFF, point clouds, meshes, DXF contours) and produce a processing report",
]
sources = ["https://www.agisoft.com/", "https://en.wikipedia.org/wiki/Metashape"]

[extra.features]
image_input = "yes"
multispectral = "yes"
thermal = "yes"
lidar = "yes"
video = "unknown"
gcp = "yes"
rtk_ppk = "unknown"
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
cloud = "yes"
self_hosted = "yes"
api = "yes"
gpu = "yes"
web_viewer = "yes"
flight_planning = "yes"
measurements = "yes"
volume = "yes"
veg_indices = "yes"
change_detection = "yes"
classification = "yes"
annotations = "yes"

[extra.feature_notes]
image_input = "Professional edition lists processing of aerial (nadir, oblique) imagery, confirming both."
multispectral = "Professional edition: RGB/NIR/thermal/multispectral imagery processing."
thermal = "Professional edition: part of 'RGB/NIR/thermal/multispectral imagery processing'."
lidar = "Professional edition: aerial LiDAR point attributes support and laser-scan registration."
gcp = "Professional edition: GCP import plus coded/non-coded target auto-detection."
accuracy_report = "Presentation states a detailed report is generated at end of processing, exportable as a PDF report."
coordinate_systems = "Professional edition: EPSG registry coordinate systems (WGS84, UTM, etc.) with configurable vertical datums."
orthomosaic = "Professional edition: georeferenced GeoTIFF orthomosaic generation."
dsm = "Professional edition: digital surface model generation."
dtm = "Professional edition: digital terrain model generation and DEM editing."
point_cloud = "Dense point cloud generation and editing."
mesh_3d = "3D model generation with photorealistic texturing."
contours = "Compare page and presentation: 'Elevation contour lines generation' (Professional edition)."
tiles_3d = "Professional edition: hierarchical tiled model generation with Cesium publishing."
cad_export = "Agisoft Cloud states export of data/measurements to GIS or CAD tools; desktop supports DXF export of contours/shapes."
cloud = "Agisoft Cloud is a separate hosted, pay-per-use processing/publishing service."
self_hosted = "Desktop app runs on-premise; network processing distributes calculations over your own local computer network."
api = "Professional edition: Python scripting and Java bindings, batch and network processing."
gpu = "Presentation lists 'GPU acceleration for faster processing'."
web_viewer = "Agisoft Cloud: visualize and share results online and embed published projects in web platforms."
flight_planning = "Presentation: 'Mission planning for complex sites' / mission planning algorithm within Metashape."
measurements = "Professional edition: inbuilt tools to measure distances, areas and volumes."
volume = "Professional edition: volume measurement; presentation shows volume and volume-change results."
veg_indices = "Professional edition: user-defined vegetation indices (e.g. NDVI) calculation and export."
change_detection = "Agisoft Cloud comparison tools to track site evolution; presentation notes volume-change and crop-growth tracking across multi-temporal UAS flights."
classification = "Professional edition: automatic multi-class dense point cloud classification."
annotations = "Agisoft Cloud hosted platform: conduct inspections and mark issues with type and severity."
+++

Agisoft Metashape (formerly PhotoScan) is a standalone photogrammetry suite developed by Agisoft LLC of St. Petersburg, Russia, first released in 2010 and renamed Metashape in 2019. It converts overlapping photographs, satellite imagery and LiDAR data into georeferenced 3D spatial products.

Outputs include dense point clouds, DSMs and DTMs, orthomosaics, textured 3D meshes and hierarchical tiled models for city-scale reconstruction. It is sold as perpetual node-locked or floating licenses in two editions: an entry-level Standard edition aimed at 3D content and interactive media, and a Professional edition that adds georeferencing control, point-cloud classification, LiDAR and multispectral/thermal processing, network and cloud processing, and Python/Java automation for GIS and survey-grade workflows.

Metashape runs on Windows, macOS and Linux, and is widely used well beyond drone mapping: in cultural heritage documentation, archaeology, film and visual effects, game development, and academic research, as well as for surveying, agriculture and environmental work.
