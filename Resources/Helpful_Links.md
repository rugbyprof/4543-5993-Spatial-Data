# 🌍 Spatial Mapping Toolbox

_A curated list of websites, tools, and libraries for formatting, visualizing, validating, and serving spatial data_

This handout collects **low-friction, browser-based tools** alongside **real-world mapping libraries** you can grow into over the semester. The idea is simple:

> **Lets you see data early, break it safely, fix it visually, then serve it like professionals.**

---

## 🎯 Teaching Philosophy (aka: Why this list exists)

- Visual feedback reduces fear
- GeoJSON makes data _tangible_
- APIs connect theory to reality
- Mapping is the reward 🎉

---

## 🧪 JSON & GeoJSON Formatting / Validation

These tools are lifesavers when students are learning JSON-based spatial formats.

- **geojson.io**
  [https://geojson.io](https://geojson.io)
  - ✔ Edit, draw, and visualize GeoJSON
  - ✔ Drag-and-drop support
  - ✔ Export clean GeoJSON

  > _This is the “whiteboard” of spatial data._

- **JSON Formatter & Validator**
  [https://jsonformatter.org](https://jsonformatter.org)
  - ✔ Pretty-print JSON
  - ✔ Tree view for nested structures
  - ✔ Syntax validation

- **JSONLint**
  [https://jsonlint.com](https://jsonlint.com)
  - ✔ Fast error detection
  - ✔ Great for debugging malformed files

- **GeoJSON Lint**
  [https://geojsonlint.com](https://geojsonlint.com)
  - ✔ GeoJSON-specific validation
  - ✔ Catches subtle geometry issues

---

## 🗺️ Quick Visualization & Exploration Tools (No Coding)

Perfect for demos, labs, and sanity-checks.

- **uMap (OpenStreetMap based)**
  [https://umap.openstreetmap.fr](https://umap.openstreetmap.fr)
  - ✔ Upload GeoJSON / CSV
  - ✔ Style layers visually
  - ✔ Share maps with URLs

- **Kepler.gl**
  [https://kepler.gl](https://kepler.gl)
  - ✔ Handles large datasets
  - ✔ Heatmaps, clustering, animations
  - ✔ Excellent for movement data

- **CARTO Builder**
  [https://carto.com](https://carto.com)
  - ✔ Interactive web GIS
  - ✔ SQL-like querying
  - ✔ Choropleths & point maps

- **Flowmap.blue**
  [https://flowmap.blue](https://flowmap.blue)
  - ✔ Origin-destination flow maps
  - ✔ Excellent for migration & traffic data

---

## 🧠 Desktop / Power Tools (Open Source)

These are _industry-grade_ and worth exposure.

- **QGIS**
  [https://qgis.org](https://qgis.org)
  - ✔ Full GIS stack
  - ✔ Vector + raster
  - ✔ CRS transformations
  - ✔ Export to GeoJSON & web formats

  > _This is the Swiss Army knife._

- **GDAL / OGR utilities**
  [https://gdal.org](https://gdal.org)
  - ✔ Convert formats
  - ✔ Reproject data
  - ✔ Command-line friendly

---

## 🌐 JavaScript Mapping Libraries (Frontend)

These are ideal when students start **building interactive maps**.

### Beginner-Friendly

- **Leaflet**
  [https://leafletjs.com](https://leafletjs.com)
  - ✔ Lightweight
  - ✔ Easy GeoJSON integration
  - ✔ Massive plugin ecosystem

  > _Best first mapping library. Period._

- **MapLibre GL JS**
  [https://maplibre.org](https://maplibre.org)
  - ✔ Open-source vector maps
  - ✔ Successor to Mapbox GL JS
  - ✔ Smooth zooming & styling

### Intermediate / Professional

- **Mapbox GL JS**
  [https://docs.mapbox.com/mapbox-gl-js](https://docs.mapbox.com/mapbox-gl-js)
  - ✔ Beautiful vector maps
  - ✔ APIs for routing, geocoding
    ⚠ Requires API keys (freemium)

- **OpenLayers**
  [https://openlayers.org](https://openlayers.org)
  - ✔ GIS-heavy
  - ✔ Supports projections & OGC services
  - ✔ More complex, very powerful

### Advanced / Visualization-Heavy

- **deck.gl**
  [https://deck.gl](https://deck.gl)
  - ✔ High-performance WebGL
  - ✔ Massive datasets
  - ✔ Works well with Mapbox / MapLibre

- **CesiumJS**
  [https://cesium.com/platform/cesiumjs](https://cesium.com/platform/cesiumjs)
  - ✔ 3D globe & terrain
  - ✔ Satellite & elevation data
  - ✔ Fantastic for Earth-scale visualization

---

## 📐 Geometry & Spatial Analysis (Client or Server)

- **Turf.js**
  [https://turfjs.org](https://turfjs.org)
  - ✔ Buffers, intersections, centroids
  - ✔ Runs in browser or backend
  - ✔ Excellent teaching tool for geometry ops

- **TopoJSON**
  [https://github.com/topojson/topojson](https://github.com/topojson/topojson)
  - ✔ Smaller than GeoJSON
  - ✔ Teaches simplification & shared boundaries

---

## 📡 Backend & API-Friendly Tools (Serving Maps)

Great for **“build an API → hit it from a map”** assignments.

### Python

- **Flask** – [https://flask.palletsprojects.com](https://flask.palletsprojects.com)

- **FastAPI** – [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com)
  - ✔ Auto-docs
  - ✔ JSON schema validation
  - ✔ Excellent for GeoJSON endpoints

- **GeoPandas**
  [https://geopandas.org](https://geopandas.org)
  - ✔ Pandas + geometry
  - ✔ Easy GeoJSON export

### Databases & Servers

- **PostGIS**
  [https://postgis.net](https://postgis.net)
  - ✔ Spatial SQL
  - ✔ Industry standard

- **GeoServer**
  [https://geoserver.org](https://geoserver.org)
  - ✔ WMS / WFS services
  - ✔ Heavy-duty GIS backend

---
