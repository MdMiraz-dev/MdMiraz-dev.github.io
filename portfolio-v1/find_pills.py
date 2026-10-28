from PIL import Image

src = r'C:\Users\mdtus\.gemini\antigravity\brain\f89021bc-d7cb-4aeb-8c8d-17364251a84f\.user_uploaded\media_1792920286718_bd8d0b28.png'
im = Image.open(src).convert('RGB')

# Let's inspect:
# 1. Name area:
# "Jenna" in orange: Y=?
# "Melinda" in white: Y=?
# line: Y=?
# "Business Analyst": Y=?

for y in range(60, 200, 5):
    # check orange pixels in row
    orange_cnt = sum(1 for x in range(30, 200) if im.getpixel((x, y))[0] > 180 and im.getpixel((x, y))[2] < 50)
    white_cnt = sum(1 for x in range(30, 200) if im.getpixel((x, y))[0] > 200 and im.getpixel((x, y))[1] > 200 and im.getpixel((x, y))[2] > 200)
    if orange_cnt > 5 or white_cnt > 5:
        print(f"Name area Y={y}: orange={orange_cnt}, white={white_cnt}")

# 2. Section pill boxes on the left:
# "Profile" pill: Y=?
# "Skills" pill: Y=?
# "Contact" pill: Y=?
print("\nFinding White Pill Boxes on left (X=0 to 150):")
for y in range(250, 800, 5):
    pill_white = sum(1 for x in range(0, 150) if im.getpixel((x, y))[0] > 240 and im.getpixel((x, y))[1] > 240 and im.getpixel((x, y))[2] > 240)
    if pill_white > 40:
        print(f"Pill Box at Y={y}: white={pill_white}")
