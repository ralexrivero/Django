# Deploy

## run on DO

### ssh to the server

- `ssh -i ~/.ssh/growthlearning root@157.230.83.162`

## installation process

### docker

```bash
sudo apt-get update

 sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

- `sudo mkdir -p /etc/apt/keyrings`
- `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg`

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

- `sudo apt-get update`
- `sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin`
- `sudo service docker start`
- `sudo groupadd docker`
- `sudo usermod -aG docker $USER`
- `newgrp docker`
- `sudo systemctl enable docker.service`
- `sudo systemctl enable containerd.service`
