'''
视频脚本生成器
技术栈：
    前端：streamlit
    后端：python
    模型：qwen
页面功能：
    1，填写api密钥
        提供超链接转至api密钥获取地址
    2，输入视频相关信息：
        输入视频主题
        输入视频大致时长
        输入温度，滑动条调节
        一键生成视频脚本
    3，模型接入wiki百科，获取实时搜索功能
技术点：
    1，streamlit前端页面设计
    2，使用加载组件显示生成状态
'''
from langchain_community.chat_models import ChatTongyi
import os
from langchain.prompts import ChatPromptTemplate
#from langchain_community.utilities import WikipediaAPIWrapper

def generate_script(subject,duration,temperature,api_key):
    #wiki百科
   # search = WikipediaAPIWrapper(lang="zh")
  #  research = search.run(subject)
    
    #模型
    model = ChatTongyi(model = "qwen-plus",api_key=api_key)
    
    #标题生成器
    title_prompt_template_text = [("human","请为'{subject}'这个主题的视频想一个吸引人的标题,结构化输出，不要有多余的符号")]
    title_prompt_template = ChatPromptTemplate.from_messages(title_prompt_template_text)
    title_prompt = title_prompt_template.invoke({"subject":subject})
    response = model.invoke(title_prompt)
    #标题解析
    title = response.content
    
    
    #脚本生成器
    script_prompt_template_text = [("human","""你是一位短视频频道的博主。根据以下标题和相关信息，为短视频频道写一个视频脚本。
             视频标题：{subject}，视频时长：{duration}分钟，生成的脚本的长度尽量遵循视频时长的要求。
             要求开头抓住限球，中间提供干货内容，结尾有惊喜，脚本格式也请按照【开头、中间，结尾】分隔。
             整体内容的表达方式要尽量轻松有趣，吸引年轻人结构化输出，不要有多余的符号。
             """)]
    script_prompt_template = ChatPromptTemplate.from_messages(script_prompt_template_text)
    script_prompt = script_prompt_template.invoke({"subject":subject,"duration":duration,"temperature":temperature})
    response = model.invoke(script_prompt)
    #脚本解析
    script = response.content

    return title,script

# response =  generate_script("2023年中国经济形势",10,0.5)

# print(response)
