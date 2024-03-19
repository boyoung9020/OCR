import os
from pathlib import Path

# 스크립트 파일이 위치한 디렉토리 가져오기
script_directory = Path(__file__).parent

# 이미지 디렉토리 경로 설정
image_dir = script_directory.parent / "HeadlineExtractor" / "runs" / "detect" / "exp" / "crops" / "HeadlineBox"

# 이미지 디렉토리에 있는 모든 파일 목록 가져오기
image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

# 이미지 파일들의 이름을 word_인덱스_0 형식으로 변경
for idx, file_name in enumerate(sorted(image_files)):
    new_name = f"word_{idx}_0" + os.path.splitext(file_name)[1]
    os.rename(os.path.join(image_dir, file_name), os.path.join(image_dir, new_name))

print("이미지 파일들의 이름을 변경하였습니다.")
