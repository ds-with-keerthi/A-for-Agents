
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
from schemas import (
    RectangleArguments,
    CircleArguments,
    TriangleArguments,
    LineArguments
)

# Create drawing canvas
fig, ax = plt.subplots(figsize=(8, 6))

ax.set_xlim(0, 500)
ax.set_ylim(0, 400)
ax.set_aspect("equal")

# def rect(x,y,w,h,c):

def draw_rectangle(
    x: float,
    y: float,
    width: float,
    height: float,
    color: str
) -> str:

    shape = Rectangle(
        (x, y),
        width,
        height,
        facecolor=color,
        edgecolor="black"
    )

    ax.add_patch(shape)
    return f"Drew a {color} rectangle."


def draw_circle(
    x: float,
    y: float,
    radius: float,
    color: str
) -> str:

    shape = Circle(
        (x, y),
        radius,
        facecolor=color,
        edgecolor="black"
    )

    ax.add_patch(shape)
    return f"Drew a {color} circle."


def draw_triangle(
    points: list[list[float]],
    color: str
) -> str:

    shape = Polygon(
        points,
        closed=True,
        facecolor=color,
        edgecolor="black"
    )

    ax.add_patch(shape)
    return f"Drew a {color} triangle."


def draw_line(
    points: list[list[float]],
    color: str
) -> str:

    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    ax.plot(
        x_values,
        y_values,
        color=color,
        linewidth=2
    )

    return f"Drew a {color} line."


def reset_canvas() -> None:
    ax.clear()
    ax.set_xlim(0, 500)
    ax.set_ylim(0, 400)
    ax.set_aspect("equal")


def show_drawing() -> None:
    ax.set_title("Silpi Drawing")
    plt.savefig("silpi_output.png", dpi=150, bbox_inches="tight")
    plt.show()

def validate_arguments(tool_name: str, arguments: dict):

    schema_registry = {
        "draw_rectangle": RectangleArguments,
        "draw_circle": CircleArguments,
        "draw_triangle": TriangleArguments,
        "draw_line": LineArguments
    }

    schema = schema_registry[tool_name]

    validated = schema.model_validate(arguments)

    return validated.model_dump()

# Map tool names to Python functions
TOOL_REGISTRY = {
    "draw_rectangle": draw_rectangle,
    "draw_circle": draw_circle,
    "draw_triangle": draw_triangle,
    "draw_line": draw_line
}

# Map tool names to Pydantic models
SCHEMA_REGISTRY = {
    "draw_rectangle": RectangleArguments,
    "draw_circle": CircleArguments,
    "draw_triangle": TriangleArguments,
    "draw_line": LineArguments
}

def execute_tool(tool_call: dict) -> str:

    function_name = tool_call["function"]["name"]
    arguments = tool_call["function"]["arguments"]

    try:
        schema = SCHEMA_REGISTRY[function_name]
        validated = schema.model_validate(arguments)

        function = TOOL_REGISTRY[function_name]

        return function(**validated.model_dump())

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":

    reset_canvas()

    tool_call = {
        "function": {
            "name": "draw_rectangle",
            "arguments": {
                "x": 100,
                "y": 150,
                "width": 200,
                "height": 100,
                "color": "blue"
            }
        }
    }

    result = execute_tool(tool_call)
    print(result)

    show_drawing()

    # arguments = {
    #     "x": 100,
    #     "y": 150,
    #     "width": 200,
    #     "height": 100,
    #     "color": "blue"
    # }

    # validated_args = validate_arguments("draw_rectangle", arguments)

    # draw_rectangle(**validated_args)

    # draw_circle(250, 250, 50, "purple")

    # draw_triangle(
    #     [[100, 200], [200, 350], [300, 200]],
    #     "orange"
    # )

    # show_drawing()
