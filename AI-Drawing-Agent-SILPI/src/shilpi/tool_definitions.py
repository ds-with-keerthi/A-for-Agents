
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "draw_rectangle",
            "description": "Draw a rectangle on the canvas.",
            "parameters": {
                "type": "object",
                "properties": {
                    "x": {"type": "number"},
                    "y": {"type": "number"},
                    "width": {"type": "number"},
                    "height": {"type": "number"},
                    "color": {"type": "string"}
                },
                "required": ["x", "y", "width", "height", "color"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "draw_circle",
            "description": "Draw a circle on the canvas.",
            "parameters": {
                "type": "object",
                "properties": {
                    "x": {"type": "number"},
                    "y": {"type": "number"},
                    "radius": {"type": "number"},
                    "color": {"type": "string"}
                },
                "required": ["x", "y", "radius", "color"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "draw_triangle",
            "description": "Draw a triangle using three coordinate points.",
            "parameters": {
                "type": "object",
                "properties": {
                    "points": {
                        "type": "array",
                        "items": {
                            "type": "array",
                            "items": {"type": "number"}
                        }
                    },
                    "color": {"type": "string"}
                },
                "required": ["points", "color"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "draw_line",
            "description": "Draw a line using two coordinate points.",
            "parameters": {
                "type": "object",
                "properties": {
                    "points": {
                        "type": "array",
                        "items": {
                            "type": "array",
                            "items": {"type": "number"}
                        }
                    },
                    "color": {"type": "string"}
                },
                "required": ["points", "color"]
            }
        }
    }
]
