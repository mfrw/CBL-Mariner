#!/usr/bin/env bash

echo Remove chromium if already exists..
rpm -e chromium --nodeps

echo Install Edge browser and its dependencies ..
# Dependencies required by Microsoft Edge
tdnf install -y chkconfig

tdnf install -y xdg-utils

tdnf install -y wget

# Dependencies required by Microsoft Edge
wget http://10.137.185.184:8080/azuremariner/rpms/x64/alien/fontpackages-filesystem-1.44-8.el7.noarch.rpm
rpm -ivh fontpackages-filesystem-1.44-8.el7.noarch.rpm

wget http://10.137.185.184:8080/azuremariner/rpms/x64/alien/liberation-fonts-common-1.07.2-16.el7.noarch.rpm
rpm -ivh liberation-fonts-common-1.07.2-16.el7.noarch.rpm

wget http://10.137.185.184:8080/azuremariner/rpms/x64/alien/liberation-sans-fonts-1.07.2-16.el7.noarch.rpm
rpm -ivh liberation-sans-fonts-1.07.2-16.el7.noarch.rpm

wget http://10.137.185.184:8080/azuremariner/rpms/x64/alien/liberation-serif-fonts-1.07.2-16.el7.noarch.rpm
rpm -ivh liberation-serif-fonts-1.07.2-16.el7.noarch.rpm

wget http://10.137.185.184:8080/azuremariner/rpms/x64/alien/liberation-narrow-fonts-1.07.2-16.el7.noarch.rpm
rpm -ivh liberation-narrow-fonts-1.07.2-16.el7.noarch.rpm

wget http://10.137.185.184:8080/azuremariner/rpms/x64/alien/liberation-mono-fonts-1.07.2-16.el7.noarch.rpm
rpm -ivh liberation-mono-fonts-1.07.2-16.el7.noarch.rpm

wget http://10.137.185.184:8080/azuremariner/rpms/x64/alien/liberation-fonts-1.07.2-16.el7.noarch.rpm
rpm -ivh liberation-fonts-1.07.2-16.el7.noarch.rpm

wget http://10.137.185.184:8080/azuremariner/rpms/x64/alien/lsb-release-3.0-1.5.noarch.rpm
rpm -ivh lsb-release-3.0-1.5.noarch.rpm

# Microsoft Edge RPM
wget http://10.137.185.184:8080/azuremariner/rpms/x64/alien/microsoft-edge-beta-78.0.249.2-1.x86_64.rpm
rpm -ivh microsoft-edge-beta-78.0.249.2-1.x86_64.rpm

# Launch Microsoft-Edge Browser
/usr/bin/microsoft-edge-beta --no-sandbox
