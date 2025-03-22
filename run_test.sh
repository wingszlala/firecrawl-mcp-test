#!/bin/bash

echo "===== Firecrawl MCP测试 ====="

# 检查Python是否已安装
if ! command -v python3 &> /dev/null; then
    echo "错误: 未检测到Python安装，请先安装Python"
    exit 1
fi

# 检查是否已配置.env文件
if [ ! -f ".env" ]; then
    echo "检测到尚未配置.env文件，正在从示例创建..."
    cp .env.example .env
    echo "请编辑.env文件，填入你的Firecrawl API密钥"
    exit 1
fi

# 安装所需依赖
echo "正在安装所需依赖..."
pip3 install -r requirements.txt

# 创建results目录
mkdir -p results

# 运行测试脚本
echo "正在运行测试脚本..."
python3 mcp_firecrawl_test.py

echo "===== 测试完成 ====="
echo "查看results目录获取结果文件"