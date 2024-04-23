# import json


# def exclude_text(json_file, output_file):
#     with open(json_file, 'r', encoding='utf-8') as f:
#         data = json.load(f)

#     # Remove text fields from each page
#     for page in data[0]['pages']:
#         page.pop('frame', None)
#         for text_data in page['text']:
#             del text_data['text_ja']
#             del text_data['text_en']
#             del text_data['text_zh']

#     with open(output_file, 'w', encoding='utf-8') as f:
#         json.dump(data, f, indent=4, ensure_ascii=False)


# # Example usage
# json_file = 'annotation.json'  # Replace with your JSON file path
# output_file = "output.json"
# exclude_text(json_file, output_file)
# # Print the modified JSON data
# # print(json.dumps(data_without_text, indent=4, ensure_ascii=False))


# import os
# import json
# import csv


# def process_json(json_file):
#     # Create the 'data' folder if it doesn't exist
#     if not os.path.exists('data'):
#         os.makedirs('data')

#     with open(json_file, 'r', encoding='utf-8') as f:
#         data = json.load(f)

#     for book_data in data:
#         book_title = book_data['book_title']
#         for page in book_data['pages']:
#             page_index = page['page_index']
#             image_path = page['image_paths']['ja']
#             image_name = os.path.basename(image_path)
#             csv_filename = os.path.join(
#                 'data', f"{book_title}_{page_index}_{image_name}.csv")

#             with open(csv_filename, 'w', newline='') as csvfile:
#                 csvwriter = csv.writer(csvfile)
#                 num_text_entries = len(page.get('text', []))
#                 # Write the number of text entries
#                 csvwriter.writerow([num_text_entries])
#                 for text_data in page.get('text', []):
#                     x = text_data['x']
#                     x_w = text_data['x'] + text_data['w']
#                     y = text_data['y']
#                     y_h = text_data['y'] + text_data['h']
#                     csvwriter.writerow([x, x_w, y, y_h])

#             print(f"CSV file saved: {csv_filename}")


# # Example usage:
# process_json('annotation.json')


import os


def rename_images(directory):
    # Iterate over each folder in the 'english' directory
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        # Check if the item in 'english' directory is a folder
        if os.path.isdir(folder_path):
            ja_path = os.path.join(folder_path, 'ja')
            # Check if 'ja' folder exists
            if os.path.exists(ja_path):
                # Iterate over each image in 'ja' folder
                for image_name in os.listdir(ja_path):
                    image_path = os.path.join(ja_path, image_name)
                    # Rename the image to 'foldername_originalname'
                    new_image_name = f"{folder_name}_{image_name}"
                    new_image_path = os.path.join(ja_path, new_image_name)
                    os.rename(image_path, new_image_path)
                    print(f"Renamed {image_name} to {new_image_name}")


# Example usage:
english_directory = 'images'
rename_images(english_directory)
