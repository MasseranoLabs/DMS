+++
title = "GeoNadir"
description = "Cloud-based drone and satellite mapping platform for storing, processing, and analyzing nadir imagery, focused on environmental monitoring."
weight = 23

[extra]
summary = "GeoNadir is a cloud-based platform for storing, processing, and analyzing drone and satellite mapping data, aimed primarily at environmental monitoring workflows."
developer = "GeoNadir"
country = "Australia"
license = "Proprietary (freemium)"
open_source = false
price_model = "Freemium with subscription and custom tiers"
price_detail = "Essentials: free ($0/month), 100 GB storage, 500 images per dataset, 1 user, 1 project. Professional: $84/month USD, 1 TB storage, 3,000 images per dataset, up to 5 users, 25 projects, adds thermal orthomosaics, advanced analysis (volumes, heights, change detection), NDVI and spectral indices. Pro+: custom pricing with add-ons (additional users, storage, multispectral processing, GCP processing). Enterprise and Mining: custom pricing via consultation. (pricing page)"
platforms = [
  "Web browser (cloud)",
]
deployment = [
  "Vendor-hosted cloud (AWS)",
]
primary_outputs = [
  "Orthomosaic",
  "DSM",
  "DTM",
  "Index maps",
]
target_use_cases = [
  "Environmental & forestry",
  "Mining & aggregates",
  "Surveying & mapping",
  "Research & education",
]
latest_version = "unknown"
first_release_year = "unknown"
official_url = "https://geonadir.com"
key_features = [
  "Cloud processing of drone imagery into RGB, thermal, and multispectral orthomosaics",
  "Digital Surface Model (DSM) and Digital Terrain Model (DTM) generation",
  "Integration of Sentinel-2 satellite data alongside drone data",
  "Volume, height, area, and distance measurement tools",
  "Multi-temporal change detection",
  "NDVI and other spectral vegetation indices",
  "GCP processing (add-on)",
  "Drawing tools and AI-assisted (Magic wand) polygon creation",
  "Searchable, map-based data library with tagging",
  "Real-time collaboration, sharing, and commenting",
  "Export to GeoTIFF, CSV, and vector; TMS links and streaming to GIS applications",
  "Reporting via on-platform graphs, charts, vector and dataset statistics",
]
pros = [
  "Free Essentials tier with 100 GB storage and no credit card required",
  "Cloud-based, so no local software installation or high-end hardware is needed",
  "Supports RGB, thermal, and multispectral imagery plus Sentinel-2 satellite data",
  "Built-in analysis tools for volumes, heights, change detection, and vegetation indices",
  "Collaboration and sharing features comparable to shared documents",
  "Integrates with existing GIS tools via streaming, TMS links, and GeoTIFF/CSV/vector export",
]
cons = [
  "Explicitly does not produce 3D models (no textured mesh output)",
  "Focused on nadir imagery",
  "Cloud-only, requiring imagery upload rather than a desktop or on-premise option",
  "Free Essentials tier is capped at 500 images per dataset, one user, and one project",
  "Several capabilities (thermal, advanced analysis, multispectral, GCP processing) are gated behind Professional or Pro+ paid tiers",
]
typical_workflow = [
  "Drag and drop drone imagery (RGB, thermal, or multispectral) into the cloud platform",
  "Cloud processing generates orthomosaics and elevation models (DSM/DTM)",
  "Datasets are organized in a searchable, map-based library",
  "Users run analysis such as volume and height measurements, change detection, and spectral indices",
  "Teams collaborate, annotate, comment, and generate reports with graphs and statistics",
  "Results are shared, exported (GeoTIFF, CSV, vector), or streamed via TMS links to GIS applications",
]
sources = [
  "https://geonadir.com",
]

[extra.features]
image_input = "yes"
multispectral = "yes"
thermal = "yes"
lidar = "unknown"
video = "unknown"
gcp = "yes"
rtk_ppk = "yes"
accuracy_report = "unknown"
coordinate_systems = "unknown"
orthomosaic = "yes"
dsm = "yes"
dtm = "yes"
point_cloud = "unknown"
mesh_3d = "unknown"
contours = "unknown"
tiles_3d = "unknown"
gaussian_splatting = "unknown"
cad_export = "unknown"
desktop = "unknown"
cloud = "yes"
self_hosted = "unknown"
api = "unknown"
gpu = "unknown"
web_viewer = "yes"
flight_planning = "unknown"
measurements = "yes"
volume = "yes"
veg_indices = "yes"
change_detection = "yes"
classification = "unknown"
annotations = "yes"

[extra.feature_notes]
image_input = "Platform processes geotagged JPG drone mapping imagery into RGB orthomosaics; nadir top-down drone mapping is the core documented workflow."
multispectral = "Multispectral orthomosaic processing is a Pro+ add-on on the pricing/features page."
thermal = "Thermal orthomosaic processing from thermal drone imagery."
gcp = "GCP processing documented, including a built-in GCP Editor to input GCP coordinates and correct positional errors."
rtk_ppk = "GeoNadir supports all methods of relative and absolute accuracy for uploaded drone data, including importing RTK images and using the GCP Editor."
cloud = "Hosted cloud platform; data stored on AWS cloud servers and processed in the cloud."
web_viewer = "Browser-based platform to view and share projects; TMS link output and shareable projects for viewing/commenting."
measurements = "In-viewer tools to measure areas, calculate heights, terrain profiles and slope."
volume = "In-viewer measure volumes tool."
veg_indices = "Spectral indices (NDVI and more) documented."
change_detection = "Detect change and compare data from multiple dates over time."
annotations = "Drawing tools plus magic-wand AI polygons to draw on maps and share insights."
+++

GeoNadir is a cloud-native geospatial platform developed by the Australian company GeoNadir for storing, processing, and analyzing drone and satellite mapping data, with a stated focus on environmental teams and ecosystem monitoring. It processes uploaded drone imagery (RGB, thermal, and multispectral) into orthomosaics and digital elevation models (DSM and DTM), and incorporates Sentinel-2 satellite imagery alongside drone data. The product runs entirely in the cloud with no local software installation required.

The platform provides analysis tools including volume and height calculation, area and distance measurement, multi-temporal change detection, and NDVI and other spectral vegetation indices. It includes drawing tools, AI-assisted (Magic wand) polygon creation, a searchable map-based data library, and reporting through on-platform graphs, charts, and vector and dataset statistics. Collaboration features cover real-time team access, sharing, and commenting, and outputs can be exported as GeoTIFF, CSV, or vector data, or streamed to external GIS applications via TMS links.

GeoNadir is offered on a freemium model: a free Essentials tier (100 GB storage, 500 images per dataset, one user, one project), a Professional tier ($84/month USD) that adds thermal orthomosaics, advanced analysis, and spectral indices, a customizable Pro+ tier with add-ons such as multispectral and GCP processing, and custom Enterprise and Mining plans. The platform is focused on nadir imagery and does not provide 3D models, distinguishing it from photogrammetry tools that generate textured meshes.
