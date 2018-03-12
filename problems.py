from collections import namedtuple
from pybullet_utils import create_box, set_base_values, set_point
import pybullet as p

Problem = namedtuple('Problem', ['movable', 'surfaces', 'goal_on'])


def holding_problem():
    plane = p.loadURDF("plane.urdf")
    table = p.loadURDF("table/table.urdf")
    box = create_box(.07, .05, .15)
    set_point(box, (0, 0, .7))

    pr2 = p.loadURDF("pr2_description/pr2.urdf", useFixedBase=True)
    set_base_values(pr2, (0, -1, 0))

    return Problem(movable=[box], surfaces=[table], goal_on=[(box, table)])