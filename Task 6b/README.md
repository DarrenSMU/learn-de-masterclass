docker pull postgrest/postgrest

run dockered postgres from 5a


docker run -p 3000:3000 -e PGRST_DB_URI="postgres://postgres@[local network ipv4 Not localhost]:5432/db" -e PGRST_DB_ANON_ROLE="postgres" postgrest/postgrest

postman get lcoalhost:3000/actor with header range : 0-9

