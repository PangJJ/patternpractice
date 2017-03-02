"""

This implementation aims to mimick the problem of many remotes to many TVs

:-> Remote_n_1, Remote_n_2, ...         [DeviceRemote implementations]
:-> AbstractRemote

:-> DeviceTV, DeviceDVD                 [Device implementation]
:-> DeviceAbstract          

A single universal remote should work with the predefined functions of multiple
different devices
"""

class AbstractRemote(object):
    def __init__(self, implementation, device):
        self._implementation = implementation
        self._device = device

    def __getattr__(self, name):
        return getattr(self._device, name)

    def power_button_pressed(self):
        pass
    def button_plus_pressed(self):
        self.volume_up()
    def button_minus_pressed(self):
        self.volume_down()

class UniversalRemote(AbstractRemote):
    def __init__(self, device):
        super(UniversalRemote, self).__init__(UniversalRemote, device)

    def power_button_pressed(self):
        if self.power_state:
            print("[info]", type(self._device), "powered off")
        else:
            print("[info]", type(self._device), "powered on")
        self.power_state = not self.power_state

    def function_button_pressed(self):
        self.next_state()

class ReversalPrankRemote(AbstractRemote):
    def __init__(self, device):
        super(ReversalPrankRemote, self).__init__(ReversalPrankRemote, device)

    def power_button_pressed(self):
        if self.power_state:
            print("[info]", type(self._device), "powered off")
        else:
            print("[info]", type(self._device), "powered on")
        self.power_state = not self.power_state

    def button_plus_pressed(self):
        self.volume_down()
    def button_minus_pressed(self):
        self.volume_up()

    def function_button_pressed(self):
        self.next_state()

class AbstractDevice(object):
    def __init__(self, implementation):
        self._implementation = implementation
        self.power_state = False
        self.volume = 0
        self.saved_state = None

    def power_on(self):
        self.power_state = True

    def power_off(self):
        self.power_state = False

    def volume_up(self):
        self.volume += 1

    def volume_down(self):
        self.volume -= 1

class DeviceToshiba(AbstractDevice):
    def __init__(self):
        super(DeviceToshiba, self).__init__(DeviceToshiba)
        self._MAX_VOLUME = 10
        self._MIN_VOLUME = 0
        self.states = ['ANTENNA', 'HDMI', 'USB_1', 'USB_2']
        self.saved_state = 0

    def volume_up(self):
        if self.volume >= self._MAX_VOLUME:
            self.volume = 0
        else:
            super(DeviceToshiba, self).volume_up()

    def volume_down(self):
        if self.volume <= self._MIN_VOLUME:
            self.volume = 0
        else:
            super(DeviceToshiba, self).volume_down()

    def next_state(self):
        self.saved_state = (self.saved_state + 1) % len(self.states)
        print("[info] State changed: [{new_state}]".format(
                new_state=self.states[self.saved_state]))

class DeviceAltecLansing(AbstractDevice):
    def __init__(self):
        super(DeviceAltecLansing, self).__init__(DeviceAltecLansing)
        self._MAX_VOLUME = 20
        self._MIN_VOLUME = 0
        self.states = ['CINEMATIC', 'DHOBLY SURROUND', 'SURROUND 5.1', 'RAW']
        self.saved_state = 0

    def volume_up(self):
        if self.volume >= self._MAX_VOLUME:
            self.volume = 0
        else:
            super(DeviceAltecLansing, self).volume_up()

    def volume_down(self):
        if self.volume <= self._MIN_VOLUME:
            self.volume = 0
        else:
            super(DeviceAltecLansing, self).volume_down()
    def next_state(self):
        self.saved_state = (self.saved_state + 1) % len(self.states)
        print("[info] State changed: [{new_state}]".format(
                new_state=self.states[self.saved_state]))










