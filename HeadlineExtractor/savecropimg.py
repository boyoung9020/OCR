import os

# 이미지 파일이 있는 디렉토리 경로
image_dir = '../save'

# detect.py 스크립트를 실행하는 명령어
command_template = 'python detect.py --weights ./runs/train/results/weights/best.pt --img 416 --conf 0.5 --source {} --save-crop'

# 디렉토리 내의 모든 이미지 파일에 대해 detect.py 스크립트 실행
for filename in os.listdir(image_dir):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # 이미지 파일인 경우에만 처리
        image_path = os.path.join(image_dir, filename)
        command = command_template.format(image_path)
        os.system(command)
