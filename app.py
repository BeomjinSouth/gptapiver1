import os
import openai
import gradio as gr

# API 키를 환경 변수에서 안전하게 가져오기
openai.api_key="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"

from collections import defaultdict

def ask_gpt(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        if not response.choices:
            return "No response received."
        response_message = response.choices[0].message.content
        print(response_message )
        return response_message

    except Exception as e:
        print(f"Error: {str(e)}")
        return str(e)

iface = gr.Interface(
    fn=ask_gpt,
    inputs=gr.Textbox(lines=2, placeholder="여기에 질문을 입력하세요..."),
    outputs="text",
    title="GPT-4 챗봇",
    description="OpenAI의 GPT-3.5 Turbo 모델을 활용한 챗봇입니다. 질문을 입력하고 '제출'을 누르세요."
)

iface.launch(server_port=7890)
