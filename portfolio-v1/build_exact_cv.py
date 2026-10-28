import os
from PIL import Image, ImageDraw, ImageFont

def generate_exact_cv():
    template_path = r'C:\Users\mdtus\.gemini\antigravity\brain\f89021bc-d7cb-4aeb-8c8d-17364251a84f\.user_uploaded\media_1792920286718_bd8d0b28.png'
    base_img = Image.open(template_path).convert('RGB')
    
    # 3x scale for high-definition 300 DPI
    SCALE = 3
    W, H = base_img.size[0] * SCALE, base_img.size[1] * SCALE
    img = base_img.resize((W, H), Image.Resampling.LANCZOS if hasattr(Image, 'Resampling') else Image.LANCZOS)
    draw = ImageDraw.Draw(img)
    
    # Palette
    DARK_BG = (38, 38, 38)     # #262626
    WHITE = (255, 255, 255)    # #ffffff
    ORANGE = (216, 111, 31)    # #d86f1f
    TEXT_DARK = (40, 40, 40)   # #282828
    TEXT_MUTED = (95, 95, 95)  # #5f5f5f
    
    def sc(val):
        return int(round(val * SCALE))
    
    # Fonts
    font_bold = lambda size: ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', sc(size))
    font_reg = lambda size: ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', sc(size))
    font_light = lambda size: ImageFont.truetype('C:/Windows/Fonts/segoeuil.ttf', sc(size))
    
    # -------------------------------------------------------------
    # 1. CLEAN ALL TEXT REGIONS & ARTIFACTS
    # -------------------------------------------------------------
    # Top left header area (including top artifacts above Merajul)
    draw.rectangle([sc(0), sc(0), sc(300), sc(265)], fill=DARK_BG)
    
    # Profile section area
    draw.rectangle([sc(0), sc(265), sc(214), sc(462)], fill=DARK_BG)
    
    # Skills section area
    draw.rectangle([sc(0), sc(463), sc(214), sc(625)], fill=DARK_BG)
    
    # Contact section area (extending all the way to bottom)
    draw.rectangle([sc(0), sc(626), sc(214), sc(842)], fill=DARK_BG)
    
    # Education section text (White canvas)
    draw.rectangle([sc(250), sc(315), sc(580), sc(525)], fill=WHITE)
    
    # Experience section text (White canvas)
    draw.rectangle([sc(250), sc(540), sc(580), sc(795)], fill=WHITE)
    
    # Footer text
    draw.rectangle([sc(260), sc(800), sc(560), sc(835)], fill=WHITE)
    
    # -------------------------------------------------------------
    # 2. COMPOSITE MERAJUL ISLAM'S SUIT PHOTO
    # -------------------------------------------------------------
    photo_path = 'images/merajul_formal_photo.png'
    photo = Image.open(photo_path).convert('RGBA')
    
    cx, cy = sc(429), sc(172)
    radius = sc(83)
    diameter = radius * 2
    
    photo_resized = photo.resize((diameter, diameter), Image.Resampling.LANCZOS)
    
    # Antialiased circular mask
    mask = Image.new('L', (diameter * 2, diameter * 2), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse([0, 0, diameter * 2 - 1, diameter * 2 - 1], fill=255)
    mask = mask.resize((diameter, diameter), Image.Resampling.LANCZOS)
    
    img.paste(photo_resized, (cx - radius, cy - radius), mask)
    
    # Thick clean circular white ring
    ring_thick = sc(4.5)
    for t in range(ring_thick):
        draw.ellipse([cx - radius - t, cy - radius - t, cx + radius + t, cy + radius + t], outline=WHITE)

    # -------------------------------------------------------------
    # 3. DRAW SHARP PILL BADGES (PROFILE, SKILLS, CONTACT)
    # -------------------------------------------------------------
    def draw_badge(y_start, y_end, x_end, label):
        # White pill with rounded right edge, flush left at x=0
        r = (y_end - y_start) // 2
        draw.rounded_rectangle([0, y_start, x_end, y_end], radius=r, fill=WHITE)
        draw.rectangle([0, y_start, r, y_end], fill=WHITE)
        f_badge = font_bold(12.2)
        bbox = draw.textbbox((0, 0), label, font=f_badge)
        lw = bbox[2] - bbox[0]
        lh = bbox[3] - bbox[1]
        lx = (x_end - lw) // 2
        ly = y_start + (y_end - y_start - lh) // 2 - sc(1)
        draw.text((lx, ly), label, font=f_badge, fill=DARK_BG)

    draw_badge(sc(272), sc(296), sc(125), "Profile")
    draw_badge(sc(468), sc(492), sc(130), "Skills")
    draw_badge(sc(632), sc(656), sc(125), "Contact")

    # -------------------------------------------------------------
    # 4. HEADER: MERAJUL ISLAM & TITLE
    # -------------------------------------------------------------
    header_x = sc(68)
    
    f_first = font_reg(37)
    f_last = font_bold(42)
    
    draw.text((header_x, sc(88)), "Merajul", font=f_first, fill=ORANGE)
    draw.text((header_x, sc(134)), "Islam", font=f_last, fill=WHITE)
    
    # Orange underline
    bar_y = sc(202)
    bar_w = sc(76)
    bar_h = sc(3.2)
    draw.rectangle([header_x, bar_y, header_x + bar_w, bar_y + bar_h], fill=ORANGE)
    
    # Title
    f_subtitle = font_reg(13)
    draw.text((header_x, sc(222)), "Web & Software Developer", font=f_subtitle, fill=WHITE)

    # -------------------------------------------------------------
    # 5. PROFILE SECTION (LEFT COLUMN)
    # -------------------------------------------------------------
    bio_lines = [
        "Enthusiastic Web & Software",
        "Developer and AI Automation",
        "Practitioner. Committed to",
        "delivering high-performance",
        "web platforms, automated",
        "workflows, and impactful digital",
        "solutions that scale."
    ]
    f_bio = font_reg(9.2)
    y_bio = sc(316)
    for line in bio_lines:
        draw.text((sc(26), y_bio), line, font=f_bio, fill=(225, 225, 225))
        y_bio += sc(16)

    # -------------------------------------------------------------
    # 6. SKILLS SECTION (LEFT COLUMN)
    # -------------------------------------------------------------
    skills = [
        ("Web Development", 0.94),
        ("Custom Software", 0.88),
        ("AI Automation", 0.95),
        ("Digital Media & UI", 0.84)
    ]
    
    f_skill = font_reg(9.0)
    y_skill = sc(510)
    bar_x = sc(106)
    bar_w_total = sc(82)
    bar_height = sc(6.5)
    
    for name, pct in skills:
        draw.text((sc(24), y_skill - sc(2)), name, font=f_skill, fill=WHITE)
        by = y_skill + sc(4)
        draw.rectangle([bar_x, by, bar_x + bar_w_total, by + bar_height], fill=(240, 240, 240))
        fill_w = int(bar_w_total * pct)
        draw.rectangle([bar_x, by, bar_x + fill_w, by + bar_height], fill=ORANGE)
        y_skill += sc(28)

    # -------------------------------------------------------------
    # 7. CONTACT SECTION (LEFT COLUMN)
    # -------------------------------------------------------------
    contact_items = [
        ("Address", ["Ashuganj, Brahmanbaria", "(Current: Dhaka, Bangladesh)"]),
        ("Phone / WhatsApp", ["+880 1339-564967"]),
        ("Email", ["mdmirazahmed3690@gmail.com"]),
        ("GitHub", ["github.com/MdMiraz-dev"])
    ]
    
    f_c_label = font_bold(9.2)
    f_c_val = font_reg(8.4)
    y_c = sc(670)
    
    for label, vals in contact_items:
        draw.text((sc(25), y_c), label, font=f_c_label, fill=ORANGE)
        y_c += sc(13)
        for v in vals:
            draw.text((sc(25), y_c), v, font=f_c_val, fill=WHITE)
            y_c += sc(12)
        y_c += sc(5)

    # -------------------------------------------------------------
    # 8. EDUCATION SECTION (RIGHT COLUMN, WHITE CANVAS)
    # -------------------------------------------------------------
    edu_x = sc(268)
    f_inst = font_bold(9.4)
    f_degree = font_bold(11.0)
    f_sub = font_reg(8.8)
    
    edu_list = [
        ("JAMIA ARABIA IMDADUL ULOOM FARIDABAD", "Dawra-e-Hadith (Master's Equivalent)", "Islamic Studies & Research • Dhaka"),
        ("JAMIA ISLAMIA DARUL ULOOM MADANIA", "Alim (Higher Secondary Equivalent)", "General & Arabic Curriculum • Jatrabari, Dhaka"),
        ("AS-SUNNAH SKILL DEVELOPMENT INSTITUTE", "AI Automation & Software Development", "Specialized Professional Training Course")
    ]
    
    y_edu = sc(338)
    for inst, degree, sub in edu_list:
        draw.text((edu_x, y_edu), inst, font=f_inst, fill=ORANGE)
        y_edu += sc(16)
        draw.text((edu_x, y_edu), degree, font=f_degree, fill=TEXT_DARK)
        y_edu += sc(16)
        draw.text((edu_x, y_edu), sub, font=f_sub, fill=TEXT_MUTED)
        y_edu += sc(32)

    # -------------------------------------------------------------
    # 9. EXPERIENCE SECTION (RIGHT COLUMN, WHITE CANVAS)
    # -------------------------------------------------------------
    exp_x = sc(268)
    f_exp_title = font_bold(10.2)
    f_exp_body = font_reg(8.8)
    
    exp_list = [
        (
            "FREELANCE & PROJECT-BASED DEVELOPER",
            [
                "Custom web and software solutions tailored to business needs.",
                "Business process AI automation and smart workflow deployment.",
                "Brand identity, modern responsive web design, and digital media."
            ]
        ),
        (
            "AS-SUNNAH SKILL DEVELOPMENT PROJECTS",
            [
                "Implemented AI-driven workflow automations reducing manual task time.",
                "Created responsive full-stack web applications and custom utilities."
            ]
        )
    ]
    
    y_exp = sc(562)
    for title, bullets in exp_list:
        draw.text((exp_x, y_exp), title, font=f_exp_title, fill=ORANGE)
        y_exp += sc(18)
        for b in bullets:
            draw.text((exp_x, y_exp), f"•  {b}", font=f_exp_body, fill=TEXT_DARK)
            y_exp += sc(16)
        y_exp += sc(24)

    # -------------------------------------------------------------
    # 10. FOOTER
    # -------------------------------------------------------------
    footer_text = "G I T H U B . C O M / M D M I R A Z - D E V"
    f_footer = font_bold(9.0)
    bbox = draw.textbbox((0, 0), footer_text, font=f_footer)
    fw = bbox[2] - bbox[0]
    fx = sc(240) + (sc(595 - 240) - fw) // 2
    fy = sc(808)
    draw.text((fx, fy), footer_text, font=f_footer, fill=(110, 110, 110))

    # -------------------------------------------------------------
    # 11. SAVE
    # -------------------------------------------------------------
    preview_path = 'images/cv_preview.png'
    img.save(preview_path, format='PNG', quality=95)
    print(f"Saved {preview_path} successfully ({W}x{H})")
    
    artifact_img = r'C:\Users\mdtus\.gemini\antigravity\brain\f89021bc-d7cb-4aeb-8c8d-17364251a84f\cv_preview.png'
    img.save(artifact_img, format='PNG', quality=95)
    
    pdf_path = 'Merajul_Islam_CV.pdf'
    img_rgb = img.convert('RGB')
    img_rgb.save(pdf_path, "PDF", resolution=300.0)
    print(f"Saved {pdf_path} successfully!")

if __name__ == '__main__':
    generate_exact_cv()
