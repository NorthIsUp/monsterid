from md5 import md5
from path import path
from PIL import Image
from PIL.ImageDraw import ImageDraw
import random


def build_monster(seed=None, size=None):
    #capture random state
    rand_state = random.getstate()

    if not seed:
        seed = md5(str(random.getrandbits(128))).hexdigest()

    random.seed(seed)

    parts = (
        ('legs', random.randint(0, 4), random.randint(1, 5)),
        ('hair', random.randint(0, 4), random.randint(1, 5)),
        ('arms', random.randint(0, 4), random.randint(1, 5)),
        ('body', random.randint(0, 4), random.randint(1, 15)),
        ('eyes', random.randint(0, 4), random.randint(1, 15)),
        ('mouth', random.randint(0, 4), random.randint(1, 10)),
    )

    #restore random state
    random.setstate(rand_state)

    # make a base monster:
    monster_im = Image.new('RGB', (120, 120))
    monster_id = ImageDraw(monster_im)
    monster_id.rectangle((0, 0, 120, 120), fill="white", outline="white")

    for part, flip, index in parts:
        f = path(__file__).dirname().abspath() / 'parts' / '%s_%d.png' % (part, index)
        part_im = Image.open(f)
        monster_im.paste(part_im, (0, 0), part_im)

    if size:
        monster_im = monster_im.resize(size, Image.ANTIALIAS)
    return monster_im
