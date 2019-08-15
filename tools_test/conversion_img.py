# encoding: utf-8
import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np

ia.seed(1)

sometimes = lambda aug: iaa.Sometimes(0.5, aug)

def func_images(images, random_state, parents, hooks):
    images[:, ::2, :, :] = 0
    return images

def func_keypoints(keypoints_on_images, random_state, parents, hooks):
    return keypoints_on_images

seq = iaa.Sequential([

    # horizontal flips
    iaa.Fliplr(0.5),

    #  random crops
    iaa.Crop(percent=(0, 0.1)),

    # Small gaussian blur with random sigma between 0 and 1.
    # But we only blur about 50% of all images.
    iaa.Sometimes(0.5, iaa.GaussianBlur(sigma=(0, 2))),

    # Strengthen or weaken the contrast in each image.
    iaa.ContrastNormalization((0.5, 2)),

    # Add gaussian noise.
    # For 50% of all images, we sample the noise once per pixel.
    # For the other 50% of all images, we sample the noise per pixel AND
    # channel. This can change the color (not only brightness) of the
    # pixels.
    iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5),
    # Make some images brighter and some darker.
    # In 20% of all cases, we sample the multiplier once per channel,
    # which can end up changing the color of the images.
    iaa.Multiply((0.8, 1.2), per_channel=0.2),
    # Apply affine transformations to each image.
    # Scale/zoom them, translate/move them, rotate them and shear them.
    iaa.Affine(
        scale={"x": (0.8, 1.2), "y": (0.8, 1.2)},
        translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)},
        rotate=(-25, 25),
        shear=(-8, 8)
    ),
    iaa.Multiply((0.8, 1.2), per_channel=0.2),


    #iaa.Sometimes(0.5, iaa.Lambda(func_images=func_images, func_keypoints=func_keypoints)),

    #iaa.Sometimes(0.5, iaa.AverageBlur(k=10, name=None, deterministic=False, random_state=True)),

    # iaa.Sometimes(0.5, iaa.PiecewiseAffine(scale=0,
    #                                        nb_rows=4,
    #                                        nb_cols=4,
    #                                        order=1,
    #                                        cval=0,
    #                                        mode='constant',
    #                                        name=None,
    #                                        deterministic=False,
    #                                        random_state=True)),


], random_order=True)


ia.seed(1)

def get_imgs(imgs):
    # imgs:(N,cls,h,w)
    imgs = np.transpose(imgs, (0, 2, 3, 1)) #(N,h,w,cls)
    images_aug = seq.augment_images(imgs)
    images_aug = np.transpose(images_aug, (0, 3, 1, 2))  # (N,h,w,cls)
    return images_aug