#!/bin/bash

set -x

vscode_bin=$1

for f in `find . -name "*.vsix" `; do
	$vscode_bin --install-extension ./$f
done

# ms-python.python
# https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-python/vsextensions/python/2024.2.1/vspackage

# ms-python.debugpy
# https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-python/vsextensions/debugpy/2024.0.0/vspackage?targetPlatform=linux-x64

# ms-toolsai.jupyter
# https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-toolsai/vsextensions/jupyter/2023.11.1100101639/vspackage?targetPlatform=linux-x64

# ms-toolsai.vscode-jupyter-slideshow
# https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-toolsai/vsextensions/vscode-jupyter-cell-tags/0.1.5/vspackage

# ms-toolsai.vscode-jupyter-cell-tags
# https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-toolsai/vsextensions/vscode-jupyter-cell-tags/0.1.8/vspackage

# ms-toolsai.jupyter-renderers
# https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-toolsai/vsextensions/jupyter-renderers/1.0.17/vspackage

# ms-toolsai.jupyter-keymap
# https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-toolsai/vsextensions/jupyter-keymap/1.1.2/vspackage?targetPlatform=linux-x64

