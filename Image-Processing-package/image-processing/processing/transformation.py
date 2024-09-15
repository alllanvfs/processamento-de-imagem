from skimage.transform import resize

def resize_image(image, propotion):
    assert 0 <= propotion <= 1, 'aplica a validacao da imagem entre 0 e 1'
    height = round(image.shape[0] * propotion)
    width = round(image.shape[1] * propotion)
    image_resize = resize(image, (height, width), anti_aliasing = True)
    return image_resize