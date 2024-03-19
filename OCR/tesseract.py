import os
import pytesseract
from PIL import Image

# 이미지 디렉토리 경로
image_dir = "../HeadlineExtractor/runs/detect/exp/crops/HeadlineBox/"

# 언어별로 OCR 수행
languages = ['kor', 'eng', 'chi_tra']

for language in languages:
    print(f"Language: {language}")
    print("=" * 20)
    
    # 이미지 디렉토리 내의 파일 목록 확인
    for filename in os.listdir(image_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image_path = os.path.join(image_dir, filename)
            
            # 이미지 열기
            image = Image.open(image_path)
            
            # OCR 수행
            text = pytesseract.image_to_string(image, lang=language)
            
            # 결과 출력
            print(f"Image: {filename}")
            print(text.strip())
            print("-" * 20)

    print("\n")
