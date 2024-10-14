from PIL import Image, ImageEnhance

# Brightness
def brightness(img, value):
    enhancer = ImageEnhance.Brightness(img)
    factor = (value + 1)  # -1 to 1 where 0 means no change
    return enhancer.enhance(factor)

# Contrast
def contrast(img, value):
    enhancer = ImageEnhance.Contrast(img)
    factor = (value + 1)  # -1 to 1 where 0 means no change
    return enhancer.enhance(factor)

# Whites (lighter areas)
def whites(img, value):
    r, g, b = img.split()
    factor = (value + 1)
    
    # Apply the factor only to the lighter areas
    r = r.point(lambda i: min(i * factor if i > 128 else i, 255))
    g = g.point(lambda i: min(i * factor if i > 128 else i, 255))
    b = b.point(lambda i: min(i * factor if i > 128 else i, 255))
    
    return Image.merge('RGB', (r, g, b))

# Blacks (darker areas)
def blacks(img, value):
    r, g, b = img.split()
    factor = (value + 1)
    
    # Apply the factor only to the darker areas
    r = r.point(lambda i: max(i * factor if i < 128 else i, 0))
    g = g.point(lambda i: max(i * factor if i < 128 else i, 0))
    b = b.point(lambda i: max(i * factor if i < 128 else i, 0))
    
    return Image.merge('RGB', (r, g, b))

# Temperature (blue to orange)
def temperature(img, value):
    r, g, b = img.split()
    factor = (value + 1)
    
    if value < 0:  # Warmer (enhance red and green)
        r = r.point(lambda i: min(i * (2 - factor), 255))
        g = g.point(lambda i: min(i * (2 - factor), 255))
    elif value > 0:  # Cooler (enhance blue)
        b = b.point(lambda i: min(i * factor, 255))
    
    return Image.merge('RGB', (r, g, b))

def tint(img, value):
    r, g, b = img.split()
    factor = (value + 1)

    if value < 0:  # Green tint (increase green only)
        g = g.point(lambda i: min(i * (2 - factor), 255))  # Increase green
    elif value > 0:  # Pink tint (increase red and blue only)
        r = r.point(lambda i: min(i * factor, 255))  # Increase red
        b = b.point(lambda i: min(i * factor, 255))  # Increase blue

    return Image.merge('RGB', (r, g, b))

    
    return Image.merge('RGB', (r, g, b))

# Saturation
def saturation(img, value):
    enhancer = ImageEnhance.Color(img)
    factor = (value + 1)  # -1 to 1 where 0 means no change
    return enhancer.enhance(factor)
