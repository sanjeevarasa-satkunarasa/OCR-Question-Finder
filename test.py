from PIL import Image, ImageDraw

def text_to_png(text, output_file):
    # Calculate the size of the image based on the length of the text
    image_width = len(text) * 10
    image_height = 20
    
    # Create a new image with a white background
    image = Image.new('RGB', (image_width, image_height), 'white')
    
    # Create a drawing object
    draw = ImageDraw.Draw(image)
    
    # Draw the text on the image
    draw.text((5, 5), text, fill='black')
    
    # Save the image
    image.save(output_file)

# Example usage
text_to_png("Hello, World!", "output.png")
