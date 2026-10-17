"""jumper.coreo_duo -- a duet and a phone call written with coreo for the contest video, learned by imitation.

A clip on the dance machinery, like `jumper.coreo_romantico`: the environment is
`tasks/jumper/common/dance/env.py`, and what this directory adds is the clip and
the numbers.

## The clip

`media/duo.npz` (24.7 s), written by the external `coreo` tool (rodhandev/jumper-
coreo) from `guiones/video-v3-duo.guion`: the robot answers a phone call (points at
the phone beside it, pokes twice in the air, waves), then plays the piano for the
duet with the second Jumper on the beats where the first plays the violin (92 bpm
ballad; coreo's `puente/instrumento.py` hears violin and piano in that track: one to
each robot). coreo detoured the claws where they would cross, balanced the body over
the four legs wherever a claw is up, checked joint speed, self-collision, tilt and
the servo's torque curve (`puente/factible.py`, with the phone on the desk as an
obstacle), and solved the base pose with `tools/import_wbc_gestures.py`'s resting-
floor solver.

The music is not in `media/` (training never reads it): export with `--no-video`.
"""

from __future__ import annotations

from ...registry import register
from ..common.assets import JUMPER_ASSETS

register(
    id="jumper.coreo_duo",
    assets=JUMPER_ASSETS,
    description="jumper hexapod imitating a duet and a phone call written with coreo "
                "(answer a call, then piano for the duet); the clip is committed in tasks/jumper/coreo_duo/media/",
    tags=("imitation", "jumper", "dance", "flat"),
)
