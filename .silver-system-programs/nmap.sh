#! /bin/bash
ip=$(hostname -I)
nip=$(echo "$ip" | xargs)
nnip=${nip}/24
folder=/usr/share/nmap
if [ -d $folder ] 
then
    sudo nmap -sn $nnip
else
    sudo apt install nmap 
    sudo nmap -sn $nnip
fi