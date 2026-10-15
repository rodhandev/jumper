"""jumper.coreo_romantico -- a romantic dance written with coreo, learned by imitation.

A clip on the dance machinery, like `jumper.coreo`: the environment is
`tasks/jumper/common/dance/env.py`, and what this directory adds is the clip and
the numbers.

## The clip

`media/romantico.npz` (28.6 s), written by the external `coreo` tool
(rodhandev/jumper-coreo) from `guiones/video-v2-romantico.guion`, on the beats of an
original 92 bpm track (generated with ACE-Step, so its rights are ours): a wave, a
head-scratch while it "thinks", the claws playing a violin, kisses, a sway and a
bow, steps from coreo's library. coreo detoured the claws where they would cross,
balanced the body over the four legs wherever a claw is up, checked joint speed,
self-collision and tilt, and solved the base pose with
`tools/import_wbc_gestures.py`'s resting-floor solver.

The music is not in `media/` (7 MB, and training never reads it): export with
`--no-video`.
"""

from __future__ import annotations

from ...registry import register
from ..common.assets import JUMPER_ASSETS

register(
    id="jumper.coreo_romantico",
    assets=JUMPER_ASSETS,
    description="jumper hexapod imitating a romantic dance written with coreo "
                "(wave, think, violin, kisses, bow); the clip is committed in tasks/jumper/coreo_romantico/media/",
    tags=("imitation", "jumper", "dance", "flat"),
)
