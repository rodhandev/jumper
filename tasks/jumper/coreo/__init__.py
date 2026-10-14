"""jumper.coreo -- a choreography written as a behaviour script, learned by imitation.

A one-shot clip on the dance machinery, like the gesture tasks: the environment is
`tasks/jumper/common/dance/env.py`, and what this directory adds is the clip and
the numbers.

## The clip

`media/<name>.npz`, written by the external `coreo` tool (Zymbiotek's Jumper
workspace, `coreo/`) from a timed behaviour script (a *guion*): named postures per
limb group on a beat grid, interpolated at minimum jerk, the right claw mirrored
from the left as an offset from `HOME`, joint ranges and speed checked, the body
shifted over the four legs by IK wherever a claw is up (at HOME the centre of mass
is 17 mm ahead of the middle feet, so a raised pair of claws otherwise tips the
robot onto its face), and the base pose solved by `tools/import_wbc_gestures.py`'s
resting-floor solver. Every posture
in its library is a frame of one of the committed gesture clips.

The clip committed now is `saludo` (10.1 s at 100 bpm): the robot leans back and
waves the left claw, offers it sitting back, and bows. It starts and ends at `HOME`
and holds `HOME` for half a second at the end, so it hands back to walking from a
still stance.

Swapping the clip means taking this one out (`media/` holds one of each kind) and
re-measuring the numbers in `env_cfg.py`, which are derived from this clip.
There is no music in `media/`: export with `--no-video`.
"""

from __future__ import annotations

from ...registry import register
from ..common.assets import JUMPER_ASSETS

register(
    id="jumper.coreo",
    assets=JUMPER_ASSETS,
    description="jumper hexapod imitating a choreography compiled from a behaviour "
                "script by the coreo tool; the clip is committed in tasks/jumper/coreo/media/",
    tags=("imitation", "jumper", "gesture", "flat"),
)
