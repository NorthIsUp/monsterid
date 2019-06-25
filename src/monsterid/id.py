"""
Build a monsterid image
"""
import os
import random
from hashlib import md5
from PIL import Image
from PIL.ImageDraw import ImageDraw


def build_monster(seed=None, size=None):
    """
    Function to create a monsterid, based on seed and size
    """
    # Capture random state
    rand_state = random.getstate()

    if not seed:
        seed = md5(bytes(str(random.getrandbits(128)), 'utf-8')).hexdigest()

    random.seed(seed)

    parts = (
        ('legs', random.randint(0, 4), random.randint(1, 5)),
        ('hair', random.randint(0, 4), random.randint(1, 5)),
        ('arms', random.randint(0, 4), random.randint(1, 5)),
        ('body', random.randint(0, 4), random.randint(1, 15)),
        ('eyes', random.randint(0, 4), random.randint(1, 15)),
        ('mouth', random.randint(0, 4), random.randint(1, 10)),
    )

    # Restore random state
    random.setstate(rand_state)

    # Make a base monster:
    monster_im = Image.new('RGB', (120, 120))
    monster_id = ImageDraw(monster_im)
    monster_id.rectangle((0, 0, 120, 120), fill="white", outline="white")

    for part, flip, index in parts:  # pylint: disable=unused-variable
        filepath = os.path.join(
            os.path.dirname(__file__),
            'parts',
            '%s_%d.png' % (part, index))
        part_im = Image.open(filepath)
        monster_im.paste(part_im, (0, 0), part_im)

    if size:
        monster_im = monster_im.resize(size, Image.ANTIALIAS)
    return monster_im
