# random-points-on-polygon

A simple Python library based on [Shapely](https://github.com/shapely/shapely) to generate random points on Polygon or MultiPolygon

## Installation

From [PyPI](https://pypi.org/project/random-points-on-polygon/) directly:

```
pip install random-points-on-polygon
```
## Graphically view the result
You can copy and paste the ```geojson_output``` content into [geojson.io](https://geojson.io) to graphically view the result

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

![geojson](https://github.com/maurosaladini/random-points-on-polygon/blob/main/geojson.png?raw=true)

Get generated points as GeoJSON
```python
geojson_output: dict = pg.points_as_geojson()
```

Get Polygon (or MultiPolygon) as GeoJSON
```python
geojson_output: dict = pg.polygon_as_geojson()
```






