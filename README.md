# PCL2 自定义主页 - 每日更新版

基于 YARN 粉色系主题设计的 PCL2 自定义主页，**每天自动更新内容**（宜忌、小贴士、问候语都不一样）。

## ✨ 功能

- 📅 **每日宜忌** - 每天不同的宜/忌内容
- 💡 **冒险生存小贴士** - 每天一条 MC 冷知识
- 🌸 **每日问候** - 每天不同的问候语和小图标
- 🔗 **常用资源导航** - MCMOD 百科、LittleSkin 皮肤站
- 💗 **专属定制 & 陪伴提示** - 暖心文案

## 📁 文件结构

```
.
├── Custom.xaml              # 生成的主页文件（自动生成，不要手动改）
├── pcl-home/
│   ├── generate.py          # 生成脚本
│   └── data/
│       └── quotes.json      # 题库（可以自己加内容）
└── .github/
    └── workflows/
        └── daily-generate.yml  # GitHub Actions 每日自动更新
```

## 🚀 本地使用

### 1. 生成本地测试

```bash
cd pcl-home
python generate.py
```

生成的 `Custom.xaml` 在项目根目录，复制到 PCL 的 Custom 文件夹即可。

### 2. 指定种子测试

```bash
python generate.py --seed 20240822   # 同一天种子生成内容一样
python generate.py --seed hello      # 随便写，每次不同
```

## ☁️ GitHub Pages 每日自动更新

### 部署步骤

1. **新建 GitHub 仓库**，把所有文件传上去
2. **开启 GitHub Pages**：Settings → Pages → Source 选 `main` 分支
3. **开启 Actions 写权限**：Settings → Actions → General → Workflow permissions → 选 "Read and write"
4. **手动触发一次**：Actions → 每日生成 PCL 主页 → Run workflow

完成后，每天凌晨自动更新 `Custom.xaml`。

### PCL 端设置

在 PCL 自定义主页设置中，把主页地址改成你的 GitHub Pages 地址：

```
https://你的用户名.github.io/仓库名/Custom.xaml
```

> 💡 PCL 支持加载网络上的 XAML 主页，每次打开都会从 GitHub 拉最新的

## 📝 自己加内容

编辑 `pcl-home/data/quotes.json`，照着格式加就行：

```json
{
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

- `theme` 可选：`Red`、`Blue`、`Yellow`
- `icon` 用 PCL 内置方块图片名（在 `images/Blocks/` 下）

## 🎨 替换顶部猫咪图片

打开 `pcl-home/generate.py`，找到 `GrassPath.png` 那行，换成你的图片链接或本地路径：

```python
Source="https://你的图片地址/cat.png"
```

然后重新生成即可。
