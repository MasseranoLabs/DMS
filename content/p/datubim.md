+++
title = "DatuBIM"
description = "Cloud-native SaaS photogrammetry and analytics platform that turns drone data into 3D maps and construction progress analytics."
weight = 22

[extra]
summary = "DatuBIM is Datumate's cloud-native SaaS photogrammetry and analytics platform that turns drone, ground-survey, and LiDAR data into survey-grade 3D maps and construction progress analytics for heavy civil infrastructure projects."
developer = "Datumate"
country = "Israel"
license = "Proprietary"
open_source = false
price_model = "Subscription / license-based (not publicly listed)"
price_detail = "Per the FAQ, pricing is based on the number of user licenses and images processed. No specific prices are published on the site."
platforms = [
  "Cloud (web-based SaaS)",
]
deployment = [
  "Vendor-hosted cloud (SaaS, with US and Europe/ROW instances)",
]
primary_outputs = [
  "Orthomosaic",
  "DSM",
  "DTM",
  "Point cloud",
  "3D mesh",
  "Contours",
]
target_use_cases = [
  "Construction",
  "Surveying & mapping",
  "Mining & aggregates",
]
latest_version = "unknown"
first_release_year = "unknown"
official_url = "https://www.datumate.com"
key_features = [
  "Cloud-native SaaS photogrammetry and construction-analytics platform",
  "Drone- and camera-agnostic; supports any drone with a 20 MP or higher camera and GPS",
  "Supports RTK and PPK images and Ground Control Points for georeferencing",
  "Outputs true orthophotos, DSM, DTM, dense point clouds, 3D texture mesh, and contours",
  "Distance, area, volume, and elevation measurements with cut/fill computation",
  "Volume grid/heatmap and cross-section volume reports",
  "Design vs. Pre-construction vs. As-built comparison and deviation detection over time",
  "API for custom integrations and broad file interoperability (DXF, DWG, DGN, LandXML, IFC, LAS, TIF, XML)",
  "Supports all published coordinate systems",
]
pros = [
  "Drone- and camera-agnostic and supports RTK/PPK imagery as well as Ground Control Points",
  "Produces a full set of photogrammetry outputs: orthophoto, DSM, DTM, point cloud, 3D mesh, and contours",
  "Includes construction analytics such as volumes, cut/fill, surface deviations, and design-vs-as-built progress tracking",
  "Broad file interoperability (DXF, DWG, DGN, LandXML, IFC, LAS, TIF) and an API for integrations",
  "Supports all published coordinate systems and multiple cloud regions (US and Europe/ROW)",
]
cons = [
  "Purpose-built for heavy civil infrastructure (roads, rail, bridges, earthworks). Is not for vertical construction",
  "Requires imagery from at least a 20 megapixel camera with GPS",
  "Pricing is not published; it is quote-based on user licenses and number of images processed",
  "Delivered as a vendor-hosted cloud SaaS (US and Europe/ROW instances); the trusted sources describe no desktop or on-premise deployment",
]
typical_workflow = [
  "Capture the site using drones, ground surveys, or LiDAR (RTK/PPK imagery and GCPs supported)",
  "Upload the data to the DatuBIM cloud platform",
  "Automated photogrammetric processing (Structure from Motion) generates georeferenced 3D outputs",
  "Review outputs: orthophoto, DSM, DTM, point cloud, 3D mesh, and contours",
  "Run analytics: measurements, volume/cut-fill, surface deviations, and design-vs-as-built comparison",
  "Generate automated reports and collaborate via annotations",
]
sources = [
  "https://www.datumate.com",
]

[extra.features]
image_input = "yes"
multispectral = "unknown"
thermal = "unknown"
lidar = "yes"
video = "unknown"
gcp = "unknown"
rtk_ppk = "yes"
accuracy_report = "unknown"
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
api = "unknown"
gpu = "unknown"
web_viewer = "yes"
flight_planning = "unknown"
measurements = "yes"
volume = "yes"
veg_indices = "unknown"
change_detection = "yes"
classification = "unknown"
annotations = "yes"

[extra.feature_notes]
image_input = "DatuBIM is a drone-mapping/photogrammetry product that produces true orthophotos, DSM and DTM from drone flights (top-down/nadir workflow); no explicit 'oblique' capture."
lidar = "A supported input/integration: 'Scan the site using drones, ground surveys, or LiDAR' plus laser-scanning integration; DatuBIM itself is a cloud analytics platform, not a LiDAR-only processor."
rtk_ppk = "FAQ: 'DatuBIM also supports RTK and PPK images.'"
coordinate_systems = "Supports all published coordinate systems plus user-defined/local systems, georeferenced outputs."
orthomosaic = "'True orthophotos' georeferenced to user coordinate systems."
dsm = "Digital Surface Model listed as output."
dtm = "Digital Terrain Model with automatic filtering of vegetation/buildings/machinery."
point_cloud = "'3D point clouds' / dense point cloud output."
mesh_3d = "'3D texture mesh models' listed as output."
contours = "Listed as DTM/DSM output ('2.5D elevation maps and contours')."
cad_export = "Explicitly DXF export ('you can export dxf formats and they will be geo-referenced'); DWG, DGN, LandXML and IFC are also cited as supported design/surface file formats."
cloud = "DatuBIM is a cloud-native SaaS; FAQ notes US and Europe/ROW cloud instances."
web_viewer = "Cloud-native SaaS accessed via browser (bim.datumate.com) where users view 3D models/maps, click model areas to see source images, take measurements, and add annotations in the platform; no standalone downloadable viewer implied."
measurements = "In-viewer distances, areas, volumes, elevations, cut/fill."
volume = "Excavation/stockpile volume analytics, volume grid and heatmap report, cross-section volume report."
change_detection = "Multi-temporal comparison ('compare digital twins..from different dates') and Deviation Detection."
annotations = "Georeferenced notes/annotations in the model viewer."
+++

DatuBIM is a cloud-native SaaS platform from Datumate for infrastructure construction data analytics. It is purpose-built for heavy civil work such as roads, rail, bridges, and earthworks, and explicitly not for vertical construction. Users scan a site with drones, ground surveys, or LiDAR, and the platform's photogrammetric engine (using Structure from Motion) converts imagery into georeferenced 3D models.

Standard mapping outputs include true orthophotos, digital surface models (DSM), digital terrain models (DTM), dense point clouds, 3D texture mesh models, and contours. On top of these, DatuBIM produces construction-analysis outputs including distance, area, volume, and elevation measurements, cut/fill computation, volume grid/heatmap and cross-section volume reports, and design vs. pre-construction vs. as-built comparisons with deviation detection over time.

The platform is drone- and camera-agnostic, supporting any drone with at least a 20 megapixel camera and GPS, and it accepts RTK and PPK images as well as Ground Control Points. It supports all published coordinate systems, offers an API for custom integrations, and interoperates with formats such as DXF, DWG, DGN, LandXML, IFC, LAS, TIF, and XML. It is offered as a hosted service with US and Europe/ROW cloud instances, and pricing is based on the number of user licenses and images processed.
