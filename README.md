# Green-Smart-Academy 
  
## 网站介绍
中文名绿色智能学院（绿智学堂），是一个讲述人工智能技术在环保领域的应用创新的知识普及类网站。网站名称结合了“绿色”（环保）和“智慧”（人工智能）的概念，传达出网站在环保科技教育方面的核心价值。

## 系统框架
本系统基于Html+Flask+Mysql框架
- static：存放各种图片及专辑音频等静态资源
- model: 实现后端各个功能
- templates: 实现前端各个页面
- app.py：连接前后端，实现交互功能

## 数据库介绍
主要从知网上下载了一些有关文章的题名、作者、日期、摘要、关键词等信息，建立了三个表
- authors:作者
- papers：文章
- create:作者与文章间的创作关系

## 运行方法
- 需要安装以下的python包：Flask(backend)、Pymysql(connecting the backend and the database)
- 数据库连接：在navicat或者mysql中运行全部的sql文件，修改data.py中有关db的username和password;
- 在编辑配置中新建编辑器如Flask Server，选择路径为app.py文件，
- 运行得到网站的url，点击url即可在浏览器中登录该歌词系统
