# add-ass-to-videos

Add .ass subtitles to videos using python. This tool is writen especially for adding danmaku to stream recordings.

为视频添加 `.ass` 格式的字幕。这个工具是专为给录播视频加弹幕而写的。

依赖：

- 配置好 `ffmpeg` 的环境变量
- 安装 `ffmpeg-python` : `pip install ffmpeg-python`

用法：

```shell
python main.py -folder [folder 视频文件夹]
```

只要指定文件夹，脚本能自动识别到文件夹下所有视频，批量加弹幕。
完成后会在原视频目录下生成和原视频同名的 `.mkv` 格式视频。
注意：`ass` 格式的文件需要与视频同名且在同一文件夹下。