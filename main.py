import os
import glob
import cv2
from ultralytics import YOLO, solutions
import numpy as np

# folderul cu imaginile de procesat
image_folder = r"imagini"

# crearea folderului pentru rezultate
output_folder = "rezultate"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# cautare fisiere jpg si png
image_paths = glob.glob(os.path.join(image_folder, "*.jpg"))
image_paths += glob.glob(os.path.join(image_folder, "*.png"))


images = []
for img_path in image_paths:
    # extrage numele fisierului fara extensie
    base_name = os.path.splitext(os.path.basename(img_path))[0]
    # json-ul are acelasi nume ca imaginea
    json_file = f"{base_name}_bounding_boxes.json"
    images.append({"img_path": img_path, "json_file": json_file})

# incarcare model YOLO
model = YOLO("yolo11m.pt")


for item in images:
    img_path = item["img_path"]
    json_file = item["json_file"]

    # citire imagine
    img = cv2.imread(img_path)
    if img is None:
        print(f"Eroare: nu s-a putut incarca {img_path}")
        continue

    img_name = os.path.basename(img_path)
    print(f"\nProcesare: {img_name}")

    base_name = os.path.splitext(os.path.basename(img_path))[0]

    # detectie obiecte cu YOLO
    results = model(img)

    # corectare clase detectate gresit
    for box in results[0].boxes:
        cls_idx = int(box.cls[0])
        label = model.names[cls_idx]
        # reclasificare obiecte confundate ca masini
        if label in ["cellphone", "book", "laptop"]:
            box.cls[0] = model.names.index("car")

    # numarare vehicule detectate
    nr_masini = 0
    for box in results[0].boxes:
        label = model.names[int(box.cls[0])]
        if label in ["car", "truck", "bus"]:
            nr_masini += 1

    print(f"Vehicule detectate: {nr_masini}")

    # desenare bounding boxes pe imagine
    annotated_img = results[0].plot()

    # salvare rezultat detectie
    output_cars = os.path.join(output_folder, f"{base_name}_masini_detectate.jpg")
    cv2.imwrite(output_cars, annotated_img)
    print(f"Salvat: {output_cars}")

    # afisare rezultat
    cv2.imshow(f"Masini detectate - {img_name}", annotated_img)
    cv2.waitKey(0)

    # detectie status locuri de parcare folosind ParkingManagement
    parking_manager = solutions.ParkingManagement(
        model="yolo11m.pt",
        json_file=json_file,
    )

    results_pm = parking_manager(img)
    result_img = results_pm.plot_im.copy()

    # inversare culori
    red_pixels = np.all(result_img == [0, 0, 255], axis=-1)
    green_pixels = np.all(result_img == [0, 255, 0], axis=-1)

    result_img[red_pixels] = [0, 255, 0]
    result_img[green_pixels] = [0, 0, 255]

    # salvare rezultat status parcare
    output_parking = os.path.join(output_folder, f"{base_name}_parking.jpg")
    cv2.imwrite(output_parking, result_img)
    print(f"Salvat: {output_parking}")

    cv2.imshow(f"Status locuri parcare - {img_name}", result_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("\nProcesare completa, toate imaginile au fost procesate")