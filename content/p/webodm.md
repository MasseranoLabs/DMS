+++
title = "WebODM"
description = "WebODM: free, open-source drone mapping software. Runs on your own machine or the hosted Lightning cloud. Compare features, outputs and pricing."
weight = 1

[extra]
summary = "Free and open-source drone mapping software that turns aerial imagery into georeferenced orthomosaics, elevation models, point clouds and 3D models, self-hosted or run on its hosted Lightning cloud."
developer = "WebODM"
license = "AGPL-3.0"
open_source = true
price_model = "Free / open source"
price_detail = "The desktop and self-hosted software is free to download and use under AGPL-3.0. WebODM Lightning is an optional paid cloud service for users who need more processing power."
platforms = ["Windows", "macOS", "Linux"]
deployment = ["Desktop", "Self-hosted server", "Cloud/SaaS"]
primary_outputs = [
  "Orthomosaic",
  "DSM",
  "DTM",
  "Point cloud",
  "3D mesh",
  "3D tiles",
  "Contours",
]
target_use_cases = ["Surveying & mapping", "Agriculture", "Construction", "Mining & aggregates"]
latest_version = "3.2.7"
first_release_year = "2016"
official_url = "https://webodm.org"
key_features = [
  "Orthomosaic, DSM and DTM generation from drone imagery",
  "Dense point clouds with filtering and classification (LAS/LAZ export)",
  "Textured 3D models in OBJ and OGC 3D Tiles formats",
  "Multispectral (reflectance) and thermal (LWIR temperature) image processing",
  "Vegetation index analysis including NDVI, VARI and GNDVI",
  "Elevation contour export to AutoCAD, ShapeFile and GeoPackage",
  "In-viewer volume, area and stockpile measurements",
  "Ground Control Point support and RTK-aware GPS handling",
  "REST API and Python SDK for workflow automation",
  "Self-hosted, offline-capable deployment with optional WebODM Lightning cloud processing",
]
pros = [
  "Completely free and open source (AGPL-3.0) with no per-seat licensing",
  "Runs fully offline and self-hosted, keeping data on your own hardware",
  "Broad input support including multispectral and thermal sensors, nadir and oblique imagery",
  "Comprehensive output set including OGC 3D Tiles, contours and classified point clouds",
  "REST API and Python SDK enable automation and integration",
]
cons = [
  "Local processing depends on your own hardware; the largest jobs can use the optional paid WebODM Lightning cloud",
  "Self-hosted deployment is Docker-based and runs on infrastructure you manage",
]
typical_workflow = [
  "Install WebODM on Windows, macOS or Linux, or use the hosted WebODM Lightning cloud",
  "Create a project and upload a set of nadir/oblique, multispectral or thermal aerial images",
  "Optionally add Ground Control Points and adjust processing options (DSM/DTM, classification, 3D Tiles, radiometric calibration)",
  "Run processing to generate the orthomosaic, elevation models, point cloud and 3D model",
  "Review in the browser: take volume and area measurements, analyse vegetation indices, and compare datasets over time",
  "Export deliverables (GeoTIFF, LAS/LAZ, OBJ, 3D Tiles, contours) or retrieve them via the REST API",
]
sources = ["https://webodm.org", "https://github.com/WebODM/WebODM", "https://docs.webodm.org"]

[extra.features]
image_input = "yes"
multispectral = "yes"
thermal = "yes"
lidar = "unknown"
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
gaussian_splatting = "unknown"
cad_export = "yes"
desktop = "yes"
cloud = "yes"
self_hosted = "yes"
api = "yes"
gpu = "yes"
web_viewer = "yes"
flight_planning = "no"
measurements = "yes"
volume = "yes"
veg_indices = "yes"
change_detection = "unknown"
classification = "yes"
annotations = "yes"

[extra.feature_notes]
image_input = "Webodm.org: 'Process aerial and ground images, captured nadir or oblique.'"
thermal = "Documented for the self-hosted app (docs.webodm.org) and the hosted WebODM Lightning edition ('Any type, RGB, multispectral, thermal')."
video = "Video input documented via WebODM Lightning 'Process Video Files' (docs.webodm.net) and docs.webodm.org media/options pages."
rtk_ppk = "'RTK/PPK/IMU support' documented on the hosted WebODM Lightning edition (webodm.net)."
accuracy_report = "'Quality Reports' on the hosted WebODM Lightning edition (webodm.net)."
coordinate_systems = "Results can be reprojected/exported to custom EPSG coordinate reference systems (docs.webodm.org; Lightning 'Export results to custom EPSGs')."
tiles_3d = "Webodm.org: textured 3D models in OGC 3D Tiles format."
cad_export = "Webodm.org: 'Preview and export elevation contours to AutoCAD, ShapeFile, GeoPackage' (AutoCAD/DXF)."
cloud = "Cloud/hosted processing is provided via WebODM Lightning (webodm.net / docs.webodm.net), the same team's hosted edition; the self-hosted app runs offline."
self_hosted = "Self-hostable server: the WebODM web application plus the NodeODM REST processing node run on your own server via Docker."
api = "Webodm.org: NodeODX REST API and PyODX Python SDK. API access with authentication."
gpu = "Webodm.org: 'Process datasets faster with CUDA.'"
web_viewer = "Web-based interface with data sharing and a Potree 3D viewer."
veg_indices = "Webodm.org: 'Easily compute NDVI, VARI, GNDVI and many other indexes.'"
classification = "Webodm.org: 'filtered and classified dense point clouds'; Lightning: 'Automatic point cloud filtering & classification.'"
annotations = "'2D and 3D measurements and annotations' documented on the hosted WebODM Lightning edition (webodm.net), which also offers an Annotations Report."
+++

WebODM is free and open-source drone mapping software that generates georeferenced maps, orthomosaics, point clouds, digital elevation models and textured 3D models from aerial imagery. Released under the AGPL-3.0 license, it runs entirely on your own computer or server, even offline, and is available for Windows, macOS and Linux.

It accepts JPG and TIFF imagery (8-bit and 16-bit) from many cameras, including fisheye and 360° lenses, in nadir or oblique orientations, and supports multispectral and thermal sensors through radiometric normalization and calibration. Outputs include orthophotos, DSMs and DTMs, filtered and classified point clouds (LAS/LAZ), elevation contours (AutoCAD, ShapeFile, GeoPackage) and 3D models in OBJ and OGC 3D Tiles formats.

Beyond processing, WebODM offers in-browser volume and area measurements, stockpile tracking, plant-health analysis with NDVI, VARI, GNDVI and other vegetation indices, Ground Control Point support, and a full REST API for automation. It can scale through parallel and distributed processing, and offers an optional paid hosted service, WebODM Lightning, for users who need additional processing power.
