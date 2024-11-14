from PIL import Image
import shutil
import sys
import os.path

def block(fc=None, bc=None) -> str:
    """Generate a block character with foreground and background colors."""
    fg_code = f'\033[38;2;{fc[0]};{fc[1]};{fc[2]}m' if fc else ''
    bg_code = f'\033[48;2;{bc[0]};{bc[1]};{bc[2]}m' if bc else ''
    reset_code = '\033[0m'
    return f'{fg_code}{bg_code}\u2584{reset_code}'

def fit_image_to_terminal(image, terminal_size) -> Image.Image:
    """Resize the image to fit within the terminal dimensions."""
    term_height, term_width = terminal_size
    new_height = term_height * 2
    new_width = int(new_height / image.height * image.width)
    
    if new_width > term_width * 2:
        new_width = term_width * 2
        new_height = int(new_width / image.width * image.height)
    
    return image.resize((new_width, new_height))

def img2txt(img_path: str) -> None:
    try:
        img = Image.open(img_path).convert('RGB')
        terminal_size = shutil.get_terminal_size(fallback=(80, 24))
        resized_img = fit_image_to_terminal(img, (terminal_size.lines, (terminal_size.columns - 4) // 2))
        
        
        for y in range(0, resized_img.height, 2):
            output = ""
            for x in range(resized_img.width):
                fc = resized_img.getpixel((x, min(y + 1, resized_img.height - 1)))
                bc = resized_img.getpixel((x, y))
                output += block(fc, bc)
            print(output)

    except IOError as e:
        print(f"Error opening image file: {e}")
        return ""

def show_help():
    print("Display an image on the terminal")
    print("Usage:")
    print("  imgcat <image_path>")

def main():
    if len(sys.argv) != 2 or not os.path.isfile(sys.argv[1]):
        if not os.path.isfile(sys.argv[1]):
            print("File does not exist")
        show_help()
    else:
        image_path = sys.argv[1]
        img2txt(image_path)

if __name__ == "__main__":
    main()