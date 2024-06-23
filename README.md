# DEVFORGE_TUJUH-II_UIN-ALAUDDIN-MAKASSAR
# smart-traffic-light
 Smart Traffic Light adalah sebuah sistem yang dapat mengetahui kondisi kemacetan dengan menghitung jumlah kendaraan. Sehingga kondisi lalu lintas dapat dilihat melalui sebuah website

 ## Fitur
- Monitoring Lalu lintas real time
- Deteksi kendaraan secara real-time menggunakan YOLOv8.
- Hitungan jumlah mobil dan motor dari video CCTV.
- Penentuan status kepadatan lalu lintas (Padat atau Ringan).
- Penyimpanan hasil deteksi dan status kepadatan dalam format video.

## Instalasi
1. Clone repositori ini:
    sh
    git clone https://github.com/obiwannn11/sistem-smart-traffic-light.git
    
2. Buat Google Colab dan create new notebook
3. 
## Penggunaan Model YOLO V8
1. Upload video ke folder Google Colab
2. Jalankan skrip file yolov8.py di Google Colab
    sh
    Ctrl C + Ctrl V
    
    
3. Ubah nama ada bagian -> # Buka video
input_video_path = '/content/heketon-pt_atas.mp4'
output_video_path = '/content/hasil_heketon-pt-atas.mp4'
output_image_path = '/content/last_frame_atas.jpg'

setelah path /content/ , isi nama file sesuai dengan yang di upload
4. Pilih Runtime T4 GPU 
5. Jalankan File dengan Klik tombol play di sebelah kodingan
6. Hasil akan disimpan di direktori output.
7. Setelah itu akan muncul file sesuai bagian output_video_path

## Website
Pada website kita menyediakan fitur yang berupa : 
1. Melihat kumpulan video rekaman CCTV diberbagai lampu lalu lintas yang sudah di analisis oleh model YOLO V8 pada bagian 'Peta'
2. Dapat melihat live simulation pada bagian 'Simulasi',
   Live Simulation atau Simulasi adalah gambaran dari lanjutan sistem yang kami kembangkan yaitu membuat sistem lampu lalu lintas yang bersifat dinamis, yaitu berdasarkan kepadatan lampu lalu lintas, dengan adanya model YOLO V8 diharapkan dapat membantu jalur mana yang cukup padat dan akan didahulukan untuk mengurangi kemacetan panjang

Projek ini dibuat untuk mengikuti lomba hackathon Devforge UC Makassar
