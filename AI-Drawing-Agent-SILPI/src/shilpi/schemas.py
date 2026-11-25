
from pydantic import BaseModel, Field


class RectangleArguments(BaseModel):
    x: float
    y: float
    width: float = Field(gt=0)
    height: float = Field(gt=0)
    color: str


class CircleArguments(BaseModel):
    x: float
    y: float
    radius: float = Field(gt=0)
    color: str


class TriangleArguments(BaseModel):
    points: list[list[float]] = Field(min_length=3)
    color: str


class LineArguments(BaseModel):
    points: list[list[float]] = Field(min_length=2)
    color: str
