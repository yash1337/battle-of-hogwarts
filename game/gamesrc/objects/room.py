"""

Template module for Rooms

Copy this module up one level and name it as you like, then
use it as a template to create your own Objects.

To make the default commands (such as @dig) default to creating rooms
of your new type, change settings.BASE_ROOM_TYPECLASS to point to
your new class, e.g.

settings.BASE_ROOM_TYPECLASS = "game.gamesrc.objects.myroom.MyRoom"

Note that objects already created in the database will not notice
this change, you have to convert them manually e.g. with the
@typeclass command.

"""

from ev import Room as DefaultRoom
from game.gamesrc.scripts.script import IrregularEvent
import random

class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """
    pass

#------------------------------------------------------------
#
# Weather room - scripted room
#
# The weather room is called by a script at
# irregular intervals.
#
#------------------------------------------------------------

class WeatherRoom(Room):
    """
    This should probably better be called a rainy room...

    This sets up an outdoor room typeclass. At irregular intervals,
    the effects of weather will show in the room. Outdoor rooms should
    inherit from this.

    """
    def at_object_creation(self):
        "Called when object is first created."
        super(WeatherRoom, self).at_object_creation()

        # we use the imported IrregularEvent script
        self.scripts.add(IrregularEvent)

    def update_irregular(self):
        "create a tuple of possible texts to return."
        strings = (
            "The rain coming down from the iron-grey sky intensifies.",
            "A gush of wind throws the rain right in your face. Despite your cloak you shiver.",
            "The rainfall eases a bit and the sky momentarily brightens.",
            "For a moment it looks like the rain is slowing, then it begins anew with renewed force.",
            "The rain pummels you with large, heavy drops. You hear the rumble of thunder in the distance.",
            "The wind is picking up, howling around you, throwing water droplets in your face. It's cold.",
            "Bright fingers of lightning flash over the sky, moments later followed by a deafening rumble.",
            "It rains so hard you can hardly see your hand in front of you. You'll soon be drenched to the bone.",
            "Lightning strikes in several thundering bolts, striking the trees in the forest to your west.",
            "You hear the distant howl of what sounds like some sort of dog or wolf.",
            "Large clouds rush across the sky, throwing their load of rain over the world.")

        # get a random value so we can select one of the strings above.
        # Send this to the room.
        irand = random.randint(0, 15)
        if irand > 10:
            return  # don't return anything, to add more randomness
        self.msg_contents("{w%s{n" % strings[irand])