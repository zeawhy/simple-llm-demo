#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的大模型聊天机器人Demo
支持DeepSeek和OpenAI API
"""

import os
import sys
import requests
from dotenv import load_dotenv
from openai import OpenAI

# 加载环境变量
load_dotenv()

def init_client():
    """
    根据环境变量初始化AI客户端
    """
    model_provider = os.getenv('MODEL_PROVIDER', 'deepseek').lower()
    
    if model_provider == 'deepseek':
        api_key = os.getenv('DEEPSEEK_API_KEY')
        if not api_key:
            print("❌ 错误：未找到DEEPSEEK_API_KEY环境变量")
            print("请在.env文件中设置DEEPSEEK_API_KEY")
            return None, None
        return 'deepseek', api_key
    
    elif model_provider == 'openai':
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            print("❌ 错误：未找到OPENAI_API_KEY环境变量")
            print("请在.env文件中设置OPENAI_API_KEY")
            return None, None
        
        client = OpenAI(api_key=api_key)
        return 'openai', client
    
    else:
        print(f"❌ 错误：不支持的模型提供商 '{model_provider}'")
        print("支持的提供商：deepseek, openai")
        return None, None

def chat_with_deepseek(api_key, message):
    """
    使用DeepSeek API进行对话
    """
    url = "https://api.deepseek.com/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": message}
        ],
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data, headers=headers, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        return result['choices'][0]['message']['content']
    
    except requests.exceptions.RequestException as e:
        return f"❌ DeepSeek API请求失败: {str(e)}"
    except KeyError as e:
        return f"❌ DeepSeek API响应格式错误: {str(e)}"
    except Exception as e:
        return f"❌ 未知错误: {str(e)}"

def chat_with_openai(client, message):
    """
    使用OpenAI API进行对话
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"❌ OpenAI API请求失败: {str(e)}"

def chat_with_ai(provider, client_or_key, message):
    """
    统一的AI对话接口
    """
    if provider == 'deepseek':
        return chat_with_deepseek(client_or_key, message)
    elif provider == 'openai':
        return chat_with_openai(client_or_key, message)
    else:
        return "❌ 不支持的AI提供商"

def main():
    print("🤖 简单的大模型聊天机器人Demo")
    print("支持DeepSeek和OpenAI模型")
    print("输入 'quit' 或 'exit' 退出程序\n")
    
    # 初始化客户端
    provider, client_or_key = init_client()
    if not provider:
        return
    
    if provider == 'deepseek':
        print("✅ DeepSeek客户端初始化成功!")
    else:
        print("✅ OpenAI客户端初始化成功!")
    
    print()
    
    # 开始对话循环
    while True:
        try:
            # 获取用户输入
            user_input = input("👤 你: ").strip()
            
            # 检查退出命令
            if user_input.lower() in ['quit', 'exit', '退出', 'q']:
                print("👋 再见!")
                break
            
            # 检查空输入
            if not user_input:
                print("请输入一些内容...")
                continue
            
            # 显示AI思考状态
            if provider == 'deepseek':
                print("🤖 DeepSeek AI正在思考...")
            else:
                print("🤖 OpenAI正在思考...")
            
            # 获取AI回复
            response = chat_with_ai(provider, client_or_key, user_input)
            
            # 显示AI回复
            print(f"🤖 AI: {response}\n")
            
        except KeyboardInterrupt:
            print("\n👋 程序被用户中断，再见!")
            break
        except Exception as e:
            print(f"❌ 发生错误: {str(e)}")
            print("请重试...\n")

if __name__ == "__main__":
    main()
