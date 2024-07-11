#!/usr/bin/env bash
# This script sets up web servers for the deployment of web_static.

# Update and install Nginx if not already installed
sudo apt-get update -y
sudo apt-get install nginx -y

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link, recreate it if it already exists
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content
config="server {
    listen 80;
    server_name _;
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}"

# Add the new server block to Nginx configuration
echo "$config" | sudo tee /etc/nginx/sites-available/default > /dev/null

# Restart Nginx to apply changes
sudo service nginx restart
