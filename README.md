# random-points-on-polygon

A simple Python library based on [Shapely](https://github.com/shapely/shapely) to generate random points on Polygon or MultiPolygon

## Installation

From [PyPI](https://pypi.org/project/random-points-on-polygon/) directly:

```
pip install random-points-on-polygon
```

## Examples

Generate 50 points on Polygon POLYGON_SAMPLE_2
```python
from random_points_on_polygon import PointsGenerator
from random_points_on_polygon.samples import POLYGON_SAMPLE_2

pg: PointsGenerator = PointsGenerator(POLYGON_SAMPLE_2)
pg.generate(50)
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

## Show the result
You can copy and paste the content of ```geojson_output``` in [geojson.io](geojson.io) to show the result





