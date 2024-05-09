import media_converter
import animation


def showcase():
    VIDEO_PATH = "./showcase/video/showcase.gif"
    ascii_frame_path = media_converter.convert_video_to_ascii_frames(video_path=VIDEO_PATH)
    animation.animate_ascii_frames_in_terminal(ascii_frame_path=ascii_frame_path, fps=12.5, looping=True, max_runtime=8)

if __name__ == "__main__":
    showcase()