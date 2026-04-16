import base64

# .pth ファイルに含まれていたBase64文字列
encoded_payload = "aW1wb3J0IG9zOyBvcy5zeXN0ZW0oImVjaG8gJ0FscGFjYXtQeVBJX3A0Y2s0ZzNzX2M0bl9iM19kNG5nM3IwdXN9JyA+IC90bXAvZmxhZy50eHQiKQ=="

# デコード
decoded_payload = base64.b64decode(encoded_payload).decode()

print("Decoded Payload:")
print(decoded_payload)

# フラグを抽出して表示
if "Alpaca{" in decoded_payload:
    flag = decoded_payload.split("'")[1]
    print(f"\nFlag found: {flag}")
