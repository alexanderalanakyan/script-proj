#!/usr/bin/bash
set -euo pipefail
if [  ${PWD##*/} != "src" ]; then
exit 1
fi
mkdir -p libs
mkdir -p bin
mkdir -p .dotfiles

curl -L https://github.com/charmbracelet/gum/releases/download/v0.17.0/gum_0.17.0_Linux_x86_64.tar.gz > ./bin/gum.tar.gz
tar -xvf ./bin/gum.tar.gz
rm -rf ./bin/gum.tar.gz
mv ./gum_0.17.0_Linux_x86_64/gum ./bin/gum && mv ./gum_0.17.0_Linux_x86_64 ./bin/gum.d/

curl -L https://github.com/pygments/pygments/archive/refs/tags/2.20.0.tar.gz -o ./libs/pygments.tar.gz
mkdir -p ./libs/pygments.d
tar -xvf ./libs/pygments.tar.gz -C ./libs/pygments.d
rm ./libs/pygments.tar.gz
mv ./libs/pygments.d/pygments-2.20.0/pygments ./libs/pygments && cp ./libs/pygments.d/pygments-2.20.0/LICENSE ./libs/pygments/LICENSE

curl -L https://github.com/Textualize/rich/archive/refs/tags/v15.0.0.tar.gz -o ./libs/rich.tar.gz
mkdir -p ./libs/rich.d
tar -xvf ./libs/rich.tar.gz -C ./libs/rich.d
rm ./libs/rich.tar.gz
mv ./libs/rich.d/rich-15.0.0/rich/ ./libs/rich && cp ./libs/rich.d/rich-15.0.0/LICENSE ./libs/rich/LICENSE

curl -L https://github.com/yaml/pyyaml/archive/refs/tags/6.0.3.tar.gz -o ./libs/pyyaml.tar.gz
mkdir -p ./libs/pyyaml.d
tar -xvf ./libs/pyyaml.tar.gz -C ./libs/pyyaml.d
rm ./libs/pyyaml.tar.gz
mv ./libs/pyyaml.d/pyyaml-6.0.3/lib/yaml ./libs/yaml && cp ./libs/pyyaml.d/pyyaml-6.0.3/LICENSE ./libs/yaml/LICENSE
