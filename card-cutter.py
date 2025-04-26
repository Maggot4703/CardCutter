#!/usr/bin/env python3
# These .png files are to be 'CUT' into individual picture files
# Each shape is recorded in a text file of Name, x, y, width, height

from PIL import Image, ImageDraw
import csv
import pandas as pd

#gridly
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

#gridify
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

#
def read_csv_builtin(filename: str) -> list:
    """
    Read CSV data using built-in csv module
    :param filename: Path to the CSV file
    :return: List of rows from CSV
    """
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row if present
        for row in csv_reader:
            data.append(row)
    return data

#
def read_csv_pandas(filename: str) -> pd.DataFrame:
    """
    Read CSV data using pandas
    :param filename: Path to the CSV file
    :return: Pandas DataFrame containing CSV data
    """
    return pd.read_csv(filename)

#
def read_excel(filename: str, sheet_name: str = None) -> pd.DataFrame:
    """
    Read Excel data using pandas
    :param filename: Path to the Excel file (.xlsx or .xls)
    :param sheet_name: Name of the sheet to read (default is first sheet)
    :return: Pandas DataFrame containing Excel data
    """
    return pd.read_excel(filename, sheet_name=sheet_name)

#
def spacer():
    """
    Print a blank line or separator for better readability in the output.
    """
    print("\n" + "-" * 40 + "\n")

#gridify scans
def job1():
    """
    Batch process images to overlay grids and save them.
    """
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
    ##########
    # list of dimensions
    pixels = [
    (3146,2382),
    (2083,1152),
    (2999,2381),
    (3308,2549),
    (1214,2114),
    (2047,1197),
    (2125,1197)
    ]
    ##########
    # grid size
    grids = [
    (42,32),
    (28,16),
    (40,32),
    (44,34),
    (14,22),
    (32,16),
    (28,16)
    ]
    ##########
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

#csv
def job2():
    '''
    Read CSV file using both built-in csv module and pandas
    '''
    # CSV file reading
    csv_file = "AADA.csv"
    try:
        data_pandas = read_csv_pandas(csv_file)
        print("\nCSV Data:")
        print(data_pandas.head())
        print(data_pandas.columns)
        print(data_pandas['TYPE'])
        print(data_pandas.iloc[0])
    except FileNotFoundError:
        print(f"Error: Could not find CSV file '{csv_file}'")
    except Exception as e:
        print(f"Error reading CSV file: {e}")

#xls
def job3():
    '''
    '''
    # Excel file reading
    excel_file = "AADA.xls"
    try:
        df = read_excel(excel_file, sheet_name=0)  # Specify the sheet name or index
        print("\nExcel Data:")
        print(df.head())
        print(df.columns)
    except FileNotFoundError:
        print(f"Error: Could not find Excel file '{excel_file}'")
    except Exception as e:
        print(f"Error reading Excel file: {e}")

#???
def job4():
    pass

def main():
    """Main execution function"""
    try:
        # Process images
        #job1()  # Process and save gridded images
        #spacer()
        
        # Process data files
        job2()  # Read and display CSV data
        spacer()
        job3()  # Read and display Excel data
        spacer()
        
    except Exception as e:
        print(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()


