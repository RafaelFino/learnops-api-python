#!/bin/bash

# To prepare a single instance
#
# 1: Create a simple ubuntu instance on killercoda.com:
#   https://killercoda.com/playgrounds/scenario/ubuntu
#
# 2: Execute this command on terminal:
#   curl https://raw.githubusercontent.com/RafaelFino/learnops-api-python/main/prepare.sh | bash && zsh
#
# Have fun! :)

#update
apt update -y
apt install -y git vim zsh curl wget unzip jq telnet htop python3 python3-pip

#install vim
git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime
sh ~/.vim_runtime/install_awesome_vimrc.sh

#install micro
curl https://getmic.ro | bash
mv micro /usr/bin

#install exa
EXA_VERSION=$(curl -s "https://api.github.com/repos/ogham/exa/releases/latest" | grep -Po '"tag_name": "v\K[0-9.]+')
curl -Lo exa.zip "https://github.com/ogham/exa/releases/latest/download/exa-linux-x86_64-v${EXA_VERSION}.zip"
unzip -qo exa.zip bin/exa -d /usr/local
rm exa.zip

#install oh-my-zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

#change ZSH theme
sed -i 's/ZSH_THEME=\"robbyrussell\"/ZSH_THEME=\"frisk\"/g' .zshrc
echo 'alias ls="exa -hHbmgaFl"' >> ~/.zshrc
echo set nu >> ~/.vim_runtime/my_configs.vim
echo zsh >> ~/.bashrc

#change default shell
chsh -s /bin/zsh

#clone lab repo
cd
git clone https://github.com/RafaelFino/learnops-api-python.git

#install python3 dependencies
cd ~/learnops-api-python
python3 -m venv .
source bin/activate
pip3 install -r requirements.txt

echo 'Done!'
