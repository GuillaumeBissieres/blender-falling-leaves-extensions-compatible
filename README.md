# blender-falling-leaves - extensions-compatible
This repository contains the Blender Extensions compatible version.  For the complete package including all the online assets and optional components, visit:  https://github.com/GuillaumeBissieres/blender-falling-leaves

An add-on to create and animate realistic falling leaves in Blender

<img width="4167" height="2083" alt="Falling_img_01" src="https://github.com/user-attachments/assets/a8edc86e-fd5a-48e2-a229-2d541f34272f" />



#

**Falling Leaves & Online Assets**

This add-on builds a complete falling-leaves scene in one click: an emitter, a leaf mesh, a ground with collision and a fully configured particle system. You can then tune the simulation, swap in your own leaf, add wind, guide the leaves along a curve, sweep them off the ground and bake the result — all from within Blender's N panel. The **Online Assets** add-on completes it with the full library of ready-made leaf assets, downloaded from Hugging Face and updated over time.

###

<img width="1641" height="989" alt="Animation_6 (1)" src="https://github.com/user-attachments/assets/b897ac34-bc40-4709-8971-927c0f902ebc" />


# Requirements

**Falling Leaves** (Blender Extensions) is fully self-contained: OpenCV and 3 Geometry Nodes leaf assets are bundled, nothing else to install.

**Falling Leaves - Online Assets** (this repository) downloads the extra leaf assets from the Hugging Face repository: [GBissieres/falling_leaves_assets](https://huggingface.co/datasets/GBissieres/falling_leaves_assets)

**The assets can be downloaded directly from the add-on preferences** — no terminal or manual download needed. Go to **Edit** > **Preferences** > **Add-ons** > **Falling Leaves - Online Assets** and click **Download Online Assets**. The full asset pack is approximately 127 MB — a stable internet connection is required.

**Allow Online Access** must be enabled in **Edit** > **Preferences** > **System** > **Network**.


###

<img width="641" height="420" alt="Capture d&#39;écran 2026-11-22 014845" src="https://github.com/user-attachments/assets/e7e5424d-abbe-4c88-93f6-78dc590c37e5" />



# Installation (Blender Extensions Version)

## Step 1 – Install Falling Leaves

1. Download and install **Falling Leaves** from [Blender Extensions](https://extensions.blender.org/add-ons/falling-leaves/).
2. Open Blender and go to **Edit > Preferences > Add-ons**.
3. Enable the **Falling Leaves** add-on.

## Step 2 – Install Falling Leaves - Online Assets

1. Download **falling_leaves_online_assets** from the [Releases](https://github.com/GuillaumeBissieres/blender-falling-leaves-extensions-compatible/releases) of this repository.
2. Open Blender and go to **Edit > Preferences > Get Extensions**, click the arrow in the top-right corner, choose **Install from Disk** and select the ZIP file.
3. Enable the **Falling Leaves - Online Assets** add-on.

## Step 3 – Download the Assets

1. Go to **Edit > Preferences > Add-ons > Falling Leaves - Online Assets**.
2. Click **Download Online Assets**. A progress counter shows the download status and Blender stays responsive.
3. Once the download is finished, the new assets appear in the Falling Leaves **Asset Panel**, after the bundled ones.

###

<img width="300" height="76" alt="Capture d&#39;écran 2026-11-22 014913" src="https://github.com/user-attachments/assets/36f06f7e-43c5-4962-a831-dfcb9008575d" />

###

New leaf assets are added over time: click **Update Online Assets** whenever you like, only new or changed files are downloaded.

> **Important:** Due to Blender Extensions rules (extensions must be self-contained and cannot download content), **Falling Leaves** and **Falling Leaves - Online Assets** must be installed separately. For full functionality, install **Falling Leaves** first, then install **Falling Leaves - Online Assets** and download the assets.

## Accessing the Add-ons

- **Falling Leaves** can be accessed from the **Falling Leaves** tab in the **N Panel** (Sidebar) of the 3D Viewport.
- **Falling Leaves - Online Assets** can be accessed from its add-on preferences, and from the **Online assets** section it adds to the Falling Leaves **Asset Panel**.

# How to Use — Quick Start

1. **Run Falling Leaves** : Creates an Emitter plane above the scene, a Leaf object, a Ground plane with Collision and a particle system (500 leaves by default) with Newtonian physics, Brownian motion, drag, damping and random rotation. Press play and the leaves fall.

2. **Delete Setup** : The trash icon next to the Run button removes the Emitter, Leaf and Ground objects in one click.

###

<img width="340" height="211" alt="Capture d&#39;écran 2026-10-28 230946" src="https://github.com/user-attachments/assets/8ac4e2fd-fa7b-4926-91a9-7a1577f884ba" />

###

<img width="1894" height="998" alt="falling_leaves_6" src="https://github.com/user-attachments/assets/bb0e2ec3-bca6-4fc1-864a-4b63a72db0e0" />


###


# How to Use — Leaf Mesh

1. **Import Leaf from Image** : Select a PNG or JPG with transparency. The add-on reads the alpha channel to extract the leaf silhouette, then builds a leaf mesh with UV mapping and a material. Adjust **Subdivisions** and **Displacement** in the Adjust Last Operation panel for a more organic shape.

2. **Replace Leaf Mesh** : Select any object in the scene and click this button to use it as the instanced leaf of the particle system. The current leaf object is displayed in the panel.

###

###


# How to Use — Asset Panel

Click an icon in the grid, then **Add to Scene** to append the matching ready-made leaf asset into your scene. **Capture Thumbnail** takes the thumbnail from the viewport and **Save Selection to Library** stores your own assets.

Below, the **Online assets** section shows how many asset packs are downloaded and the **Download / Update Online Assets** button. This section only appears once the Online Assets add-on is installed and enabled.

###

<img width="432" height="275" alt="Capture d&#39;écran 2026-10-28 231211" src="https://github.com/user-attachments/assets/5413b8e4-2567-4e19-936c-8809d583cd99" />

###

<img width="1894" height="998" alt="falling_leaves_10 (2)" src="https://github.com/user-attachments/assets/e15339c4-2b88-4fbe-b8ae-8b8d0e66b364" />

###


# How to Use — Simulation Settings

Fine-tune the particle system without leaving the N panel:

- **Particles** : Leaf Count, Lifetime, Start Frame, End Frame
- **Size** : leaf size and size randomness
- **Physics** : Mass, Brownian, Drag, Damping
- **Rotation** : Randomize and Angular Velocity

### Settings Export

- **Export to Clipboard** : Copies all particle and wind settings as text.
- **Apply from Clipboard** : Pastes them back — handy to reuse a look in another scene.
- **Reset** : Restores the default values.

###

<img width="442" height="477" alt="Capture d&#39;écran 2026-10-28 234453" src="https://github.com/user-attachments/assets/db97228c-8d68-4495-90d3-ad0515c3aeb7" />


###


# How to Use — Wind & Forces

1. **Add Wind** : Adds a Wind force field with a ready-made preset and adjusts the particle settings to match, so leaves drift naturally.
2. **Strength / Noise** : Two sliders control the wind directly from the panel.
3. **Delete Wind** : The trash icon next to Add Wind removes the wind field in one click.
4. **Bake Simulation** : Bakes the particle simulation for reliable playback and rendering.

<img width="346" height="153" alt="Capture d&#39;écran 2026-10-28 224025" src="https://github.com/user-attachments/assets/37d0811f-6dd6-4390-b712-a349cf6bdc0b" />

###

<img width="1894" height="998" alt="falling_leaves_5" src="https://github.com/user-attachments/assets/d0ee873d-c904-42bc-9c69-51e02caede3e" />


###

###

# How to Use — Leaf Path

1. **Add Leaf Path** : Pick a curve of your scene in the **Leaf Path** panel. It becomes the path the leaves follow, like a stream of leaves carried by the wind. The trash icon removes it in one click.
2. **Speed / Noise / Spin** : Control how fast the leaves travel along the curve, how wavy the flow is, and how fast they rotate on themselves.
3. **Entry / Exit Diameter** : Set the width of the flow where the leaves enter and leave the path.
4. **Disappear at Beginning / End of Path** : Choose whether the leaves are born exactly on the path (none visible before it starts) and whether they vanish when they reach the end of the curve.

###

<img width="1894" height="998" alt="falling_leaves_16" src="https://github.com/user-attachments/assets/59523fec-d0b4-4b83-a69f-735827947c64" />

###
###


# How to Use — Ground Wind

Blow the leaves lying on your Geometry Nodes ground, like a gust sweeping them away. It runs in real time: just play the timeline.

1. **Add Ground Wind** : In **Wind & Forces** > **Ground Wind**, pick your **Ground** object and click the button. A **GroundWind** empty is created with a default sweep across the ground. Move or keyframe it to steer the gust.
2. **Wind Strength / Wind Radius** : How hard the leaves are swept and the size of the zone affected around the wind.
3. **Spread / Turbulence / Orientation** : How much the leaves are pushed apart from the center, how random the motion is, and how much the wind tilts and flips them.
4. **Gravity / Friction** : How fast lifted leaves fall back, and how quickly they stop on the ground.
5. **Leaves Left Behind** : The proportion of leaves that stay in place after the wind passes.
6. **Rebuild / Hide / Delete** : Regenerate the effect, show or hide the wind helpers, or remove everything and restore your original ground in one click.

###

<img width="1894" height="982" alt="falling_leaves_21 (2)" src="https://github.com/user-attachments/assets/02381276-440e-4acf-ba5d-f3b8c8c31042" />

###

<img width="1894" height="982" alt="falling_leaves_20 (2)" src="https://github.com/user-attachments/assets/df8a86e7-5c9f-4057-baac-219c59638c8e" />


###

# Advanced Options

- **Self-contained Main Add-on** : Falling Leaves from Blender Extensions never connects to the internet — it only reads the assets stored on your disk.
- **One-click Asset Download** : The extra assets are downloaded directly from the add-on preferences or the Asset Panel, without any terminal or manual file handling.
- **Assets Added Over Time** : **Update Online Assets** fetches only new or changed files.
- **Online Access Only on Click** : The Online Assets add-on connects to the internet only when you press the button, and only if **Allow Online Access** is enabled in Blender.
- **Survives Updates** : The assets are stored in the Falling Leaves user folder, so updating either add-on does not remove them.
- **Background Download** : The assets download in a separate thread with a progress counter — Blender never freezes.
- **Safe Download** : Files are written to a temporary `.part` file and size-checked before being validated, so an interrupted download never leaves a corrupted asset.
- **Copy & Share Settings** : Particle and wind settings can be exported to the clipboard and applied in another scene.
- **Non-destructive Cleanup** : Delete Setup and Delete Wind only remove the objects created by the add-on.
