#!/usr/bin/env python3


#  Author  : Kourva
#  Github  : https://github.com/kourva/V2Paste
#  Version : 1.1
#  About   : Create Vless proxies via given config with this simple app
#
#  Changes:
#          + new light UI
#          + Fixed bugs
#          + Multi screen
#          + Notification


# Imports
import sys
import webbrowser

from plyer import notification
from plyer import vibrator
from plyer.utils import platform

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.actionbar import *


# KV config
for Sources in ["main.kv", "settings.kv"]:
    with open("Sources/%s" % Sources, "r") as kv:
        Builder.load_string(kv.read())


# ImageButton
class ImageButton(ButtonBehavior, Image):
    def on_press(self):
        pass


# StartMenu screen
class MainMenuScreen(Screen):
    # Path to font & background
    font = "Sources/Assets/font.ttf"
    background = "Sources/Assets/white.jpg"

    # Load config from config file: so it will save previous config.
    def load_config(self):
        # Uses get_screen to get IDs from another class
        worker = self.manager.get_screen("Settings").ids.CloudFlare
        address = self.manager.get_screen("Settings").ids.IP_address
        port = self.manager.get_screen("Settings").ids.Port
        uuid = self.manager.get_screen("Settings").ids.UUID
        remark = self.manager.get_screen("Settings").ids.Remark
        path = self.manager.get_screen("Settings").ids.Path

        # Loads config file. if face any problem, resets it.
        with open("Data/config.conf", "r") as data:
            lines = data.readlines()
            try:
                worker._set_text(lines[0].split("\n")[0])
                address._set_text(lines[1].split("\n")[0])
                port._set_text(lines[2].split("\n")[0])
                uuid._set_text(lines[3].split("\n")[0])
                remark._set_text(lines[4].split("\n")[0])
                path._set_text(lines[5].split("\n")[0])

            except IndexError:
                worker = ""
                address = ""
                port = ""
                uuid = ""
                remark = ""
                path = ""

    # Vless generator
    def generate(self, output) -> None:
        # Uses get_screen to get IDs from another class
        worker = self.manager.get_screen("Settings").ids.CloudFlare.text
        address = self.manager.get_screen("Settings").ids.IP_address.text
        port = self.manager.get_screen("Settings").ids.Port.text
        uuid = self.manager.get_screen("Settings").ids.UUID.text
        remark = self.manager.get_screen("Settings").ids.Remark.text
        path = self.manager.get_screen("Settings").ids.Path.text

        # Send error notification if any field is empty
        if (
            worker == ""
            or address == ""
            or port == ""
            or uuid == ""
            or remark == ""
            or path == ""
        ):
            title = "Error"
            message = "Fill the requirements"
            ticker = "New message"
            kwargs = {
                "title": title,
                "message": message,
                "ticker": ticker,
                "toast": True,
            }
            notification.notify(**kwargs)

        else:
            vless_url = f"vless://{uuid}@{address}:{port}?encryption=none&security=tls&sni={worker}&alpn=http%2F1.1&type=ws&host={worker}&path=/{path}#{remark}"
            output._set_text(vless_url)

    # Copies the Vless proxy to Clipboard & send notification
    def copy_output(self, output):
        Clipboard.copy(output.text)
        title = "Copied"
        message = "Proxy Copied"
        ticker = "New message"
        kwargs = {
            "title": title,
            "message": message,
            "ticker": ticker,
            "toast": True,
        }
        notification.notify(**kwargs)

    # Resets output text
    def reset_output(self, output):
        output._set_text("")

    # Notify user to wait until the next update
    def notify_next_update(self):
        try:
            vibrator.vibrate(0.3)
        except:
            pass

        title = "Developer"
        message = "This option is under the development"
        ticker = "New message"
        kwargs = {"title": title, "message": message, "ticker": ticker, "toast": True}
        notification.notify(**kwargs)

    # Exit the app
    def exit_app(self):
        sys.exit()

    # Opens GitHub
    def open_github(self):
        webbrowser.open("https://github.com/Kourva/V2Paste")

    # Opens Telegram
    def open_telegram(self):
        webbrowser.open("https://t.me/Kourva")


# Settings screen
class SettingsScreen(Screen):
    # Path to font & # Uses get_screen to get IDs from another class
    font = "Sources/Assets/font.ttf"
    background = "Sources/Assets/white.jpg"

    # Resets settings & Sends notification
    def reset_settings(self, *args):
        for item in args:
            item._set_text("")

        title = "Reset"
        message = "Data reset"
        ticker = "New message"
        kwargs = {"title": title, "message": message, "ticker": ticker, "toast": True}
        notification.notify(**kwargs)

    # Saves configs
    def save_config(self, *args):
        with open("Data/config.conf", "w") as data:
            # Tries to save config and reset them when facing error
            try:
                data.write(
                    f"""{args[0].text}
{args[1].text}
{args[2].text}
{args[3].text}
{args[4].text}
{args[5].text}"""
                )

                # Sends notification
                title = "Saved"
                message = "Data saved!"
                ticker = "New message"
                kwargs = {
                    "title": title,
                    "message": message,
                    "ticker": ticker,
                    "toast": True,
                }
                notification.notify(**kwargs)

            except IndexError:
                worker = ""
                address = ""
                port = ""
                uuid = ""
                remark = ""
                path = ""

    # Notify user to wait until the next update
    def notify_next_update(self):
        try:
            vibrator.vibrate(0.3)
        except:
            pass

        title = "Developer"
        message = "This option is under the development"
        ticker = "New message"
        kwargs = {"title": title, "message": message, "ticker": ticker, "toast": True}
        notification.notify(**kwargs)


# Main class
class V2PasteApp(App):
    # Build method
    def build(self):
        # Root screen
        root = ScreenManager()

        # Main menu screen
        self.MainMenuScreen = MainMenuScreen(name="MainMenu")
        root.add_widget(self.MainMenuScreen)

        # Settings menu screen
        self.SettingsScreen = SettingsScreen(name="Settings")
        root.add_widget(self.SettingsScreen)

        # Set current screen to main menu and return root
        root.current = "MainMenu"
        return root


# Run App
V2PasteApp().run()

# EOF
