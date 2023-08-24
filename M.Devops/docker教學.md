### 建立docker的Image

>docker build -t hello-world-docker .


#會把容器的80port指向機器的5000port，接下來在瀏覽器輸入
>docker run -p 5000:5000 hello-world-docker

CONTAINER ID   IMAGE                COMMAND           CREATED          STATUS         PORTS                    NAMES
edb52717a93d   hello-world-docker   "python app.py"   10 minutes ago   Up 2 seconds   0.0.0.0:5000->5000/tcp   eloquent_bouman

>docker logs edb52717a93d

>curl http://127.0.0.1:5000

Hello, World! (from a Docker container)%

#### To tag a Docker image, run docker tag
>docker tag hello-world-docker hello-world-docker:v1

>docker images hello-world-docker

#### Publish both image tags to Docker Hub with docker push
#### you need to tag it with the Docker Hub repository name
>docker tag hello-world-docker:latest e49134030e hello-world-docker:latest
##### 上傳自己的版本
>docker push e49134030e/hello-world-docker:latest

#### Running a Docker Container with the Same Image on a Different Host



