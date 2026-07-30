+++
title = "DroneDeploy"
description = "Cloud drone-mapping and photogrammetry platform turning aerial imagery into orthomosaics, 3D models, elevation data, and site analytics."
weight = 4

[extra]
summary = "DroneDeploy is a cloud-based drone mapping and photogrammetry platform that processes aerial imagery into orthomosaics, 3D models, elevation models, and analytics for industrial and survey workflows."
developer = "DroneDeploy"
country = "United States"
license = "Proprietary"
open_source = false
price_model = "Subscription"
price_detail = "Tiered annual subscription plans (e.g., Flight & Analysis, Advanced Flight & Analysis, Ag Lite, and a custom-quoted Unified plan). A 14-day free trial is offered with no credit card required. Image upload limits apply per plan tier. Enterprise/custom quotes available."
platforms = [
  "Web browser",
  "iOS",
  "Android",
]
deployment = [
  "Cloud (vendor-hosted)",
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
  "Agriculture",
  "Mining & aggregates",
  "Inspection & infrastructure",
]
latest_version = "unknown"
first_release_year = "unknown"
official_url = "https://www.dronedeploy.com"
key_features = [
  "Automated flight planning and execution for drone image capture",
  "Cloud processing of aerial imagery into 2D orthomosaic maps",
  "3D textured models and point clouds viewable in-browser",
  "Digital Surface Models (DSM) and AI-generated Digital Terrain Models (DTM)",
  "Contour generation from DSM or DTM with multiple export formats",
  "Ground Control Point (GCP), RTK, and PPK workflows with automatic accuracy verification after each flight",
  "In-viewer distance, area, and volume (including cut/fill and stockpile) measurements",
  "Plant Health toolbox with vegetation indices (NDVI for multispectral/NIR, VARI for RGB)",
  "Multispectral and thermal imagery processing",
  "Upload of preprocessed LiDAR point clouds (.las)",
  "On-demand point cloud classification",
  "Change/temporal analysis by comparing data sets over time (Progress AI, Earthworks)",
  "Export API and open API for programmatic data access",
  "Exports in formats including GeoTIFF, LAS, XYZ, OBJ, DXF, SHP, and RCP",
]
pros = [
  "Broad output set from a single cloud workflow: orthomosaics, DSM, DTM, point clouds, 3D models, and contours",
  "Documented ground control support (GCP, RTK, PPK) with automatic post-flight accuracy verification",
  "Multiple export formats (GeoTIFF, LAS, XYZ, OBJ, DXF, SHP, RCP) plus an Export API",
  "Handles multispectral and thermal imagery and can ingest preprocessed LiDAR .las files",
  "In-viewer measurement and analysis tools (distance, area, volume, cross sections, classification)",
]
cons = [
  "Some capabilities are gated by plan or add-on (e.g., RCP export limited to Enterprise; advanced plant-health indices via Precision Ag Package)",
  "NDVI requires a multispectral or NIR-capable camera; RGB imagery is limited to the VARI index",
  "Point clouds are not classified by default; classification is generated on demand",
  "LiDAR support is documented as uploading preprocessed .las point clouds (under 5GB), not native LiDAR data reduction",
]
typical_workflow = [
  "Plan and fly an automated drone mission (or capture with supported hardware), optionally placing GCPs and using RTK/PPK",
  "Upload imagery to DroneDeploy's cloud for processing",
  "Platform generates orthomosaic, DSM/DTM, point cloud, and 3D model outputs, with accuracy verified automatically",
  "Review, annotate, and measure (distance, area, volume, cross sections) in the 2D/3D web viewer",
  "Run analyses such as vegetation indices, point cloud classification, and change/progress comparison over time",
  "Export deliverables in formats such as GeoTIFF, LAS, XYZ, OBJ, DXF, SHP, or RCP, or retrieve them via the Export API",
]
sources = [
  "https://www.dronedeploy.com",
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
desktop = "unknown"
cloud = "yes"
self_hosted = "unknown"
api = "yes"
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
image_input = "Captured via Enhanced 3D / Perimeter 3D / Crosshatch flight modes producing oblique (angled ~65 degrees) imagery."
multispectral = "Processes multispectral imagery (e.g. MicaSense/Sentera, BGRRE-NIR bands); requires a multispectral camera."
lidar = "Supports uploading/importing preprocessed LiDAR point clouds (.las, up to 5GB) and offers photogrammetry+LiDAR processing; RCP export is Enterprise-only."
gcp = "Ground Control Points and independent checkpoints supported."
rtk_ppk = "Both RTK and PPK correction workflows are documented."
accuracy_report = "Processing Report / Accuracy Report with GCP and checkpoint RMSE and per-checkpoint location error."
coordinate_systems = "Supports EPSG projections including WGS84 (4326), Web Mercator (3857), and custom State Plane / UTM."
dtm = "DTM (Digital Terrain Model) available as a layer and as a source for DTM contours."
point_cloud = "Dense point cloud exports in LAS/XYZ (Individual and Enterprise) and RCP (Enterprise only)."
mesh_3d = "3D textured mesh exported as OBJ with MTL material and JPG textures."
gaussian_splatting = "DroneDeploy's own help center article \\\"Gaussian Splats\\\" (help.dronedeploy.com/hc/en-us/articles/36102714208023-Gaussian-Splats) explicitly states: \\\"Splats provide a photorealistic 3D viewing mode, powered by Gaussian Splatting, that makes sites look smooth, clear, and easy to understand during reviews,\\\" and describes first-person W/A/S/D navigation controls for reviewing sites. DroneDeploy's Insid"
cad_export = "Contours exportable as DXF (and SHP) for AutoCAD / Civil 3D; LandXML export not confirmed on vendor pages."
cloud = "Cloud-hosted processing; documented as running on AWS and Google Cloud."
api = "Open API available for automation/integration."
web_viewer = "Browser-based viewer for sharing 2D maps and 3D models."
flight_planning = "Automated drone flight/mission planning via DroneDeploy mobile and web apps."
veg_indices = "NDVI and other vegetation indices supported; require a multispectral/NIR-capable camera."
change_detection = "Side-by-side map layer comparison plus Automatic Map Alignment enabling change detection over time."
+++

DroneDeploy is a cloud-hosted platform for drone-based mapping and photogrammetry, made by DroneDeploy (which has entered a definitive agreement to be acquired by Procore). Users plan and fly automated drone missions and upload the captured imagery to DroneDeploy's cloud, which processes it into 2D orthomosaic maps, 3D models and point clouds, Digital Surface Models, and AI-generated Digital Terrain Models. Accuracy is verified automatically after every flight, and the platform documents Ground Control Point, RTK, and PPK workflows.

Beyond base processing, the platform provides in-viewer analysis: distance, area, and volume measurements (including cut/fill and stockpile volumes), cross sections, contour generation, annotations, and on-demand point cloud classification. It processes multispectral and thermal imagery and offers a Plant Health toolbox with vegetation indices such as NDVI (for multispectral/NIR captures) and VARI (for RGB). Preprocessed LiDAR point clouds can be uploaded in .las format, and data sets can be compared over time for change and progress tracking.

Data can be exported in formats including GeoTIFF, LAS, XYZ, OBJ, DXF, SHP, and RCP, and accessed programmatically through an Export API and open API. DroneDeploy markets to industries including construction, mining, oil and gas, renewable energy, agriculture, utilities, roofing, and property management. Pricing is subscription-based across tiered plans with a 14-day free trial, and some features are gated by plan or add-on package.
