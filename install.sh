echo -e "\e[1;35mInstalling...... \e[0m"
sudo mv .silver-system-programs /usr/.silver-system-programs && chmod +x /usr/.silver-system-programs/main.sh && sudo mv silver-system.desktop /usr/share/applications && cp /usr/share/applications/silver-system.desktop ~/Desktop
echo -e "\e[1;31mInstalled\e[0m"