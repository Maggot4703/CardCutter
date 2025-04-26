#!/usr/bin/env python3
# These .png files are to be 'CUT' into individual picture files
# Each shape is recorded in a text file of Name, x, y, width, height

from PIL import Image, ImageDraw

def markHorizontalLine(x1: int, y1: int, x2: int, y2: int, color: str = 'red', thickness: int = 1):
    """
    Draw a horizontal line on the image using Pillow.
    :param x1: Starting x-coordinate
    :param y1: Starting y-coordinate
    :param x2: Ending x-coordinate
    :param y2: Ending y-coordinate
    :param color: Color of the line (default is red)
    :param thickness: Thickness of the line (default is 1)
    """
    # Create a blank image
    #img = Image.new("RGB", (500, 500), "white")
    img = Image.new("RGB", (3146, 2382), "white")
   
    draw = ImageDraw.Draw(img)

    # Draw the line
    draw.line([(x1, y1), (x2, y2)], fill=color, width=thickness)

    # Return the image
    return img

def overlayGrid(image_path: str, grid_color: str = 'lightgrey', grid_size: tuple = (42,32)):
    """
    Overlay a grid on top of an image.
    :param image_path: Path to the input image
    :param grid_color: Color of the grid lines (default is light gray)
    :param grid_size: Tuple specifying the number of columns and rows in the grid
    """
    # Load the image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Get image dimensions
    img_width, img_height = img.size

    # Calculate grid cell size
    cols, rows = grid_size
    cell_width = img_width / cols
    cell_height = img_height / rows

    # Draw vertical grid lines
    for col in range(1, cols):
        x = int(col * cell_width)  # Fixed: renamed col to x for the line coordinate
        draw.line([(x, 0), (x, img_height)], fill=grid_color, width=1)

    # Draw horizontal grid lines
    for row in range(1, rows):
        y = int(row * cell_height)
        draw.line([(0, y), (img_width, y)], fill=grid_color, width=1)

    # Return the image with the grid
    return img

if __name__ == "__main__":
    # Example usage for markHorizontalLine
    #x1, y1, x2, y2 = 50, 100, 450, 100  # Coordinates for the line
    #color = 'blue'
    #thickness = 2

    # Create the image with the line
    #image = markHorizontalLine(x1, y1, x2, y2, color, thickness)

    # Save the image to a file
    #output_file = "output_line.png"
    #image.save(output_file)
    #print(f"Image saved as {output_file}")

    # Display the image (optional)
    #image.show()

    # Example usage for overlayGrid
    input_image = "/home/me/BACKUP/Links/CardCutter/gimp/_cars1.png"  # Replace with the path to your image
    output_image = "cars1.png"

    # Overlay the grid
    grid_image = overlayGrid(input_image, grid_color='lightgrey', grid_size=(42,32))

    # Save the image with the grid
    #grid_image.save(output_image)
    #print(f"Image with grid saved as {output_image}")

##########
# list of pictures
files = [
"/home/me/BACKUP/PROJECTS/CardCutter/gimp/_cars1.png",
"/home/me/BACKUP/PROJECTS/CardCutter/gimp/_cars1+.png",
"/home/me/BACKUP/PROJECTS/CardCutter/gimp/_cars2.png",
"/home/me/BACKUP/PROJECTS/CardCutter/gimp/_cars3.png",
"/home/me/BACKUP/PROJECTS/CardCutter/gimp/_cars57+.png",
"/home/me/BACKUP/PROJECTS/CardCutter/gimp/_cars78+.png",
"/home/me/BACKUP/PROJECTS/CardCutter/gimp/_cars114+.png"
]
#print(type(files))
##########
# list of save names
names = [
"Cars1.png",
"Cars2.png",
"Cars3.png",
"Cars4.png",
"Cars5.png",
"Cars6.png",
"Cars7.png"
]
#print(type(names))
##########
# dimensions
pixels = [
(3146,2382),
(2083,1152),
(2999,2381),
(3308,2549),
(1214,2114),
(2047,1197),
(2125,1197)
]
#print(type(pixels))
##########
# grid size
grids = [
(42,32),
(14,16),
(20,32),
(44,34),
(14,22),
(32,16),
(28,16)
]
#print(type(grids))
##########

'''
##########
#
# REPEAT FOR EACH PICTURE IN files VARIABLE
#
##########

    # Example usage for overlayGrid
    input_image = "/home/me/BACKUP/Links/CardCutter/gimp/_cars1.png"  # Replace with the path to your image
    output_image = "cars1.png" # Replace with the desired output file name

    # Overlay the grid
    grid_image = overlayGrid(input_image, grid_color='lightgrey', grid_size=(42,32)) # Replace with the desired grid size

    # Save the image with the grid
    grid_image.save(output_image)
    print(f"Image with grid saved as {output_image}")


'''

# Process each image
for i in range(len(files)):
    # Get input and output paths
    input_image = files[i]
    output_image = names[i]

    # Overlay the grid
    grid_image = overlayGrid(input_image, grid_color='lightgrey', grid_size=grids[i])

    # Save the image with the grid
    grid_image.save(output_image)
    print(f"Image with grid saved as {output_image}")

import this