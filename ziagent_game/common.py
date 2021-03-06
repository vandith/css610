'''
This file is used to store default settings.
'''

__all__ = ['nagents', 'move_choices', 'get_id', 'payoffs', 'TimeTick']

# default number of agents
nagents = 100

# Game select
move_choices = (
    ('swerve', 0),
    ('straight', 1),
)

payoffs = (
    ((0,0), (1,1)),     #Both players swerve
    ((0,1), (0,2)),     #a1 swerves, a2 goes straight
    ((1,0), (2,0)),     #a1 goes straight, a2 swerves
    ((1,1), (-1,-1)),   #Both players go straight
)

def get_id(obj_class):
    'Function to establish agent ids.'

    try:
        all_ids = [a.id for a in obj_class.instances.values()]
        last_id = sorted(all_ids)[-1]
        return last_id + 1
    except (AttributeError, IndexError) as e:
        return 1

class TimeTick(object):
    """
        Object class that keeps track of the time.
    """

    now = 0

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = 0
        self.update_now()

    def update_now(self):
        'Updates now value.'
        self.__class__.now = self.current

    def inc_time(self):
        'Increases time'
        self.current += 1
        self.update_now()