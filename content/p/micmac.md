+++
title = "MicMac"
description = "Free, open-source (CeCILL-B) photogrammetry suite from IGN/ENSG for 3D reconstruction and orthophotos from ground, drone, aerial and satellite images."
weight = 16

[extra]
summary = "MicMac is a free, open-source photogrammetry suite developed by France's IGN and ENSG for 3D reconstruction and ortho-imagery from ground, drone, aerial and satellite imagery, operated mainly through command-line tools (mm3d) with optional Qt GUI utilities."
developer = "IGN (Institut national de l'information geographique et forestiere) and ENSG, LASTIG laboratory"
country = "France"
license = "CECILL-B"
open_source = true
price_model = "Free / open source"
price_detail = "Free and open source, distributed under the CeCILL-B licence since 2007; source code available on GitHub."
platforms = [
  "Windows",
  "macOS",
  "Linux",
  "Raspberry Pi",
]
deployment = [
  "Local desktop install (pre-compiled binaries or self-compiled from source)",
  "Docker image",
]
primary_outputs = [
  "Orthomosaic",
  "DSM",
  "Point cloud",
  "3D mesh",
]
target_use_cases = [
  "Surveying & mapping",
  "Cultural heritage & archaeology",
  "Environmental & forestry",
  "Research & education",
]
latest_version = "unknown"
first_release_year = "2007"
official_url = "https://micmac.ensg.eu"
key_features = [
  "Command-line photogrammetry toolset invoked through the mm3d launcher, each command with inline help and, in Qt builds, an optional GUI dialog",
  "Tie point detection and matching (Tapioca, Pastis, Sift) and camera orientation/calibration (Tapas, Apero, Campari)",
  "Ground Control Point workflow: interactive capture (SaisieAppuisInit/Predic), georeferencing (GCPBascule, CenterBascule) and accuracy control (GCPCtrl)",
  "Dense image matching and DEM generation (Malt, C3DC, PIMs, PIMs2Mnt)",
  "Point cloud generation (Nuage2Ply, PIMs2Ply, AperiCloud) and mesh creation and texturing (TiPunch, Tequila)",
  "Orthophoto generation (Malt, Porto, Tawny)",
  "Handles ground/close-range, drone, aerial and satellite imagery, plus scanned historical photogrammetric films and video frames",
  "Cross-platform: Windows, macOS, Linux (Ubuntu/Fedora/RHEL) and Raspberry Pi",
]
pros = [
  "Free and open source under the CeCILL-B licence with source code on GitHub",
  "Cross-platform, including Windows, macOS, Linux and Raspberry Pi",
  "Broad command-line toolset spanning tie points, orientation, dense matching, DEM, orthophoto and mesh generation",
  "Dedicated GCP capture, georeferencing and accuracy-control tools",
  "Processes a wide range of inputs: ground, drone, aerial, satellite, scanned historical films and video",
  "Automatable through the mm3d command line and batch/scripting tools (BatchFDC, MapCmd)",
]
cons = [
  "Primary interface is the command line (mm3d); a GUI is only available in Qt builds or via the third-party AperoDeDenis application",
  "Visualization of 3D products relies on external tools such as MeshLab or CloudCompare",
  "The official documentation wiki is noted on the homepage as still under construction",
  "Several listed commands are marked as in development or early work in progress (e.g. Digeo, Martini, SateLib, Arsenic)",
]
typical_workflow = [
  "Detect and match tie points across the image set (Tapioca)",
  "Compute internal and external camera orientation (Tapas)",
  "Capture Ground Control Points and georeference the block (SaisieAppuisInit, GCPBascule, Campari), then check accuracy (GCPCtrl)",
  "Run dense matching to produce depth maps / DEM (Malt, C3DC or PIMs)",
  "Export a dense point cloud (Nuage2Ply, PIMs2Ply) and, if needed, build and texture a mesh (TiPunch, Tequila)",
  "Generate the orthophoto (Malt Ortho, Porto, Tawny)",
  "Visualize the outputs in external tools such as MeshLab or CloudCompare",
]
sources = [
  "https://micmac.ensg.eu",
  "https://github.com/micmacIGN/micmac",
]

[extra.features]
image_input = "yes"
multispectral = "unknown"
thermal = "unknown"
lidar = "unknown"
video = "yes"
gcp = "yes"
rtk_ppk = "unknown"
accuracy_report = "yes"
coordinate_systems = "yes"
orthomosaic = "yes"
dsm = "yes"
dtm = "unknown"
point_cloud = "yes"
mesh_3d = "yes"
contours = "unknown"
tiles_3d = "unknown"
gaussian_splatting = "unknown"
cad_export = "unknown"
desktop = "yes"
cloud = "unknown"
self_hosted = "unknown"
api = "yes"
gpu = "unknown"
web_viewer = "unknown"
flight_planning = "unknown"
measurements = "unknown"
volume = "unknown"
veg_indices = "unknown"
change_detection = "yes"
classification = "unknown"
annotations = "unknown"

[extra.feature_notes]
image_input = "Presentation page states MicMac handles aerial and satellite acquisitions of cities and natural areas; Historical_Orthoimage tutorial processes aerial images into DEM and orthoimages."
video = "Video input supported via DIV (video development using ffmpeg) and VV (3D model from video, described as experimental/'just for fun')."
gcp = "Multiple documented GCP tools: GCPBascule, GCPConvert, GCPCtrl, SaisieAppuisInit/Predic, Aspro (init orientation from GCP)."
accuracy_report = "Documented via GCPCtrl 'Control accuracy with GCP' plus bundle-adjustment residuals/covariance analysis; output is command-line/statistics rather than a formatted PDF report."
coordinate_systems = "Georeferencing to local/global/absolute coordinate systems; ChgSysCo changes coordinate system, dedicated Coordinates Systems doc page, and PROJ dependency for CRS handling."
orthomosaic = "Documented commands Tawny and Porto generate ortho-images/global ortho-photo (orthomosaic from merged orthoimages)."
dsm = "Documented DEM/DSM generation via Malt and PIMs2Mnt; the wiki links a 'How to produce a Digital Surface Model' tutorial and Canopy DCM example."
point_cloud = "Dense point cloud in PLY via Nuage2Ply, AperiCloud, PIMs2Ply, and C3DC."
mesh_3d = "TiPunch computes mesh and Tequila textures the mesh (3D textured mesh)."
desktop = "Command-line desktop suite (mm3d) for Linux/Windows/macOS with optional QT GUI tools and a Docker image."
api = "Scriptable command-line toolset (mm3d commands) with batch/automation tools (BatchFDC, MapCmd) and an underlying C++ library; no documented REST/web API."
change_detection = "Historical_Orthoimage tutorial states products let you 'monitor changes' (urbanization, landscape) from multi-temporal historical imagery; deformation tools MM2DPosSism/FieldDep3d support 2D/3D displacement studies."
+++

MicMac is a free, open-source photogrammetric suite developed at France's IGN (National Institute of Geographic and Forest Information) and ENSG (National School of Geographic Sciences), within the LASTIG laboratory, and distributed under the CeCILL-B licence since 2007. It is aimed mainly at professional and academic users and supports a range of 3D reconstruction scenarios, allowing both the creation of 3D models and, where appropriate, ortho-imagery.

The software is presented as versatile across scales and fields (cartography, environment, industry, forestry, heritage, archaeology), handling objects from ground-captured statues and building facades to churches and castles via drone acquisition, up to buildings, cities and natural areas from aerial or satellite imagery. It also handles scanned historical photogrammetric films and video frames, and provides tools to georeference end products in local, global or absolute coordinate systems.

MicMac is operated primarily through command-line programs launched via mm3d, each with inline help; when built with the Qt option (or using IGN-provided binaries), commands also expose GUI dialogs. It is cross-platform (Windows, macOS, Linux and Raspberry Pi), installable from pre-compiled binaries, source compilation or a Docker image. Visualization of the resulting 3D products is typically done with external software such as MeshLab or CloudCompare.
