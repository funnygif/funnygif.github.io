from PIL import Image, ImageDraw, ImageFont
import sys

def generate_gif(ip, output_file):
    width, height = 200, 100
    image = Image.new('RGB', (width, height), color = (73, 109, 137))
    
    font = ImageFont.load_default()
    d = ImageDraw.Draw(image)
    
    text_position = (10, 40)
    
    d.text(text_position, f'IP: {ip}', font=font, fill=(255, 255, 255))
    
    image.save(output_file, save_all=True, append_images=[image], loop=0, duration=500)

if __name__ == "__main__":
    ip = sys.argv[1]
    output_file = sys.argv[2]
    generate_gif(ip, output_file)
