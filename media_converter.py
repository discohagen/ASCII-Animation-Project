import math
import os
import re
import cv2
import json
from PIL import Image
from typing import Any


GRAY_RAMP = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,"^`\'. '
RAMP_LENGTH = len(GRAY_RAMP)
CONFIG_FILE_PATH = "./config.json"

def load_config() -> Any:
    with open(CONFIG_FILE_PATH, "r") as f:
        config = json.load(f)
    return config

config = load_config()

MAX_WIDTH = config.get("maxWidth")
MAX_HEIGHT = config.get("maxHeight")
TERMINAL_ASPECT_RATIO = config.get("terminalAspectRatio")


def convert_video_to_ascii_frames(video_path: str, output_directory: str = "./output/ascii_frames", output_file_name: str = "ascii_frame") -> str:
    video_frames_path = convert_video_to_frames(video_path=video_path)
    return convert_image_frames_to_ascii(input_directory=video_frames_path, output_directory=output_directory, output_file_name=output_file_name)

def convert_video_to_frames(video_path: str, output_directory: str = "./output/image_frames", output_file_name: str = "frame_", output_file_extension: str = "jpg") -> str:
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        raise ValueError("Could not open video file")
    if output_file_extension not in ["jpg", "jpeg", "png"]:
        raise ValueError("Unsupported or invalid output file extension")
    if not bool(re.match(r'^[a-zA-Z0-9_]+', output_file_name)):
        raise ValueError("Output file name must contain only alphanumeric characters and underscores")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    frame_count = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break
        frame_path = f"{output_directory}/{output_file_name}{frame_count}.{output_file_extension}"
        cv2.imwrite(frame_path, frame)
        frame_count += 1
    video.release()
    return output_directory

def convert_image_frames_to_ascii(input_directory: str, output_directory: str = "./output/ascii_frames", output_file_name: str = "ascii_frame") -> str: 
    print(input_directory)
    if not os.path.exists(input_directory):
        raise ValueError("Input directory does not exist")
    if os.listdir(input_directory) == []:
        raise ValueError("Input directory is empty")
    if not bool(re.match(r'^[a-zA-Z_]+', output_file_name)):
        raise ValueError("Output file name must contain only alphabetic characters and underscores")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    for filename in os.listdir(input_directory):
        if os.path.isfile(os.path.join(input_directory, filename)):
            image_path = os.path.join(input_directory, filename)
            image = Image.open(image_path).convert('RGB')
            width, height = image.size
            width, height = clamp_dimensions(width, height)
            image = image.resize((width, height))
            pixels = list(image.getdata())
            ascii = ""
            for y in range(height):
                for x in range(width):
                    pixel = pixels[y * width + x]
                    r, g, b = pixel
                    grayscale = convert_rgb_to_grayscale(r, g, b)
                    ascii += get_characters_for_grayscale(grayscale)
                ascii += '\n'
            image.close()
            with open(os.path.join(output_directory, f"{filename}_{output_file_name}.txt"), "w") as f:
                f.write(ascii)
    return output_directory

def convert_rgb_to_grayscale(r: int, g: int, b: int) -> int:
    return r * 0.21 + g * 0.72 + b * 0.07

def get_characters_for_grayscale(grayscale: int) -> str:
    return GRAY_RAMP[math.ceil((RAMP_LENGTH - 1) * grayscale / 255)]

def clamp_dimensions(width: int, height: int) -> tuple[int, int]:
    new_width = min(MAX_WIDTH, width)
    new_height = min(MAX_HEIGHT, int(new_width * TERMINAL_ASPECT_RATIO))
    return (new_width, new_height)