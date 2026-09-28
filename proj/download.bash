#!/usr/bin/env bash
proj_name=("hog"  "cats" "ants" "scheme" "scheme_contest")
base_url="https://lr2933.github.io/cs61a-spring-2026/proj/"

for name in ${proj_name[@]};do
    zipurl="${base_url}${name}/${name}.zip"
    htmlurl="${base_url}${name}/"
    zipfile="${name}.zip"
    dir="${name}"

    # ---------- 1. 检查 zip 是否已存在 ----------
    if [[ -f "$zipfile" ]]; then
        read -r -p "文件 $zipfile 已存在，是否重新下载覆盖? [y/N] " ans
        case "$ans" in
            [yY]|[yY][eE][sS])
                echo "重新下载 $zipurl ..."
                wget -O "$zipfile" "$zipurl" || { echo "下载失败: $zipurl"; continue; }
                ;;
            *)
                echo "跳过下载，使用已有 $zipfile"
                ;;
        esac
    else
        echo "下载 $zipurl ..."
        wget -O "$zipfile" "$zipurl" || { echo "下载失败: $zipurl"; continue; }
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

    wget -qO- "${htmlurl}" | markdownify > "${dir}/index.md"
done