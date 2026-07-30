+++
title = "PhotoModeler"
description = "Photogrammetry software that turns photos and video into 3D models, measurements, orthophotos, dense surfaces, and contours."
weight = 17

[extra]
summary = "PhotoModeler is close-range and aerial photogrammetry software from PhotoModeler Technologies that derives 3D models, measurements, orthophotos, and surface models from photographs and video."
developer = "PhotoModeler Technologies (Eos Systems Inc.)"
country = "Canada"
license = "Proprietary"
open_source = false
price_model = "Paid: perpetual license or subscription (monthly/yearly)"
price_detail = "Standard: perpetual $998, yearly $548, monthly $68. Premium: perpetual $2,298, yearly $968, monthly $118 (prices listed on the products page)."
platforms = [
  "Windows desktop",
]
deployment = [
  "Desktop",
]
primary_outputs = [
  "Orthomosaic",
  "DSM",
  "Point cloud",
  "3D mesh",
  "Contours",
  "Index maps",
]
target_use_cases = [
  "Surveying & mapping",
  "Construction",
  "Mining & aggregates",
  "Inspection & infrastructure",
  "Public safety & emergency response",
  "Cultural heritage & archaeology",
  "Film, VFX & games",
  "Research & education",
]
latest_version = "unknown"
first_release_year = "unknown"
official_url = "https://www.photomodeler.com"
key_features = [
  "Extraction of 2D and 3D measurements and CAD-like models from photographs and video",
  "Coded target detection and SmartMatch automated point matching",
  "Dense Surface Modeling (dense point clouds and triangulated meshes) in the Premium edition",
  "Orthophoto generation with layer control, blending, masking, and occlusion checking",
  "Import of LiDAR and point cloud data (including LAS format)",
  "Ground Control Points and camera-station GPS/EXIF geo-coordinates, with PPK GPS correction",
  "Multispectral data processing producing NDVI and similar index ortho-mosaics",
  "In-viewer measurements (length, diameter, area) and volume/cut-fill calculations",
  "Project Review tool and processing report for quality/accuracy feedback",
  "Script commands and DDE automation",
]
pros = [
  "Produces both close-range CAD-style measurements and aerial mapping outputs (orthophoto, dense surface, contours, volumes)",
  "Provides a Project Review tool and processing report giving quality/accuracy feedback",
  "Supports coded targets and SmartMatch for automated point detection",
  "Handles Ground Control Points plus camera GPS/EXIF geotags, with PPK correction",
  "Imports LiDAR and point cloud data (LAS)",
  "Offers scripting and DDE commands for automation",
  "Available as either a perpetual license or a subscription",
]
cons = [
  "Aerial/UAV imagery, dense surface modeling, point cloud/LiDAR handling, geographic coordinate systems, and video import are limited to the higher-priced Premium edition",
  "The documented UAV workflow requires manually marking Ground Control Points across multiple images with the Triangle tool",
  "The help. Mismatched vertical datums commonly cause discrepancies between GCPs and UAV GPS, requiring manual coordinate-system verification",
  "Only a Windows desktop application; no vendor-hosted cloud or self-hosted server option",
]
typical_workflow = [
  "Create a SmartMatch/DSM (UAV) project and load photos or video via the New Project Wizard",
  "Apply EXIF/GPS geo-locations as camera-station control and run automatic feature detection, matching, and camera orientation",
  "Import and mark Ground Control Points and set the coordinate system",
  "Re-process (optimize) to refine the solution and check accuracy via the Project Review tool and processing report",
  "Generate dense surfaces, point clouds, triangulated meshes, contours, orthophotos, and measurements/volumes",
  "Export models to CAD or other software",
]
sources = [
  "https://www.photomodeler.com",
]

[extra.features]
image_input = "yes"
multispectral = "unknown"
thermal = "unknown"
lidar = "yes"
video = "yes"
gcp = "yes"
rtk_ppk = "yes"
accuracy_report = "yes"
coordinate_systems = "yes"
orthomosaic = "yes"
dsm = "yes"
dtm = "unknown"
point_cloud = "yes"
mesh_3d = "yes"
contours = "yes"
tiles_3d = "unknown"
gaussian_splatting = "unknown"
cad_export = "yes"
desktop = "yes"
cloud = "unknown"
self_hosted = "unknown"
api = "yes"
gpu = "unknown"
web_viewer = "unknown"
flight_planning = "unknown"
measurements = "yes"
volume = "yes"
veg_indices = "unknown"
change_detection = "unknown"
classification = "unknown"
annotations = "unknown"

[extra.feature_notes]
image_input = "Aerial drone/UAS mapping over an area (top-down); UAS support is now part of PhotoModeler Premium."
lidar = "Premium can import LiDAR and point cloud data to work alongside photos; import only, not LiDAR capture/generation."
video = "Video files (MOV/MP4/AVI/etc.) can be imported and used like still photos; Premium."
gcp = "Ground Control Point setup documented for UAV/drone projects; control points are core to PhotoModeler."
rtk_ppk = "Vendor drone/survey article states the software supports PPK and RTK camera positioning to reduce/eliminate ground control."
accuracy_report = "Project quality/accuracy output (residuals/precision statistics) plus PDF report export; PDF report is Premium only."
coordinate_systems = "Geographic Coordinate Systems with georeferencing, definable by WKT and Proj4; Premium (Geographic Systems)."
orthomosaic = "Ortho-photo output (rectified imagery over the mapped area), exported to TIF/JPG."
dsm = "Dense Surface Model (DSM) via SmartMatch; a Premium feature."
point_cloud = "Dense point cloud from DSM; import/export via LAS, PLY, etc."
mesh_3d = "Dense/photo-textured mesh; some mesh formats (PLY, FACET, etc.) are Premium only."
contours = "Listed as a Premium feature."
cad_export = "Exports DXF (2D and 3D) and IGES; DWG and LandXML are not documented."
desktop = "Windows desktop application."
api = "Automation via external commands/scripting documented on the new-features page."
volume = "Listed as a Premium feature."
+++

PhotoModeler is photogrammetry software developed by PhotoModeler Technologies (associated with Eos Systems Inc.) that converts photographs and video from ordinary cameras into 2D and 3D measurements and models. It is offered in two editions: Standard, which centers on CAD-like modeling with points, lines, curves, and surfaces plus coded-target and SmartMatch automation, and Premium, which adds Dense Surface Modeling, point cloud and LiDAR handling, geographic coordinate systems, video import, time-based motion measurement, and UAV/drone imagery support.

For aerial and mapping work, the Premium edition processes UAV imagery using GPS data from EXIF or an external file together with surveyed Ground Control Points. Documented outputs include orthophotos (with layer control, blending, masking, and occlusion checking), dense point clouds, triangulated meshes, computed contours, and surface models, along with volume, cut/fill, and dimensional measurements. The software also supports importing LiDAR and point cloud data (including LAS), PPK GPS correction, and multispectral data processing that produces NDVI and similar index ortho-mosaics.

The software runs as a desktop application and is applied across surveying and engineering, architecture, mining and geology, forensics and accident reconstruction, manufacturing and fabrication, marine fabrication, film/gaming/animation, and academic research. A Project Review tool and processing report provide quality and accuracy feedback, and script commands and DDE support enable automation. It is sold under perpetual licenses or monthly/yearly subscriptions.
