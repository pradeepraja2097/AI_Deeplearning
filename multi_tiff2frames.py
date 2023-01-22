from PIL import Image, ImageSequence

im = Image.open("/home/pradeep/Downloads/Semantic_unet_model/mask/training_groundtruth.tif")

for i, page in enumerate(ImageSequence.Iterator(im)):
    page.save("/home/pradeep/Downloads/Semantic_unet_model/mask/frame%d.jpg" % i)
