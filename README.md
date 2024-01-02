# WebFramework
基于PyQT5的html套壳框架
基于python的PyQT5中的browser.load方法加载Html

<h1>详细介绍🤡</h1>
#语言与根框架
使用PyQT中的Web组件对本地段的html文件进行加载，实现html打包
<h1>使用教程-文件介绍</h1>
<h2>main.py --框架源文件</h2>
<h2>package.json --框架的配置文件</h2>
<h2>参数设置</h2>
<h4>name：标题</h4>
<h4>version:版本号</h4>
<h4>size_winth,size_height:生成窗口的长，宽</h4>
<h4>icon:图标</h4>
<h4>main_html:加载html文件地址</h4>
<h1>使用教程-操作步骤</h1>
1.配置 .package.json的加载参数
2.打开命令行运行main.py（python ./main.py)
<h1>常见错误❌</h1>
1.No module named 'PyQt5'
错误原因：PyQT5安装异常，可以在重新安装PyQT5库（pip install pyqt5)
2.No module named 'PyQt5.QtWebEngineWidgets'
错误原因：PyQT5.QtWebEngineWidgets异常，可以在重新安装库（pip install PyQtWebEngine)
