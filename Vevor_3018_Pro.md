Requirement : 

# 1. Configuration for laserweb

## A. Lasercutter

### 1) Configuration of the lasercutter

First, you have to create a new profile for this lasercutter on the sofware.

(on machine part)
Second, you have to specify the dimension of the working space (_you have to keep in mind that in somecase the working surface is not the same as the surface of the bed. It's the case here._)

- Machine width : 290 MM
- Machine height : 135 MM

Third, you have to choose show the space. 

Fourth, you have to specify the width of the laser beam.
- Here is 0,2MM

### 2) Use of the lasercutter
#### a)Creation of the file
You can choose to have a vector file (vector - cutting/engraving) or a raster file (image - engraving)

If you have a vector file, only the following extension can be use
 - svg 

If you have a raster file, only the following extension can be use
- bmp

#### b)Creation of the Gcode
- In the left panel, you have to navigate to "Files".
- Choose "Add Document".
- Select all the documents you want to use.
- From the document list, select either multiple or single objects and drag them to the G-code "placeholder".
- Choose the parameters you desire (refer to Annex A: Benchmark for details).
- Click on "generate"

#### c)Preparation of the working space

1. Take the plate called the "standard plate" and position the bottom-left corner of the plate at the bottom-left corner of the bed.
2. Within the software "Laserweb", move the blue LED of the laser to the center of the crosshair.
3. Remove the "standard plate".
Fourth, choose the desired location for your plate (taking into consideration where the X = 0, Y = 0 coordinates will be for the software).


### 3) Issues - solutions
- Issue for width border : maybe 1 pt too tinny
- SVG files made on illustrator was not accepte by laserweb.
-> From illustrator you have to save it on SVG not 