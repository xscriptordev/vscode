# XGlass for VS Code

An extension that makes your editor looks like glass.

![Preview](https://raw.githubusercontent.com/xscriptordev/vscode/main/extensions/xglass/images/preview.png)

## Features
- Change the window transparency using keyboard shortcuts.  
- Configure the level and step size from VS Code settings.

## Requirements
- **Windows:** Windows 10+  
- **Linux:** Xorg session

```shell
#make sure you have installed:
sudo dnf install xorg-x11-utils
sudo apt install x11-utils
#or
sudo pacman -S xorg-xprop
#depending of your distro
```

## Usage
- `Ctrl + Alt + Z` → Increase transparency  
- `Ctrl + Alt + C` → Decrease transparency  

## Settings
- `xglass.alpha`: Transparency level (1–255).  
- `xglass.step`: Step size when adjusting transparency.  

## More information
- [GitHub repository](https://github.com/xscriptordev/vscode)  
