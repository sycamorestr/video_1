'''
前端页面设计
    1，导入相关库
    2，标题
    3，侧边栏，apikey输入框+获取超链接
    4，主题内容
        4.1，输入框，输入视频主题
        4.2，输入框，输入视频时长
        4.3，滑动条，视频温度
        4.4，按钮，生成视频
-----------------------------------------
'''
import streamlit as st
from project1_video_script import generate_script

st.title("视频脚本生成器")
with st.sidebar:
    api_key = st.text_input("请输入您的Tongyi API Key")
    st.markdown("[获取通义APIkey](https://www.aliyun.com/product/qwen)")
subject = st.text_input("请输入您的视频主题")
duration = st.number_input("请输入您的视频时长",min_value=1,max_value=10,value=5)
temperature = st.slider("请输入您的视频温度",min_value=0.1,max_value=1.0,value=0.5,step=0.1)
submit = st.button("生成脚本")
if submit and not api_key:
    st.warning("请输入您的Tongyi API Key")
    st.stop()
if submit and not subject:
    st.warning("请输入您的视频主题")
    st.stop()
if submit and not duration:
    st.warning("请输入您的视频时长")
    st.stop()
if submit and not temperature:
    st.warning("请输入您的视频温度")
    st.stop()
if submit:
    with st.spinner("正在生成脚本..."):
        title, script = generate_script(subject,duration,temperature,api_key)
    st.success("脚本生成成功")
    
    # 显示结果
    st.subheader(f"视频标题：{title}")
    st.subheader("视频脚本：")
    st.text(script.replace('\\n', '\n'))

