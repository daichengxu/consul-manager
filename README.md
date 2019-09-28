# consul-manager
# 一、用途
1.查找consul状态异常的service

2.清除异常service

# 二、运行环境
centos7.5

python2.7

urllib2、json、time、os、ast

# 三、安装
1.下载项目

cd /opt

git clone https://github.com/daichengxu/consul-manager.git

# 四、配置文件
## ./consul-manager/config/configer.py
## 注:需要修改Node_IP,部署节点机器的ip地址.
## SET PATH
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Data_DIR=os.path.join(BASE_DIR, 'data')

Node_IP='10.0.0.x'

# 五、运行项目
1)
python /opt/consul-manager/run.py
2)
chmod +x /opt/consul-manager/run.py
/opt/consul-manager/run.py

# 六、目录结构
./consul-manager

├── config

│   ├── configer.py

│   ├── configer.pyc

│   ├── __init__.py

│   └── __init__.pyc

├── core

│   ├── deregister.py

│   ├── deregister.pyc

│   ├── __init__.py

│   ├── __init__.pyc

│   ├── node.py

│   ├── node.pyc

│   ├── service.py

│   ├── service.pyc

│   ├── views.py

│   └── views.pyc

├── data

│   ├── data.json

│   ├── __init__.py

│   ├── node.json

│   └── run.log

├── __init__.py

├── LICENSE

├── README.md

└── run.py
