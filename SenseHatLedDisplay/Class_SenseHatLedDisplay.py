import time
from SenseHatCustomExceptions import DisplayErrors as DiEr
from SenseHatLedDisplay import show_animated as anim
from SenseHatLedDisplay import show_pictures as pict

LIVE = None
try:
    from sense_hat import SenseHat
    LIVE = True
except ImportError as e1:
    try:
        from sense_emu import SenseHat
        LIVE = False
    except ImportError as e2:
        raise DiEr.MissingDisplay()

print("===========================")
print("= using: {:^16} =".format({True: "SenseHat", False: "Emulator"}[LIVE]))
print("===========================")


class LedDisplay:
    """=== Class name: LedDisplay ======================================================================================
    Main Led Display Object, to display a set of different images and animations
    on RaspberryPi's SenseHat 8x8 LED Display
    ============================================================================================== by Sziller ==="""
    def __init__(self,
                 dyn: bool = True,
                 alias: int = 0,
                 duration: int = 0,
                 low_light: bool = True,
                 heartbeat: float = 0.1):
        self.sense                      = SenseHat()
        self.sense.low_light            = low_light
        self.duration: int              = duration
        self.heartbeat: float = heartbeat
        
        self.dynamic: bool              = dyn
        self.alias: int                 = alias

        self.pattern_dict               = PATTERN_DICT
        self.image_dict                 = IMAGE_DICT
        
        self.delta_t_h = -2  # time as returned by time.time - your time
        self.delta_t_m = 0

    def run(self):
        """=== Method name: run ========================================================================================
        Method actually runs instance.
        ========================================================================================== by Sziller ==="""
        starting_time = time.time()
        ellapsed_time = 0
        if self.dynamic:
            while ellapsed_time < self.duration:
                current_time = time.time()
                ellapsed_time = current_time - starting_time
                kwargs = {'coldict': COL_DICT, 'ellapsed': ellapsed_time}
                flatmat = self.pattern_dict[self.alias](**kwargs)
                
                self.sense.set_pixels(flatmat)
                time.sleep(self.heartbeat)
        else:
            kwargs = {'coldict': COL_DICT, 'title': self.image_dict[self.alias]}
            flatmat = pict.picture(**kwargs)
            self.sense.set_pixels(flatmat)
            time.sleep(self.heartbeat)


PATTERN_DICT    = {0: anim.mode_0, 1: anim.mode_1, 2: anim.mode_2}
IMAGE_DICT      = {0: "heart", 1: "smiley", 2: "snail", 3: "target", 4: "sun"}
COL_DICT        = {0: (0, 0, 0), 1: (0, 0, 0), 2: (0, 0, 0), 3: (0, 0, 0),
                   4: (125, 0, 0), 5: (0, 125, 0), 6: (0, 0, 125),
                   7: (125, 125, 0), 8: (125, 0, 125), 9: (0, 125, 125)}


if __name__ == "__main__":
    display = LedDisplay(dyn=True, alias=1, duration=30)
    display.run()
