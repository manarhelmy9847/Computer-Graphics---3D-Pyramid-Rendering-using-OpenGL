from glumpy import app, gl, gloo, glm
from glumpy.transforms import Rotate
import numpy as np

# -----------------------------
# Shaders
# -----------------------------

# Vertex Shader
vertex_shader = """
#version 330 core
uniform vec4 u_color;
attribute vec3 position;
attribute vec4 color;
varying vec4 v_color;

void main(void){
    gl_Position = vec4(<transform(0.7 * position)>, 1.0);
    v_color = color;
}
"""

# Fragment Shader
fragment_shader = """
#version 330 core
varying vec4 v_color;

void main(void){
    gl_FragColor = v_color;
}
"""

# -----------------------------
# Window Setup
# -----------------------------

app.use("glfw")
window = app.Window(width=512, height=512, title="3D Modelling - INDEX BUFFER", color=(0.1, 0.1, 0.1, 1))

# -----------------------------
# Pyramid Geometry and Transform
# -----------------------------

# Define vertex positions (5 vertices)
vertex_positions = [
    (0, 1, 0),    # Top
    (0, 0, -1),   # Back center
    (-1, 0, 1),   # Bottom left
    (1, 0, 1),    # Bottom right
    (0, 0, -1)    # Duplicate for base triangle
]

# Define vertex colors in shades of brown
vertex_colors = [
    (0.36, 0.25, 0.20, 1.0),  # Dark brown
    (0.55, 0.27, 0.07, 1.0),  # Saddle brown
    (0.72, 0.52, 0.04, 1.0),  # Golden brown
    (0.59, 0.29, 0.0, 1.0),   # Chocolate
    (0.82, 0.71, 0.55, 1.0)   # Tan (light brown)
]

# Create shader program
pyramid = gloo.Program(vertex_shader, fragment_shader, count=len(vertex_positions))
pyramid['position'] = vertex_positions
pyramid['color'] = vertex_colors

# Add rotation transform
pyramid['transform'] = Rotate(angle=20, axis=(0.0, 1.0, 0.0))

# -----------------------------
# Index Buffer for Pyramid Faces
# -----------------------------

indices = np.array([
    0, 1, 2,    # Side face 1
    0, 2, 3,    # Side face 2
    0, 1, 4,    # Side face 3
    0, 3, 4     # Side face 4
], dtype=np.uint32)

index_buffer = indices.view(gloo.IndexBuffer)

# -----------------------------
# Draw Event
# -----------------------------

@window.event
def on_draw(dt):
    window.clear()
    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glClear(gl.GL_DEPTH_BUFFER_BIT)
    
    pyramid.draw(gl.GL_TRIANGLES, index_buffer)
    
    # Update rotation angle
    pyramid['transform'].angle += 1

# -----------------------------
# Run the Application
# -----------------------------

app.run()
