import os
import gdown

# Main function to parse the text file and download each file in each Google Drive link
def download_files_from_links(text_file_path):
    with open(text_file_path, "r") as file:
        lines = file.readlines()

    for line in lines:
        if "Chapter:" in line:
            chapter_name = line.split("Chapter: ")[-1].strip().replace(" ", "_")
        elif "Link:" in line:
            link = line.split("Link: ")[-1].strip()
            file_id = link.split("id=")[-1]

            # Create a directory for each chapter
            folder_path = os.path.join(os.getcwd(), chapter_name)
            os.makedirs(folder_path, exist_ok=True)

            # Attempt to download each file using its direct link
            print(f"Downloading file for chapter: {chapter_name}...")
            try:
                gdown.download(f"https://drive.google.com/uc?id={file_id}", output=os.path.join(folder_path, f"{chapter_name}.pdf"), quiet=False)
            except Exception as e:
                print(f"Failed to download file for {chapter_name}: {e}")

# Call the main function with the path to the txt file
download_files_from_links("urls.txt")
