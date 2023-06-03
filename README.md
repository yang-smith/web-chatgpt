# web-chatgpt

这是一个全栈应用，包括前端和后端。前端使用 Vue.js 构建，后端使用 Python Flask 构建。这是一个基于 OpenAI 的 ChatGPT的聊天应用。

![image text](https://github.com/yang-smith/web-chatgpt/blob/main/img/home.png)

试用：http://49.234.79.245:8080/UserChat      （测试账户：test@qq.com  密码：123）

了解更多：[GPT-4实战：从零开始的全栈开发](https://autumnriver.blue/GPT-4-dd16b378166b4264b3f0fd12eb91b003)

## 功能介绍

- 基于 ChatGPT 的聊天功能
- 用户注册和登录
- 用户信息管理
- 用户充值

## 技术栈

- 前端：Vue.js，Vuex
- 后端：Python Flask
- 数据库：Mysql
- AI模型：OpenAI GPT

## 安装指南

1. 克隆仓库到本地

```bash
git clone https://github.com/yang-smith/web-chatgpt.git
```

2. 安装前端依赖

```bash
npm install
```

3. 安装后端依赖

```bash
pip install -r ./backend/requirements.txt
```
4. 修改参数

 修改backend/.envexample中的参数，将之替换为你自己的API，并修改.envexample名称为.env

5. 启动前端服务器

```bash
npm run serve
```

5. 启动后端服务器

```bash
python ./backend/run.py
```

## 使用指南

- 打开浏览器，访问 `http://localhost:8080`，开始使用。

## 许可证

- 这个项目遵循 MIT 许可，详情请参阅 [LICENSE](LICENSE) 文件。

## 联系方式

如果你有任何问题或建议，欢迎联系我：zy892065502@gmail.com

## 鸣谢

感谢 OpenAI 提供的 GPT-4 AI 模型。

---

Ⓒ Copyright 2023, Your Name. All Rights Reserved.