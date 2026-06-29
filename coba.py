data = {
    "math"  : 99,
    "fiscal": 87,
    "bio"   : 99,
    "english" : 99
}
tertinggi = max(data.values())


for a,b in data.items():
    if b >= tertinggi:
        print(f"{a} {b}")

