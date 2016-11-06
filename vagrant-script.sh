#!/bin/sh

# To directly enter in /vagrant folder when ssh
grep -q 'vagrant' /home/vagrant/.bashrc || echo "cd /vagrant" >> /home/vagrant/.bashrc

apt-get update
apt-get install -y curl docker docker-compose python-pip python-virtualenv

# https://github.com/docker/compose/issues/1214#issuecomment-102246925
usermod -aG docker vagrant
