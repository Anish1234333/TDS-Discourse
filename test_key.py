"""
Quick standalone test — checks ONLY whether your OPENAI_API_KEY / OPENAI_BASE_URL
are valid. Does not touch index.py, embeddings, or the frontend.

Run:
    python test_key.py
"""
import os
import openai

api_key  = os.environ.get("OPENAI_API_KEY")
base_url = os.environ.get("OPENAI_BASE_URL")

print(f"Using base_url: {base_url}")
print(f"Key present: {bool(api_key)} (first 10 chars: {api_key[:10] if api_key else 'NONE'}...)")
print("-" * 50)

if not api_key:
    print("❌ OPENAI_API_KEY is not set in this session. Set it with:")
    print('   $env:OPENAI_API_KEY = "your-token-here"')
    raise SystemExit(1)

client = openai.OpenAI(api_key=api_key, base_url=base_url)

# 1) Try a tiny embedding call (same call your app makes)
try:
    r = client.embeddings.create(model="text-embedding-3-small", input="hello world")
    print(f"✅ Embedding call succeeded. Vector length: {len(r.data[0].embedding)}")
except Exception as e:
    print(f"❌ Embedding call failed: {e}")

# 2) Try a tiny chat completion call (same model your app uses for answers)
try:
    r = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say OK if you can read this."}]
    )
    print(f"✅ Chat completion succeeded: {r.choices[0].message.content.strip()}")
except Exception as e:
    print(f"❌ Chat completion failed: {e}")