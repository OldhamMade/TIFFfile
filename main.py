from tifffile import TIFFfile

def main():
    for page in TIFFfile('ullswater.tiff'):
        for tag in page.tags.values():
            if not tag.name.isdigit():
                print tag.name, tag.code, tag.dtype, tag.count, tag.value
