import os

def rename_images(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Filter only image files (you can modify this list of extensions if needed)
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    image_files = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]

    # Sort files to ensure the order is consistent
    image_files.sort()

    # Rename each image
    for i, filename in enumerate(image_files, start=1):
        # Get the file extension
        ext = os.path.splitext(filename)[1]
        
        # Create the new filename
        new_name = f"img{i:02d}{ext}"
        
        # Rename the file
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
        print(f"Renamed '{filename}' to '{new_name}'")

# Usage example
folder_path = 'C:/Users/mathe/Music/Dev/koniedotcom/static/images' 
 # Replace with your folder path
rename_images(folder_path)
