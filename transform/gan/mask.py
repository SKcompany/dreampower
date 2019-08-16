from transform.gan import ImageTransformGAN
from config import Config as conf


class CorrectToMask(ImageTransformGAN):
    """
    Correct -> Mask [GAN]
    """

    def __init__(self):
        """
        CorrectToMask Constructor
        """
        super().__init__(conf.args['checkpoints']["correct_to_mask"], "correct_to_mask")


class MaskrefToMaskdet(ImageTransformGAN):
    """
    Maskref -> Maskdet [GAN]
    """

    def __init__(self):
        """
        MaskrefToMaskdet Constructor
        """
        super().__init__(conf.args['checkpoints']["maskref_to_maskdet"], "maskref_to_maskdet")


class MaskfinToNude(ImageTransformGAN):
    """
    Maskfin -> Nude [GAN]
    """

    def __init__(self):
        """
        MaskfinToNude Constructor
        """
        super().__init__(conf.args['checkpoints']["maskfin_to_nude"], "maskfin_to_nude")
