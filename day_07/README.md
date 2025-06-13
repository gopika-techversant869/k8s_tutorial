docker volume without docker compose
-------------------------------------
First you create the app with docker file - You can refer day_04 or using the "flask-volume-up" app.

First case - Without Volume
--------------------------------

Build the image
------------------------
docker build -t flask-no-volume-app .

Run the image
--------------------

docker run -d --name flask-no-volume -p 5000:5000 flask-no-volume-app

Test the API
---------------------------
Add data
-----------
curl -X POST -H "Content-Type: application/json" \
  -d '{"name": "Alice"}' \
  http://localhost:5000/add

Get data
------------------
curl http://localhost:5000/users

Then stop and remove the container
---------------------------------------
docker stop flask-no-volume
docker rm flask-no-volume

Agian run 
-------------
docker run -d --name flask-no-volume -p 5000:5000 flask-no-volume-app

Then test API
-----------
curl http://localhost:5000/users

Here you got an empty list []
Because data.json was stored inside container filesystem, and when container was deleted, the file was deleted.

Second Case - With Volume
-------------------------------------

Here we use the volume concept 
---------------------------------

Create a named volume in side the docker:

  docker volume create flask-data

Then run the same image that we already created above.

docker run -d \
  --name flask-with-volume \
  -p 5000:5000 \
  -v flask-data:/app \
  flask-no-volume-app

Here 
      - This mounts volume flask-data into /app directory inside container.
      - data.json will now live inside volume.

Then you should follow this:
------------------------------------

- Test the API again:
      - Add the data
      - get the data

- stop and delete the container
- Again start the container with same volume 
- Test the get data
   You have to see the difference here.




