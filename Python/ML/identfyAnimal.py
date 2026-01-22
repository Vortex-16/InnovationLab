from ultralytics import YOLO
import cv2
import os
import pandas as pd

model = YOLO("yolov8n.pt")

image_folder = "Python/ML/images"
output_folder = "Python/ML/output"
excel_file = "Python/ML/results.xlsx"

os.makedirs(output_folder, exist_ok=True)

data = []

# Loop through images
for image_name in os.listdir(image_folder):
    image_path = os.path.join(image_folder, image_name)

    # Detect objects
    results = model(image_path)

    annotated_image = results[0].plot()
    cv2.imwrite(os.path.join(output_folder, image_name), annotated_image)

    for box in results[0].boxes:
        class_id = int(box.cls[0])
        label = model.names[class_id]
        confidence = float(box.conf[0])

        # Add row to data list
        data.append([image_name, label, confidence])

# Convert to Excel
df = pd.DataFrame(data, columns=["Image Name", "Object", "Confidence"])
df.to_excel(excel_file, index=False)

print(" Detection results saved to results.xlsx")