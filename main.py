import os
from google import genai

# 1. 验证环境变量是否生效，如果打印出 None，说明你前面 Edit Configurations 没配成功
print("检查 API KEY 是否存在:", "存在" if os.environ.get("GEMINI_API_KEY") else "不存在 (None)")

try:
    # 2. 初始化客户端
    client = genai.Client()

    print("正在请求 Gemini API，请稍候...")

    # 3. 调用最新的 Gemini 3.5 Flash 模型
    response = client.models.generate_content(
        model='gemini-3.5-flash',
        contents='用 Python 写一个预测双色球中奖号码的脚本',
    )

    # 4. 打印返回结果
    print("\n--- Gemini 回复内容 ---")
    print(response.text)

except Exception as e:
    print(f"\n❌ 请求发生异常: {e}")
