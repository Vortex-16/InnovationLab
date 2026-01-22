import os
import cv2
import torch
from pathlib import Path

# -----------------------------
# CONFIGURATION
# -----------------------------
INPUT_FOLDER = "Python/ML/images"       # Folder containing images
OUTPUT_FOLDER = "Python/ML/output_result"    # Folder to save results
BATCH_SIZE = 4                      # Number of images to process at once
CONF_THRESHOLD = 0.5                # Confidence threshold for detection

# Create output folder if not exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# -----------------------------
# LOAD YOLOv5 MODEL (Pre-trained on COCO dataset)
# -----------------------------
# This will download the model if not already present
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model.conf = CONF_THRESHOLD  # Set confidence threshold

# -----------------------------
# FUNCTION: Process a batch of images
# -----------------------------
def process_batch(image_paths):
    # Load images into memory
    imgs = [cv2.imread(str(p)) for p in image_paths]
    # Convert BGR (OpenCV) to RGB for YOLO
    imgs_rgb = [cv2.cvtColor(img, cv2.COLOR_BGR2RGB) for img in imgs]

    # Run detection
    results = model(imgs_rgb)

    # Iterate over each image and save results
    for img_path, img, pred in zip(image_paths, imgs, results.pred):
        for *box, conf, cls in pred:
            x1, y1, x2, y2 = map(int, box)
            label = f"{model.names[int(cls)]} {conf:.2f}"
            # Draw bounding box
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Save processed image
        out_path = Path(OUTPUT_FOLDER) / Path(img_path).name
        cv2.imwrite(str(out_path), img)

# -----------------------------
# MAIN: Load images batch-wise
# -----------------------------
image_files = list(Path(INPUT_FOLDER).glob("*.jpg")) + list(Path(INPUT_FOLDER).glob("*.png"))

if not image_files:
    print("No images found in the input folder.")
else:
    for i in range(0, len(image_files), BATCH_SIZE):
        batch_paths = image_files[i:i + BATCH_SIZE]
        process_batch(batch_paths)
        print(f"Processed batch {i//BATCH_SIZE + 1}")

print("Object detection completed. Results saved in:", OUTPUT_FOLDER)
