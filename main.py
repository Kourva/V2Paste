#!/usr/bin/env python3

# V2Paste powered by Kourva
# Version 3.0.0

import webbrowser, random, uuid, json, base64, urllib.parse
from plyer import vibrator, notification
from threading import Thread
from plyer.utils import platform
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.properties import ListProperty, BooleanProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.app import App 
from kivy.factory import Factory
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.core.text import LabelBase
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.image import Image
from kivy.uix.button import Button, ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import RoundedRectangle, Color, Line
from kivy.uix.floatlayout import FloatLayout
from kivy.network.urlrequest import UrlRequest
from kivy.uix.tabbedpanel import TabbedPanel

for filename in ["CloneMenu", "DecodeMenu", "MainMenu", "Settings", "StartMenu"]:
    Builder.load_file("Scripts/%s.kv" % filename)

class ImageButton(ButtonBehavior, Image):
    def on_press(self):
        pass

class StartMenu(Screen):

    font = "Assets/font.ttf"

    def open_url(self, pf):
        url = (
            "https://t.me/V2Paste"
            if pf == "Telegram"
            else "https://github.com/Kourva/V2Paste"
        )
        webbrowser.open(url)

    def load_config(self):
        worker = self.manager.get_screen("Settings").ids.CloudFlare
        address = self.manager.get_screen("Settings").ids.IP_address
        port = self.manager.get_screen("Settings").ids.Port
        uuid = self.manager.get_screen("Settings").ids.UUID_input
        remark = self.manager.get_screen("Settings").ids.Remark
        pathvmess = self.manager.get_screen("Settings").ids.Pathvmess
        pathvless = self.manager.get_screen("Settings").ids.Pathvless

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
                worker._set_text("")
                address._set_text("")
                port._set_text("")
                uuid._set_text("")
                remark._set_text("")
                pathvmess._set_text("")
                pathvless._set_text("")

class MainMenu(Screen):

    font = "Assets/font.ttf"

    def show_exit_popup(self, *args):
        popup = Factory.ExitPopup().open()
        try:
            vibrator.vibrate(0.1)
        except:
            pass

    def Show_Qrcode_popup(self, *args):
        try:
            try:
                vibrator.vibrate(0.1)
            except:
                pass
            kwargs = {
                "title": "Notification",
                "message": "Wait until QRcode is being generated",
                "ticker": "New message",
                "toast": True,
                "app_icon": "Data/icon.png",
            }
            notification.notify(**kwargs)

            qrtext = self.manager.get_screen("MainMenu").ids.Proxy_Output.text.strip()
            en_qrtext = urllib.parse.quote(qrtext)
            
            url = f"https://api.qrserver.com/v1/create-qr-code/?data={en_qrtext}&size=500x500"

            Clock.start_clock()
            req1 = UrlRequest(url, timeout=5)
            while not req1.is_finished:
                Clock.tick()
            Clock.stop_clock()

            result = req1.result
            with open("Data/qrcode.png", "wb") as data:
                data.write(result)

            popup = Factory.QRcodePopup()
            qrcode_id = popup.ids.Proxy_QRcode
            qrcode_id.source = "Data/qrcode.png"
            popup.open()

        except Exception as e:
            print(e)
            try:
                vibrator.vibrate(0.1)
            except:
                pass
            kwargs = {
                "title": "Notification",
                "message": "Error while generating QRcode",
                "ticker": "New message",
                "toast": True,
                "app_icon": "Data/icon.png",
            }
            notification.notify(**kwargs)

    def load_config(self):
        worker = self.manager.get_screen("Settings").ids.CloudFlare
        address = self.manager.get_screen("Settings").ids.IP_address
        port = self.manager.get_screen("Settings").ids.Port
        uuid = self.manager.get_screen("Settings").ids.UUID_input
        remark = self.manager.get_screen("Settings").ids.Remark
        pathvmess = self.manager.get_screen("Settings").ids.Pathvmess
        pathvless = self.manager.get_screen("Settings").ids.Pathvless

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
                try:
                    vibrator.vibrate(0.1)
                except:
                    pass
                kwargs = {
                    "title": "Notification",
                    "message": "Can't load data",
                    "ticker": "New message",
                    "toast": True,
                    "app_icon": "Data/icon.png",
                }
                notification.notify(**kwargs)

                worker._set_text("")
                address._set_text("")
                port._set_text("")
                uuid._set_text("")
                remark._set_text("")
                pathvmess._set_text("")
                pathvless._set_text("")
    
    def generate_vmess(self):
        worker = self.manager.get_screen("Settings").ids.CloudFlare.text.strip()
        address = self.manager.get_screen("Settings").ids.IP_address.text.strip()
        port = self.manager.get_screen("Settings").ids.Port.text.strip()
        uuid = self.manager.get_screen("Settings").ids.UUID_input.text.strip()
        remark = self.manager.get_screen("Settings").ids.Remark.text.strip()
        pathvless = self.manager.get_screen("Settings").ids.Pathvless.text.strip()
        pathvmess = self.manager.get_screen("Settings").ids.Pathvmess.text.strip() 

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
                vibrator.vibrate(0.1)
            except:
                pass
            kwargs = {
                    "title": "Notification",
                    "message": "Not enough data",
                    "ticker": "New message",
                    "toast": True,
                    "app_icon": "Data/icon.png",
                }
            notification.notify(**kwargs)
            return

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
        vmess_url_str = 'vmess://' + base64.urlsafe_b64encode(json.dumps(vmess_url).encode('utf-8')).decode('utf-8')
        self.manager.get_screen("MainMenu").ids.Proxy_Output.text = vmess_url_str + "\n\n"

    def generate_vless(self):
        worker = self.manager.get_screen("Settings").ids.CloudFlare.text.strip()
        address = self.manager.get_screen("Settings").ids.IP_address.text.strip()
        port = self.manager.get_screen("Settings").ids.Port.text.strip()
        uuid = self.manager.get_screen("Settings").ids.UUID_input.text.strip()
        remark = self.manager.get_screen("Settings").ids.Remark.text.strip()
        pathvless = self.manager.get_screen("Settings").ids.Pathvless.text.strip()
        pathvmess = self.manager.get_screen("Settings").ids.Pathvmess.text.strip() 

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
                vibrator.vibrate(0.1)
            except:
                pass
            kwargs = {
                "title": "Notification",
                "message": "Not enough data",
                "ticker": "New message",
                "toast": True,
                "app_icon": "Data/icon.png",
            }
            notification.notify(**kwargs)
            return

        vless_url = f"vless://{uuid}@{address}:{port}?encryption=none&security=tls&sni={worker}&alpn=http%2F1.1&type=ws&host={worker}&path=/{pathvless}#{remark}"
        self.manager.get_screen("MainMenu").ids.Proxy_Output.text = vless_url + "\n\n"

    def copy_to_clipboard(self, Output):
        try:
            Clipboard.copy(Output.text)
            try:
                vibrator.vibrate(0.1)
            except:
                pass
            kwargs = {
                "title": "Notification",
                "message": "Output copied",
                "ticker": "New message",
                "toast": True,
                "app_icon": "Data/icon.png",
            }
            notification.notify(**kwargs)
        except:
            try:
                vibrator.vibrate(0.1)
            except:
                pass
            kwargs = {
                "title": "Notification",
                "message": "Error while copying!",
                "ticker": "New message",
                "toast": True,
                "app_icon": "Data/icon.png",
            }
            notification.notify(**kwargs)

class Settings(Screen):

    font = "Assets/font.ttf"

    def generate_string(*widgets):
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
        for w in widgets:
            w.text = "".join(
                random.choice(consonants if i % 2 == 0 else vowels) for i in range(8)
            ).capitalize()

    def generate_uuid(self, uuid_widget):
        try:
            vibrator.vibrate(0.1)
        except:
            pass
        uuid_widget.text = str(uuid.uuid4()).upper()

    def get_ip_port(self, IP_address, Port):
        with open("Data/servers.txt", "r") as data:
            servers = data.readlines()
            IP_address._set_text(random.choice(servers).split("\n")[0])
            Port._set_text("443")
            try:
                vibrator.vibrate(0.1)
            except:
                pass

    def save_config(self, *args):
        with open("Data/config.conf", "w") as data:
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
                try:
                    vibrator.vibrate(0.1)
                except:
                    pass
                kwargs = {
                    "title": "Notification",
                    "message": "Data saved",
                    "ticker": "New message",
                    "toast": True,
                    "app_icon": "Data/icon.png",
                }
                notification.notify(**kwargs)

            except IndexError:
                pass

    def reset_config(self, *args):
        for arg in args:
            arg._set_text("")

            try:
                vibrator.vibrate(0.1)
            except:
                pass
        kwargs = {
            "title": "Notification",
            "message": "Config reset",
            "ticker": "New message",
            "toast": True,
            "app_icon": "Data/icon.png",
        }
        notification.notify(**kwargs)

class DecodeMenu(Screen):

    font = "Assets/font.ttf"

    def change_mode(self, mode, inpt):
        try:
            vibrator.vibrate(0.1)
        except:
            pass
        kwargs = {
            "title": "Notification",
            "message": "There is no other mods yet!",
            "ticker": "New message",
            "toast": True,
            "app_icon": "Data/icon.png",
        }
        notification.notify(**kwargs)
        return

    def Decode(self, mode, Input, Output):
        if Input.text == "":
            try:
                vibrator.vibrate(0.1)
            except:
                pass
            kwargs = {
                "title": "Notification",
                "message": "Input can't be empty",
                "ticker": "New message",
                "toast": True,
                "app_icon": "Data/icon.png",
            }   
            notification.notify(**kwargs)
            return
        
        if mode.text == 'Current Mode: [color=#ffff00]Vmess[/color]':
            try:
                encoded_data = Input.text if not "vmess://" in Input.text else Input.text.split("vmess://")[1]
                output = json.loads(base64.b64decode(encoded_data).decode('utf-8').replace("'", "\""))
                Output.text = "Here is your output for Vmess URL:\n\n" + str(json.dumps(output, indent=1))
            except:
                try:
                    vibrator.vibrate(0.1)
                except:
                    pass
                kwargs = {
                    "title": "Notification",
                    "message": "Input seems to be wrong",
                    "ticker": "New message",
                    "toast": True,
                    "app_icon": "Data/icon.png",
                } 
                notification.notify(**kwargs)
                return

    def copy_to_clipboard(self, Output):
        try:
            Clipboard.copy(Output.text)
            try:
                vibrator.vibrate(0.1)
            except:
                pass
            kwargs = {
                "title": "Notification",
                "message": "Output copied",
                "ticker": "New message",
                "toast": True,
                "app_icon": "Data/icon.png",
            }
            notification.notify(**kwargs)
        except:
            try:
                vibrator.vibrate(0.1)
            except:
                pass
            kwargs = {
                "title": "Notification",
                "message": "Error while copying!",
                "ticker": "New message",
                "toast": True,
                "app_icon": "Data/icon.png",
            }
            notification.notify(**kwargs)

class CloneMenu(Screen):

    font = "Assets/font.ttf"

    def clone_vmess(self, Input, Output, Clone_Nums):
        try:
            if not Input.text.startswith("vmess://"):
                raise
        except:
            try:
                vibrator.vibrate(0.1)
            except:
                pass
            kwargs = {
                "title": "Notification",
                "message": "Not a valid url",
                "ticker": "New message",
                "toast": True,
                "app_icon": "Data/icon.png",
            }
            notification.notify(**kwargs)
            return

        try:
            encoded_data = Input.text.split("vmess://")[1].strip()
            output = json.loads(base64.b64decode(encoded_data).decode('utf-8').replace("'", "\""))

            ipaddr, port, remark = (
                output["add"],
                output["port"],
                output["ps"],
            )

            with open("Data/servers.txt", "r") as file:
                all_servers = file.readlines()
                iplist = [random.choice(all_servers).split("\n")[0] for _ in range(Clone_Nums.value)]

            clones = []
            for index, server in enumerate(iplist, start=1):
                temp = output
                temp["add"] = server
                temp["port"] = "443"
                temp["ps"] = remark + "-" + str(index)

                vmess_config = str(temp).encode("ascii")
                vmess_url = base64.b64encode(vmess_config).decode("ascii")
                result = "vmess://" + vmess_url + "\n\n"
                clones.append(result)

            result = "".join(clones)
            Output.text = result
            try:
                vibrator.vibrate(0.1)
            except:
                pass
            kwargs = {
                "title": "Notification",
                "message": f"{Clone_Nums.value} Proxies generated",
                "ticker": "New message",
                "toast": True,
                "app_icon": "Data/icon.png",
            }    
            notification.notify(**kwargs)

        except:
            try:
                vibrator.vibrate(0.1)
            except:
                pass
            kwargs = {
                "title": "Notification",
                "message": "Error while cloning!",
                "ticker": "New message",
                "toast": True,
                "app_icon": "Data/icon.png",
            }    
            notification.notify(**kwargs)
            return

    def clone_vless(self, Input, Output, Clone_Nums):
        try:
            target = Input.text.split("@")[1].split("?")[0]
            ipaddr, port = target.split(":")
            remark = Input.text.strip().split("#")[1]

            with open("Data/servers.txt", "r") as file:
                all_servers = file.readlines()
                iplist = [random.choice(all_servers).split("\n")[0] for _ in range(Clone_Nums.value)]

            clones = []
            for index, server in enumerate(iplist, start=1):
                tempvar = (
                    Input.text.strip()
                    .replace(ipaddr, server)
                    .replace(port, "443")
                    .replace(remark, remark + "-" + str(index) + "\n\n")
                )
                clones.append(tempvar)

            result = "".join(clones)
            Output.text = result
            try:
                vibrator.vibrate(0.1)
            except:
                pass
            kwargs = {
                "title": "Notification",
                "message": f"{Clone_Nums.value} Proxies generated",
                "ticker": "New message",
                "toast": True,
                "app_icon": "Data/icon.png",
            } 
            notification.notify(**kwargs)

        except:
            try:
                vibrator.vibrate(0.1)
            except:
                pass
            kwargs = {
                "title": "Notification",
                "message": "Error while cloning!",
                "ticker": "New message",
                "toast": True,
                "app_icon": "Data/icon.png",
            } 
            notification.notify(**kwargs)
            return

    def copy_to_clipboard(self, Output):
        try:
            Clipboard.copy(Output.text)
            try:
                vibrator.vibrate(0.1)
            except:
                pass
            kwargs = {
                "title": "Notification",
                "message": "Output copied",
                "ticker": "New message",
                "toast": True,
                "app_icon": "Data/icon.png",
            }
            notification.notify(**kwargs)
        except:
            try:
                vibrator.vibrate(0.1)
            except:
                pass
            kwargs = {
                "title": "Notification",
                "message": "Error while copying!",
                "ticker": "New message",
                "toast": True,
                "app_icon": "Data/icon.png",
            }
            notification.notify(**kwargs)

class V2PasteApp(App):
    def build(self):

        root = ScreenManager()

        self.StartMenu = StartMenu(name="StartMenu")
        root.add_widget(self.StartMenu)

        self.CloneMenu = CloneMenu(name="CloneMenu")
        root.add_widget(self.CloneMenu)

        self.DecodeMenu = DecodeMenu(name="DecodeMenu")
        root.add_widget(self.DecodeMenu)

        self.MainMenu = MainMenu(name="MainMenu")
        root.add_widget(self.MainMenu)

        self.Settings = Settings(name="Settings")
        root.add_widget(self.Settings)

        root.current = "StartMenu"
        return root

if __name__ == "__main__":
    V2PasteApp().run()
