+++
title = "RealityScan"
description = "Photogrammetry software by Epic Games that builds 3D meshes, point clouds, orthomosaics, and terrain models from photographs and laser or LiDAR scans."
weight = 5

[extra]
summary = "Photogrammetry software by Epic Games that turns photographs and laser/LiDAR scans into 3D meshes, point clouds, orthomosaics, and terrain models."
developer = "Epic Games"
license = "Proprietary (freemium)"
open_source = false
price_model = "Freemium"
price_detail = "Free for students, educators, individuals, and companies with under $1 million USD in annual gross revenue (educators and schools have no revenue limit). Businesses over the $1 million USD threshold purchase a yearly \"RealityScan seat.\" The legacy RealityCapture pay-per-input (PPI) licensing server is stated to close on August 3, 2026."
platforms = [
  "Windows",
  "Linux",
  "iOS",
  "Android",
]
deployment = [
  "Desktop application (Windows and Linux, installed via the Epic Games Launcher)",
  "Mobile app (iOS and Android) with on-device processing",
]
primary_outputs = [
  "Orthomosaic",
  "DTM",
  "Point cloud",
  "3D mesh",
  "3D tiles",
  "Contours",
]
target_use_cases = [
  "Surveying & mapping",
  "Construction",
  "Inspection & infrastructure",
  "Public safety & emergency response",
  "Cultural heritage & archaeology",
  "Environmental & forestry",
  "Film, VFX & games",
  "Research & education",
]
latest_version = "2.2 (released June 24, 2026)"
official_url = "https://www.realityscan.com"
key_features = [
  "Image alignment and 3D reconstruction from photographs and laser/LiDAR scans",
  "Dense point cloud and high-triangle textured mesh generation",
  "Orthomosaic/orthophoto, digital terrain model, contour line, and heightmap output",
  "Georeferencing using coded markers, ground control-point measurements, flight logs, and RTK/PPK accuracies",
  "Point cloud classification, including AI Classification that separates ground from structures",
  "Built-in measurement tools for distances, areas, volumes, cross-sections, and cutting planes",
  "UV unwrapping, texturing, normal/displacement map baking, plus simplification and cleanup tools",
  "AI Masking/background removal and multi-layer image workflows",
  "Export to standard GIS formats and Cesium 3D Tiles",
  "Automation via a headless command-line interface, interface macros, and a built-in scripting/reporting language",
  "Import of aerial and ground LiDAR scans and SLAM data",
  "RealityScan Mobile companion app (iOS, Android) using the same engine",
]
pros = [
  "Accepts imagery from many source types (smartphones, DSLR, mirrorless cameras, drone rigs, video frames, screenshots) and can fuse it with aerial and ground LiDAR/laser scans",
  "Out-of-core algorithms are processing large datasets with no fixed limit on image count or resolution on a single machine",
  "Provides survey-oriented georeferencing via coded markers, ground control points, flight logs, and RTK/PPK data",
  "Includes built-in measurement tools for distances, areas, volumes, cross-sections, and cutting planes",
  "Offers automation through a headless command-line interface, macros, and a scripting/reporting language",
  "Free for students, educators, individuals, and businesses under $1 million USD in annual gross revenue",
]
cons = [
  "Desktop installation requires the Epic Games Launcher and an Epic Games account",
  "Minimum desktop. An NVIDIA CUDA-capable GPU; full AMD GPU support was introduced only in version 2.2 (Windows)",
  "Businesses over $1 million USD in annual gross revenue must purchase a paid yearly seat",
  "The legacy RealityCapture pay-per-input licensing server is being shut down (August 3, 2026), affecting older PPI projects",
]
typical_workflow = [
  "Capture images (smartphone, DSLR, mirrorless, drone rig, or video frames) and optionally laser/LiDAR scans or SLAM data",
  "Import imagery and scans and, for georeferencing, add coded markers, ground control-point measurements, flight logs, or RTK/PPK data",
  "Align images and reconstruct a dense point cloud and mesh",
  "Optionally classify points, mask backgrounds, clean up geometry, and texture the model with UV unwrapping and normal/displacement baking",
  "Export outputs (textured mesh, point cloud, orthomosaic, terrain model/heightmap, contours, GIS formats, Cesium 3D Tiles) or automate the pipeline via the command-line interface and scripting",
]
sources = [
  "https://www.realityscan.com",
  "https://www.realityscan.com/features",
]

[extra.features]
image_input = "yes"
multispectral = "unknown"
thermal = "unknown"
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
contours = "yes"
tiles_3d = "yes"
gaussian_splatting = "unknown"
cad_export = "yes"
desktop = "yes"
cloud = "yes"
self_hosted = "unknown"
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
image_input = "Aerial Data tutorial states there is no difference between creating models from aerial imagery or terrestrial data and that you can freely combine aerial and street-level photos; software produces orthographic projections and maps from aerial imagery."
accuracy_report = "Built-in report templates include an Overview Report and a Registration and Georeferencing Accuracy Report (camera position deviations, GCP statistics); reports open in a web browser."
coordinate_systems = "Ships with the EPSG database; supports selecting project and output coordinate systems and using multiple coordinate systems at once."
contours = "Contour lines (isolines) and cross sections can be computed and exported (RealityScan.Export.Isolines) from ortho projections."
tiles_3d = "Cesium 3D Tiles export via the Level of Detail export (and Cesium ion integration)."
cad_export = "AutoCAD DXF (.dxf) export is listed; DWG and LandXML are not documented."
cloud = "Cloud processing applies to the free RealityScan Mobile app (photos upload and are processed in the cloud). The desktop application processes locally."
api = "Automation is via a command-line interface (CLI) for scripting/batch tasks, not a REST web API."
gpu = "GPU-accelerated reconstruction; RealityScan 2.2 adds full AMD GPU support (in addition to existing CUDA support)."
web_viewer = "Documented sharing path is publishing/exporting results to Sketchfab (an Epic-owned browser-based 3D viewer), primarily from RealityScan Mobile."
classification = "LiDAR/point cloud classification into ASPRS classes (ground, vegetation, buildings); classification is also used to generate a DTM."
+++

RealityScan (formerly RealityCapture) is photogrammetry software developed by Epic Games that reconstructs 3D models and point clouds from photographs and laser/LiDAR scans. It accepts imagery from smartphones, DSLR and mirrorless cameras, drone rigs, video frames, and screenshots, and its out-of-core algorithms process large datasets without fixed limits on image count or resolution on a single machine. Aerial and ground LiDAR scans, as well as imported SLAM data and classified point clouds, can be fused with the imagery.

For mapping and surveying workflows, the software can georeference models using coded markers, ground control-point measurements, flight logs, and RTK/PPK accuracies. Outputs include textured meshes, point clouds, orthomosaics/orthophotos, digital terrain models, contour lines, and heightmaps, with export to standard GIS formats and Cesium 3D Tiles. Built-in measurement tools extract distances, areas, volumes, cross-sections, and cutting planes, AI Classification separates ground from structures, and capturing sites at intervals supports monitoring change over time.

RealityScan runs as a desktop application on Windows and Linux (installed through the Epic Games Launcher) and has a companion mobile app for iOS and Android that uses the same engine. Workflows can be automated through a headless command-line interface, interface macros, and a built-in scripting/reporting language. It is free for students, educators, individuals, and businesses under $1 million USD in annual gross revenue, with paid yearly seats required above that threshold.
