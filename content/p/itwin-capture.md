+++
title = "iTwin Capture"
description = "Bentley reality modeling software that turns imagery and point clouds into 3D reality meshes, orthophotos, DSMs, and point clouds."
weight = 9

[extra]
summary = "Bentley iTwin Capture is reality modeling software (desktop iTwin Capture Modeler plus iTwin Capture cloud services) that processes imagery, video, and point clouds into reality meshes, orthophotos, DSMs, and point clouds for infrastructure digital twins."
developer = "Bentley Systems"
country = "United States"
license = "Proprietary"
open_source = false
price_model = "Subscription (perpetual also referenced); pricing not disclosed on the sources"
price_detail = "The iTwin Capture Modeler page references subscription and perpetual license models, and processing in the cloud via a subscription to iTwin Capture Cloud Services. No specific prices are published on the reviewed pages."
platforms = [
  "Windows",
]
deployment = [
  "Desktop application (iTwin Capture Modeler, Windows 10 64-bit)",
  "Cloud processing via iTwin Capture Cloud Services",
  "Web, mobile, and desktop clients (iTwin Capture platform)",
]
primary_outputs = [
  "Orthomosaic",
  "DSM",
  "Point cloud",
  "3D mesh",
  "3D tiles",
  "Gaussian splats",
]
target_use_cases = [
  "Surveying & mapping",
  "Construction",
  "Inspection & infrastructure",
]
latest_version = "unknown"
first_release_year = "unknown"
official_url = "https://www.bentley.com/software/itwin-capture/"
key_features = [
  "Reality mesh (3D textured mesh) generation from imagery and point clouds",
  "True orthophoto and 2.5D digital surface model output (TIFF/GEOTIFF/KML)",
  "Colored point cloud export (LAS/OPC/POD)",
  "Mesh export in multiple formats including 3MX, 3SM, DGN, I3S, OBJ, FBX, STL, DAE, OSGB, and Cesium",
  "Ground control point import, recording, and automatic detection",
  "Handles flight metadata from EXIF tags to external columned files",
  "Camera calibration report import",
  "Quality reports and 3D quality metrics review",
  "In-viewer/precision measurement",
  "Parallel (cluster) processing for scalability; up to 2 engines in the Center edition",
  "AI feature extraction with trained detectors (3D segmentation, orthophoto segmentation, photo object detection, photo segmentation)",
  "Classified point clouds and anonymized images (iTwin Capture platform)",
  "SDK; iTwin Platform Reality Modeling/Management/Analysis APIs",
  "Retouching tools: remove floating artifacts, fill holes, flatten areas, improve orthophoto image transitions",
]
pros = [
  "Produces multiple engineering-ready outputs (reality mesh, true orthophoto, DSM, point cloud) from imagery and point clouds",
  "Wide range of mesh and point cloud export formats for downstream design, GIS, and web workflows",
  "Supports ground control points, flight metadata, and camera calibration to improve geo-registration and precision",
  "Generates quality reports and 3D quality metrics for accuracy assessment",
  "Offers both local desktop processing and cloud processing, plus parallel/cluster processing for scaling",
  "Provides an SDK and iTwin Platform reality-modeling APIs for automation",
]
cons = [
  "Desktop application requires Microsoft Windows (Windows 10 64-bit stated); no other desktop OS confirmed on the sources",
  "Some advanced functions (machine learning, automatic color equalization, ground and feature extraction) require an NVIDIA graphics card",
  "Public pricing is not disclosed on the reviewed pages",
  "AI detector quality depends on how similar the input data is to each detector's training dataset (stated on the AI Detectors page)",
]
typical_workflow = [
  "Import reality data (images, video, or point clouds) from any digital camera, scanner, or mobile mapping device",
  "Add ground control points, flight metadata, and/or camera calibration to improve geo-registration and precision",
  "Process (locally or via cloud services, optionally with parallel engines) to generate reality meshes, orthophotos, DSMs, and point clouds",
  "Review quality reports and 3D quality metrics, and apply retouching (remove artifacts, fill holes, flatten areas)",
  "Export in the required formats and share to a connected reality data environment for downstream workflows",
]
sources = [
  "https://www.bentley.com/software/itwin-capture/",
]

[extra.features]
image_input = "yes"
multispectral = "unknown"
thermal = "yes"
lidar = "yes"
video = "yes"
gcp = "yes"
rtk_ppk = "unknown"
accuracy_report = "yes"
coordinate_systems = "yes"
orthomosaic = "yes"
dsm = "yes"
dtm = "yes"
point_cloud = "yes"
mesh_3d = "yes"
contours = "unknown"
tiles_3d = "yes"
gaussian_splatting = "yes"
cad_export = "yes"
desktop = "yes"
cloud = "yes"
self_hosted = "yes"
api = "yes"
gpu = "yes"
web_viewer = "yes"
flight_planning = "unknown"
measurements = "yes"
volume = "yes"
veg_indices = "unknown"
change_detection = "unknown"
classification = "yes"
annotations = "unknown"

[extra.feature_notes]
image_input = "iTwin Capture Engine calibrates all images by automatically identifying the relative position and orientation of each photo, i.e. reconstructs from images at any position/angle using any digital camera."
thermal = "Input supports RGB and thermal imagery; produces RGB and thermal orthophotos (iTwin Capture Engine page)."
lidar = "Accepts lidar point clouds in LAS, LAZ, OPC, and POD formats."
video = "Datasheet lists video as an importable reality data input type alongside image and point cloud."
gcp = "Datasheet lists ground control point import, recording, and automatic detection (QR/April/Chili tags)."
accuracy_report = "Datasheet: generate quality reports and review quality metrics in 3D; Engine produces aerotriangulation reports."
coordinate_systems = "Georeferencing / geo-registration to coordinate systems is a listed capability."
dsm = "True orthophoto / 2.5D digital surface model export (TIFF/GEOTIFF/KML) per datasheet."
dtm = "iTwin Capture Engine/WorkSuite pages list DEM/DSM and DTM (terrain models) output."
tiles_3d = "Mesh export formats include 3MX, 3SM, I3S, and Cesium 3D Tiles (tiled/streamable formats)."
gaussian_splatting = "The vendor-owned page https://www.bentley.com/software/itwin-capture-modeler/ (Bentley's official iTwin Capture Modeler product page) explicitly states the iTwin Capture Engine produces \\\"Gaussian splats\\\" as an output, twice: in the overview (\\\"transforms your imagery and lidar point clouds into precise digital assets - including 3D meshes, Gaussian splats, orthomosaics, digital surface models, and"
cad_export = "Exports to Bentley DGN (a CAD format) among mesh formats; no explicit DXF/DWG/LandXML confirmed on vendor pages."
desktop = "iTwin Capture Modeler / Modeler Flex are desktop applications for local processing."
cloud = "Cloud processing available via the iTwin Capture Cloud Services subscription."
self_hosted = "Engine runs locally on your own Windows hardware with parallel/cluster processing (local processing for speed and security)."
api = "Datasheet lists an SDK; a Reality Modeling API is available on the iTwin developer platform to convert photos into 3D reality meshes."
gpu = "GPU acceleration used for processing; NVIDIA GPU required for advanced ML functions; parallel computing with a powerful GPU."
web_viewer = "Reality meshes are web-ready for navigation in iTwin web applications; image collections shareable as mapping runs for web-based photo navigation in the connected reality data environment."
measurements = "In-viewer measurements: points, lines, areas, and volumes in 2D and 3D; quality metrics reviewed in 3D."
volume = "Measure volumes in 2D and 3D (iTwin Capture WorkSuite / Manage & Extract)."
classification = "Produces classified point clouds; AI feature extraction and ground extraction included."
+++

iTwin Capture is Bentley Systems' reality modeling offering for creating and managing reality data used in infrastructure digital twins. It centers on iTwin Capture Modeler, a desktop photogrammetry application distributed in two editions (iTwin Capture Modeler and iTwin Capture Modeler Center), and is complemented by iTwin Capture Cloud Services for hosted processing and by web, mobile, and desktop clients on the broader iTwin Capture platform.

The software imports reality data of any type (image, point cloud, or video) captured with digital cameras, scanners, or mobile mapping devices, and produces reality meshes, true orthophotos, 2.5D digital surface models, and colored point clouds. Precision can be improved with ground control point import, recording, and automatic detection, flight metadata from EXIF tags or external files, and imported camera calibration reports, with quality reports and 3D quality metrics available for assessment. Outputs export in a wide range of mesh formats (including 3MX, 3SM, DGN, I3S, OBJ, FBX, STL, DAE, OSGB, and Cesium) and point cloud formats (LAS, OPC, POD).

Processing can run locally on the user's own hardware or in the cloud through a subscription to iTwin Capture Cloud Services, and parallel/cluster processing supports larger, city-scale projects. The platform includes AI feature extraction via downloadable trained detectors (3D segmentation, orthophoto segmentation, photo object detection, and photo segmentation), and outputs such as classified point clouds and anonymized images. An SDK is provided, and Bentley's iTwin Platform exposes reality modeling, management, and analysis APIs. Documented use cases include infrastructure, construction and engineering, surveying, and inspection/monitoring such as bridge and dam monitoring.
