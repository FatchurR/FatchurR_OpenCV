import cv2

def load_and_display_image(image_path):
    """
    Memuat dan menampilkan gambar
    """
    image = cv2.imread(image_path)

    if image is None:
        print("Gambar tidak ditemukan.")
        return None

    cv2.imshow('Gambar', image)

    #e
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    return image

def save_image(image, save_path):
    """
    Menyimpan gambar ke file baru
    """
    cv2.imwrite(save_path, image)
    print(f"Gambar disimpan di {save_path}")

if __name__ == "__main__":
    image_path = 'images/kali-oleo.png'  
    image = load_and_display_image(image_path)

    if image is not None:
        save_path = 'images/hasil.jpg'
        save_image(image, save_path)
