"""jumper.coreo_dj -- the contest video's first part, written with coreo, learned by imitation.

A clip on the dance machinery, like `jumper.coreo_romantico`: the environment is
`tasks/jumper/common/dance/env.py`, and what this directory adds is the clip and
the numbers.

## The clip

`media/dj.npz` (12.0 s), written by the external `coreo` tool (rodhandev/jumper-coreo)
from `guiones/video-v2-B1.guion`, on the beats of an original 120 bpm track
(generated with ACE-Step, so its rights are ours): the robot hears «turn down the
heating» as «turn up the beat», scratches its head while it thinks, and plays DJ
twice -- one claw on its «headphones», the other scratching a record on the half
beat, the body bouncing on the beat. coreo's `puente/instrumento.py` hears
electronic music in that track, which is why the step is `dj`. coreo detoured the
claws where they would cross, balanced the body over the four legs wherever a claw
is up, checked joint speed, self-collision, tilt and the servo's torque curve
(`puente/factible.py`), and solved the base pose with
`tools/import_wbc_gestures.py`'s resting-floor solver.

The music is not in `media/` (training never reads it): export with `--no-video`.
"""

from __future__ import annotations

from ...registry import register
from ..common.assets import JUMPER_ASSETS

register(
    id="jumper.coreo_dj",
    assets=JUMPER_ASSETS,
    description="jumper hexapod imitating a DJ dance written with coreo "
                "(think, then scratch and bounce); the clip is committed in tasks/jumper/coreo_dj/media/",
    tags=("imitation", "jumper", "dance", "flat"),
)
