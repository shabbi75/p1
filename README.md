# homework
Back-end api update:
Prefixed all end points to /api

frontend folder contains all the static assets or front end code

Prerequisite to run frontend:
1. Node
2. NPM
Once navigated to frontend folder, run npm install

once all dependencies installed locally or globally,
run gulp
This will run a web server at port 5001 which can be accessed at
localhost:5001

gulp's web server proxies all backend calls to api being served by python web server
 at port 3000 (if running, it can be accessed at localhost:3000)
