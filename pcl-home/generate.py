#!/usr/bin/env python3
"""
PCL2 自定义主页生成器 - YARN 粉色系主题
从题库中随机抽取内容，生成 Custom.xaml 文件

用法:
    python generate.py                 # 按当天日期生成（同一天内容一样）
    python generate.py --seed hello    # 指定种子
    python generate.py --repo gxynpb/Custom.xaml  # 指定 GitHub 仓库（用于图片路径）
"""

import json
import random
import argparse
import os
from datetime import datetime

# ⚙️ 配置：改成你的 GitHub 用户名/仓库名，图片会自动用 Pages 地址
DEFAULT_REPO = "gxynpb/Custom.xaml"  # 格式：用户名/仓库名

XAML_TEMPLATE = '''<!-- PCL2 自定义主页 - YARN 粉色系主题
     由 generate.py 自动生成，每天内容不一样
     生成时间: {gen_time}
     种子: {seed}
     如果玩炸了，把这个文件直接删除即可恢复默认。 -->

<!-- ============================================ -->
<!--  顶部双栏：左侧猫咪插画 + 右侧今日宜忌 -->
<!-- ============================================ -->
<Grid Margin="0,0,0,15">
    <Grid.ColumnDefinitions>
        <ColumnDefinition Width="2*" />
        <ColumnDefinition Width="1*" />
    </Grid.ColumnDefinitions>

    <!-- 左侧：猫咪插画横幅 -->
    <local:MyCard Grid.Column="0" CanSwap="False" HasMouseAnimation="False" Margin="0,0,8,0">
        <StackPanel Margin="0,0,0,0">
            <local:MyImage Height="180" HorizontalAlignment="Stretch"
                           Source="{banner_url}"
                           FallbackSource="pack://application:,,,/images/Blocks/GrassPath.png" />
        </StackPanel>
    </local:MyCard>

    <!-- 右侧：今日宜忌 -->
    <local:MyCard Grid.Column="1" Title="今日宜忌" CanSwap="True" IsSwapped="False" Margin="8,0,0,0">
        <StackPanel Margin="20,40,18,15">
            <TextBlock TextWrapping="Wrap" Margin="0,0,0,6" Foreground="#2E7D32" FontWeight="Bold" FontSize="12"
                       Text="【宜】{yi}" />
            <TextBlock TextWrapping="Wrap" Margin="0,0,0,0" Foreground="#C62828" FontWeight="Bold" FontSize="12"
                       Text="【忌】{ji}" />
        </StackPanel>
    </local:MyCard>
</Grid>

<!-- ============================================ -->
<!--  第二行双栏：左侧冒险生存小贴士 + 右侧每日问候 -->
<!-- ============================================ -->
<Grid Margin="0,0,0,15">
    <Grid.ColumnDefinitions>
        <ColumnDefinition Width="1.5*" />
        <ColumnDefinition Width="1*" />
    </Grid.ColumnDefinitions>

    <!-- 左栏：冒险生存小贴士 -->
    <local:MyCard Grid.Column="0" Title="冒险生存小贴士" CanSwap="True" IsSwapped="False" Margin="0,0,8,0">
        <StackPanel Margin="25,40,23,15">
            <local:MyHint Theme="{tip_theme}"
                          Text="{tip_title}" />
            <TextBlock TextWrapping="Wrap" Margin="0,8,0,0"
                       Text="{tip_content}" />
        </StackPanel>
    </local:MyCard>

    <!-- 右栏：每日问候 -->
    <local:MyCard Grid.Column="1" Title="每日问候" CanSwap="True" IsSwapped="False" Margin="8,0,0,0">
        <StackPanel Margin="25,40,23,15">
            <Grid>
                <Grid.ColumnDefinitions>
                    <ColumnDefinition Width="*" />
                    <ColumnDefinition Width="Auto" />
                </Grid.ColumnDefinitions>
                <TextBlock Grid.Column="0" TextWrapping="Wrap" VerticalAlignment="Center" FontSize="12"
                           Text="{greeting_text}" />
                <local:MyImage Grid.Column="1" Width="35" Height="35"
                               Source="{greeting_icon_url}"
                               FallbackSource="pack://application:,,,/images/Blocks/Grass.png" />
            </Grid>
        </StackPanel>
    </local:MyCard>
</Grid>

<!-- ============================================ -->
<!--  常用资源导航（双列并排） -->
<!-- ============================================ -->
<local:MyCard Title="常用资源导航" Margin="0,0,0,15" CanSwap="True" IsSwapped="False">
    <StackPanel Margin="25,40,23,15">
        <Grid>
            <Grid.ColumnDefinitions>
                <ColumnDefinition Width="1*" />
                <ColumnDefinition Width="1*" />
            </Grid.ColumnDefinitions>
            <local:MyListItem Grid.Column="0" Margin="-5,2,5,8"
                              Logo="{mcmod_icon_url}"
                              Title="MCMOD 百科"
                              Info="最大的 Minecraft 中文 MOD 百科"
                              EventType="打开网页"
                              EventData="https://www.mcmod.cn/"
                              Type="Clickable" />
            <local:MyListItem Grid.Column="1" Margin="5,2,-5,8"
                              Logo="{littleskin_icon_url}"
                              Title="LittleSkin 皮肤站"
                              Info="快速、可靠的 Minecraft 皮肤站"
                              EventType="打开网页"
                              EventData="https://littleskin.cn/"
                              Type="Clickable" />
        </Grid>
    </StackPanel>
</local:MyCard>

<!-- ============================================ -->
<!--  专属定制 & 陪伴提示 -->
<!-- ============================================ -->
<local:MyCard Margin="0,0,0,15" CanSwap="False" HasMouseAnimation="False">
    <StackPanel Margin="25,18,23,18">
        <Grid>
            <Grid.ColumnDefinitions>
                <ColumnDefinition Width="*" />
                <ColumnDefinition Width="Auto" />
            </Grid.ColumnDefinitions>
            <TextBlock Grid.Column="0" TextWrapping="Wrap" FontWeight="Bold" FontSize="13"
                       Text="💗 Crafted with love · For My Baby 专属定制 🌸" />
            <TextBlock Grid.Column="1" Foreground="#888888" FontSize="11"
                       Text="⏱ 本次已陪伴 5 分钟" />
        </Grid>
        <TextBlock TextWrapping="Wrap" Margin="0,8,0,0" Foreground="#666666" FontSize="11"
                   Text="已经玩了 5 分钟啦，今天有没有挖到钻石？有没有在悄悄想我吖~ 💎💘" />
    </StackPanel>
</local:MyCard>

<!-- ============================================ -->
<!--  主题定制与管理 -->
<!-- ============================================ -->
<local:MyCard Title="主题定制与管理" Margin="0,0,0,0" CanSwap="True" IsSwapped="True">
    <StackPanel Margin="25,40,23,15">
        <TextBlock TextWrapping="Wrap" Margin="0,0,0,8"
                   Text="在这里管理你的主题配置和自定义内容。" />
        <local:MyButton Height="35" HorizontalAlignment="Left" Padding="20,0,20,0" Margin="0,4,0,4"
                        Text="打开 PCL 个性化设置"
                        EventType="打开帮助"
                        EventData="个性化/主页自定义.json" />
    </StackPanel>
</local:MyCard>
'''


def main():
    parser = argparse.ArgumentParser(description='PCL2 自定义主页生成器')
    parser.add_argument('--seed', type=str, default=None,
                        help='随机种子（默认用当天日期，保证同一天内容一致）')
    parser.add_argument('--data', type=str, default='data/quotes.json',
                        help='题库 JSON 文件路径')
    parser.add_argument('--output', type=str, default='Custom.xaml',
                        help='输出 XAML 文件路径')
    parser.add_argument('--repo', type=str, default=DEFAULT_REPO,
                        help='GitHub 仓库 用户名/仓库名，用于生成图片地址')
    args = parser.parse_args()

    # 确定种子
    if args.seed:
        seed = args.seed
    else:
        seed = datetime.now().strftime('%Y%m%d')

    random.seed(seed)

    # 读取题库
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, args.data)
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 随机抽取横幅
    banner_file = random.choice(data['banners'])

    # 随机抽取3个不重复的图标（MCMOD / LittleSkin / 每日问候）
    icon_pool = data['icons'].copy()
    random.shuffle(icon_pool)
    mcmod_icon_file = icon_pool[0]
    littleskin_icon_file = icon_pool[1]
    greeting_icon_file = icon_pool[2]

    # 随机抽取文字内容
    yiji = random.choice(data['yiji'])
    tip = random.choice(data['tips'])
    greeting = random.choice(data['greetings'])

    # 构建图片地址（GitHub Pages）
    repo_parts = args.repo.split('/')
    if len(repo_parts) == 2:
        user, repo_name = repo_parts
        base_url = f"https://{user}.github.io/{repo_name}/pcl-home/assets"
        banner_url = f"{base_url}/{banner_file}"
        greeting_icon_url = f"{base_url}/{greeting_icon_file}"
        mcmod_icon_url = f"{base_url}/{mcmod_icon_file}"
        littleskin_icon_url = f"{base_url}/{littleskin_icon_file}"
    else:
        base_url = "pcl-home/assets"
        banner_url = f"{base_url}/{banner_file}"
        greeting_icon_url = f"{base_url}/{greeting_icon_file}"
        mcmod_icon_url = f"{base_url}/{mcmod_icon_file}"
        littleskin_icon_url = f"{base_url}/{littleskin_icon_file}"

    # 生成 XAML
    xaml = XAML_TEMPLATE.format(
        gen_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        seed=seed,
        banner_url=banner_url,
        yi=yiji['yi'],
        ji=yiji['ji'],
        tip_theme=tip['theme'],
        tip_title=tip['title'],
        tip_content=tip['content'],
        greeting_text=greeting['text'],
        greeting_icon_url=greeting_icon_url,
        mcmod_icon_url=mcmod_icon_url,
        littleskin_icon_url=littleskin_icon_url,
    )

    # 写入文件
    output_path = os.path.join(script_dir, '..', args.output)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(xaml)

    print(f'✅ 生成成功！')
    print(f'   种子: {seed}')
    print(f'   横幅图: {banner_file}')
    print(f'   MCMOD图标: {mcmod_icon_file}')
    print(f'   LittleSkin图标: {littleskin_icon_file}')
    print(f'   问候图标: {greeting_icon_file}')
    print(f'   今日宜忌: {yiji["yi"][:15]}...')
    print(f'   小贴士: {tip["title"]}')
    print(f'   问候语: {greeting["text"][:20]}...')
    print(f'   输出: {output_path}')


if __name__ == '__main__':
    main()
