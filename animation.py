import os
import time


def animate_ascii_frames_in_terminal(ascii_frame_path: str, fps: int, looping: bool = False, max_runtime: int = None) -> None:
    if not os.path.exists(ascii_frame_path):
        raise ValueError("ASCII frame directory does not exist")
    if os.listdir(ascii_frame_path) == []:
        raise ValueError("ASCII frame directory is empty")
    if fps < 1:
        raise ValueError("Unexpected fps value")
    if looping and not max_runtime:
        # default for looping animation without given max_runtime
        max_runtime = 60                                                
    ascii_files = sorted(os.listdir(ascii_frame_path), key=lambda x: int(''.join(filter(str.isdigit, x))))
    num_files = len(ascii_files)
    start_time = time.time()
    while looping:
        for i, file in enumerate(ascii_files):
            with open(os.path.join(ascii_frame_path, file), 'r') as f:
                ascii_art = f.read()
            print('\033c', end='')
            print(ascii_art)
            time.sleep(1 / fps)
            if time.time() - start_time >= max_runtime:
                return
            if i == num_files - 1:
                i = 0
            else:
                i += 1
    return