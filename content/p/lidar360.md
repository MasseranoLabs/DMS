+++
title = "LiDAR360"
description = "Desktop software from GreenValley International for processing LiDAR point clouds and imagery into terrain, classification, and mapping outputs."
weight = 20

[extra]
summary = "LiDAR360 is GreenValley International's desktop platform for processing LiDAR point clouds and photogrammetric imagery into terrain and mapping products."
developer = "GreenValley International Inc (GVI)"
country = "United States"
license = "Proprietary"
open_source = false
price_model = "Subscription (annual or permanent), licensed per selected modules"
price_detail = "The GVI store lists LiDAR360 V9 with two options, an annual subscription and a permanent (perpetual) subscription. Each purchase provides one license for the selected modules; multiple licenses require separate purchases. Minor version updates are free; major version upgrades are free within one year of delivery, with fees afterward. Online purchasing is not supported for education or concurrent-use licenses (contact sales). The public listing price appears as a placeholder ($0)."
platforms = [
  "Desktop",
]
deployment = [
  "Desktop application",
  "Distributed computing across local or cloud clusters (Distributed Computing module)",
]
primary_outputs = [
  "Orthomosaic",
  "DSM",
  "DTM",
  "Point cloud",
  "3D mesh",
  "3D tiles",
  "Contours",
  "Index maps",
]
target_use_cases = [
  "Surveying & mapping",
  "Construction",
  "Mining & aggregates",
  "Inspection & infrastructure",
  "Environmental & forestry",
  "Research & education",
]
latest_version = "V9"
first_release_year = "2013"
official_url = "https://www.greenvalleyintl.com/LiDAR360"
key_features = [
  "Processing of massive point cloud datasets (more than 300 GB of point cloud data can be processed)",
  "Point cloud classification with multiple methods: ground, model key points, machine learning and deep learning models, plus custom trained models, covering over 32 features",
  "Terrain module producing DEM, DSM, DTM, CHM, contours and related products, plus REM, drainage and flood-area analysis",
  "Photo (photogrammetry) module creating RGB, infrared and multispectral orthophotos (DOM), with automatic target detection and GCP matching",
  "Spectrum module for spectral data with NDVI, NDWI and other indices (113 spectral indices cited)",
  "Forestry module for individual tree segmentation and attributes such as trunk volume, DBH, crown, curvature and biomass",
  "Mine module for earthwork/volume calculation, crest and toe extraction, section analysis, and tunnel modeling and deformation monitoring",
  "Vectorization module with 2D/3D semi-automatic extraction and drawing tools and SAM-based outline extraction",
  "Model Builder with 200+ functional modules supporting command-line and distributed operations for automated workflows",
  "Distributed Computing module for multi-task parallel scheduling across local or cloud clusters",
  "Preprocessing tools: trajectory adjustment, data registration, color adjustment, and reprojection between coordinate systems",
  "UAV LiDAR quality control / accuracy inspection with calibration and flight status reports",
  "Format support including LAS, E57, PLY and 3D Tiles, with export to 3D Tiles (and conversion to S3M/OSGB/OBJ)",
  "In-viewer measurement tools and change detection / multi-period analysis",
]
pros = [
  "Broad module set covering terrain, forestry, mining, 3D building, photogrammetry, spectral analysis and distributed computing",
  "Multiple point cloud classification approaches including machine learning and deep learning with support for custom trained models",
  "Model Builder and command-line operation enable batch and automated workflows",
  "Distributed Computing module allows parallel processing across multiple nodes",
  "Handles large datasets (docs cite processing of more than 300 GB of point cloud data)",
  "Supports common point cloud formats (LAS, E57, PLY, 3D Tiles) and 3D Tiles export",
]
cons = [
  "Proprietary commercial software, not open source",
  "Licensing is per selected module, and multiple licenses require separate purchases (per the GVI store)",
  "Major version upgrades are free only within one year of delivery, with fees afterward (per the GVI store)",
  "Public pricing is not transparently listed online (a placeholder $0 is shown, and education or concurrent-use licenses require contacting sales)",
]
typical_workflow = [
  "Import point cloud or imagery data (formats include LAS, E57, PLY, 3D Tiles)",
  "Preprocess: trajectory adjustment, data registration, color adjustment, and coordinate system reprojection",
  "Run photogrammetry in the Photo module with target detection and GCP matching to produce orthophotos (DOM)",
  "Classify the point cloud using ground, machine learning, deep learning or custom AI models",
  "Generate terrain products such as DEM, DSM, DTM, CHM and contours in the Terrain module",
  "Perform analysis: volume and earthwork, section analysis, change detection, forestry, mining, and spectral indices",
  "Automate and scale using Model Builder, command-line operations, and the Distributed Computing module",
]
sources = [
  "https://greenvalleyintl.com",
  "https://www.greenvalleyintl.com/LiDAR360",
  "https://www.greenvalleyintl.com/resource/lidar360/index.html",
]

[extra.features]
image_input = "yes"
multispectral = "yes"
thermal = "unknown"
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
mesh_3d = "unknown"
contours = "yes"
tiles_3d = "yes"
gaussian_splatting = "unknown"
cad_export = "yes"
desktop = "yes"
cloud = "unknown"
self_hosted = "unknown"
api = "yes"
gpu = "yes"
web_viewer = "unknown"
flight_planning = "unknown"
measurements = "unknown"
volume = "yes"
veg_indices = "yes"
change_detection = "yes"
classification = "yes"
annotations = "unknown"

[extra.feature_notes]
image_input = "Documented via the LiDAR360 photogrammetry (Photo) module: 3D reconstruction from overlapping nadir and oblique images."
multispectral = "Spectral analysis module with 113 spectral indices plus multispectral/hyperspectral ortho and SAM classification."
lidar = "Core purpose of the product; LiDAR point cloud processing."
gcp = "Control points used by the DEM accuracy analysis tool to verify elevation error; framed as accuracy checkpoints."
accuracy_report = "DEM accuracy analysis tool generates accuracy reports; also one-click individual tree and stand analysis reports."
coordinate_systems = "EPSG/UTM projection support, geoid models (EGM2008 etc.), datum and ellipsoidal/orthometric height conversion."
orthomosaic = "True orthoimage / DOM generation from point cloud plus imagery fusion."
dsm = "DEM/DSM generation with IDW/TIN/Spike-Free TIN interpolation."
dtm = "DTM/DEM produced from IPTD ground-point classification."
point_cloud = "Dense point cloud processing and image-derived dense point cloud generation."
contours = "Contour extraction from DEM/point cloud, exportable to DXF/SHP."
tiles_3d = "Exports 3D Tiles (tileset.json / 2dtin.json / 3dtin.json)."
cad_export = "DXF export confirmed; LandXML/DWG not stated."
desktop = "Windows 64-bit desktop application (Win 7/8/10/11, Server 2012+)."
api = "Command-line operations and Model Builder for scripted/batch automation; no REST API stated."
gpu = "NVIDIA GPU required (GTX 970+, 4GB); used for deep learning classification and rendering."
volume = "Stockpile, cut-and-fill, and closed-model volume calculation."
veg_indices = "NDVI included within the 113 built-in spectral indices (vegetation category)."
change_detection = "Multi-temporal dataset comparison and multi-temporal volume change detection."
classification = "Point cloud classification with 26 AI categories, deep learning, IPTD ground detection."
+++

LiDAR360, launched in 2013 by GreenValley International Inc (GVI), a company headquartered in Berkeley, California, is a desktop platform for processing point cloud data. It employs point cloud algorithms together with artificial intelligence and machine learning to process LiDAR and photogrammetric data. The software is organized into modules, and the GVI store lists a V9 release with Framework, Terrain, Forestry, Mine, 3D Building, Photo, Spectrum and Distributed Computing modules.

The platform covers preprocessing (trajectory adjustment, data registration, color adjustment and reprojection), point cloud classification (ground, machine learning, deep learning and custom trained models, covering over 32 features), and generation of terrain products such as DEM, DSM, DTM, CHM and contours. A Photo module performs photogrammetry with GCP matching and produces RGB, infrared and multispectral orthophotos (DOM), while the Spectrum module computes indices such as NDVI and NDWI. Additional modules address forestry (individual tree segmentation and attributes), mining (earthwork, section and volume-change analysis, tunnel modeling), and vectorization.

For automation and scale, LiDAR360 provides a Model Builder that combines over 200 functional modules and supports command-line operation, along with a Distributed Computing module for parallel processing across local or cloud clusters. The documentation cites processing of more than 300 GB of point cloud data and format support including LAS, E57, PLY and 3D Tiles, with export to 3D Tiles. The software is sold as a proprietary product via the GVI store under annual or permanent subscription options, licensed per selected modules.
