class GarageServo:

    home_pos = 0
    park_pos = 0
    cur_pos = 0
    channel = 0
    stop_dc = 0
    down_dc = 2
    up_dc = 11
    up_rate = 1

    def __init__(self, home_pos, park_pos, channel, stop_dc):
        self.home_pos = home_pos
        self.park_pos = park_pos
        self.channel = channel
        self.stop_dc = stop_dc

    def set_pos(self, pos):
        self.cur_pos = pos

    def set_home(self, pos):
        self.home_pos = pos

    def set_channel(self, channel):
        self.channel = channel

    def set_park_pos(self, park_pos):
        self.park_pos = park_pos