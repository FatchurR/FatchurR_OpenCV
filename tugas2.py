import cv2

def load_display_save_video(video_path, output_path):
    """
    Memuat, menampilkan, dan menyimpan video
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Gagal membuka video.")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height), isColor=False)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Ubah ke grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('Video', gray_frame)
        out.write(gray_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Video disimpan di {output_path}")

if __name__ == "__main__":
    video_path = 'videos/rahasia.mp4'  # Ganti dengan nama file kamu
    load_display_save_video(video_path, 'videos/output_video.avi')
