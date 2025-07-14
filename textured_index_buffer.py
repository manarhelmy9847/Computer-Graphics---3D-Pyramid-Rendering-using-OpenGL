# ------------------ Imports ------------------
from glumpy import app, gloo, gl, glm, data             
from glumpy.transforms import Rotate                    
import numpy as np                                      
from PIL import Image                                   

# ------------------ Load Texture Image ------------------
img = Image.open('pyramid.jpeg')                        

# ------------------ Vertex Shader ------------------
vertex = """
    #version 440 core
    attribute vec3 position;                             
    attribute vec2 texcoord;                             
    varying vec2 v_texcoord;                             

    void main()
    {
        gl_Position = vec4(<transform(position*0.7)>,1.0);  
        v_texcoord = texcoord;                             
    }
"""

# ------------------ Fragment Shader ------------------
fragment = """
    #version 440 core
    uniform sampler2D texture;                           
    varying vec2 v_texcoord;                              

    void main()
    {
        gl_FragColor = texture2D(texture, v_texcoord);    
    }
"""

# ------------------ Window Setup ------------------
app.use("glfw")                             
window = app.Window(width=512, height=512, title="GREAT PYRAMID OF OPENGL")  

# ------------------ Render Function ------------------
@window.event
def on_draw(dt):
    window.clear()                          # Clear color buffer
    gl.glEnable(gl.GL_DEPTH_TEST)           # Enable depth testing
    gl.glClear(gl.GL_DEPTH_BUFFER_BIT)      # Clear depth buffer
    pyramid.draw(gl.GL_TRIANGLES, I)        # Draw pyramid geometry
    pyramid['transform'].angle += 1         # Increment rotation angle

# ------------------ Program Setup ------------------
pyramid = gloo.Program(vertex, fragment, count=5)   # Compile shader program with 5 vertices

# Assign vertex positions (5 vertices)
pyramid['position'] = [(0, 1, 0),            # Apex
                       (0, 0, -1),           # Back
                       (-1, 0, 1),           # Left
                       (1, 0, 1),            # Right
                       (0, 0, -1)]           # Duplicate back (for texture mapping)

# ------------------ Index Buffer ------------------
I = np.array([0,1,2,                         # Face 1: apex, back, left
              0,2,3,                         # Face 2: apex, left, right
              0,1,4,                         # Face 3: apex, back, duplicate
              0,3,4], dtype=np.uint32)       # Face 4: apex, right, duplicate
I = I.view(gloo.IndexBuffer)                 # Convert to index buffer

# ------------------ Texture Coordinates ------------------
pyramid['texcoord'] = [(0, 0),               # UV for apex
                       (0.5, 1),             # UV for back
                       (0, 1),               # UV for left
                       (1, 1),               # UV for right
                       (0, 1)]               # UV for back duplicate

# ------------------ Rotation Transform ------------------
pyramid['transform'] = Rotate(axis=(0.0, 1.0, 0.0))      

# ------------------ Texture Assignment ------------------
pyramid['texture'] = np.asarray(img)                    
     
# ------------------ Run Application ------------------
app.run()