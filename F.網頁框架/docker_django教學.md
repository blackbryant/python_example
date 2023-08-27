### 建立docker的Image

>docker build -t myblog .  


#會把容器的80port指向機器的5000port，接下來在瀏覽器輸入
>docker run -p 8000:8000 myblog


