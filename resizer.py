import os
from PIL import Image

# Input & output folder
input_folder = "images"
output_folder = "resized"

# Make sure output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Resize dimensions
new_width = 800
new_height = 600

# Loop through all files in images folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        # Open image
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Resize
        img_resized = img.resize((new_width, new_height))

        # Save to output folder
        save_path = os.path.join(output_folder, filename)
        img_resized.save(save_path)

        print(f"✅ Resized and saved: {save_path}")

print("🎉 All images have been resized successfully!")
