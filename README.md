# 🧱 3D Pyramid Rendering with OpenGL (Glumpy & PyOpenGL)

This project demonstrates a rotating 3D pyramid rendered using **Python**, **OpenGL**, and **Glumpy**. It applies texture mapping, real-time transformation, and custom vertex/fragment shaders to simulate modern graphics pipeline operations.

---

## 🧠 Overview

This is a computer graphics practical project focused on:
- Creating a 3D pyramid using vertex and index buffers.
- Applying texture mapping using `Pillow`.
- Implementing a real-time rotation using `glumpy.transforms.Rotate`.
- Rendering using modern OpenGL shaders (GLSL).

---

## ✨ Features

-  Real-time rotation
-  Texture mapping
   Depth buffering
-  Vertex & Fragment shaders (GLSL)
-  Index buffer optimization

---

## 🛠️ Technologies Used

- Python 3.8  
- [PyOpenGL](https://pypi.org/project/PyOpenGL/) – OpenGL bindings for Python  
- [Glumpy](https://glumpy.github.io/) – Fast, GPU-based visualization  
- [GLFW](https://www.glfw.org/) – Context/window creation  
- [Pillow](https://python-pillow.org/) – Image handling  
- NumPy – Numerical operations  
- VS Code – Recommended IDE

---

## ⚙️ How It Works

- Loads a pyramid mesh with 5 vertices
- Assigns UV coordinates for texture mapping
- Loads an external image (`pyramid.jpeg`) as texture
- Uses custom GLSL shaders:
  - **Vertex Shader:** Applies rotation and passes UV
  - **Fragment Shader:** Maps UV to pixel color
- Uses `glumpy.app.Window` to render and rotate the pyramid in real-time

---

