"""下载 Windows Python 3.11 的 wheel 依赖。"""
import subprocess
import sys
from pathlib import Path

REQ_FILE = Path(__file__).parent.parent / "requirements.txt"
WHEELS_DIR = Path(__file__).parent.parent / "build_cache" / "wheels_windows"

WHEELS_DIR.mkdir(parents=True, exist_ok=True)

# 读取 requirements，排除纯源码包（jieba 无预编译 wheel）
with open(REQ_FILE) as f:
    all_pkgs = [l.strip() for l in f if l.strip() and not l.startswith('#')]

binary_pkgs = [p for p in all_pkgs if 'jieba' not in p]
source_pkgs = [p for p in all_pkgs if 'jieba' in p]

# 写入临时 requirements 文件（仅二进制包）
tmp_req = Path(__file__).parent / "_tmp_req_binary.txt"
tmp_req.write_text('\n'.join(binary_pkgs))

# Step 1: 下载平台相关的二进制 wheel
print("[1/2] 下载平台相关 wheel（--python-version 3.11 --platform win_amd64）...")
subprocess.run([
    sys.executable, "-m", "pip", "download",
    "-r", str(tmp_req),
    "-d", str(WHEELS_DIR),
    "--python-version", "3.11",
    "--platform", "win_amd64",
    "--only-binary=:all:",
], capture_output=False)

# Step 2: 补充下载纯源码包
if source_pkgs:
    print("\n[2/2] 补充下载纯源码包...")
    subprocess.run([
        sys.executable, "-m", "pip", "download",
    ] + source_pkgs + [
        "-d", str(WHEELS_DIR),
        "--no-binary=:all:",
    ], capture_output=False)

# 清理临时文件
tmp_req.unlink(missing_ok=True)

print("\n完成！Wheels 已下载到:", WHEELS_DIR)
