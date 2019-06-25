from id import build_monster
from hashlib import md5
from path import path
import random
import subprocess

seed = md5(str(random.getrandbits(128))).hexdigest()
size = (120, 120)

monster = build_monster(seed=seed, size=size)

out = path('/tmp') / seed + '.png'
monster.save(out)

print(out)
subprocess.Popen(('open', out))
