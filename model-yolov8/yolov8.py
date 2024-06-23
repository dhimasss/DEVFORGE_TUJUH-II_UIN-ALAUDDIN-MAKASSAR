!pip install ultralytics -q
import cv2
from ultralytics import YOLO

# Muat model YOLOv8
model = YOLO('yolov8m.pt')

# Daftar kelas yang diinginkan (misalnya 'car' dan 'motorcycle')
desired_classes = ['car', 'motorcycle']

# Fungsi untuk memfilter hasil prediksi
def filter_predictions(results, desired_classes):
    filtered_preds = []
    for box, cls in zip(results.boxes.xyxy, results.boxes.cls):
        class_name = model.names[int(cls)]
        if class_name in desired_classes:
            filtered_preds.append((box, class_name))
    return filtered_preds

# Buka video
input_video_path = '/content/heketon-pt_bawah.mp4'
output_video_path = '/content/hasil_heketon-pt-bawah.mp4'
output_image_path = '/content/last_frame_bawah.jpg'

cap = cv2.VideoCapture(input_video_path)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

last_frame = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Lakukan deteksi menggunakan YOLOv8
    results = model(frame)[0]

    # Filter hasil prediksi
    filtered_results = filter_predictions(results, desired_classes)

    # Hitung jumlah mobil dan motor
    car_count = sum(1 for _, class_name in filtered_results if class_name == 'car')
    motorcycle_count = sum(1 for _, class_name in filtered_results if class_name == 'motorcycle')
    total_count = car_count + motorcycle_count

    # Gambar hasil prediksi pada frame
    for box, class_name in filtered_results:
        x1, y1, x2, y2 = map(int, box)
        label = f"{class_name}"

        # Gambarkan kotak pembatas
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Tampilkan jumlah mobil dan motor pada frame
    count_label = f"Mobil: {car_count}, Motor: {motorcycle_count}"
    cv2.putText(frame, count_label, (10, height - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Tentukan kepadatan lalu lintas
    if total_count >= 12:
        density_label = "Kepadatan: Padat"
    else:
        density_label = "Kepadatan: Ringan"

    # Tampilkan kepadatan lalu lintas pada frame
    cv2.putText(frame, density_label, (width - 300, height - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Tulis frame ke output video
    out.write(frame)

    # Simpan frame terakhir
    last_frame = frame

# Simpan frame terakhir sebagai gambar
if last_frame is not None:
    cv2.imwrite(output_image_path, last_frame)

# Lepas resource
cap.release()
out.release()