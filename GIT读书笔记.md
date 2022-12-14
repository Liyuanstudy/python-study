#                             GIT原理及基本使用

### 一、简述

**在Git出现之前，大部分公司还是用SVN进行项目管理的，这里来对比一下:**

#### 集中式（svn）：

​        **集中式的版本控制系统都有一个单一的几种管理的服务器，保存所有文件的修订版本，而协同工作的人们都通过客户端连接到这台服务器，取出最新的文件或者提交更新。**

##### 优点：1、管理方便，符合一般逻辑；2、安全性高；3、代码一致性高；4、适合人数不多的开发。

#####  缺点：**1、服务器压力大，数据库容量暴增；如果连接不上服务器，基本不能工作；3、不适合开源开发**。

#### 分布式（Git）：

​       **在[分布式]版本控制系统中，客户端不只提取最新版本的文件快照，而是把原始的代码仓库完整的镜像下来，因此任何一处的服务器发生崩溃，都可以用任意本地仓库进行恢复；这个系统可以指定和不同的远端代码仓库进行交互。**

##### 优点：1、适合分布式开发，强调个体；2、公共服务器压力和数据量都不会太大；3、速度快，灵活性高；4、任意两个开发人员更容易冲突；5、离线工作。

##### 缺点：代码保密性差，一旦开发者把整个库克隆下来，就可以公开所有版本和版本信息。

###  二、配置信息

```
配置用户名：git config --global user.name "xxx"
配置邮箱：git config --global user.email "xxx"
配置大小写敏感：git config --global core.ignorecase false
查看配置信息：git config --list
```

### 三、基本原理

#### Git工作区：

**1、Remote：远程仓库，托管代码的服务器（类似github）**

**2、Repository：仓库区，也就是本地仓库（.git文件夹），安全存放数据的位置，里面有提交所有版本的数据，其中HEAD指向最新放入仓库的版本；**

**3、index/Stage：暂存区，用于临时存放改动，实际上是一个文件，用于保存即将提交到文件列表的信息；**

**4、workspace：工作区，也就是编辑文件的位置。**

#### Git文件状态：

- **Untracked：未跟踪，在此文件夹中，但没有加到git库，不参与版本控制，通过git add状态变为staged；**
- **Unmodified：文件已经入库，未修改，即版本库中的文件快照内容与文件夹一致这种类型的文件有两种取出，如果被修改，变为modified，如果被移除版本库git rm，变为Untracked；**
- **Modified：文件已被修改，这个文件有两个去处，第一个是staged，第二个是unmodified；**
- **Staged：执行git commit 则将修改同步到库中，这时库中的文件和本地文件虽为一致，文件为Unmodified。执行git reset HEAD filename取消暂存，文件状态为modified。**

### 四、基本操作

1、git add          添加文件

2、git mv            移动或重命名文件，目录或符号链接   

3、git rm             从工作区和索引中删除文件

4、git commit    添加文件到本地仓库

5、git reset        回退版本/提交

6、git push        将本地修改推送到远程库

7、git fetch        更新远程库信息

8、git diff           显示提交和工作树之间的更改

9、git clone       拉取远程仓库到本地

10、git pull        蒋远程库最新修改更新到本地

11、git status    显示工作目录和暂存区的状态

##### 下面讲解一些简单操作：

- **初始化本地仓库**

  ```java
  git init     # 将本地文件夹变成一个本地仓库
  ll -ah       #可以看到。git隐藏文件夹
  ```

- **新增一个文件**

  ```java
  git add text.txt                #新增一个文件
  git commit -m "add a text.txt"  #提交信息
  ```

- **如果提交新版本有bug，回退版本**

  ```java
  git log                #查看提交的日志
  git reset --head Head^ #回退到上个版本，^代表回退几个版本（如果已经commit，需要这样回退）
  ```

- **分支与标签管理**

  ```java
  git checkout -b dev  #创建dev分支
  git branch           #查看当前分支
  git checkout master  #切换到master分支
  git merge dev        #将dev分支合并到当前分支
  git branch -d dev    #删除dev分支
  ```

### 五、总结

**1、Git实际上操作命令并不多，主要是要理解其中的工作区和文件状态的概念，这个是Git最本质的部分；**

**2、我们在使用Git的时候不怕出错，实际上会有很多容错空间，也不怕突然有人删库跑路**

**3、当然Git的命令远不止上面提到的这些，还有很多需要在实际使用中不断了解；**





