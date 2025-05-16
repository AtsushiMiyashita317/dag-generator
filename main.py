"""
uvicorn main:app --host 0.0.0.0 --port 8000
"""

from fastapi import FastAPI, Request
import graphviz
import base64

app = FastAPI()

@app.post("/")
async def generate_dag(request: Request):
    data = await request.json()
    nodes = data["nodes"]
    edges = data["edges"]

    # エッジに登場するノードラベル一覧
    connected_labels = set()
    for edge in edges:
        connected_labels.add(edge['source'])
        connected_labels.add(edge['target'])

    # 使うノードだけフィルタリング
    used_nodes = [node for node in nodes if node['label'] in connected_labels]

    # DAG描画
    dot = graphviz.Digraph(format='png')
    dot.attr(fontname='Noto Sans CJK JP')
    # dot.attr(dpi="300")  # 解像度下げる
    # dot.attr(size="30,30")  # サイズ制限（インチ）
    # dot.attr(ratio="compress")  # レイアウト圧縮
    # dot.attr('node', fontsize='8')  # フォントサイズ縮小
    # dot.attr('edge', fontsize='8')
    for node in nodes:
        if node in used_nodes:
            dot.node(node['label'], f"{node['label']}")
    for edge in edges:
        dot.edge(edge['source'], edge['target'], label="")
    output_path = dot.render('dag_output', view=False)

    # 画像Base64化
    with open(output_path, "rb") as f:
        img_data = base64.b64encode(f.read()).decode("utf-8")

    return {"image_base64": img_data}
