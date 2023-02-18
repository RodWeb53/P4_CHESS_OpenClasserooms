"""Module main pour lancer l'application"""
from controllers.application_controller import ApplicationController

if __name__ == "__main__":
    app = ApplicationController()

    app.start()
    