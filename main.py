#!/usr/bin/env python3


#  Author  : Kourva
#  Github  : https://github.com/kourva/V2Paste
#  Version : 1.1
#  About   : Create Vless/Vmess proxies via given config with this simple app
#
#  Changes:
#          + Vmess proxy added
#          + Bug fixes

# Imports
import sys
import base64
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
        pathvmess = self.manager.get_screen("Settings").ids.Pathvmess
        pathvless = self.manager.get_screen("Settings").ids.Pathvless

        # Loads config file. if face any problem, resets it.
        with open("Data/config.conf", "r") as data:
            lines = data.readlines()
            try:
                worker._set_text(lines[0].split("\n")[0])
                address._set_text(lines[1].split("\n")[0])
                port._set_text(lines[2].split("\n")[0])
                uuid._set_text(lines[3].split("\n")[0])
                remark._set_text(lines[4].split("\n")[0])
                pathvmess._set_text(lines[5].split("\n")[0])
                pathvless._set_text(lines[6].split("\n")[0])

            except IndexError:
                worker = ""
                address = ""
                port = ""
                uuid = ""
                remark = ""
                pathvmess = ""
                pathvless = ""

    # Vless/Vmess generator
    def generate(self, output) -> None:
        # Uses get_screen to get IDs from another class
        worker = self.manager.get_screen("Settings").ids.CloudFlare.text.strip()
        address = self.manager.get_screen("Settings").ids.IP_address.text.strip()
        port = self.manager.get_screen("Settings").ids.Port.text.strip()
        uuid = self.manager.get_screen("Settings").ids.UUID.text.strip()
        remark = self.manager.get_screen("Settings").ids.Remark.text.strip()
        pathvless = self.manager.get_screen("Settings").ids.Pathvless.text.strip()
        pathvmess = self.manager.get_screen("Settings").ids.Pathvmess.text.strip()

        # Send error notification if any field is empty
        if (
            worker == ""
            or address == ""
            or port == ""
            or uuid == ""
            or remark == ""
            or pathvmess == ""
            or pathvless == ""
        ):
            try:
                vibrator.vibrate(0.3)
            except:
                pass

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
            # Vless
            vless_url = f"vless://{uuid}@{address}:{port}?encryption=none&security=tls&sni={worker}&alpn=http%2F1.1&type=ws&host={worker}&path=/{pathvless}#{remark}"

            # Vmess
            vmess_url = {
                "v": "2",
                "ps": remark,
                "add": address,
                "port": port,
                "id": uuid,
                "aid": "0",
                "scy": "auto",
                "net": "ws",
                "type": "none",
                "host": worker,
                "path": pathvmess,
                "tls": "tls",
                "alpn": "http/1.1",
            }
            message = str(vmess_url).encode("ascii")
            base64_bytes = base64.b64encode(message).decode("ascii")
            output._set_text("vmess://" + base64_bytes + "\n\n" + vless_url)

    # Copies the Vless/Vmess proxies to Clipboard & send notification
    def copy_output(self, output):
        Clipboard.copy(output.text)
        title = "Copied"
        message = "Proxies Copied"
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
        try:
            vibrator.vibrate(0.1)
        except:
            pass
        webbrowser.open("https://github.com/Kourva")

    # Opens Telegram
    def open_telegram(self):
        try:
            vibrator.vibrate(0.1)
        except:
            pass
        webbrowser.open("https://t.me/Kourva")

    # Opens Source Code
    def open_source(self):
        try:
            vibrator.vibrate(0.1)
        except:
            pass
        webbrowser.open("https://github.com/Kourva/V2Paste")


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
{args[5].text}
{args[6].text}"""
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
                pathvmess = ""
                pathvless = ""

    # Opens help page
    def open_help(self):
        try:
            vibrator.vibrate(0.1)
        except:
            pass
        # Sends notification
        title = "Saved"
        message = "Oops! Under development"
        ticker = "New message"
        kwargs = {
            "title": title,
            "message": message,
            "ticker": ticker,
            "toast": True,
        }
        notification.notify(**kwargs)

    # Simple notification
    def do_game(self):
        try:
            vibrator.vibrate(0.1)
        except:
            pass

        # Sends notification
        title = "Saved"
        message = "¯\_(ツ)_/¯"
        ticker = "New message"
        kwargs = {
            "title": title,
            "message": message,
            "ticker": ticker,
            "toast": True,
        }
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
