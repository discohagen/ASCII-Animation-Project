# ASCII Animation Project

This project started with me wanting to convert a GIF to ASCII art,
which gets animated in my terminal.

It now consists of two (almost) ready-to-use modules for conversions and animation.
These are designed to be used together, but can probably be used individually.

## Project Structure

-   `media_converter.py`:
    The Module to convert any Video files into its Frames (as jpeg, jpg or png)
    and or these into ASCII art represtantations (as txt files).
    It also consists of some helper functions and is partly controlled by the `config.json`
-   `config.json`:
    These configs consist of maximum dimensions to use when turning an image / frame into ASCII art
    and an aspect ratio of your terminal, which can be estimated and configured by you.
-   `animation.py`:
    The Module to animate given txt files in your terminal.
-   `showcase.py`:
    A showcase of how you could use the two mentioned Modules.

## Installation

1. Clone the repository:

```
git clone https://github.com/discohagen/ascii-animation-project.git
```

2. Navigate to the project directoy:

```
cd ascii-animation-project
```

3. Install the required Python packages:

```
pip install opencv-python Pillow
```

4. Run the `showcase.py` script too see an usage example.

```
python3 showcase.py
```

## Dependencies

To function you also need to install the packages OpenCV and Pillow.
As an Example you can install these packages throguh pip:

```

pip install opencv-python Pillow

```

Also make sure to have pythons standard library packages math, os, re, json (and typing) installed.
