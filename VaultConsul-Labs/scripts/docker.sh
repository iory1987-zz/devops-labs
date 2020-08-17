#!/bin/bash

centos(){
    yum install epel-release -y

    yum install vim htop curl wget bash-completion unzip jq python3-pip -y

    yum install -y https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.2.6-3.3.el7.x86_64.rpm

    systemctl stop firewalld

    systemctl disable firewalld

    setenforce 0

    sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
}

debian(){
    apt-get update

    apt-get install -y vim htop curl wget bash-completion unzip jq python3-pip
}

docker_install(){
    curl https://get.docker.com | bash

    curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /bin/docker-compose

    chmod +x /bin/docker-compose

    systemctl start docker

    systemctl enable docker

    sudo usermod -aG docker vagrant

    echo 'vm.overcommit_memory = 1' >> /etc/sysctl.conf

    sysctl -p

    cd /vagrant

    pip3 install -r appV1/requirements.txt


    docker-compose up -d
}

if [ -f /etc/redhat-release ]; then
    echo "Redhat Like"
    centos
    docker_install

elif [ -f /etc/debian_version ]; then
    echo "Debian Like"
    debian
    docker_install

else
    echo "Unknown Operating System"

fi