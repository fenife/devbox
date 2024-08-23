
## 安装时可限制访问vscode，否则安装会很慢 (TODO: not work)
sudo iptables -A OUTPUT -m string --string "visualstudio.com" --algo bm --to 65535 -j DROP
sudo iptables -nvL | grep visual
sudo iptables -D OUTPUT -m string --string "visualstudio.com" --algo bm --to 65535 -j DROP


## vscode
```text
版本: 1.85.2 (system setup)
提交: 8b3775030ed1a69b13e4f4c628c612102e30a681
日期: 2024-01-18T06:40:10.514Z
Electron: 25.9.7
ElectronBuildId: 26354273
Chromium: 114.0.5735.289
Node.js: 18.15.0
V8: 11.4.183.29-electron.0
OS: Windows_NT x64 10.0.22631
```

## install extension
~/.vscode-server/bin/8b3775030ed1a69b13e4f4c628c612102e30a681/bin/code-server --install-extension ./ms-python.vscode-pylance-2021.2.0.vsix --force 

ls ~/.vscode-server/extensions

# vscode-server-linux-x64
wget -O vscode-server-linux-x64-1.85.2.tar.gz https://update.code.visualstudio.com/commit:8b3775030ed1a69b13e4f4c628c612102e30a681/server-linux-x64/stable 

# ms-python.python
https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-python/vsextensions/python/2021.9.1246542782/vspackage

# ms-python.debugpy
https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-python/vsextensions/debugpy/2023.1.12492010/vspackage

# ms-python.vscode-pylance
https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-python/vsextensions/vscode-pylance/2021.1.2/vspackage

# ms-toolsai.jupyter
https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-toolsai/vsextensions/jupyter/2023.11.1100101639/vspackage?targetPlatform=linux-x64

# ms-toolsai.vscode-jupyter-slideshow
https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-toolsai/vsextensions/vscode-jupyter-cell-tags/0.1.5/vspackage

# ms-toolsai.vscode-jupyter-cell-tags
https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-toolsai/vsextensions/vscode-jupyter-cell-tags/0.1.8/vspackage

# ms-toolsai.jupyter-renderers
https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-toolsai/vsextensions/jupyter-renderers/1.0.17/vspackage

# ms-toolsai.jupyter-keymap
https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-toolsai/vsextensions/jupyter-keymap/1.1.2/vspackage?targetPlatform=linux-x64

