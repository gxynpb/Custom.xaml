# PCL2 自定义主页 - 每日更新版

基于 YARN 粉色系主题设计的 PCL2 自定义主页，**每天自动更新内容**。

## ✨ 每天随机的内容

- 🖼️ **顶部猫咪横幅** - 3 张不同风格随机（雨天撑伞、星空赏月、樱花树下）
- 📅 **今日宜忌** - 7 组不同的宜/忌内容
- 💡 **冒险生存小贴士** - 8 条 MC 冷知识
- 🌸 **每日问候** - 8 种问候语 + 对应小图标
- 🔗 **常用资源导航** - MCMOD 百科、LittleSkin 皮肤站
- 💗 **专属定制 & 陪伴提示**

## 📁 文件结构

```
.
├── Custom.xaml                  # 生成的主页文件（自动生成）
├── README.md
├── .github/
│   └── workflows/
│       └── daily-generate.yml   # 每日自动更新
└── pcl-home/
    ├── generate.py              # 生成脚本
    ├── data/
    │   └── quotes.json          # 题库（自己加内容改这个）
    └── assets/
        ├── banner-cat.jpg       # 横幅图1：雨天撑伞
        ├── banner-cat2.jpg      # 横幅图2：星空赏月
        └── banner-cat3.jpg      # 横幅图3：樱花树下
```

## 🚀 GitHub Pages 部署

### 1. 上传到 GitHub

把整个项目传到 GitHub 仓库（`.github` 文件夹是隐藏的，要手动创建 workflow 文件）。

### 2. 开启 Pages

- Settings → Pages → Source 选 **Deploy from a branch**
- Branch 选 **main** / **root** → Save

### 3. 给 Actions 写权限

- Settings → Actions → General → **Workflow permissions**
- 选 **Read and write permissions** → Save

### 4. 手动跑一次

- Actions → 每日生成 PCL 主页 → **Run workflow**

### 5. PCL 端设置

PCL 自定义主页地址填：
```
https://你的用户名.github.io/你的仓库名/Custom.xaml
```

## 💻 本地使用

```bash
cd pcl-home
python generate.py                  # 按当天日期生成
python generate.py --seed hello     # 指定种子测试
```

## 📝 自己加内容

编辑 `pcl-home/data/quotes.json`：

```json
{
  "banners": ["banner-cat.jpg", "banner-cat2.jpg"],
  "yiji": [
    { "yi": "宜的内容", "ji": "忌的内容" }
  ],
  "tips": [
    { "theme": "Red", "title": "【标题】", "content": "内容" }
  ],
  "greetings": [
    { "text": "问候语", "icon": "Egg.png" }
  ]
}
```

- `theme`：`Red` / `Blue` / `Yellow`
- `icon`：PCL 内置方块图片名
- `banners`：横幅图文件名，放在 `pcl-home/assets/` 里

## 🎨 修改仓库地址

打开 `pcl-home/generate.py`，把顶部的 `DEFAULT_REPO` 改成你自己的：

```python
DEFAULT_REPO = "你的用户名/你的仓库名"
```
