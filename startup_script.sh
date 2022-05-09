sudo usermod -aG docker $USER
newgrp docker
sudo curl -L https://github.com/docker/compose/releases/download/v2.4.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
curl https://raw.githubusercontent.com/majdi912/supervision/main/docker-compose.yml --output docker-compose.yml
printf "yes" | gcloud auth configure-docker
docker-compose up
