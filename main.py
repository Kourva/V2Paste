#!/usr/bin/env python3


#  Author  : Kourva
#  Github  : https://github.com/kourva/V2Paste
#  Version : 1.2
#  About   : Create Vless/Vmess proxies via given config with this simple app
#
#  Changes:
#          + Multi Vmess Generator
#          + Vmess decoder
#          + Changed some functions
#          + UUID generator

# All imported Libraries
# Built-in modules for basic stuff
import sys
import json
import uuid
import base64
import random
import webbrowser

# Plyer modules: for android functionality
from plyer import notification
from plyer import vibrator
from plyer.utils import platform

# Kicy modules: for the app
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.actionbar import *


# KV config files
# All extra kivy files to include
# Main menu screen
# Settings screen
# Decode menu screen
for Sources in ["main.kv", "settings.kv", "decode.kv"]:
    with open("Sources/%s" % Sources, "r") as kv:
        Builder.load_string(kv.read())


# ImageButton
# This is for clickable image buttons
class ImageButton(ButtonBehavior, Image):
    def on_press(self):
        pass


# StartMenu screen
# All needed functions for main menu
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
        uuid = self.manager.get_screen("Settings").ids.UUID_input
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

            # If any error, let empty
            except IndexError:
                worker = ""
                address = ""
                port = ""
                uuid = ""
                remark = ""
                pathvmess = ""
                pathvless = ""

    # Vless/Vmess generator will generate 2 vless and vmess proxies
    def generate(self, output) -> None:
        # Uses get_screen to get IDs from another class
        worker = self.manager.get_screen("Settings").ids.CloudFlare.text.strip()
        address = self.manager.get_screen("Settings").ids.IP_address.text.strip()
        port = self.manager.get_screen("Settings").ids.Port.text.strip()
        uuid = self.manager.get_screen("Settings").ids.UUID_input.text.strip()
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
                "app_icon": "Data/notification.png",
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

    # Vless/Vmess generator_20 will generate 20 vmess vless proxies
    def generate_20(self, output) -> None:
        # Uses get_screen to get IDs from another class
        worker = self.manager.get_screen("Settings").ids.CloudFlare.text.strip()
        address = self.manager.get_screen("Settings").ids.IP_address.text.strip()
        port = self.manager.get_screen("Settings").ids.Port.text.strip()
        uuid = self.manager.get_screen("Settings").ids.UUID_input.text.strip()
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
                "app_icon": "Data/notification.png",
            }
            notification.notify(**kwargs)

        else:
            generated_proxies = []
            with open("Data/servers.txt", "r") as data:
                servers = data.readlines()
                random_servers = [
                    random.choice(servers).split("\n")[0] for _ in range(10)
                ]

                for index, server in enumerate(random_servers, start=1):
                    # Vless
                    vless_url = f"vless://{uuid}@{server}:{port}?encryption=none&security=tls&sni={worker}&alpn=http%2F1.1&type=ws&host={worker}&path=/{pathvless}#{remark + '-vless' + str(index)}"

                    # Vmess
                    vmess_url = {
                        "v": "2",
                        "ps": remark + "-vmess" + str(index),
                        "add": server,
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
                    generated_proxies.append(vless_url + "\n\n")
                    generated_proxies.append("vmess://" + base64_bytes + "\n\n")

                result = "".join(generated_proxies)
                Clipboard.copy(result)
                output._set_text(
                    "20 Vless/Vmess proxies generated copied to clipboard.\n\nEnjoy the freedom ;]"
                )
                title = "Generator"
                message = "20 Vless & Vmess proxies Generated."
                ticker = "New message"
                kwargs = {
                    "title": title,
                    "message": message,
                    "ticker": ticker,
                    "app_name": "V2Paste",
                    "app_icon": "Data/notification.png",
                }
                notification.notify(**kwargs)

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
            "app_icon": "Data/notification.png",
        }
        notification.notify(**kwargs)

    # Resets output text
    def reset_output(self, output):
        output._set_text("")

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
# All needed functions for settings menu
class SettingsScreen(Screen):
    # Path to font background
    font = "Sources/Assets/font.ttf"
    background = "Sources/Assets/white.jpg"

    # Resets settings & Sends notification
    def reset_settings(self, *args):
        for item in args:
            item._set_text("")

        title = "Reset"
        message = "Data reset"
        ticker = "New message"
        kwargs = {
            "title": title,
            "message": message,
            "ticker": ticker,
            "toast": True,
            "app_icon": "Data/notification.png",
        }
        notification.notify(**kwargs)

    # Saves configs so don't need to fill them again
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
                    "app_icon": "Data/notification.png",
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

    # Simple notification for fun
    def do_game(self):
        try:
            vibrator.vibrate(0.1)
            time.sleep(0.3)
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
            "app_icon": "Data/notification.png",
        }
        notification.notify(**kwargs)

    # Generate Path name for vless and vmess
    def generate_path(self, Pathvmess, Pathvless):
        possibles = "abcedfghigklmnopqrstuvwxyw"
        generated = "".join(random.choices(possibles, k=5))
        Pathvless._set_text(generated + "-vless")
        Pathvmess._set_text(generated + "-vmess")

    # Generates UUID version 4. If you don't have one
    def generate_uuid(self, UUID_input):
        generated_uuid = uuid.uuid4()
        UUID_input._set_text(str(generated_uuid))

    # Get servers from servers file (about 27000 IPs)
    def get_server(self, IP_address, Port):
        with open("Data/servers.txt", "r") as data:
            servers = data.readlines()
            IP_address._set_text(random.choice(servers).split("\n")[0])
            Port._set_text("443")

        try:
            vibrator.vibrate(0.1)
        except:
            pass

        # Sends notification
        title = "Saved"
        message = "Got server"
        ticker = "New message"
        kwargs = {
            "title": title,
            "message": message,
            "ticker": ticker,
            "toast": True,
            "app_icon": "Data/notification.png",
        }


# Decode menu screen
# All needed functions for decode menu
class DecodeScreen(Screen):
    # Path to font & background
    font = "Sources/Assets/font.ttf"
    background = "Sources/Assets/white.jpg"

    # Simple notification for fun
    def do_game(self):
        try:
            vibrator.vibrate(0.1)
            time.sleep(0.3)
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
            "app_icon": "Data/notification.png",
        }
        notification.notify(**kwargs)

    # Decode vmess proxy and extract it's config
    def decode_vmess(self, vmessurl, vmessdecoded):
        if vmessurl == "":
            try:
                vibrator.vibrate(0.1)
            except:
                pass

            # Sends notification
            title = "Saved"
            message = "Input is empty"
            ticker = "New message"
            kwargs = {
                "title": title,
                "message": message,
                "ticker": ticker,
                "toast": True,
                "app_icon": "Data/notification.png",
            }
            return
        try:
            # Gets message
            target = vmessurl.text.split("vmess://")[1].strip()

            # Decodes message
            tempvar = target.encode("ascii")
            message = base64.b64decode(tempvar)
            configs = message.decode("ascii")

            # Converts to json
            ugly_json = configs.replace("'", '"')
            parsed_json = json.loads(ugly_json)
            pretty_json = json.dumps(parsed_json, indent=4)

            # Shows json config
            vmessdecoded.text = str(pretty_json)

        except:
            try:
                vibrator.vibrate(0.1)
            except:
                pass

            # Sends notification
            title = "Saved"
            message = "URL is incorrect"
            ticker = "New message"
            kwargs = {
                "title": title,
                "message": message,
                "ticker": ticker,
                "toast": True,
                "app_icon": "Data/notification.png",
            }

    # Copies config to clipboard
    def copy_config(self, vmessdecoded):
        Clipboard.copy(vmessdecoded.text)
        title = "Copied"
        message = "Config Copied"
        ticker = "New message"
        kwargs = {
            "title": title,
            "message": message,
            "ticker": ticker,
            "toast": True,
        }
        notification.notify(**kwargs)


# Main class of the app
class V2PasteApp(App):
    # Build method
    def build(self):
        # Root screen
        root = ScreenManager()

        # Main menu screen
        self.MainMenuScreen = MainMenuScreen(name="MainMenu")
        root.add_widget(self.MainMenuScreen)

        # Decode menu screen
        self.DecodeScreen = DecodeScreen(name="DecodeMenu")
        root.add_widget(self.DecodeScreen)

        # Settings menu screen
        self.SettingsScreen = SettingsScreen(name="Settings")
        root.add_widget(self.SettingsScreen)

        # Set current screen to main menu and return root
        root.current = "MainMenu"
        return root


# Run App
V2PasteApp().run()

# EOF
