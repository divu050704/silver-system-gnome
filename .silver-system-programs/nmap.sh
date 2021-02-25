#! /bin/bash
ip=$(hostname -I)
nip=$(echo "$ip" | xargs)
cla=$(ip a | grep $nip)
read string1 string2 string3 <<< "$cla"
folder=/usr/share/nmap
if [ -d $folder ] 
then
    sudo nmap -sn $string2
else
    sudo apt install nmap 
    sudo nmap -sn $string2
fi