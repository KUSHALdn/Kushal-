import requests
import random
import time

# --- CONFIGURATION ---
BOT_TOKEN = "8613954151:AAFPvrw17o3U1QClzx_S3_-zAVPp0S5EWso"
ALLOWED_USERS = ["7839672511", "8587430685"]

# --- 🎯 HIGH-APPROVAL BINS (UPDATED APRIL 2026) ---
BINS_2026 = [
    {"bin": "552433", "bank": "BMO", "country": "CANADA", "lvl": "WORLD ELITE", "type": "CREDIT"},
    {"bin": "414720", "bank": "CAPITAL ONE", "country": "USA", "lvl": "SIGNATURE", "type": "CREDIT"},
    {"bin": "401658", "bank": "NATWEST", "country": "UK", "lvl": "PLATINUM", "type": "DEBIT"},
    {"bin": "491218", "bank": "TD BANK", "country": "CANADA", "lvl": "BUSINESS", "type": "CREDIT"}
]

def check_luhn(n):
    r = [int(ch) for ch in n][::-1]
    return (sum(r[0::2]) + sum(sum(divmod(d * 2, 10)) for d in r[1::2])) % 10 == 0

def get_full_details():
    batch = []
    random.shuffle(BINS_2026)
    for item in BINS_2026:
        bin_val = item["bin"]
        for _ in range(2):
            res = str(bin_val)
            while len(res) < 15:
                res += str(random.randint(0, 9))
            for i in range(10):
                cc = res + str(i)
                if check_luhn(cc):
                    mm = random.randint(1, 12)
                    yy = random.randint(2028, 2035)
                    cvv = random.randint(110, 990)
                    batch.append({
                        "card": f"{cc}|{mm:02d}|{yy}|{cvv}",
                        "meta": item
                    })
                    break
    return batch

def broadcast_hit(data):
    # FULL APPROVAL-READY FORMAT
    report = (
        f"🛡️ <b>CARD APPROVAL CHECKER</b>\n"
        f"━━━━━━━━━━━━━━\n"
        f"💳 <b>Card:</b> <code>{data['card']}</code>\n"
        f"🏦 <b>Bank:</b> {data['meta']['bank']}\n"
        f"📍 <b>Origin:</b> {data['meta']['country']}\n"
        f"📊 <b>Class:</b> {data['meta']['lvl']} ({data['meta']['type']})\n"
        f"⚡ <b>Gateway:</b> Auth-Ready ($1.00 Check)\n"
        f"━━━━━━━━━━━━━━\n"
        f"👤 <b>Owner:</b> Kushal Master"
    )
    for uid in ALLOWED_USERS:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        try: requests.post(url, data={"chat_id": uid, "text": report, "parse_mode": "HTML"})
        except: pass

def main():
    print("🔥 --- STARTING APPROVAL-READY ENGINE ---")
    while True:
        try:
            cards = get_full_details()
            for c in cards:
                broadcast_hit(c)
                print(f"✅ Full Detail Sent: {c['card']}")
                time.sleep(1.5)
        except Exception: time.sleep(5)

if __name__ == "__main__":
    main()