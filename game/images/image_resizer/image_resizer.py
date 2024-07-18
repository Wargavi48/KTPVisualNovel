from PIL import Image
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define input and output directories relative to the script directory
input_dir = os.path.join(script_dir, 'resizer_input')
output_dir = os.path.join(script_dir, 'resizer_output')

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Ask user for new size
try:
    new_width = int(input("Enter the new width: "))
    new_height = int(input("Enter the new height: "))
except ValueError:
    print("Invalid input for width or height. Please enter integer values.")
    exit(1)

# Function to maintain aspect ratio
def resize_image(image, width, height):
    img_aspect_ratio = image.width / image.height
    new_aspect_ratio = width / height
    
    if img_aspect_ratio > new_aspect_ratio:
        # Image is wider than the desired aspect ratio
        new_width = width
        new_height = int(width / img_aspect_ratio)
    else:
        # Image is taller than the desired aspect ratio
        new_height = height
        new_width = int(height * img_aspect_ratio)
    
    return image.resize((new_width, new_height), Image.Resampling.LANCZOS)

# Iterate through all files in the input directory
resized_images = []
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):  # Add other formats if needed
        # Open an image file
        with Image.open(os.path.join(input_dir, filename)) as img:
            # Resize image while maintaining aspect ratio
            img_resized = resize_image(img, new_width, new_height)
            # Save the resized image to the output directory
            img_resized.save(os.path.join(output_dir, filename))
            resized_images.append(filename)

print("Batch resizing completed.")

# Ask for confirmation to delete the input files
confirm_delete = input("Do you want to delete the original input files? (y/n): ")

if confirm_delete.lower() in ('y', 'yes'):
    for filename in resized_images:
        os.remove(os.path.join(input_dir, filename))
    print("Original input files have been deleted.")
else:
    print("Original input files have been kept.")
