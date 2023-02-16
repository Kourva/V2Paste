<p>
    <img align="left" src="https://user-images.githubusercontent.com/118578799/219364816-7bb81cac-2cb5-4e52-bbc7-9bf907d016b1.png" width=140 height=140 />
    <h1> V2Paste </h1>
    <p><b> Create Vless proxies via given config with this simple app in Android </b></p>
</p>
<br>

# Setup
+ clone
```bash
git clone https://github.com/Kourva/V2Paste && cd V2Paste
```
+ requirements
```bash
pip install -r requirements.txt
```
+ run
```bash
python main.py
```

# Kivy to APK
###### You have 2 ways to do this. first way is [Google Colab](https://colab.research.google.com/). you can convert your Kivy file into APK fast and easy.
###### Second way is manual way. you need to do following stuff step by step
+ install required python libraries
```bash
pip install buildozer cython kivy pillow
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
+ build the app
```bash
buildozer -v android debug
```
+ if you get any error, clear the data and rebuild again
```bash
buildozer android clean
```
