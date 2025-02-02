BlenderImageLUT
---
Real time image-based color grading in Blender's compositor.
# WARNING
There is NO correctness guarantee for this implementation and is currently *NOT* color correct. Use at your own risk.

# Usage
## Loading the Nodes
- [Download `BlenderImageLut.blend`](https://github.com/mos9527/blender-image-lut/raw/refs/heads/main/BlenderImageLUT.blend)
- In your Blender project, Go to `File > Append...`
<img width="318" alt="image" src="https://github.com/user-attachments/assets/346d0ecb-cd1c-4a60-a09c-413434504b72" />

- Open the downloaded `.blend` file and go to `NodeTree`, where you can find the node **`BlenderImageLUT`**. Click `Append`
<img width="560" alt="image" src="https://github.com/user-attachments/assets/c29c85e4-f952-4b3a-8ec5-d2fae1e550e2" />

- In the `Compositor` tab, enable `Use Nodes` and search for `BlenderImageLUT` with F3, add it to your node tree
<img width="764" alt="image" src="https://github.com/user-attachments/assets/e0e06b70-0f8b-4a27-a099-650cf651a656" />

## Loading the LUT image
- Add an `Image` node with F3 and then load the LUT image of your choice **and setup the `LUT Dimension` ($D$) properly**.
  - **ATTENTION:** Please refer to the [Notes](#notes) section for what kind of LUT image you should be using.
- Connect the nodes. Your final node setup should look like this:
<img width="541" alt="image" src="https://github.com/user-attachments/assets/96aa0891-651f-4958-820f-6a308b50b12f" />

- To view the result, you can enable the compositor under the `Viewport Shading` tab and set the compositor option to `Always` as shown below
<img width="1272" alt="image" src="https://github.com/user-attachments/assets/9fdb32a7-e8fb-4199-a4a3-d3e09aead871" />

# Notes
## Notes on the LUT image
Your 3D LUT image should be a **2D Image** of pixel dimension $(D^2,D)$, where $$D$$ is the **uniform size in pixel of your LUT**

The 3D texture should be swizzled onto the 2D plane like this:
```
Numbers indicate the index of the Z-slice
 ┌───────┬───────┬───────┬─────┐ 
 │       │       │       │     │ 
 │   1   │   2   │   3   │ ..n │ 
 │       │       │       │     │ 
 └───────┴───────┴───────┴─────┘
```
For example, here's a *netural* one with $D=16$

![image](https://github.com/user-attachments/assets/60dac6c8-bfb6-45dd-8017-da5003cbc777)

The $R,G,B$ channels should advance in value in the UV (pixel) direction shown in the following diagrams:
- $R$ channel
<img width="512" alt="image" src="https://github.com/user-attachments/assets/4009e5f4-3eac-43d2-ad2e-4f029ad79669" />

- $G$ channel
<img width="512" alt="image" src="https://github.com/user-attachments/assets/7595ebe0-17a7-49a3-b206-e5a399d93e98" />

- $B$ channel
<img width="512" alt="image" src="https://github.com/user-attachments/assets/4aecd6e1-e3e6-44d9-9ceb-98f5de5c2504" />

## Transposing LUTs of different dimensions
(todo)

# How it works
By implementing Bilinear Filtering and 3D texture sampling from scratch with Compositor Nodes and performs LERPed color look-up in runtime.

Generally there will be 8 texture lookups for each pixel - which is expensive. Use this node setup sparingly or only at render-time!

# References
- Real Time Rendering 4th Edition
- https://github.com/mos9527/sssekai_blender_io
