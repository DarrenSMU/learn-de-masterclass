notes : docker entrypoint runs sql in lexicographic order 

cd into folder 

docker build -t custom_psql .

docker run -d --name custom_psql_running -p 5432:5432 -e POSTGRES_HOST_AUTH_METHOD=trust custom_psql