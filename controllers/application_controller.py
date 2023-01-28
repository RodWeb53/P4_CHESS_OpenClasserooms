""" Module controller"""
from .menu_home_controller import HomeMenuController

class ApplicationController:

    def __init__(self):
        self.controller = None

    def start(self):
        self.controller = HomeMenuController()
        while self.controller:
            self.controller = self.controller()
            