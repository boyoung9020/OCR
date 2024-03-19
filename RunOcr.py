import argparse
import subprocess
import os

def run_commands(commands):
    for command in commands:
        process = subprocess.Popen(command, shell=True)
        process.wait()

def main(input_path=None):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if input_path:
        commands = [
            f"cd {os.path.join(script_dir, 'HeadlineExtractor')} && python detect.py --source {input_path}",
            f"cd {os.path.join(script_dir, 'CRAFT')} && python test.py",
            f"cd {os.path.join(script_dir, 'OCR')} && python EasyocrC.py"
        ]
    else:
        commands = [
            f"cd {os.path.join(script_dir, 'HeadlineExtractor')} && python detect.py",
            f"cd {os.path.join(script_dir, 'CRAFT')} && python test.py",
            f"cd {os.path.join(script_dir, 'OCR')} && python EasyocrC.py"
        ]
    run_commands(commands)

def parse_opt():
    parser = argparse.ArgumentParser(description="Run OCR pipeline")
    parser.add_argument("--input_path", default= "../input", help="Input image or directory path for OCR pipeline")
    args = parser.parse_args()
    return args.input_path

if __name__ == "__main__":
    input_path = parse_opt()
    print(f"input_path :############################################# {input_path}")
    main(input_path)
