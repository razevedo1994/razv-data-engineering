# /!\ WARNING: RESET EVERYTHING! 
# Remove all containers/networks/volumes/images and data in db
docker-compose down
docker system prune -f
docker volume prune -f
docker network prune -f
docker rmi -f $(docker images -a -q)