# 🖱️ Mouse Reset Position

A small app to reset your mouse position and open a simple UI.

## 🔧 Usage
- To **reset position**: press `Home`  
- To **open the UI**: press `Home + End`

## 📦 Requirements
Make sure you have Python installed, then run:
```bash
pip install pyautogui
pip install keyboard
pip install pillow
```
if you want to build it yourself you need pyinstaller
```bash
pip install pyinstaller
```
then cd
```bash
cd "The app location"
```
and to build the app run this
```bash
pyinstaller --onefile --noconsole --icon=mouse_icon.ico Mouse.py
```
![Alt text](mouse_icon.png)
