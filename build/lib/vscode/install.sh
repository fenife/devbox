#!/bin/bash

set -x

vscode_bin=$1

for f in `find ./ext -name "*.vsix" `; do
	$vscode_bin --install-extension $f --force
done
