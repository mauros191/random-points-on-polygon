import json
import random
from shapely.geometry import mapping, MultiPolygon, Point, Polygon
from typing import List, Union


class PointsGenerator:
    """Generate random points on a Polygon/MultiPolygon

    Attributes:
        geometry: A Polygon/MultiPolygon
        points: List of random points on polygon
    """

    __slots__ = ["geometry", "points", "min_x", "max_x", "min_y", "max_y"]

    def __init__(self, geometry: Union[Polygon, MultiPolygon]) -> None:
        """Inits PointsGenerator with a Polygon/MultiPolygon"""
        if type(geometry) not in [Polygon, MultiPolygon]:
            raise TypeError("geometry must be a Polygon or a MultiPolygon")

        self.geometry: Union[Polygon, MultiPolygon] = geometry
        self.points: List[Point] = []
        self.min_x, self.min_y, self.max_x, self.max_y = geometry.bounds

    @staticmethod
    def geojson_boilerplate() -> dict:
        return {"type": "FeatureCollection", "features": []}

    def reset(self) -> None:
        """Reset the list of generated points"""
        self.points.clear()

    def generate(self, n: int) -> None:
        """Generate n random points on geometry

        Args:
                n: number of points to generate
        """
        if type(n) is not int:
            raise TypeError("n must be an integer.")
        if n <= 0:
            raise ValueError(f"n must be at least 1, not {n}.")

        while n > 0:
            random_point: Point = Point(
                random.uniform(self.min_x, self.max_x),
                random.uniform(self.min_y, self.max_y),
            )
            if random_point.within(self.geometry):
                self.points.append(random_point)
                n -= 1

    def add_feature(self, geojson_: dict, feature: Union[MultiPolygon, Point, Polygon]) -> None:
        geojson_["features"].append(
            {"type": "Feature", "properties": {}, "geometry": mapping(feature)}
        )

    def polygon_as_geojson(self) -> str:
        """Get Polygon (or MultiPolygon) without generated points as GeoJSON"""
        geojson: dict = PointsGenerator.geojson_boilerplate()
        self.add_feature(geojson, self.geometry)
        return json.dumps(geojson, indent=2)

    def points_as_geojson(self) -> str:
        """Get generated points as GeoJSON"""
        geojson: dict = PointsGenerator.geojson_boilerplate()
        for point in self.points:
            self.add_feature(geojson, point)
        return json.dumps(geojson, indent=2)

    def geojson(self) -> str:
        """Get Polygon (or MultiPolygon) including generated points as GeoJSON"""
        geojson: dict = PointsGenerator.geojson_boilerplate()
        self.add_feature(geojson, self.geometry)
        for point in self.points:
            self.add_feature(geojson, point)
        return json.dumps(geojson, indent=2)
