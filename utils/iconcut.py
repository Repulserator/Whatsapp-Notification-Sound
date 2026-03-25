from PIL import Image, ImageDraw
import os

# 🔧 CONFIG
INPUT_IMAGE = "icons/input.jpg"   # your source image
OUTPUT_NAME = "icon"       # base name
SIZES = [16, 32, 48, 128]  # icon sizes
OUTPUT_DIR = "icons"


def crop_circle(image):
    width, height = image.size

    # smallest side determines circle diameter
    diameter = min(width, height)

    # center crop square first
    left = (width - diameter) // 2
    top = (height - diameter) // 2
    right = left + diameter
    bottom = top + diameter

    square = image.crop((left, top, right, bottom))

    # create circular mask
    mask = Image.new("L", (diameter, diameter), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, diameter, diameter), fill=255)

    # apply mask
    result = Image.new("RGBA", (diameter, diameter))
    result.paste(square, (0, 0), mask)

    return result


def generate_icons(input_path):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    img = Image.open(input_path).convert("RGBA")

    circle_img = crop_circle(img)

    for size in SIZES:
        resized = circle_img.resize((size, size), Image.LANCZOS)

        output_path = os.path.join(OUTPUT_DIR, f"{OUTPUT_NAME}{size}.png")
        resized.save(output_path)

        print(f"✅ Saved: {output_path}")


if __name__ == "__main__":
    generate_icons(INPUT_IMAGE)