import cv2

def load_display_save_video(video_path, output_path):
    """
    Memuat, menampilkan, dan menyimpan video
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Gagal membuka video.")
        return
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = 'videos/rahasia.mp4'  # Ganti dengan nama file kamu
    load_display_save_video(video_path, 'videos/output_video.avi')
