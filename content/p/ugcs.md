+++
title = "UgCS"
description = "Desktop drone flight and mission planning software for photogrammetry, LiDAR and sensor surveys, with terrain following and 3D route preview."
weight = 21

[extra]
summary = "UgCS is desktop drone flight and mission planning software by SPH Engineering, used to plan photogrammetry, LiDAR, and multi-sensor surveys with 3D terrain-following route design; it plans data acquisition rather than processing imagery into map products."
developer = "SPH Engineering"
country = "Latvia"
license = "Proprietary (freemium)"
open_source = false
price_model = "Freemium: a free tier (UgCS Open) plus paid editions offered as both subscription and perpetual licenses"
price_detail = "Free UgCS Open tier with daily limits (up to 2 route uploads/exports per day, routes limited to 250 m between furthest points, max 2 concurrent projects). Paid editions per the shop license page: PRO ($109/month or $1,090 perpetual), EXPERT ($189/month or $1,890 perpetual), ENTERPRISE ($279/month or $2,790 perpetual); perpetual licenses include the first year of support and require an annual Support & Update pack from the second year for continued updates and support."
platforms = [
  "Windows",
  "macOS",
]
deployment = [
  "Desktop application (Windows, macOS)",
  "Self-hosted / server (multi-node) deployment in the ENTERPRISE edition",
]
primary_outputs = [
]
target_use_cases = [
  "Surveying & mapping",
  "Mining & aggregates",
  "Inspection & infrastructure",
  "Public safety & emergency response",
  "Research & education",
]
latest_version = "unknown"
first_release_year = "unknown"
official_url = "https://www.ugcs.com"
key_features = [
  "Desktop mission planning with full-screen 3D mission preview, elevation profiles and multi-segment routes",
  "Terrain following using custom DEM/DSM import to hold altitude above ground level",
  "Photogrammetry and area-scan mapping grids for survey planning",
  "LiDAR-specific planning tools (figure-8 IMU calibration, automated loop turns, scan pattern control) in EXPERT and ENTERPRISE editions",
  "Support for 100+ drone platforms including DJI, Autel, Freefly, ArduPilot, PX4 and NDAA-compliant drones",
  "Offline operation with cached maps and elevation data",
  "KML/CSV coordinate import/export",
  "Mission sync to DJI controllers via UgCS Cloud sync with DJI Pilot 2",
  "Multi-drone operation (up to 10 simultaneous connections), live video streaming, centralized mission sharing and SDK access in the ENTERPRISE edition",
]
pros = [
  "Terrain-following planning with custom DEM/DSM import for consistent above-ground-level altitude",
  "Broad hardware support across 100+ drone platforms and multiple sensor/LiDAR manufacturers",
  "Dedicated LiDAR mission tools in the EXPERT and ENTERPRISE editions",
  "Works offline with cached maps and elevation data for remote sites",
  "Free UgCS Open tier for evaluation, learning and academic use",
  "Flexible licensing with both subscription and perpetual options across PRO, EXPERT and ENTERPRISE tiers",
]
cons = [
  "The free UgCS Open tier is limited to 2 route uploads/exports per day, routes no longer than 250 m between the furthest points, and no more than 2 concurrent projects",
  "LiDAR toolset and DSM support require the EXPERT edition, while multi-drone operation, live video streaming, SDK access and server deployment require the ENTERPRISE edition",
  "Perpetual licenses require purchasing an annual Support & Update pack from the second year to keep receiving updates and support",
  "The vendor describes UgCS as flight/mission planning software and offers a separate product (GeoHammer) for multi-sensor data processing, so imagery-to-map processing is not documented as part of UgCS itself",
]
typical_workflow = [
  "Define the survey area and import terrain data (custom DEM/DSM) or use cached elevation data",
  "Select a survey/mission type (photogrammetry mapping grid, LiDAR scan, corridor, vertical scan, etc.) and set parameters such as altitude/AGL and scan pattern",
  "Preview the route in full-screen 3D against terrain, elevation profile and obstacles, adjusting for battery range and adding battery-swap waypoints",
  "Upload or sync the mission to the drone controller (for example via UgCS Cloud sync with DJI Pilot 2) or fly directly",
  "Execute the flight, including offline in areas without connectivity",
  "Process the captured imagery or sensor data in separate photogrammetry/GIS software",
]
sources = [
  "https://www.ugcs.com",
]

[extra.features]
image_input = "yes"
multispectral = "yes"
thermal = "unknown"
lidar = "unknown"
video = "yes"
gcp = "unknown"
rtk_ppk = "unknown"
accuracy_report = "unknown"
coordinate_systems = "unknown"
orthomosaic = "yes"
dsm = "yes"
dtm = "unknown"
point_cloud = "unknown"
mesh_3d = "unknown"
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
flight_planning = "yes"
measurements = "yes"
volume = "unknown"
veg_indices = "yes"
change_detection = "unknown"
classification = "unknown"
annotations = "yes"

[extra.feature_notes]
image_input = "UgCS Mapper stitches georeferenced aerial JPG images into an orthomosaic (nadir/top-down mapping imagery). No explicit oblique/3D reconstruction is documented."
multispectral = "UgCS Mapper stitches multispectral 3-channel RGN JPEG images (e.g., Micasense RedEdge-M / RedEdge-MX)."
video = "UgCS Mapper does 'Video orthophoto processing' (video frames turned into maps); UgCS Enterprise also supports a live geotagged video stream."
orthomosaic = "Produced by UgCS Mapper, a UgCS-branded desktop image/video processing tool: 'Stitch multispectral and any other aerial drone images into one orthomosaic.'"
dsm = "UgCS Mapper 'Generate DSM/elevation data from georeferenced JPG images'; UgCS planning also imports DEM/DTM/DSM layers for terrain following (import, not generation)."
desktop = "Both UgCS ('installs locally, works offline') and the UgCS Mapper processing tool are desktop apps (UgCS Mapper runs on Windows, macOS, Ubuntu)."
api = "UgCS Mapper provides a documented command line interface for automation. The UgCS planning app itself does not document an API/SDK."
flight_planning = "Core UgCS function: 3D mission/flight planning with terrain following, area scan, photogrammetry tool, corridor/vertical scan, and LiDAR mission planning (sphengineering.com/flight-planning/ugcs)."
measurements = "UgCS flight-planning interface includes documented 'Measurement tools'."
veg_indices = "UgCS Mapper generates NDVI indexes from multispectral RGN images."
annotations = "UgCS supports placemarks and placemark layers on the map ('Work with placemarks', 'Placemark layers')."
+++

UgCS (Universal Ground Control Software) is a desktop drone flight and mission planning application developed by SPH Engineering, a company based in Latvia (EU) and the USA that has worked on drone applications since 2013. The vendor positions UgCS as flight planning and control software: users design missions with a full-screen 3D preview, elevation profiles and multi-segment routes before flying, rather than processing captured imagery into map products.

The software supports planning for a range of survey types, including nadir and oblique photogrammetry mapping grids, LiDAR missions (with tools such as figure-8 IMU calibration, automated loop turns and scan pattern control), corridor and vertical scans, and geophysical/multi-sensor surveys via the SkyHub onboard computer. It offers terrain following through custom DEM/DSM import to hold altitude above ground level, supports more than 100 drone platforms (including DJI, Autel, Freefly, ArduPilot, PX4 and NDAA-compliant drones), and can operate offline using cached maps and elevation data. Missions can be synced to DJI controllers through UgCS Cloud sync with DJI Pilot 2.

UgCS is available in a free UgCS Open tier (limited to 2 route uploads/exports per day, 250 m between the furthest route points and 2 concurrent projects) and paid PRO, EXPERT and ENTERPRISE editions offered as monthly/yearly subscriptions or perpetual licenses. Higher tiers add capabilities such as the advanced LiDAR toolset and DSM support (EXPERT) and multi-drone operation, live video streaming, centralized mission sharing, SDK access and server/multi-node deployment (ENTERPRISE).
