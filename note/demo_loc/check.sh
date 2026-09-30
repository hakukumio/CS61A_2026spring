#!/usr/bin/env bash
# 这个文件就是"完成的定义"。
# 绿了 = 当前代码在约定范围内是对的。红了 = 不许往下走,先看 diff。
# 用法:  bash check.sh
set -u
cd "$(dirname "$0")"

expected=$(cat data/expected.txt)
actual=$(python3 loc.py data/sample 2>&1)

if [ "$actual" = "$expected" ]; then
    echo "PASS"
else
    echo "FAIL  —— 左边是期望,右边是实际:"
    diff <(echo "$expected") <(echo "$actual")
    exit 1
fi
