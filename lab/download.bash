#!/usr/bin/env bash
set -uo pipefail

labnum=1
base_url="https://lr2933.github.io/cs61a-spring-2026/lab/"

for labnum in {0..11}; do
    lab=$(printf "lab%02d" "$labnum")
    url="${base_url}${lab}/${lab}.zip"
    htmlurl="${base_url}${lab}"
    zipfile="${lab}.zip"
    dir="${lab}"

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

    echo "----- $lab 处理完成 -----"
    wget -qO- "${htmlurl}" | markdownify > "${dir}/index.md"
done