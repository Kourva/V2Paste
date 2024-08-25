<p>
    <img align="left" src="https://github.com/Kourva/V2Paste/blob/main/Data/icon.png" width=140 height=140 />
    <h1> V2Paste </h1>
    <p><b> Multi-Tool V2ray proxy app for android.</b></p>
</p>
<br>

### ▍Version 3.0.0 Update
&nbsp;&nbsp;&nbsp;&nbsp; ▣ Fixed Vmess decode function <br>
&nbsp;&nbsp;&nbsp;&nbsp; ▣ Cloner limit up to 50 <br>
&nbsp;&nbsp;&nbsp;&nbsp; ▣ QRcode in single proxy generator <br>
&nbsp;&nbsp;&nbsp;&nbsp; ▣ New theme and icons <br>
&nbsp;&nbsp;&nbsp;&nbsp; ▣ New Status bar <br>
&nbsp;&nbsp;&nbsp;&nbsp; ▣ Cloner limit controller <br>

### ▍Download 
Feel free to download this app from releases page
<br>Download: [V2Paste-1.2](https://github.com/Kourva/V2Paste/releases/tag/v3.0.0)

### ▍Idea
So this app works online with public APIs. if you have any idea to add let me know in [Issues](https://github.com/Kourva/V2Paste/issues).

### ▍Guide
If you have any question or help, check out our Telegram channel<br>
Link: [V2Paste Updates](https://t.me/V2Paste)

# Setup
#### First you need to install [python](https://www.python.org/) and [pip](https://pypi.org/project/pip/) from Official pages or Terminal
#### ⒈ clone the reposytory
```bash
git clone https://github.com/Kourva/V2Paste && cd V2Paste
```
#### ⒉ Navigate to V2Paste directory
```bash
cd V2Paste
```
#### ⒊ install requirements for app
```bash
chmod +x Lib/install.sh && ./Lib/install.sh
```
#### ⒋ Install python-dbus for notification (optional)
&nbsp;&nbsp;&nbsp;&nbsp; ▣ Debian based
```bash
sudo apt install python-dbus
```
&nbsp;&nbsp;&nbsp;&nbsp; ▣ Arch based
```bash
sudo pacman -S python-dbus
```
#### ⒌ run the app
&nbsp;&nbsp;&nbsp;&nbsp; ▣ Normally
```bash
python main.py
```
&nbsp;&nbsp;&nbsp;&nbsp; ▣ Specific phone
```
python main.py -m screen:600x800
```

<p>
    <img align="left" src="https://user-images.githubusercontent.com/118578799/219371927-2ebe765b-cdef-4b61-94d5-abd2b63d56f9.png" width=140 height=140 />
    <h1> Kivy to APK </h1>
    <p><b> Convert your Kivy file into apk </b></p>
</p><br>

###### You have 2 ways to do this. first way is [Google Colab](https://colab.research.google.com/). you can convert your Kivy file into APK fast and easy.
###### Second way is manual way. you need to do following stuff step by step
+ install required python libraries
```bash
pip install buildozer cython kivy pillow plyer
```
+ install required developer packages
```bash
sudo apt-get install -y \
    python3-pip \
    build-essential \
    git \
    python3 \
    python3-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev
```
+ install required plugins
```bash
sudo apt-get install -y \
    libgstreamer1.0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good
```
+ install required packages
```bash
sudo apt-get install -y \
    build-essential \
    libsqlite3-dev \
    sqlite3 \
    bzip2 \
    libbz2-dev \
    zlib1g-dev \
    libssl-dev \
    openssl \
    libgdbm-dev \
    libgdbm-compat-dev \
    liblzma-dev \
    libreadline-dev \
    libncursesw5-dev \
    libffi-dev \
    uuid-dev \
    libffi6
```
+ install this package
```bash
sudo apt-get install libffi-dev
```
+ init buildozer file (If you don't have **buildozer.spec** file. otherwise skip this step)
```bash
buildozer init
```
+ build the app
```bash
buildozer -v android debug
```
+ if you get any error, clear the data and rebuild again
```bash
buildozer android clean
```

<p>
    <img align="left" src="https://i0.wp.com/img.aapks.com/imgs/c/9/5/c95d7d8f2388afd94a20fd5004105246_icon.png?w=180" width=140 height=140 />
    <h1> V2rayDoprax </h1>
    <p><b> V2ray is a tool to create thousands of vless and vmess proxies at ones! includes more tools... for Doprax</b></p>
</p><br>

###### There is another tool for creating Vless proxies and some other stuff.
###### Check it out: https://github.com/Kourva/V2rayDoprax


# Thanks
###### You can give me a star if you find this tool helpfull. Wishing you all the best.
