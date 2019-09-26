# python native modules

# third-party modules
from PyQt5.QtCore import pyqtSignal

# labtool project modules
from labtool.oscilloscope.base.oscilloscope import Oscilloscope
from labtool.generator.base.generator import Generator


class MeasureAlgorithm(object):
    """ Base class of a MeasureAlgorithm. Defines the way all algorithms
    are instantiated, by receiving the same data to connect with devices
    and set up values.
    """

    def __init__(self,
                 oscilloscope: Oscilloscope,
                 generator: Generator,
                 requirements: dict,
                 channel_setup: dict,
                 trigger_setup: dict,
                 acquire_setup: dict,
                 timebase_setup: dict,
                 generator_setup: dict,
                 preferences_setup: dict):
        self.oscilloscope = oscilloscope
        self.generator = generator
        self.channel_setup = channel_setup
        self.trigger_setup = trigger_setup
        self.acquire_setup = acquire_setup
        self.timebase_setup = timebase_setup
        self.generator_setup = generator_setup
        self.preferences_setup = preferences_setup
        self.requirements = requirements

    def __call__(self, *args, **kwargs):
        raise NotImplemented

    def what(self) -> str:
        raise NotImplemented
