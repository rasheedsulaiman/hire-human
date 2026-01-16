#!/usr/bin/env python3
"""
Create a favicon PNG with hh-symbol on a colored background.
"""
from PIL import Image

def create_favicon(symbol_path, output_path, bg_color='#f47753', size=512):
    """
    Create a favicon with the symbol on a colored background.
    
    Args:
        symbol_path: Path to the hh-symbol.png
        output_path: Path to save the favicon
        bg_color: Background color (hex)
        size: Size of the favicon (will be square)
    """
    # Open the symbol image
    symbol = Image.open(symbol_path)
    
    # Convert hex color to RGB
    bg_color = bg_color.lstrip('#')
    bg_rgb = tuple(int(bg_color[i:i+2], 16) for i in (0, 2, 4))
    
    # Create a square background with the specified color
    background = Image.new('RGB', (size, size), bg_rgb)
    
    # Convert symbol to RGBA if it isn't already
    if symbol.mode != 'RGBA':
        symbol = symbol.convert('RGBA')
    
    # Calculate size to fit symbol with some padding
    padding = int(size * 0.1)  # 10% padding
    max_symbol_size = size - (2 * padding)
    
    # Resize symbol to fit within the background with padding
    symbol.thumbnail((max_symbol_size, max_symbol_size), Image.Resampling.LANCZOS)
    
    # Calculate position to center the symbol
    symbol_width, symbol_height = symbol.size
    x = (size - symbol_width) // 2
    y = (size - symbol_height) // 2
    
    # Paste the symbol onto the background
    background.paste(symbol, (x, y), symbol)
    
    # Save the favicon
    background.save(output_path, 'PNG', optimize=True)
    print(f"Created favicon: {output_path}")
    print(f"Size: {size}x{size}px")
    print(f"Background color: #{bg_color}")

def main():
    symbol_path = "assets/hh-symbol.png"
    output_path = "assets/favicon.png"
    
    # Create favicon at 512x512 (common size for modern favicons)
    create_favicon(symbol_path, output_path, bg_color='#f47753', size=512)
    
    # Also create a smaller 32x32 version
    create_favicon(symbol_path, "assets/favicon-32x32.png", bg_color='#f47753', size=32)
    
    # And a 16x16 version
    create_favicon(symbol_path, "assets/favicon-16x16.png", bg_color='#f47753', size=16)

if __name__ == "__main__":
    main()
