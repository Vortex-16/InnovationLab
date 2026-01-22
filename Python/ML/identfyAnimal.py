from ultralytics import YOLO
import cv2
import os

model = YOLO("yolov8n.pt")

image_folder = "Python/ML/images"
output_folder = "Python/ML/output"

os.makedirs(output_folder, exist_ok=True)

# Loop through all images
for image_name in os.listdir(image_folder):
    image_path = os.path.join(image_folder, image_name)

    # Detect objects
    results = model(image_path)

    # Draw boxes on image
    annotated_image = results[0].plot()

    # Save output image
    cv2.imwrite(os.path.join(output_folder, image_name), annotated_image)

    # Print detected objects
    print(f"\nImage: {image_name}")
    for box in results[0].boxes:
        class_id = int(box.cls[0])
        label = model.names[class_id]
        confidence = float(box.conf[0])
        print(f" - {label} ({confidence:.2f})")
print("Detection complete. Check the output folder for results.")