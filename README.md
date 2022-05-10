# random-points-on-polygon

A simple Python library based on [Shapely](https://github.com/shapely/shapely) to generate random points on Polygon or MultiPolygon

## Installation

From [PyPI](https://pypi.org/project/random-points-on-polygon/) directly:

```
pip install random-points-on-polygon
```
## Examples

Generate 10 random points on a polygon
```python
from random_points_on_polygon import PointsGenerator
from random_points_on_polygon.samples import POLYGON_SAMPLE_1

pg: PointsGenerator = PointsGenerator(POLYGON_SAMPLE_1)
pg.generate(10)
```

Get Polygon (or MultiPolygon) including generated points as GeoJSON. 
```python
geojson_output: dict = pg.geojson()
```

Get generated points as GeoJSON
```python
geojson_output: dict = pg.points_as_geojson()
```

Get Polygon (or MultiPolygon) as GeoJSON
```python
geojson_output: dict = pg.polygon_as_geojson()
```
## Display result on the map
You can copy and paste the ```geojson_output``` content into [geojson.io](https://geojson.io) to display result on the map

<img src="https://github.com/maurosaladino/random-points-on-polygon/blob/main/public/geojson.jpg?raw=true" width="450" height="487">

## Create a Polygon from GeoJSON
You can create a Polygon/MultiPolygon from GeoJSON using Shapely:

```python
from shapely.geometry import shape

POLYGON_GEOJSON = {
    "type": "Polygon",
    "coordinates": [
        [
            [-73.9932632446289, 40.737892702684064],
            [-73.9815902709961, 40.743355347975395],
            [-73.96476745605469, 40.76650157923057],
            [-73.99463653564453, 40.762341053140275],
            [-73.9932632446289, 40.737892702684064],
        ]
    ],
}

p = shape(POLYGON_GEOJSON)
```



