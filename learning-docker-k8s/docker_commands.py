# build a docker image out of Dockerfile
docker build -t <image_tag> <Dockerfile_path>

# to see detailed output of building an image
docker build --progress=plain -t <image_tag> <Dockerfile_path>

# run a docker container
docker run \
-it \			# remove container after it starts running
--rm \
-e <ENV_NAME>=<ENV_VALUE> \
-p <port_on_laptop_browser>:<container_port> \
--name <container_name> \
-v "<local_path_or_path_on_laptop>:<path_inside_container>" \
-t <image_name>

# shut down a container
docker stop <container_id_or_name>

# remove a container
docker rm <container_id_or_name>

# remove exited containers
docker rm $(docker ps --filter status=exited -q)

# remove dangling images
docker rmi $(docker images --filter dangling=true)

docker inspect <image_name>

docker image history <image_name>

docker ps -all

# to start shell by changing the entrypoint
docker run --entrypoint=/bin/sh -it <image_name>

# to start python interpreter with entrypoint
docker run --entrypoint=python -it <python_image_name> 



# run tensorflow/serving where -e is for environment, -it is for interactive terminal
docker run -it --rm -p 8501:8501 --name my_container_name \
--mount type=bind,source=Users\Arslan\Desktop...,target=/models/my_test_model \
-e MODEL_NAME=my_test_model -t tensorflow/serving

# alternate way to run tensorflow/serving with volumes, note the quotes 
# and colon where left is computer's file system, right of colon is container's file system
docker run -it --rm -p 8501:8501 --name my_model_container \
-v "C:\Users\Arslan\Desktop\tensorflow-serving-example\models-2023-08-26-13-01-24:/models/my_basic_model" \
-e MODEL_NAME=my_basic_model -t tensorflow/serving




# TENSORFLOW saved_model_cli
# shows serving model's tag 
saved_model_cli show --dir <directory_containing_model>

# uses tag to show serving_default
saved_model_cli show --dir <directory_containing_model> --tag_set serve

# shows model's input and output structure among other things
saved_model_cli show --dir <directory_containing_model> --tag_set serve \
--signature_def serving_default