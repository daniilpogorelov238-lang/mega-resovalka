import requests

# Замените эту ссылку на вашу raw-ссылку на APK из GitHub
APK_RAW_URL = "https://raw.githubusercontent.com/ВАШ_ЛОГИН/ВАШ_РЕПОЗИТОРИЙ/ВЕТКА/path/to/app-debug.apk"
OUTPUT_FILENAME = "app-debug.apk"

def download_file(url, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Файл успешно скачан: {filename}")
    except Exception as e:
        print(f"Ошибка при скачивании: {e}")

if __name__ == "__main__":
    if APK_RAW_URL == "https://raw.githubusercontent.com/ВАШ_ЛОГИН/ВАШ_РЕПОЗИТОРИЙ/ВЕТКА/path/to/app-debug.apk":
        print("Пожалуйста, замените APK_RAW_URL на вашу реальную raw-ссылку из GitHub.")
    else:
        download_file(APK_RAW_URL, OUTPUT_FILENAME)