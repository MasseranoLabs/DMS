+++
title = "3DF Zephyr"
description = "Desktop photogrammetry software by 3Dflow that builds point clouds, meshes, orthophotos and DEMs from photos, video frames and laser scans."
weight = 12

[extra]
summary = "3DF Zephyr is a desktop photogrammetry application by 3Dflow (Verona, Italy) that reconstructs point clouds, textured meshes, orthophotos and DEMs from photographs, video frames and laser scans, sold in Free, Lite and Professional editions."
developer = "3Dflow SRL"
country = "Italy"
license = "Proprietary (freemium)"
open_source = false
price_model = "Freemium with perpetual and subscription paid editions"
price_detail = "Free edition (up to 50 photos/frames, single GPU); Lite perpetual 199 EUR + VAT; Professional monthly 250 EUR + VAT/month; Professional perpetual 4,200 EUR + VAT. Perpetual licenses include 12 months of updates; optional renewal is 20% of the license price per year."
platforms = []
deployment = [
  "Desktop",
]
primary_outputs = [
  "Orthomosaic",
  "DSM",
  "Point cloud",
  "3D mesh",
  "Gaussian splats",
  "Contours",
]
target_use_cases = [
  "Surveying & mapping",
  "Mining & aggregates",
  "Cultural heritage & archaeology",
  "Inspection & infrastructure",
  "Film, VFX & games",
]
latest_version = "unknown"
first_release_year = "unknown"
official_url = "https://www.3dflow.net/3df-zephyr-pro-3d-models-from-photos/"
key_features = [
  "Structure from Motion camera orientation with global and incremental pipelines and dense point cloud generation (all editions)",
  "Textured mesh generation with multi-texturing/UDIM, plus normal and displacement maps (Lite and up)",
  "Orthophoto/orthomosaic and DEM generation with elevation profiles (Professional)",
  "DXF contour lines, sections/track sections and CAD polyline drawing (Professional)",
  "Ground Control Points alignment and 3D metric measurements of distances, areas and volumes (Professional)",
  "Volume computation of a full mesh or projected on a plane, including hollow volumes such as tunnels or sewers (Professional)",
  "Multispectral camera support with radiometric calibration wizard and DEM/multispectral viewer (Professional)",
  "Native laser scan support (.fls,.rdbx,.zfs,.dp) with 3DF Scarlet registration bundled and Multi-ICP alignment (Professional; viewer-only in Free/Lite)",
  "Ground Extraction filter and AI point cloud classification tool (Professional)",
  "Point cloud comparison tool reporting differences between two point clouds (Professional)",
  "Python scripting and XML-based batch processing (Professional)",
  "Multi-GPU acceleration via NVIDIA CUDA and AMD/Intel OpenCL",
  "Broad export formats: ply, obj, stl, wrl, 3mf, alembic, glb, dxf, plus PDF3D, u3d, Collada and WebGL/HTML in Professional; point clouds as e57, las, laz, ply, xyz, pts, dxf, rcp",
]
pros = [
  "Multiple entry points, from a Free edition (up to 50 photos/frames) through Lite and Professional (perpetual or monthly)",
  "Accepts photographs, video frames and native laser scan formats (.fls,.rdbx,.zfs,.dp), with 3DF Scarlet registration bundled in Professional",
  "Professional edition covers a full survey toolset: orthophoto/orthomosaic, DEM, contour lines, GCP alignment, measurements, volumes, multispectral, AI classification and Python scripting",
  "Documented drone/UAV and RTK workflows in the tutorial library",
  "Multi-GPU acceleration and a wide range of mesh and point cloud export formats",
]
cons = [
  "Most geospatial and survey features (orthophoto/orthomosaic, DEM, contour lines, GCP, measurements, volumes, multispectral, classification, Python scripting, batch processing) require the Professional edition and are not in Free or Lite (feature comparison page)",
  "Free edition is limited to 50 photos/video frames and a single GPU; native laser scans are viewer-only in Free and Lite (feature comparison page)",
  "Professional perpetual license is priced at 4,200 EUR + VAT, with an optional 20%-per-year renewal to keep receiving updates",
]
typical_workflow = [
  "Import photographs, video frames or laser scans into a project",
  "Run Structure from Motion to orient cameras and recover their positions",
  "Generate a dense point cloud",
  "Extract and texture a 3D mesh",
  "In Professional, georeference with GCPs/GPS EXIF and derive orthophoto, DEM, contour lines, measurements, volumes and classified/ground-extracted outputs",
  "Export results in mesh or point cloud formats, or upload to Sketchfab",
]
sources = [
  "https://www.3dflow.net/3df-zephyr-pro-3d-models-from-photos/",
]

[extra.features]
image_input = "yes"
multispectral = "yes"
thermal = "unknown"
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
tiles_3d = "unknown"
gaussian_splatting = "yes"
cad_export = "yes"
desktop = "yes"
cloud = "unknown"
self_hosted = "unknown"
api = "yes"
gpu = "yes"
web_viewer = "yes"
flight_planning = "unknown"
measurements = "yes"
volume = "yes"
veg_indices = "yes"
change_detection = "unknown"
classification = "yes"
annotations = "unknown"

[extra.feature_notes]
image_input = "An 'unordered' image option and reconstruction from images at arbitrary angles. DJI Mavic 3 RTK nadir (90 deg) flights."
multispectral = "Full multispectral camera support with radiometric calibration wizard; multiband datasets supported (agriculture pages and feature comparison)."
lidar = "Imports native laser scan formats (.fls,.fws,.e57,.rdbx,.zfs,.dp) and exports/aligns point clouds (laser-laser and laser-photogrammetry ICP)."
video = "Imports movie files (.mpeg,.wmv,.avi,.mp4) and uses video frames for reconstruction."
rtk_ppk = "Docs: images with RTK coordinates are auto-detected from EXIF and camera position accuracy set accordingly; GPS/RTK/PPK import supported."
accuracy_report = "Control-points tutorial: an error report appears after scaling/georeferencing (Tools > Control points > Show alignment info) with global/local reprojection error and checkpoints; also PDF report of workspace."
coordinate_systems = "Select coordinate system by name or EPSG code, import custom CRS, auto-detect projection, and georeference/reproject to a projected coordinate system."
dtm = "Generate DTM option plus AI Ground Extraction filter to isolate ground/non-ground and produce DTMs."
contours = "Creates and exports DXF contour lines."
gaussian_splatting = "Vendor documentation at 3dflow.net/zephyr-doc/en/GaussianSplatting.html states: \"Since version 9.0, 3DF Zephyr also supports a Gaussian Splatting workflow that ties directly within the established photogrammetry pipeline.\" It generates splats from sparse/dense clouds, external data, or meshes for view-synthesis visualization. The vendor release page 3dflow.net/3df-zephyr-9-0-has-been-released/ add"
cad_export = "Exports DXF (meshes, contour lines, drawing elements) plus DGN and SHP; DWG and LandXML not documented."
desktop = "3DF Zephyr is desktop software (Free, Lite, Pro editions)."
api = "Python scripting to automate the workflow and XML-based batch reconstruction; FlowEngine SDK available separately."
gpu = "Multi-GPU acceleration via CUDA and OpenCL (single GPU in Free, multi-GPU in paid editions)."
web_viewer = "Product exports HTML (WebGL) web viewer and offers direct upload to the Sketchfab web viewer for online sharing."
measurements = "Place control points and measure distances, areas, and volumes in the viewer."
volume = "Compute volume of a full mesh or volume projected on a plane."
veg_indices = "Creates index maps including NDVI (R, G, B, NIR, RE) with customizable vegetation indexes; export to GeoTIFF."
classification = "AI Classification for point cloud segmentation and Ground Extraction filter (ground vs non-ground) on point clouds and meshes."
+++

3DF Zephyr is a photogrammetry and 3D reconstruction desktop application developed by 3Dflow SRL, based in Verona, Italy. It reconstructs 3D models from photographs and video frames using a Structure from Motion pipeline followed by dense point cloud generation, mesh extraction and texturing. It is distributed in several editions: a Free edition limited to 50 photos or video frames and a single GPU, a Lite perpetual edition (199 EUR + VAT), and a Professional edition available monthly (250 EUR + VAT/month) or as a perpetual license (4,200 EUR + VAT). Perpetual licenses include 12 months of updates with an optional 20%-per-year renewal.

The Professional edition adds geospatial and survey capabilities, including orthophoto/orthomosaic and DEM generation with elevation profiles, DXF contour lines and sections, alignment to Ground Control Points, 3D metric measurements of distances and areas, and volume computation for full meshes, planar projections and hollow structures such as tunnels or sewers. It supports multispectral cameras with a radiometric calibration wizard, a Ground Extraction filter and an AI point cloud classification tool, a point cloud comparison tool, and automation through Python scripting and XML-based batch processing. Native laser scan formats (.fls, .rdbx, .zfs, .dp) are supported in Professional, which also bundles the 3DF Scarlet laser scan registration software, while Free and Lite offer viewer-only access.

The vendor documents drone/UAV and RTK workflows in its tutorial library and shows example projects spanning cultural heritage and archaeology, UAV mapping of mining sites and factories, vertical structures such as telecommunication towers and aqueducts, close-range objects and underwater subjects. Processing runs on the desktop with multi-GPU acceleration (NVIDIA CUDA, AMD and Intel OpenCL), and results can be exported in a broad set of mesh and point cloud formats or uploaded to services such as Sketchfab.
