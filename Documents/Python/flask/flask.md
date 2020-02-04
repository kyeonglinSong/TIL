191110(일)

# Flask

### flask

python 웹 어플리케이션 프레임워크. Django 보다 스케일이 작다.



### flask로 서버 구동시키기



####1. flask 설치

```bash
$pip install flask
```

#### 2. flask 어플리케이션 만들기

app.py

```python
from flask import flask

app = Flask(__name__)

if __name__ == '__main__':
  app.run(host, port)
```



