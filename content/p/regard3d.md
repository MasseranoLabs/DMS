+++
title = "Regard3D"
description = "Free, open source structure-from-motion desktop program that builds 3D point clouds and textured meshes from multiple photos of an object."
weight = 24

[extra]
summary = "Regard3D is a free, open source (MIT) structure-from-motion desktop program that reconstructs 3D point clouds and surface meshes from multiple photographs of an object, running on Windows, macOS and Linux."
developer = "Roman Hiestand"
country = "Switzerland"
license = "MIT"
open_source = true
price_model = "Free (open source)"
price_detail = "Free to use, released under the MIT license, which permits commercial and non-commercial use."
platforms = [
  "Windows",
  "macOS",
  "Linux",
]
deployment = [
  "Desktop",
]
primary_outputs = [
  "Point cloud",
  "3D mesh",
]
target_use_cases = []
latest_version = "unknown"
first_release_year = "unknown"
official_url = "https://www.regard3d.org"
key_features = [
  "Structure-from-motion pipeline that reconstructs 3D geometry from multiple photographs taken from different viewpoints",
  "Feature detection using A-KAZE and mathematical descriptors using LIOP (Local Intensity Order Pattern)",
  "Two triangulation (SfM) engines: incremental and global (global available only when all pictures use the same camera and zoom setting)",
  "Densification with a choice of three multi-view stereo toolsets: CMVS/PMVS, MVE (Multi-View Environment), and SMVS (Shading-aware Multi-View Stereo)",
  "Surface reconstruction with a choice of Poisson Surface Reconstruction or Floating Scale Surface Reconstruction (FSSR)",
  "Colorization by vertex coloring or texture mapping, with optional photometric outlier removal, geometric visibility testing, and seam leveling",
  "3D viewer with virtual-trackball navigation, adjustable point size, and surface rendering options (texture, lighting, shading, polygon modes)",
  "Export of point clouds (PLY, PCD) and surfaces (OBJ, PLY); textured surfaces export as OBJ plus MTL and PNG texture files",
  "Export of triangulations to external MVS tools (CMPMVS, MeshRecon, OpenMVS, SURE) and export of MeshLab projects with camera information",
  "Uses a camera database (based on the openMVG sensor_database.csv) plus user-defined entries for focal length and sensor size",
]
pros = [
  "Free and open source under the permissive MIT license, allowing commercial and non-commercial use",
  "Runs as a cross-platform desktop application on Windows, macOS, and Linux",
  "Guided, step-by-step project workflow from photographs to exported 3D model",
  "Offers multiple selectable algorithms for both densification (CMVS/PMVS, MVE, SMVS) and surface reconstruction (Poisson, FSSR)",
  "Exports to standard formats (OBJ, PLY, PCD) and integrates with external tools such as MeshLab and additional MVS programs",
]
cons = [
  "Only JPEG images are supported as input",
  "Requires the focal length and sensor size of at least some pictures to be known, either via EXIF metadata with the camera present in the camera database or entered manually",
  "The global structure-from-motion engine is available only when all pictures are taken from the same camera and with the same zoom setting",
  "64-bit only; does not run on Windows XP (Vista untested), requires Windows 7 or newer or macOS 10.7 or newer, an OpenGL-capable graphics card, and 4 GB RAM minimum (8 GB or more recommended for larger projects)",
  "Texture creation requires substantially more time and memory than vertex coloring, especially with large projects",
]
typical_workflow = [
  "Create a project",
  "Add a picture set (JPEG images with camera focal length and sensor size available via EXIF or manual entry)",
  "Compute matches (feature detection, descriptor matching, geometric filtering, and track generation)",
  "Triangulate to produce a sparse point cloud and camera positions (incremental or global SfM)",
  "Densify the sparse point cloud into a dense point cloud (CMVS/PMVS, MVE, or SMVS)",
  "Generate a surface mesh (Poisson or FSSR) with vertex coloring or texture mapping",
  "Export point clouds, surfaces, or triangulations to files or external tools",
]
sources = [
  "https://www.regard3d.org",
]

[extra.features]
image_input = "yes"
multispectral = "unknown"
thermal = "unknown"
lidar = "unknown"
video = "unknown"
gcp = "unknown"
rtk_ppk = "unknown"
accuracy_report = "unknown"
coordinate_systems = "unknown"
orthomosaic = "unknown"
dsm = "unknown"
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
api = "unknown"
gpu = "unknown"
web_viewer = "unknown"
flight_planning = "unknown"
measurements = "unknown"
volume = "unknown"
veg_indices = "unknown"
change_detection = "unknown"
classification = "unknown"
annotations = "unknown"

[extra.feature_notes]
image_input = "Regard3D is a general structure-from-motion tool that reconstructs from photos of an object taken from different angles/viewpoints (not drone-specific); the arbitrary-viewpoint reconstruction covers top-down imagery."
point_cloud = "Dense point cloud produced via densification (CMVS/PMVS, MVE, or SMVS); exportable as PLY or PCD."
mesh_3d = "Textured 3D surface mesh via Poisson Surface Reconstruction or FSSR; textured export as OBJ (.obj/.mtl/.png), colored-vertex export as PLY or OBJ."
desktop = "Free and open-source desktop application for Windows, macOS, and Linux."
+++

Regard3D is a free and open source structure-from-motion program that creates 3D models from a series of photographs of an object taken from different viewpoints. It is released under the MIT license (copyright 2015-2018 Roman Hiestand) and is written by a software engineer based in Switzerland. It runs as a desktop application on Windows, macOS (OS X), and Linux, and is distributed via SourceForge.

The processing pipeline moves through defined stages: creating a project, adding a picture set, computing matches (feature detection with A-KAZE, descriptors with LIOP, descriptor matching and geometric filtering, and track generation requiring a point to be seen in at least three images), triangulation to compute a sparse point cloud and camera poses (via an incremental or global SfM engine), densification into a dense point cloud (using CMVS/PMVS, MVE, or SMVS), and surface reconstruction (using Poisson or FSSR) with optional vertex coloring or texture mapping.

Inputs are JPEG images whose camera focal length and sensor size must be known, drawn from EXIF metadata combined with a camera database (based on the openMVG sensor_database.csv) or entered manually. Outputs include sparse and dense point clouds and surface meshes, exportable as PLY and PCD (point clouds) and OBJ and PLY (surfaces), with textured meshes exported as OBJ plus MTL and PNG files. Triangulations can also be exported to external multi-view stereo tools (CMPMVS, MeshRecon, OpenMVS, SURE) and to MeshLab projects that include camera information.
