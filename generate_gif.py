from PIL import Image, ImageDraw, ImageFont
import sys

def generate_gif(ip, output_file):
    # Create a blank image 
    width, height = 200, 100
    image = Image.new('RGB', (width, height), color = (73, 109, 137))
    
    # Use a font
    font = ImageFont.load_default()
    d = ImageDraw.Draw(image)
    
    # Position of the IP text
    text_position = (10, 40)
    
    # Draw the IP address on the image
    d.text(text_position, f'IP: {ip}', font=font, fill=(255, 255, 255))
    
    # Save the image
    image.save(output_file, save_all=True, append_images=[image], loop=0, duration=500)

if __name__ == "__main__":
    ip = sys.argv[1]
    output_file = sys.argv[2]
    generate_gif(ip, output_file)
