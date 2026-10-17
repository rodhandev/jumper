"""jumper.coreo_batalla -- a battle written with coreo for the contest video, learned by imitation.

A clip on the dance machinery, like `jumper.coreo_romantico`: the environment is
`tasks/jumper/common/dance/env.py`, and what this directory adds is the clip and
the numbers.

## The clip

`media/batalla.npz` (8.5 s), written by the external `coreo` tool (rodhandev/jumper-
coreo) from `guiones/video-v3-batalla.guion`: Jumper Arena, the battle from the
phone app: on guard (claws up in front, shaken), aims and fires (the shot is the
app's augmented reality; the robot only aims), takes a hit (leans back behind a
claw), twice, at 120 bpm. coreo detoured the claws where they would cross, balanced
the body over the four legs wherever a claw is up, checked joint speed, self-
collision, tilt and the servo's torque curve (`puente/factible.py`, with the phone
on the desk as an obstacle), and solved the base pose with
`tools/import_wbc_gestures.py`'s resting-floor solver.

The music is not in `media/` (training never reads it): export with `--no-video`.
"""

from __future__ import annotations

from ...registry import register
from ..common.assets import JUMPER_ASSETS

register(
    id="jumper.coreo_batalla",
    assets=JUMPER_ASSETS,
    description="jumper hexapod imitating a battle written with coreo "
                "(guard, aim and fire, take a hit); the clip is committed in tasks/jumper/coreo_batalla/media/",
    tags=("imitation", "jumper", "dance", "flat"),
)
