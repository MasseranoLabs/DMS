+++
title = "KIRI Engine"
description = "Mobile and web 3D scanning app converting photos, video, or device LiDAR into textured meshes, point clouds, and Gaussian splats via cloud processing."
weight = 25

[extra]
summary = "KIRI Engine is a cloud-based 3D scanning application for iOS, Android, and web that reconstructs objects and scenes from photos, video, or device LiDAR into textured meshes, point clouds, and 3D Gaussian splats."
developer = "KIRI Innovations"
country = "unknown"
license = "Proprietary (freemium)"
open_source = false
price_model = "Freemium with subscription (free tier plus paid Pro plan); separate credit-based pricing for the API"
price_detail = "Free (Basic) plan: up to 150 photos per scan, 2 GB max file size, unlimited scans and exports, no ads. Pro plan: $17.99/month or $79.99/year, adding Featureless Object Scan, Mesh-Inclusive 3DGS, PBR material maps, quad-mesh retopology, auto-rigging, 500 photos per scan and 5 GB max. API: credit system priced at $1 per credit, 1 credit per call, minimum recharge 500 credits, 10 free credits for new users; in a testing phase."
platforms = [
  "iOS / iPadOS",
  "Android",
  "Web browser",
]
deployment = [
  "Vendor cloud processing (uploads processed on KIRI servers)",
  "Mobile apps (iOS, Android)",
  "Web application",
  "REST API (cloud)",
]
primary_outputs = [
  "Point cloud",
  "3D mesh",
  "Gaussian splats",
]
target_use_cases = [
  "Film, VFX & games",
  "Research & education",
]
latest_version = "unknown"
first_release_year = "unknown"
official_url = "https://www.kiriengine.app"
key_features = [
  "Photo Scan photogrammetry that reconstructs 3D mesh and textures from photos",
  "LiDAR Scan using compatible iOS device sensors for room, scene, and object capture",
  "Featureless Object Scan (NeRF-derived) for reflective, shiny, or transparent objects (Pro)",
  "3D Gaussian Splatting (3DGS) with mesh export (Pro)",
  "Export to OBJ, FBX, STL, GLB, GLTF, USDZ, PLY, and XYZ",
  "PBR material maps (albedo, roughness, normal, displacement) (Pro)",
  "Quad-mesh retopology and decimation with adjustable poly counts and up to 8K textures",
  "Automatic AI rigging for animation (Pro)",
  "In-app editing tools for cropping and texturing",
  "RESTful cloud API for programmatic scan creation and retrieval",
]
pros = [
  "Available across iOS/iPadOS, Android, and web browser",
  "Free tier provides unlimited scans and exports without ads or export restrictions (per the pricing page)",
  "Multiple capture methods: photogrammetry, device LiDAR, Featureless Object Scan, and 3D Gaussian Splatting",
  "Wide range of export formats including mesh (OBJ, FBX, STL, GLB, GLTF, USDZ) and point cloud (PLY, XYZ)",
  "RESTful cloud API for integrating scanning into external applications",
  "Advanced mesh outputs including PBR materials, quad retopology, and auto-rigging on the Pro plan",
]
cons = [
  "Several capabilities (Featureless Object Scan, Mesh-Inclusive 3DGS, PBR maps, quad retopology, auto-rigging) require the paid Pro plan",
  "Free plan is capped at 150 photos per scan and a 2 GB file size (per the pricing page)",
  "The API on the vendor site as being in a testing phase with pricing subject to change",
  "Scan processing is cloud-based (uploads required), and LiDAR scanning requires a compatible iOS device",
]
typical_workflow = [
  "Capture an object or scene with photos, video, or a compatible iOS device's LiDAR sensor (or supply a photoset/video via the API)",
  "Upload the capture to KIRI's cloud servers for processing",
  "The service reconstructs a 3D model using the selected scan method (Photo Scan, Featureless, LiDAR, or 3DGS)",
  "Edit the result with in-app tools (crop, texture, decimate, retopologize)",
  "Export the model in a chosen format such as OBJ, FBX, GLB, USDZ, PLY, or XYZ",
]
sources = [
  "https://www.kiriengine.app",
  "https://www.kiriengine.app/features/photo-scan",
  "https://www.kiriengine.app/features/lidar-scan",
  "https://www.kiriengine.app/features/3d-gaussian-splatting",
  "https://www.kiriengine.app/features",
]

[extra.features]
image_input = "yes"
multispectral = "unknown"
thermal = "unknown"
lidar = "yes"
video = "unknown"
gcp = "unknown"
rtk_ppk = "unknown"
accuracy_report = "unknown"
coordinate_systems = "unknown"
orthomosaic = "unknown"
dsm = "unknown"
dtm = "unknown"
point_cloud = "unknown"
mesh_3d = "yes"
contours = "unknown"
tiles_3d = "unknown"
gaussian_splatting = "yes"
cad_export = "unknown"
desktop = "unknown"
cloud = "yes"
self_hosted = "unknown"
api = "yes"
gpu = "unknown"
web_viewer = "yes"
flight_planning = "unknown"
measurements = "yes"
volume = "unknown"
veg_indices = "unknown"
change_detection = "unknown"
classification = "unknown"
annotations = "unknown"

[extra.feature_notes]
image_input = "Confirmed via the special-case rule:. Reconstruction from unstructured/unordered image sets. This is object/scene capture, not aerial nadir imagery per se."
lidar = "Uses the built-in LiDAR sensor of iPhone/iPad Pro devices for on-device Room Scan and Object Capture; mobile scanning, not aerial LiDAR point clouds."
gaussian_splatting = "Native 3DGS generation with PLY export; optional 3DGS-to-mesh conversion and 3DGS masking/editing tools."
cloud = "Server-side cloud processing for Photo Scan and AI enhancement of LiDAR data."
api = "Documented RESTful API (docs.kiriengine.app) with API keys, webhooks, and credit-based balance; covers Photo Scan, Featureless Object Scan, and 3DGS scan endpoints."
web_viewer = "Web application platform; 3D Gaussian Splatting real-time rendering is accessible in the browser."
measurements = "LiDAR Room Scan generates layout/dimensions and an exportable floor plan with detailed measurements."
+++

KIRI Engine is a 3D scanning application developed by KIRI Innovations and available on iOS/iPadOS, Android, and through a web browser. It captures real-world objects and spaces and reconstructs them into 3D digital models using several methods: Photo Scan (photogrammetry), LiDAR Scan on compatible iOS devices, Featureless Object Scan (a NeRF-derived technique for reflective or transparent items), and 3D Gaussian Splatting with mesh export. Processing is performed on KIRI's cloud servers.

Outputs center on textured 3D meshes and point clouds, with export to OBJ, FBX, STL, GLB, GLTF, USDZ, PLY, and XYZ. Higher-end outputs on the Pro plan include PBR material maps, quad-mesh retopology with adjustable polygon counts and textures up to 8K, and automatic rigging. The product is offered under a freemium model: a free Basic plan (up to 150 photos per scan, 2 GB file size, unlimited scans and exports) and a Pro plan at $17.99/month or $79.99/year that raises limits and unlocks the advanced scan and mesh features.

KIRI Engine also provides a RESTful cloud API (docs.kiriengine.app) that lets developers create and retrieve scan tasks programmatically for Photo Scan, Featureless Object Scan, and 3DGS-with-mesh. The API uses a credit system priced at $1 per credit with a 500-credit minimum recharge and 10 free credits for new users, and it is in a testing phase. The product is oriented toward object and scene capture for uses such as game and 3D asset creation, 3D printing, and research/spatial documentation rather than aerial or survey mapping; no drone/aerial mapping, orthomosaic, DSM/DTM, GCP, RTK/PPK, multispectral, or thermal capabilities are available.
