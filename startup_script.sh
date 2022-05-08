sudo usermod -aG docker $USER
newgrp docker
printf 'yes' | gcloud auth configure-docker
curl https://raw.githubusercontent.com/majdi912/supervision/main/docker-compose.yml --output docker-compose.yml
docker-compose up 
