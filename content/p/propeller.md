+++
title = "Propeller"
description = "Propeller is a cloud platform that processes drone imagery and LiDAR into survey-grade maps, 3D models, and earthwork measurements."
weight = 11

[extra]
summary = "Propeller is a cloud-based drone survey processing and site-analytics platform for construction, mining, and aggregates, producing survey-grade maps and 3D models from drone imagery and LiDAR."
developer = "Propeller Aero"
country = "unknown"
license = "Proprietary"
open_source = false
price_model = "Subscription (paid); 14-day free trial"
price_detail = "No public pricing is published on the trusted sources. The site offers a 14-day free trial (no credit card required) and a request-a-demo path. AeroPoints ground control hardware is sold separately via the Propeller store."
platforms = [
  "Web browser (cloud)",
  "Mobile app",
]
deployment = [
  "Vendor cloud (hosted on Amazon Web Services)",
]
primary_outputs = [
  "Orthomosaic",
  "DTM",
  "Point cloud",
  "Contours",
]
target_use_cases = [
  "Surveying & mapping",
  "Construction",
  "Mining & aggregates",
]
latest_version = "unknown"
first_release_year = "unknown"
official_url = "https://www.propelleraero.com"
key_features = [
  "Cloud photogrammetry processing of geotagged drone imagery into orthomosaics, point clouds, DTM, and TIN surfaces",
  "LiDAR processing accepting raw DJI Zenmuse L1/L2 files or preprocessed data from other sensors, with PPK correction, strip alignment, and QA/QC",
  "Point cloud classification into Ground and Unclassified categories (preserves customer-assigned classes for preprocessed clouds)",
  "Ground control via AeroPoints and PPK workflow for survey-grade positioning (stated ~3 cm accuracy)",
  "In-viewer measurement toolbox: distance, elevation, elevation difference, surface area, and cross section",
  "Volume calculations for stockpiles and cut/fill with shrink/swell adjustment and automated reports",
  "Surface comparison between any two surveys or design surfaces, cut/fill heat maps, and timeline history",
  "QA/QC validation and PDF processing/accuracy reports",
  "Support for over 5,000 published coordinate reference systems plus custom uploads",
  "Read-only public API to pull terrain files into CAD and GIS platforms",
  "Exports including LAS, LAZ, DXF, GeoTIFF, PDF reports, contours, and 3D model (DXF)",
]
pros = [
  "Processing runs in the vendor cloud, so no local specialist hardware is required for the processing step",
  "Handles both photogrammetry and LiDAR inputs within one platform",
  "Published accuracy figures are stated (~3 cm for photogrammetry with PPK and AeroPoints; ~5 to 6 cm horizontal for LiDAR)",
  "Built-in earthwork tooling: volumes, cut/fill, cross sections, and multi-survey comparison",
  "Broad coordinate reference system support (over 5,000 published systems) plus custom uploads",
  "Read-only public API and integrations with tools such as Trimble Connect, Procore, and Autodesk Build",
]
cons = [
  "Product is oriented toward construction, mining, aggregates, waste, transportation, and survey/engineering, not general-purpose mapping domains",
  "Processing is offered only as a vendor-hosted cloud service on AWS; the trusted sources describe no desktop or self-hosted/on-premise processing option",
  "LiDAR point cloud classification is limited to two categories, Ground and Unclassified, per the LiDAR processing page",
  "The public API is read-only",
  "No public pricing is disclosed",
]
typical_workflow = [
  "Fly the site with an RTK-enabled or Propeller PPK-compatible drone and place AeroPoints for ground control",
  "Drag and drop geotagged imagery, ground control points, and GNSS data into the cloud platform (or upload raw LiDAR files)",
  "Propeller georeferences and processes the data, builds the 3D model and orthophoto, and runs QA/QC",
  "Receive notification when outputs (orthomosaic, point cloud, DTM, TIN surfaces, contours) are ready",
  "Review the interactive 3D/2D map, take measurements, compute volumes, compare surveys, and export or share deliverables",
]
sources = [
  "https://www.propelleraero.com",
  "https://www.propelleraero.com/survey-processing/",
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
tiles_3d = "unknown"
gaussian_splatting = "unknown"
cad_export = "yes"
desktop = "unknown"
cloud = "yes"
self_hosted = "unknown"
api = "yes"
gpu = "unknown"
web_viewer = "yes"
flight_planning = "unknown"
measurements = "yes"
volume = "yes"
veg_indices = "unknown"
change_detection = "yes"
classification = "yes"
annotations = "yes"

[extra.feature_notes]
image_input = "Nadir/top-down 'nadir shots' as the standard survey flight imagery."
lidar = "Cloud LiDAR processing service; accepts DJI Zenmuse L1/L2 raw data or pre-processed classified LAS/LAZ from any sensor."
gcp = "Via Propeller AeroPoints smart GCPs and/or GCPs uploaded as CSV."
rtk_ppk = "Propeller PPK workflow using RTK/PPK-compatible drones plus AeroPoints."
accuracy_report = "QA/QC step in processing; PDF processing reports and Drone Data Accuracy documentation."
coordinate_systems = "5,000+ published coordinate reference systems, or upload your own / local calibration file."
dsm = "Exportable as GeoTIFF (unedited DEM/DSM)."
dtm = "DTM produced via terrain filtering; exportable as GeoTIFF."
mesh_3d = "'Hyper-realistic textured 3D models' from photogrammetry; exportable as DXF at selectable face counts."
contours = "Generated in-platform; exported as DXF, Shapefile, or PDF."
cad_export = "Exports DXF (and TTM surfaces); imports DXF/DWG/LandXML. Note: LandXML is import-only, not export."
cloud = "Propeller Platform is a cloud/managed processing service; processing is done for the user in the cloud."
api = "Public read-only API for querying sites/surveys and downloading data; a paid/premium feature."
web_viewer = "Browser-based cloud platform to view and share 2D maps and 3D models with stakeholders."
measurements = "In-viewer measurements of distances, volumes, heights, grades."
change_detection = "Timeline tool and Surface Comparison tool compare surveys over time / survey-to-design."
classification = "LiDAR point clouds classified into Ground/Unclassified; filtering of vegetation, structures, equipment."
annotations = "'Markup' feature for drawing, highlighting, text, and icons on the map."
+++

Propeller, made by Propeller Aero, is a cloud-based platform for processing and analyzing drone survey data, aimed at construction, mining, aggregates, waste management, transportation, and survey and engineering teams. Users upload geotagged drone imagery together with ground control points and GNSS data, and the platform performs georeferencing, 3D model creation, orthophoto generation, and QA/QC validation, then delivers the results with a notification when ready. Processing runs in the vendor cloud (hosted on Amazon Web Services), so no local specialist hardware is required for the processing step.

Photogrammetry outputs include orthomosaics (GeoTIFF), point clouds (LAS/LAZ), digital terrain models, TIN surfaces, and 3D worksite models. A separate LiDAR processing path accepts raw files from DJI Zenmuse L1 and L2 sensors, or preprocessed data from any sensor if it is registered and classified, handling PPK corrections, strip alignment, point classification (Ground and Unclassified), and QA/QC. LiDAR outputs include DTM, TIN surfaces, orthophotos, contours, and point clouds, with export formats of LAS, LAZ, DXF, GeoTIFF, and PDF processing reports. Stated accuracy figures are approximately 3 cm for photogrammetry with Propeller PPK-compatible drones plus AeroPoints, and roughly 5 to 6 cm horizontal for LiDAR.

The platform provides an interactive 3D and 2D map with a measurement toolbox (distance, elevation, elevation difference, surface area, and cross section), volume calculations for stockpiles and cut/fill with a shrink/swell calculator, and surface comparison between any two surveys or design surfaces for progress tracking and change detection. It supports over 5,000 published coordinate reference systems plus custom uploads, offers a read-only public API to pull terrain files into CAD and GIS tools, and integrates with third-party systems such as Trimble Connect, Procore, and Autodesk Build. A 14-day free trial is available; no public pricing is listed on the trusted sources.
