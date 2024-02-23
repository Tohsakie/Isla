docker-compose down
docker images --format "{{.Repository}}:{{.Tag}}" | grep '^isla_' | xargs -I {} docker rmi {}
./init_docker-compose.sh
docker-compose up