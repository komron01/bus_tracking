from PIL import Image, ImageDraw, ImageFont

def text_to_png(input_text, output_path, font_size=20, image_size=(300, 150), background_color=(255, 255, 255), text_color=(0, 0, 0), transparent_background=False):
    # Create a new image with the specified size and background color
    if transparent_background:
        img = Image.new("RGBA", image_size, (0, 0, 0, 0))
    else:
        img = Image.new("RGB", image_size, background_color)

    # Create a drawing object
    draw = ImageDraw.Draw(img)

    # Use a default font (you can customize the font by providing the path to a TTF file)
    font = ImageFont.truetype("arial.ttf", font_size)

    # Calculate text position to center it in the image
    textbbox = draw.textbbox((0, 0), input_text, font=font)
    text_position = ((image_size[0] - textbbox[2]) // 2, (image_size[1] - textbbox[3]) // 2)

    # Add text to the image
    draw.text(text_position, input_text, font=font, fill=text_color)

    # Save the image to the specified file path
    img.save(output_path)

# Example usage
for i in range(46,100):
    text_to_png(str(i), str(i)+".png", font_size=40, image_size=(70, 90), background_color=(255, 255, 255), text_color=(0, 0, 0), transparent_background=True)
