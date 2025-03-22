@echo off
echo ===== Firecrawl MCP测试 =====

REM 检查Python是否已安装
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo 错误: 未检测到Python安装，请先安装Python
    exit /b 1
)

REM 检查是否已配置.env文件
if not exist ".env" (
    echo 检测到尚未配置.env文件，正在从示例创建...
    copy .env.example .env
    echo 请编辑.env文件，填入你的Firecrawl API密钥
    exit /b 1
)

REM 安装所需依赖
echo 正在安装所需依赖...
pip install -r requirements.txt

REM 创建results目录
if not exist "results" mkdir results

REM 运行测试脚本
echo 正在运行测试脚本...
python mcp_firecrawl_test.py

echo ===== 测试完成 =====
echo 查看results目录获取结果文件
pause