#!/usr/bin/env bash
# Sets up the web servers for deployment

# Install Nginx if not exists
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create needed diretories
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test/
echo '<html><head></head><body>Holberton School</body></html>' > /data/web_static/releases/test/index.html

# Create symbolic link
sudo rm -f "/data/web_static/current"
sudo ln -s "/data/web_static/releases/test/" "/data/web_static/current"

# Give user ownership of /data
sudo chown -R ubuntu:ubuntu "/data/"

# set nginx location block replacement text
location_directive="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\
\t}"

# set nginx config file
config_file="/etc/nginx/sites-available/default"

# Add location to nginx config
sudo sed -i "29i\ $location_directive" "$config_file"

# Restart nginx service
sudo service nginx restart
