import os
from firecrawl import FirecrawlApp
import json
from dotenv import load_dotenv

# ANSI color codes
class Colors:
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

# 加载环境变量
load_dotenv()

# 获取API密钥
firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")

# 初始化FirecrawlApp
app = FirecrawlApp(api_key=firecrawl_api_key)

def test_scrape():
    """测试网页抓取功能"""
    try:
        print(f"{Colors.YELLOW}开始抓取测试页面...{Colors.RESET}")
        # 抓取百度首页作为示例
        url = "https://www.baidu.com"
        result = app.scrape_url(url, params={'formats': ['markdown', 'html']})
        
        print(f"{Colors.GREEN}抓取成功！{Colors.RESET}")
        print(f"{Colors.CYAN}标题: {result.get('metadata', {}).get('title', '未知')}{Colors.RESET}")
        print(f"{Colors.CYAN}描述: {result.get('metadata', {}).get('description', '未知')}{Colors.RESET}")
        
        # 将结果保存到文件中
        with open("scrape_result.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        print(f"{Colors.GREEN}结果已保存到scrape_result.json{Colors.RESET}")
        return True
    
    except Exception as e:
        print(f"{Colors.RED}抓取失败: {str(e)}{Colors.RESET}")
        return False

def test_map():
    """测试网站地图功能"""
    try:
        print(f"{Colors.YELLOW}开始获取网站地图...{Colors.RESET}")
        # 抓取GitHub作为示例
        url = "https://github.com/mendableai"
        result = app.map_url(url)
        
        print(f"{Colors.GREEN}获取地图成功！{Colors.RESET}")
        print(f"{Colors.CYAN}找到 {len(result.get('links', []))} 个链接{Colors.RESET}")
        
        # 将结果保存到文件中
        with open("map_result.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        print(f"{Colors.GREEN}结果已保存到map_result.json{Colors.RESET}")
        return True
    
    except Exception as e:
        print(f"{Colors.RED}获取地图失败: {str(e)}{Colors.RESET}")
        return False

def test_extract():
    """测试结构化提取功能"""
    try:
        print(f"{Colors.YELLOW}开始测试结构化提取...{Colors.RESET}")
        # 抓取Github关于页面作为示例
        url = "https://github.com/about"
        
        # 定义要提取的模式
        extract_params = {
            "url": url,
            "prompt": "从页面中提取公司名称、描述和特点",
            "schema": {
                "company_name": "公司名称",
                "description": "公司描述",
                "features": ["主要特点"]
            }
        }
        
        result = app.extract_url(extract_params)
        
        print(f"{Colors.GREEN}提取成功！{Colors.RESET}")
        print(f"{Colors.CYAN}公司名称: {result.get('company_name', '未知')}{Colors.RESET}")
        
        # 将结果保存到文件中
        with open("extract_result.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        print(f"{Colors.GREEN}结果已保存到extract_result.json{Colors.RESET}")
        return True
    
    except Exception as e:
        print(f"{Colors.RED}提取失败: {str(e)}{Colors.RESET}")
        return False

def main():
    print(f"{Colors.BLUE}===== Firecrawl MCP 测试 ====={Colors.RESET}")
    
    # 创建保存结果的目录
    try:
        os.makedirs("results", exist_ok=True)
        print(f"{Colors.GREEN}已创建results目录用于保存测试结果{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}创建目录失败: {str(e)}{Colors.RESET}")
    
    # 测试各个功能
    print(f"{Colors.MAGENTA}正在测试网页抓取功能...{Colors.RESET}")
    scrape_success = test_scrape()
    
    print(f"{Colors.MAGENTA}正在测试网站地图功能...{Colors.RESET}")
    map_success = test_map()
    
    print(f"{Colors.MAGENTA}正在测试结构化提取功能...{Colors.RESET}")
    extract_success = test_extract()
    
    # 输出测试结果摘要
    print(f"\n{Colors.BLUE}===== 测试结果摘要 ====={Colors.RESET}")
    print(f"{Colors.CYAN}网页抓取: {'✅ 成功' if scrape_success else '❌ 失败'}{Colors.RESET}")
    print(f"{Colors.CYAN}网站地图: {'✅ 成功' if map_success else '❌ 失败'}{Colors.RESET}")
    print(f"{Colors.CYAN}结构化提取: {'✅ 成功' if extract_success else '❌ 失败'}{Colors.RESET}")

if __name__ == "__main__":
    main()