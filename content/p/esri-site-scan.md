+++
title = "Esri Site Scan"
description = "Esri's cloud-based drone mapping software for flight planning, image processing, and analysis of drone imagery."
weight = 6

[extra]
summary = "Site Scan for ArcGIS is Esri's cloud-based drone mapping software covering flight planning, image processing, and analysis, producing orthomosaics, elevation models, point clouds, and 3D meshes that publish into the ArcGIS system."
developer = "Esri"
country = "USA"
license = "Proprietary"
open_source = false
price_model = "Quote-based"
price_detail = "No pricing is published on the product pages; Esri directs prospective users to contact sales."
platforms = [
  "Cloud (web browser)",
  "iOS (ArcGIS Flight app)",
]
deployment = [
  "Cloud (hosted by Esri)",
]
primary_outputs = [
  "Orthomosaic",
  "DSM",
  "DTM",
  "Point cloud",
  "3D mesh",
  "Gaussian splats",
  "Contours",
  "Index maps",
]
target_use_cases = [
  "Surveying & mapping",
  "Construction",
  "Inspection & infrastructure",
  "Environmental & forestry",
]
official_url = "https://www.esri.com/en-us/arcgis/products/site-scan-for-arcgis/overview"
key_features = [
  "Cloud-based processing of drone imagery into 2D and 3D products",
  "Automated drone flight planning via the ArcGIS Flight mobile app",
  "Drone fleet management with custom preflight checklists",
  "Outputs include orthomosaic, DSM, DTM, point cloud, and textured mesh, stored in the cloud",
  "Point clouds exported in .rcs, .las, and .laz formats",
  "In-viewer measurement of distances, surface areas, and volumetrics",
  "Cut/fill maps and volume calculations, including import of a LandXML surface",
  "Ground control point support with automatic GCP detection and checkpoint accuracy validation",
  "Support for thermal and multispectral sensors",
  "Temporal analysis and change detection over time",
  "Publishing of outputs to ArcGIS Online and ArcGIS Enterprise",
]
pros = [
  "Processing runs in the cloud, so no local workstation is required for image processing",
  "Outputs publish directly into ArcGIS Online and ArcGIS Enterprise for further GIS analysis",
  "Supports thermal and multispectral sensors in addition to standard mapping cameras",
  "Ground control point workflow with automatic detection and checkpoint-based accuracy validation",
  "Covers the full workflow from flight planning through processing and analysis",
]
cons = [
  "Pricing is not published; a sales inquiry is required to obtain cost information",
  "Processing is described only as cloud-based, with no self-hosted or offline processing option documented",
  "Deeper spectral analysis such as pixel querying and image classification is directed to ArcGIS Pro rather than performed in Site Scan itself",
]
typical_workflow = [
  "Plan and fly the mission using the ArcGIS Flight mobile app",
  "Upload captured drone imagery to Site Scan for cloud processing",
  "Generate 2D and 3D products (orthomosaic, DSM, DTM, point cloud, textured mesh, contours)",
  "Optionally apply ground control points and validate with checkpoints",
  "Measure distances, areas, and volumes and generate cut/fill maps",
  "Perform temporal analysis and change detection",
  "Publish results to ArcGIS Online or ArcGIS Enterprise",
]
sources = [
  "https://www.esri.com/en-us/arcgis/products/site-scan-for-arcgis/overview",
]

[extra.features]
image_input = "yes"
multispectral = "yes"
thermal = "yes"
lidar = "unknown"
video = "no"
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
desktop = "unknown"
cloud = "yes"
self_hosted = "unknown"
api = "unknown"
gpu = "unknown"
web_viewer = "yes"
flight_planning = "yes"
measurements = "yes"
volume = "yes"
veg_indices = "yes"
change_detection = "yes"
classification = "unknown"
annotations = "yes"

[extra.feature_notes]
image_input = "Standard nadir/area surveys; crosshatch combines oblique and nadir imagery."
multispectral = "FAQ: multispectral imagery can be processed (processed via the Legacy engine)."
thermal = "FAQ: thermal imagery can be processed; Reality Engine also generates thermal True Orthos."
rtk_ppk = "RTK drone support is documented (e.g. DJI Matrice 300 RTK, Freefly Astro); PPK not explicitly named."
accuracy_report = "Site Scan processing report conveys quality and accuracy of outputs; GCPs enable ~1 cm accuracy."
coordinate_systems = "Output settings let you set output horizontal coordinate system and vertical datum."
point_cloud = "Dense point cloud output in LAS and LAZ formats."
mesh_3d = "3D mesh outputs in SLPK (default) and OBJ; RCM/FBX via Autodesk ReCap engine."
gaussian_splatting = "Esri's own ArcGIS blog \\\"What's New in Site Scan for ArcGIS\\\" (Q2/May 2026, www.esri.com/arcgis-blog/products/site-scan/imagery/whats-new-in-site-scan-for-arcgis-q2-2026) states Site Scan \\\"now supports cloud-based generation of Gaussian splat layers... directly from drone imagery\\\" and instructs users to \\\"select Generate Gaussian Splat Layer under Processing Settings.\\\" A second Esri blog (how-to-crea"
cad_export = "Contours can be exported to DXF (Autodesk/AutoCAD format); DWG and LandXML not documented."
cloud = "Site Scan is a cloud-based SaaS; imagery is processed in Esri's cloud."
web_viewer = "Browser-based Site Scan Manager with 2D/3D viewers; publish/share to ArcGIS Online/Enterprise."
flight_planning = "ArcGIS Flight iPad app plans and controls autonomous 2D/3D drone missions."
measurements = "In-viewer distance, surface area, and volumetric measurements."
volume = "Volume tool estimates stockpiles/trenches with lowest-point, highest-point, and best-fit base planes."
veg_indices = "VARI (Visible Atmospherically Resistant Index) vegetation visualization layer from RGB imagery."
change_detection = "Temporal analysis, cut/fill maps, and measuring change over time."
annotations = "Site Scan Manager provides web-based measurement and annotation tools."
+++

Site Scan for ArcGIS is Esri's cloud-based drone mapping software that spans imagery data collection, processing, and analysis. Flight planning is performed through the ArcGIS Flight mobile application, and the platform includes drone fleet management with custom preflight checklists. Imagery is uploaded to Site Scan Manager, where it is processed in the cloud into 2D and 3D products.

Processing outputs include orthomosaics, Digital Surface Models (DSM), Digital Terrain Models (DTM), dense point clouds, and textured 3D meshes, which are stored in the cloud and can be published to ArcGIS Online and ArcGIS Enterprise. Point clouds are provided in .rcs, .las, and .laz formats, and contours can be generated and overlain on the orthomosaic. DSMs and other products can be opened in ArcGIS Pro and third-party CAD/GIS tools. The platform supports thermal sensors (for example DJI Zenmuse XT and XT2) and multispectral sensors (for example Parrot Sequoia+, MicaSense RedEdge, RedEdge-M, Altum, and DJI P4 Multispectral).

Analytic capabilities include in-viewer measurement of distances, surface areas, and volumetrics; cut/fill maps; and temporal analysis and change detection over time. Ground control points are supported, including automatic GCP detection, and accuracy can be validated with a checkpoint feature. Volume and cut/fill accuracy can be refined by importing a surface in LandXML format. Esri directs deeper spectral work such as querying individual pixel values and image classification to ArcGIS Pro after publishing or downloading the outputs.
