+++
title = "Pix4D"
description = "Pix4D: Swiss professional photogrammetry suite (Pix4Dmapper, Pix4Dmatic, Pix4Dcloud and more). Compare features, outputs and pricing for drone mapping."
weight = 2

[extra]
summary = "A Swiss photogrammetry and drone-mapping suite that turns RGB, multispectral, thermal and LiDAR captures into georeferenced 2D maps and 3D models across desktop, cloud and mobile products."
developer = "Pix4D"
country = "Switzerland"
license = "Proprietary"
open_source = false
price_model = "Subscription"
price_detail = "Subscription only (monthly, yearly or 3-year), with a 15-day free trial. Indicative starting prices: Pix4Dmapper from USD333/month, Pix4Dmatic from USD125/month, Pix4Dfields from USD111/month, Pix4Dreact from USD55/month. Pix4Dcloud is a credit-based add-on; Pix4Dcatch ships in hardware kit bundles."
platforms = ["Windows", "macOS", "iOS", "Web/Cloud"]
deployment = ["Desktop", "Cloud/SaaS", "Mobile", "On-premise"]
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
target_use_cases = ["Surveying & mapping", "Agriculture", "Construction", "Mining & aggregates", "Inspection & infrastructure", "Public safety & emergency response", "Environmental & forestry"]
latest_version = "Pix4Dmapper 4.10.1 (February 2026)"
first_release_year = "2011"
official_url = "https://pix4d.com"
key_features = [
  "End-to-end photogrammetry from any camera or drone, with nadir, oblique, fisheye and 360° imagery",
  "Multi-sensor input: RGB, multispectral, thermal, and LiDAR (import via Pix4Dsurvey, device LiDAR via Pix4Dcatch)",
  "Survey-grade accuracy with GCPs, RTK/PPK support, and a detailed quality and accuracy report",
  "Outputs including orthomosaic, DSM, DTM, point cloud, 3D textured mesh, contour lines and Cesium 3D tiles",
  "Machine-learning point-cloud classification and terrain modelling",
  "Agriculture toolset with vegetation indices, zonation and variable-rate prescription maps",
  "Cloud collaboration with measurements, volumes, annotations and 2D/3D change tracking over time",
  "Automation via the Pix4Dengine SDK and the Pix4Dcloud Enterprise API",
]
pros = [
  "Broad, mature product ecosystem across desktop, cloud, mobile and on-premise SDK",
  "Wide sensor support (RGB, thermal, multispectral, LiDAR) with survey-grade RTK/PPK and GCP accuracy",
  "Rich deliverables including 3D tiles, contours and CAD-ready vectorization",
  "Specialized apps tuned to specific industries such as agriculture, public safety and terrestrial scanning",
]
cons = [
  "Subscription only, with no perpetual licenses; premium desktop tiers are relatively costly",
  "Capabilities are split across multiple separately licensed products rather than one application",
  "Cloud processing is vendor-hosted; heavy on-premise automation uses the Pix4Dengine SDK",
  "Proprietary and closed-source",
]
typical_workflow = [
  "Capture imagery or scan data with a drone or Pix4Dcatch (optionally with a viDoc RTK rover) and add GCPs",
  "Import into Pix4Dmapper or Pix4Dmatic (or upload to Pix4Dcloud) and calibrate using RTK/PPK where available",
  "Process to generate orthomosaic, DSM/DTM, point cloud, 3D mesh, contours and 3D tiles, then review the quality report",
  "Classify the point cloud and, for agriculture, compute vegetation indices and prescription maps in Pix4Dfields",
  "Vectorize points and terrain into CAD/GIS deliverables in Pix4Dsurvey; take measurements and volumes",
  "Publish to Pix4Dcloud to share, annotate, measure and track change over time",
]
sources = ["https://pix4d.com", "https://en.wikipedia.org/wiki/Pix4D"]

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
image_input = "PIX4Dmapper documents capturing images with any camera/drone including terrestrial/oblique; PIX4Dcatch and PIX4Dmatic support aerial and terrestrial capture."
multispectral = "PIX4Dmapper processes multispectral images; PIX4Dfields is the dedicated multispectral agriculture product."
thermal = "PIX4Dmapper documents processing thermal images."
lidar = "PIX4Dmatic fuses LiDAR and photogrammetry point clouds; PIX4Dsurvey imports LAS/LAZ LiDAR."
video = "PIX4Dmapper documents using video frames for processing."
rtk_ppk = "RTK/PPK workflow documented for PIX4Dmatic (PPK corrections must be done in third-party software beforehand); PIX4Dcatch pairs with RTK devices."
coordinate_systems = "EPSG/coordinate system georeferencing and .prj outputs documented across PIX4Dmapper, PIX4Dmatic, PIX4Dsurvey."
dtm = "DTM generation documented in PIX4Dmatic and PIX4Dsurvey (not standalone in PIX4Dmapper, which produces DSM)."
contours = "Contour line generation documented in PIX4Dmatic and PIX4Dsurvey."
tiles_3d = "PIX4Dmatic exports Cesium 3D Tiles."
gaussian_splatting = "The Pix4D homepage (pix4d.com) carries a hero banner \\\"Gaussian splatting arrives in PIX4Dmatic\\\" linking to the vendor blog post at pix4d.com/blog/gaussian-splatting-pix4dmatic/. That blog page states PIX4Dmatic generates and processes Gaussian splats as part of its reconstruction workflow, that outputs \\\"including Gaussian splats, can easily be shared to PIX4Dcloud using the 'Share to Cloud' option"
cad_export = "PIX4Dsurvey and PIX4Dmatic export DXF, SHP, and LandXML for CAD/GIS integration."
cloud = "PIX4Dcloud is the hosted cloud processing product; PIX4Dengine Cloud API also offered."
self_hosted = "PIX4Dengine SDK runs on your own infrastructure (Linux/Windows), enterprise product."
api = "PIX4Dengine SDK (Python) and PIX4Dengine Cloud REST API for programmatic/automated processing."
gpu = "GPU-accelerated processing documented for PIX4Dmatic."
web_viewer = "PIX4Dcloud provides a browser-based viewer with shareable and embeddable URLs."
flight_planning = "PIX4Dcapture is the drone flight planning and image acquisition app."
veg_indices = "PIX4Dfields provides predefined vegetation indices (NDVI, NDRE, etc.); PIX4Dmapper generates index maps."
change_detection = "PIX4Dfields Comparison Tool enables multi-temporal analysis across projects; PIX4Dcloud offers timeline/progress tracking."
classification = "Automatic ground/non-ground point cloud classification in PIX4Dmatic, PIX4Dsurvey, and PIX4Dmapper."
annotations = "PIX4Dcloud supports synchronized 2D/3D annotations and markups."
+++

Pix4D is a photogrammetry and drone-mapping company founded in 2011 as a spinoff of EPFL's Computer Vision Lab, headquartered in Lausanne, Switzerland. Rather than a single application, it ships a modular product family covering the whole capture-to-deliverable pipeline.

The core products are Pix4Dmapper and Pix4Dmatic for photogrammetric processing, Pix4Dfields for agriculture, Pix4Dsurvey for CAD/GIS vectorization, Pix4Dcatch for LiDAR and photogrammetry mobile capture, Pix4Dcloud for cloud processing and collaboration, and Pix4Dreact for rapid emergency mapping, all backed by the Pix4Dengine processing SDK.

Across the family, Pix4D converts RGB, fisheye, thermal, multispectral and LiDAR data into orthomosaics, DSM/DTM, point clouds, 3D textured meshes, contours and 3D tiles, and serves surveying, agriculture, construction, mining, inspection, public safety and environmental markets. The current stable Pix4Dmapper release is version 4.10.1 (February 2026).
