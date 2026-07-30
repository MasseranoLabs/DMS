+++
title = "Polycam"
description = "Cloud-based 3D scanning and drone mapping app that builds 3D models, point clouds, and floor plans from phone, LiDAR, and drone imagery."
weight = 26

[extra]
summary = "Polycam is a cross-platform reality-capture app that turns phone/tablet LiDAR scans and photogrammetry (including drone photos and video) into 3D meshes, point clouds, and floor plans, with cloud-based drone mapping."
developer = "Polycam"
license = "Proprietary (freemium)"
open_source = false
price_model = "Freemium subscription"
price_detail = "Free tier ($0, GLTF export only). Basic: $150/year (billed yearly, $12.50/month) or $30/month monthly. Business: $400/year per user (billed yearly, $34/month per user), adds 2D & 3D floor plans and advanced measure tools. Enterprise: contact for pricing. A capture API is referenced as \"Contact us.\" (pricing page)"
platforms = [
  "iOS",
  "Android",
  "Web",
  "Apple Vision Pro",
]
deployment = [
  "Cloud (vendor-hosted)",
]
primary_outputs = [
  "Point cloud",
  "3D mesh",
  "Gaussian splats",
  "Floor plans",
]
target_use_cases = [
  "Surveying & mapping",
  "Construction",
  "Inspection & infrastructure",
  "Public safety & emergency response",
]
official_url = "https://poly.cam"
key_features = [
  "Drone mapping: upload drone photos or video to the web and process with 1-click, then view, measure, and edit the resulting 3D model (drone-mapping page)",
  "Accepts PNG, JPG, MP4, MOV, AVI, and M4V files from most commercial-grade drones (drone-mapping page)",
  "Photogrammetry from drone photos/video with a stated minimum of 60 photos or 1-minute video (drone-photogrammetry tool page)",
  "LiDAR scanning on supported iPhone/iPad Pro devices; previously created LiDAR scans can be uploaded for viewing and editing (3d-lidar-scanner page)",
  "Gaussian splat and object/space capture modes",
  "2D & 3D floor plan generation (Business tier)",
  "In-model measurements and advanced measure tools (Business tier)",
  "Export to 12+ formats including GLTF, OBJ, FBX, DAE, STL, USDZ (mesh) and PLY, LAS, DXF and geo-referenced LAS (point cloud)",
  "Compatibility with SketchUp, AutoCAD, Revit, Blender, Unity, and Unreal Engine",
]
pros = [
  "Cloud processing with a simple upload-and-1-click workflow, no software download required for drone processing (drone-mapping page)",
  "Accepts both drone photos and video in several common formats (drone-mapping page)",
  "Runs across iOS, Android, web, and Apple Vision Pro",
  "Wide range of export formats (12+) spanning mesh and point cloud types for use in CAD, DCC, and game-engine tools",
  "Geo-referenced LAS point cloud export is supported (help center: Geo LAS to CloudCompare)",
  "In-viewer measurement tools included on paid tiers",
]
cons = [
  "Free tier is limited to GLTF export only; other formats require a paid plan (pricing page)",
  "Point cloud exports (LAS, PLY, DXF) require a Business or higher plan (pricing/help center)",
  "Floor plans and advanced measure tools require the Business tier or higher (pricing page)",
  "Per-capture image limits apply by plan (300 images on Basic, 2000 on Business) (pricing page)",
  "Drone data processing is offered only through vendor-hosted cloud processing (drone-mapping page)",
]
typical_workflow = [
  "Capture aerial imagery with a commercial-grade drone as photos or video (aim for high overlap, around 80% per the drone photogrammetry guidance)",
  "Upload the drone photos or video to Polycam on the web",
  "Process the data into a 3D model with 1-click cloud processing",
  "View, measure, and edit the resulting model in the browser",
  "Export the model in a chosen format (e.g., OBJ, FBX, LAS, geo-referenced LAS) into tools such as SketchUp, AutoCAD, Unity, or Blender",
]
sources = [
  "https://poly.cam",
]

[extra.features]
image_input = "yes"
multispectral = "unknown"
thermal = "unknown"
lidar = "yes"
video = "yes"
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
gaussian_splatting = "yes"
cad_export = "yes"
desktop = "unknown"
cloud = "yes"
self_hosted = "unknown"
api = "unknown"
gpu = "unknown"
web_viewer = "yes"
flight_planning = "unknown"
measurements = "yes"
volume = "unknown"
veg_indices = "unknown"
change_detection = "unknown"
classification = "unknown"
annotations = "yes"

[extra.feature_notes]
image_input = "General photogrammetry/object capture is documented as capturing a subject from different angles (walking around at different angles); not a drone-specific nadir/oblique flight spec."
lidar = "LiDAR 3D scanner is a core Polycam capture mode (requires a device with a LiDAR sensor); produces LiDAR 3D models/point clouds."
video = "Accepts video input for reconstruction (MP4, MOV, AVI, M4V)."
point_cloud = "Point cloud processing and LAS/PLY point cloud export documented; point cloud export is on Business/Enterprise tiers."
mesh_3d = "Textured 3D mesh with photorealistic textures is the standard output."
gaussian_splatting = "The vendor-owned page https://poly.cam/gaussian-splatting explicitly states Polycam generates, edits, exports, and views 3D Gaussian Splats. Quoted text includes \\\"You can create a Gaussian Splatting reconstruction right on this page,\\\" a \\\"Fully featured suite of splat editing tools,\\\" ability to download \\\"mesh for any Gaussian Splat,\\\" and a library to view existing splats. Note: WebSearch budget was"
cad_export = "Exports DXF and is AutoCAD/CAD/BIM compatible (DXF listed among drone photogrammetry export formats)."
cloud = "Cloud/web-hosted processing; upload drone data to the web and process with one click."
web_viewer = "Browser-based collaborative viewer/sharing of 3D models across devices."
measurements = "In-app measurements documented (view, measure, edit); automated measurements and reports tied to Business/Enterprise floor-plan features."
annotations = "Comment and annotation tools on 3D models documented."
+++

Polycam is a reality-capture product from the company Polycam that creates 3D models from several input types, including LiDAR scans on supported iPhone/iPad Pro devices, photogrammetry from ordinary photos, Gaussian splats, and 360 images. It runs on iOS, Android, the web, and Apple Vision Pro, and lets users capture, edit, and export models on-device or in the browser.

For drone mapping, Polycam accepts photos or video from most commercial-grade drones in PNG, JPG, MP4, MOV, AVI, and M4V formats. Data is uploaded to the web and processed with a 1-click, cloud-based workflow that requires no downloaded software. The resulting 3D model can be viewed, measured, and edited, and the vendor positions this for uses such as construction site monitoring and surveying.

Outputs and features vary by subscription tier. The free tier exports only GLTF; paid tiers unlock mesh formats (OBJ, FBX, DAE, STL, USDZ), point cloud formats (PLY, LAS, DXF, and geo-referenced LAS), 2D & 3D floor plans, and advanced measure tools. Exported files are documented as compatible with tools including SketchUp, AutoCAD, Revit, Blender, Unity, and Unreal Engine. A capture API is referenced on the pricing page under a contact request.
