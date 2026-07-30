+++
title = "Autel Mapper"
description = "Autel Robotics' 2D/3D reconstruction software that turns drone imagery into maps and 3D models, with local (Windows) or cloud processing."
weight = 19

[extra]
summary = "Autel Mapper is Autel Robotics' 2D and 3D reconstruction (photogrammetry) software that processes drone imagery into orthophotos, surface models, point clouds, and 3D models using local (Windows) or cloud processing."
developer = "Autel Robotics"
country = "China"
license = "Proprietary"
open_source = false
price_model = "Paid (commercial license)"
price_detail = "The official product page presents a \"Buy Now\" option and references a \"Limited Offer\" but does not display a price. No pricing figures are stated on the official source."
platforms = [
  "Windows 10 or later (64-bit)",
  "Cloud",
]
deployment = [
  "Desktop (local processing on Windows)",
  "Cloud processing",
]
primary_outputs = [
  "Orthomosaic",
  "DSM",
  "Point cloud",
  "3D mesh",
  "3D tiles",
]
target_use_cases = [
  "Surveying & mapping",
  "Public safety & emergency response",
  "Inspection & infrastructure",
]
latest_version = "unknown"
first_release_year = "unknown"
official_url = "https://www.autelrobotics.com/productdetail/autel-mapper/"
key_features = [
  "2D reconstruction producing orthophoto output (GeoTIFF). Meets a 1:500 mapping precision requirement without GCPs",
  "3D reconstruction with selectable quality (high, medium, low), outputting B3DM, OSGB, OBJ, and PLY",
  "Aerial triangulation supporting both rolling shutter and global shutter cameras, with block processing for large datasets (output XML)",
  "Real-time 2D stitching during flight from the remote controller's streamed images to produce orthophotos on site",
  "Quick Stitching mode outputting DOM, DSM, and 2.5D visualization, with on-the-fly and rapid processing methods",
  "Dense point cloud output in PNTS, LAS, and XYZ",
  "Rebuild optimization tools: KML import, model reconstruction processing, camera parameters, image POS data management, and Ground Control Point (GCP) management",
  "Local processing on Windows or cloud processing",
  "Stated capacity of up to 30,000 images per processing node",
]
pros = [
  "Outputs span 2D and 3D deliverables: orthophoto (GeoTIFF/DOM), DSM, dense point cloud (LAS/XYZ/PNTS), textured 3D models (OBJ/OSGB), and tiled 3D models (B3DM)",
  "Offers both local (Windows) and cloud processing",
  "Includes Ground Control Point management for georeferencing/accuracy",
  "Supports both rolling shutter and global shutter cameras in aerial triangulation",
  "Provides real-time 2D stitching during flight for on-site feedback",
  "Stated centimeter-level (1:500) mapping accuracy with compatible Autel hardware",
]
cons = [
  "Only Windows 10 or later (64-bit) as the operating system; no other OS is listed",
  "Recommended hardware is demanding (e.g. NVIDIA RTX 2080 Ti or higher, 32GB RAM or higher)",
  "No price is published on the official product page",
  "Some capabilities are tied to Autel drones and compatible hardware (e.g. accuracy figures cited for the EVO II Pro RTK V3)",
]
typical_workflow = [
  "Batch import images captured by Autel drones (KML import and image POS data are supported), or stream images from the remote controller during flight for real-time 2D stitching",
  "Run aerial triangulation, which supports rolling and global shutter cameras and uses block processing for large datasets",
  "Optionally manage Ground Control Points, camera parameters, and reconstruction settings via rebuild optimization",
  "Select processing (2D reconstruction, 3D reconstruction with high/medium/low quality, or Quick Stitching) and run locally on Windows or in the cloud",
  "Export deliverables: GeoTIFF orthophoto; DOM/DSM/2.5D from Quick Stitching; dense point clouds (LAS/XYZ/PNTS); and 3D models (B3DM/OSGB/OBJ/PLY)",
]
sources = [
  "https://www.autelrobotics.com",
  "https://www.autelrobotics.com/productdetail/autel-mapper/",
]

[extra.features]
image_input = "yes"
multispectral = "unknown"
thermal = "unknown"
lidar = "unknown"
video = "unknown"
gcp = "yes"
rtk_ppk = "yes"
accuracy_report = "unknown"
coordinate_systems = "unknown"
orthomosaic = "yes"
dsm = "yes"
dtm = "unknown"
point_cloud = "yes"
mesh_3d = "yes"
contours = "unknown"
tiles_3d = "yes"
gaussian_splatting = "unknown"
cad_export = "unknown"
desktop = "yes"
cloud = "yes"
self_hosted = "unknown"
api = "unknown"
gpu = "yes"
web_viewer = "unknown"
flight_planning = "unknown"
measurements = "unknown"
volume = "unknown"
veg_indices = "unknown"
change_detection = "unknown"
classification = "unknown"
annotations = "unknown"

[extra.feature_notes]
image_input = "Documented via 2D orthophoto / orthomosaic surveying-and-mapping output (GeoTIFF, DOM); imagery type is not named 'nadir' but the core documented product is top-down mapping."
gcp = "Technical specs list 'Ground Control Point (GCP) Management' as a supported function."
rtk_ppk = "Supported via POS data import (TXT/CSV) with adjustable POS Data Accuracy; FAQ lists 'GPS/RTK positioning accuracy' as an accuracy factor and specs were tested with the EVO II Pro RTK V3."
orthomosaic = "2D reconstruction outputs GeoTIFF orthophoto; Quick Stitching outputs DOM (Digital Orthophoto Map)."
dsm = "Quick Stitching output formats include DSM (plus 2.5D visualization)."
point_cloud = "Dense point cloud output in PNTS, LAS, XYZ."
mesh_3d = "3D model output in OBJ, PLY, OSGB, B3DM (textured 3D reconstruction)."
tiles_3d = "Output formats include B3DM (3D Tiles), PNTS (tiled point cloud), and OSGB (tiled model)."
desktop = "Windows 10+ (64-bit) desktop application with local processing."
cloud = "Offers cloud processing ('cloud or local processing', 'Cloud Ready')."
gpu = "Not called 'GPU acceleration' explicitly, but system requirements mandate a discrete NVIDIA GeForce GPU (GTX 1070 min / RTX 2080 Ti recommended) with 6-8GB VRAM for the deep-learning reconstruction processing."
+++

Autel Mapper is a 2D and 3D reconstruction (photogrammetry) software from Autel Robotics that processes drone imagery into mapping and modeling deliverables. It runs on Windows 10 or later (64-bit) and supports both local and cloud processing. Its type is 2D/3D reconstruction.

For 2D output, the software generates orthophotos in GeoTIFF, and its Quick Stitching mode produces DOM, DSM, and 2.5D visualization, including an on-the-fly stitching option. For 3D output, reconstruction quality can be set to high, medium, or low, producing models in B3DM, OSGB, OBJ, and PLY, alongside dense point clouds in PNTS, LAS, and XYZ. Aerial triangulation (output as XML) supports both rolling shutter and global shutter cameras and uses intelligent block processing for large datasets. Rebuild optimization includes KML import, model reconstruction processing, camera parameters, image POS data management, and Ground Control Point management.

The page lists applications in Public Safety, Search and Rescue, Surveying and Mapping, and Powerline Inspection. Stated performance figures include a maximum of 30,000 images per processing node and centimeter-level (1:500) mapping accuracy, with timing examples based on imagery collected by the EVO II Pro RTK V3 and processed on a high-performance workstation at the 'high' setting. Recommended hardware is substantial (for example an NVIDIA RTX 2080 Ti or higher and 32GB RAM or more).
