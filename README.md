# AlpacaHack Daily: LiteAlpaca Writeup

## 課題の概要
- **名称**: LiteAlpaca
- **トピック**: Supply Chain
- **難易度**: Easy
- **URL**: [https://alpacahack.com/daily/challenges/litealpaca](https://alpacahack.com/daily/challenges/litealpaca?month=2026-04)

「`litealpaca` モジュールに何かおかしなものが紛れ込んだ。何が起きたか分かるか？」という問題です。

## 技術解説
この問題は、Pythonパッケージの配布形式（Wheel）における **Supply Chain Attack (サプライチェーン攻撃)** をテーマにしています。

攻撃の鍵となるのは **`.pth` ファイル** です。

### 1. `.pth` ファイルとは？
Pythonの `site-packages` ディレクトリ（ライブラリがインストールされる場所）に配置される `.pth` ファイル（Path Configuration Files）は、本来ライブラリのパスを追加するために使われます。

しかし、このファイルには **`import` 文から始まるコードを記述すると、Pythonインタープリタの起動時にそのコードが実行される** という副作用があります。これを利用して、ライブラリをインストールしただけで悪意のあるコードを実行させることが可能です。

### 2. 調査と特定
提供されたファイルを展開すると、以下のパスに不審なファイルが見つかりました。

`litealpaca/chall/extracted-wheel/litealpaca-1.0.0-py3-none-any.whl/litealpaca_init.pth`

中身を確認すると、以下のような単一行のコードが含まれていました。

```python
import os, subprocess, sys; subprocess.Popen([sys.executable, "-c", "import base64; exec(base64.b64decode('aW1wb3J0IG9zOyBvcy5zeXN0ZW0oImVjaG8gJ0FscGFjYXtQeVBJX3A0Y2s0ZzNzX2M0bl9iM19kNG5nM3IwdXN9JyA+IC90bXAvZmxhZy50eHQiKQ=='))"])
```

### 3. ペイロードの解析
Base64でエンコードされている部分をデコードすると、以下のようになります。

```python
import os; os.system("echo 'Alpaca{PyPI_p4ck4g3s_c4n_b3_d4ng3r0us}' > /tmp/flag.txt")
```

このコードは、OSのシステムコマンドを呼び出し、フラグを `/tmp/flag.txt` というファイルに書き出しています。

## 結論
悪意のあるパッケージを不用意にインストールしたり、信頼できないソースからライブラリを読み込んだりすると、インポートすらしていない状態で任意のコードが実行される危険性があります。

今回のケースでは、`.pth` ファイルの特性を利用したコード実行がフラグ取得の鍵でした。

---
Solved with Google Antigravity
