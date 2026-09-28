#!/usr/bin/env bash
hwnum=1
base_url="https://lr2933.github.io/cs61a-spring-2026/hw/"
for hwnum in {1..10};do
    hw=$(printf "hw%02d" "$hwnum")
    url="${base_url}${hw}/${hw}.zip"
    htmlurl="${base_url}${hw}/"
    zipfile="${hw}.zip"
    dir="${hw}"

    # ---------- 1. 检查 zip 是否已存在 ----------
    if [[ -f "$zipfile" ]]; then
        read -r -p "文件 $zipfile 已存在，是否重新下载覆盖? [y/N] " ans
        case "$ans" in
            [yY]|[yY][eE][sS])
                echo "重新下载 $url ..."
                wget -O "$zipfile" "$url" || { echo "下载失败: $url"; continue; }
                ;;
            *)
                echo "跳过下载，使用已有 $zipfile"
                ;;
        esac
    else
        echo "下载 $url ..."
        wget -O "$zipfile" "$url" || { echo "下载失败: $url"; continue; }
    fi

    # ---------- 2. 检查解压目录是否已存在 ----------
    if [[ -d "$dir" ]]; then
        read -r -p "目录 $dir 已存在，是否删除并重新解压? [y/N] " ans
        case "$ans" in
            [yY]|[yY][eE][sS])
                echo "删除旧目录 $dir 并重新解压 ..."
                rm -rf "$dir"
                unzip -o "$zipfile" -d .
                ;;
            *)
                echo "跳过解压，保留已有目录 $dir"
                ;;
        esac
    else
        echo "解压 $zipfile ..."
        unzip -o "$zipfile" -d .
    fi

    echo "----- $hw 处理完成 -----"
    wget -qO- "${htmlurl}" | markdownify > "${dir}/index.md"
done
