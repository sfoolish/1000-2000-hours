## build flask dev images

docker build -t flask:sf .

## Run flask

docker run -v $(pwd):/var/www -P flask:sf
