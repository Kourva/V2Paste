#!/usr/bin/env python3


# Author: Kourva
# Github: https://github.com/kourav/V2Paste
# About : Create Vless proxies via given config with this simple app


# Imports
import sys
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.actionbar import *


# KV config
for Sources in ["main.kv", "help.kv"]:
    with open("Sources/%s" % Sources, "r") as kv:
        Builder.load_string(kv.read())


# StartMenu screen
class MainMenuScreen(Screen):
    # Path to font
    Cyberverse = "Sources/Assets/Cyberverse.otf"

    # Path to background
    background = "Sources/Assets/background.jpg"

    # Vless generator
    def vless_generator(self, worker, doprax, uuid, alias, address, output) -> None:
        # Sends error if any of fields are empty
        if (
            worker.text == ""
            or doprax.text == ""
            or alias.text == ""
            or address.text == ""
        ):
            output.text = "[b][color=#ff0000]Fill the requirements!![/color][/b]"

        # Copies the Vless proxy to Clipboard
        else:
            vless_url = f"vless://{uuid.text}@{address.text}?encryption=none&security=tls&sni={worker.text}&alpn=http%2F1.1&type=ws&host={worker.text}&path=/vless#{alias.text}"
            Clipboard.copy(vless_url)
            output.text = f"[b]Copied to Clipboard.[/b]"


# HelpManu screen
class HelpMenuScreen(Screen):
    # Path to font
    Cyberverse = "Sources/Assets/Cyberverse.otf"

    # Path to background
    background = "Sources/Assets/background.jpg"


# Main class
class V2PasteApp(App):
    # Build method
    def build(self):
        # Root screen
        root = ScreenManager()

        # Main menu screen
        self.MainMenuScreen = MainMenuScreen(name="MainMenu")
        root.add_widget(self.MainMenuScreen)

        # Help menu screen
        self.HelpMenuScreen = HelpMenuScreen(name="HelpMenu")
        root.add_widget(self.HelpMenuScreen)

        # Set current screen to main menu and return root
        root.current = "MainMenu"
        return root


# Run App
V2PasteApp().run()

# EOF
