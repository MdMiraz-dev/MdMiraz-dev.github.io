import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, Image as RLImage, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

def generate_photoshop_cv():
    pdf_filename = "Merajul_Islam_CV.pdf"

    # Exact A4 dimensions: 595.28 x 841.89 points
    PAGE_WIDTH, PAGE_HEIGHT = A4
    SIDEBAR_WIDTH = 202
    MAIN_WIDTH = PAGE_WIDTH - SIDEBAR_WIDTH

    doc = BaseDocTemplate(pdf_filename, pagesize=A4, leftMargin=0, rightMargin=0, topMargin=0, bottomMargin=0)

    # Canvas background painter: full-bleed two-tone layout
    def draw_photoshop_background(canvas, doc):
        canvas.saveState()
        # 1. Left Sidebar Background (Deep Dark Obsidian)
        canvas.setFillColor(colors.HexColor("#080B12"))
        canvas.rect(0, 0, SIDEBAR_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

        # 2. Right Canvas Background (Dark Executive Titanium)
        canvas.setFillColor(colors.HexColor("#0E131F"))
        canvas.rect(SIDEBAR_WIDTH, 0, MAIN_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

        # 3. Subtle Elegant Vertical Divider Line
        canvas.setStrokeColor(colors.HexColor("#1E293B"))
        canvas.setLineWidth(1)
        canvas.line(SIDEBAR_WIDTH, 0, SIDEBAR_WIDTH, PAGE_HEIGHT)

        # 4. Top Crimson Accent Strip on Left Sidebar
        canvas.setFillColor(colors.HexColor("#FF2A3B"))
        canvas.rect(0, PAGE_HEIGHT - 4, SIDEBAR_WIDTH, 4, fill=1, stroke=0)

        canvas.restoreState()

    # Full page frame with padding inside table
    main_frame = Frame(0, 0, PAGE_WIDTH, PAGE_HEIGHT, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='FullFrame')
    template = PageTemplate(id='DesignerPage', frames=main_frame, onPage=draw_photoshop_background)
    doc.addPageTemplates([template])

    styles = getSampleStyleSheet()

    # Premium Palette
    c_accent_red = colors.HexColor("#FF2A3B")    # Signature Vivid Crimson Red
    c_white = colors.HexColor("#FFFFFF")         # Pure White
    c_text_bright = colors.HexColor("#F8FAFC")   # Crisp High-Contrast White
    c_text_muted = colors.HexColor("#CBD5E1")    # Slate 300
    c_text_dim = colors.HexColor("#94A3B8")      # Slate 400
    c_card_bg = colors.HexColor("#141A29")       # Elevated Dark Card Fill
    c_border_subtle = colors.HexColor("#263248") # Elevated Card Border
    c_green = colors.HexColor("#10B981")         # Emerald Green for badges

    # ==========================================
    # TYPOGRAPHY STYLES
    # ==========================================
    # Left Sidebar Styles
    side_section_h = ParagraphStyle(
        'SideSecH',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=c_accent_red,
        textTransform='uppercase',
        spaceBefore=7,
        spaceAfter=4
    )

    side_label = ParagraphStyle(
        'SideLbl',
        fontName='Helvetica-Bold',
        fontSize=7.2,
        leading=9.5,
        textColor=c_text_dim,
        textTransform='uppercase'
    )

    side_val = ParagraphStyle(
        'SideVal',
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=10,
        textColor=c_text_bright
    )

    side_skill_label = ParagraphStyle(
        'SideSkillLbl',
        fontName='Helvetica-Bold',
        fontSize=7.4,
        leading=9.5,
        textColor=c_text_bright
    )

    # Right Main Styles
    name_style = ParagraphStyle(
        'MainName',
        fontName='Helvetica-Bold',
        fontSize=23,
        leading=25,
        textColor=c_white,
        spaceAfter=3
    )

    tagline_style = ParagraphStyle(
        'MainTagline',
        fontName='Helvetica-Bold',
        fontSize=8.8,
        leading=11.5,
        textColor=c_accent_red,
        spaceAfter=7
    )

    main_section_h = ParagraphStyle(
        'MainSecH',
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12.5,
        textColor=c_white,
        textTransform='uppercase',
        spaceBefore=6,
        spaceAfter=3
    )

    body_style = ParagraphStyle(
        'MainBody',
        fontName='Helvetica',
        fontSize=7.6,
        leading=11,
        textColor=c_text_bright,
        alignment=TA_JUSTIFY
    )

    item_title = ParagraphStyle(
        'ItemTitle',
        fontName='Helvetica-Bold',
        fontSize=8.2,
        leading=10.5,
        textColor=c_white
    )

    item_sub = ParagraphStyle(
        'ItemSub',
        fontName='Helvetica-Bold',
        fontSize=7.4,
        leading=10,
        textColor=c_accent_red
    )

    item_note = ParagraphStyle(
        'ItemNote',
        fontName='Helvetica',
        fontSize=7.0,
        leading=9.5,
        textColor=c_text_dim
    )

    bullet_style = ParagraphStyle(
        'MainBullet',
        fontName='Helvetica',
        fontSize=7.3,
        leading=10.2,
        textColor=c_text_bright,
        leftIndent=8
    )

    # Progress bar helper
    def make_progress_bar(percent_val, width=164, height=3.5):
        fill_w = (width * percent_val) / 100
        unfill_w = width - fill_w
        data = [['', '']]
        t = Table(data, colWidths=[fill_w, unfill_w], rowHeights=[height])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, 0), c_accent_red),
            ('BACKGROUND', (1, 0), (1, 0), colors.HexColor("#222C3E")),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ]))
        return t

    # ==========================================
    # 1. BUILD SIDEBAR CONTENT
    # ==========================================
    side_elements = []

    # Circular Avatar
    avatar_path = "images/cv_avatar_circular.png"
    if os.path.exists(avatar_path):
        avatar_img = RLImage(avatar_path, width=82, height=82)
        avatar_table = Table([[avatar_img]], colWidths=[172])
        avatar_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ]))
        side_elements.append(avatar_table)

    # Status Pill Badge
    badge_html = "<font color='#10B981'>●</font> <b>AVAILABLE FOR HIRE</b>"
    badge_p = Paragraph(badge_html, ParagraphStyle('Bdg', fontName='Helvetica-Bold', fontSize=6.8, leading=8.5, textColor=c_green, alignment=TA_CENTER))
    side_elements.append(badge_p)
    side_elements.append(Spacer(1, 4))

    # Contact Info
    side_elements.append(Paragraph("CONTACT INFO", side_section_h))
    side_elements.append(HRFlowable(width="100%", thickness=1, color=c_accent_red, spaceBefore=0, spaceAfter=4))

    contacts = [
        ("PHONE / WHATSAPP", '<a href="https://wa.me/8801339564967"><font color="#F8FAFC">+880 1339-564967</font></a>'),
        ("EMAIL", '<a href="mailto:mdmirazahmed3690@gmail.com"><font color="#F8FAFC">mdmirazahmed3690@gmail.com</font></a>'),
        ("LOCATION", "Dhaka, Bangladesh"),
        ("PERMANENT", "Ashuganj, Brahmanbaria"),
        ("GITHUB PROFILE", '<a href="https://github.com/MdMiraz-dev"><font color="#FF2A3B"><u>github.com/MdMiraz-dev</u></font></a>'),
        ("PORTFOLIO", '<a href="https://further-across-munich-hon.trycloudflare.com"><font color="#FF2A3B"><u>View Live Portfolio</u></font></a>')
    ]
    for lbl, val in contacts:
        side_elements.append(Paragraph(lbl, side_label))
        side_elements.append(Paragraph(val, side_val))
        side_elements.append(Spacer(1, 2))

    side_elements.append(Spacer(1, 2))

    # Core Technical Skills
    side_elements.append(Paragraph("TECHNICAL SKILLS", side_section_h))
    side_elements.append(HRFlowable(width="100%", thickness=1, color=c_accent_red, spaceBefore=0, spaceAfter=4))

    skills_data = [
        ("Website Development (Main)", 95),
        ("Custom Software Engineering", 92),
        ("AI & Workflow Automation", 90),
        ("AI Video Creation", 88),
        ("Brand Logo & Graphic Design", 85),
        ("Full-Stack Architecture", 90)
    ]
    for s_name, s_pct in skills_data:
        side_elements.append(Paragraph(f"{s_name} &nbsp;<font color='#FF2A3B'><b>{s_pct}%</b></font>", side_skill_label))
        side_elements.append(Spacer(1, 1.5))
        side_elements.append(make_progress_bar(s_pct, width=168, height=3.2))
        side_elements.append(Spacer(1, 3))

    side_elements.append(Spacer(1, 2))

    # Languages
    side_elements.append(Paragraph("LANGUAGES", side_section_h))
    side_elements.append(HRFlowable(width="100%", thickness=1, color=c_accent_red, spaceBefore=0, spaceAfter=4))
    side_elements.append(Paragraph("<b>Bengali:</b> Native (মাতৃভাষা)", side_val))
    side_elements.append(Spacer(1, 1.5))
    side_elements.append(Paragraph("<b>Arabic:</b> Proficient (পড়া ও বোঝায় পারদর্শী)", side_val))
    side_elements.append(Spacer(1, 1.5))
    side_elements.append(Paragraph("<b>English:</b> Professional Working Knowledge", side_val))

    side_elements.append(Spacer(1, 3))

    # Personal Profile & License
    side_elements.append(Paragraph("PERSONAL DETAILS", side_section_h))
    side_elements.append(HRFlowable(width="100%", thickness=1, color=c_accent_red, spaceBefore=0, spaceAfter=4))
    side_elements.append(Paragraph("FATHER'S NAME", side_label))
    side_elements.append(Paragraph("Abdul Kadir (আব্দুল কাদির)", side_val))
    side_elements.append(Spacer(1, 2))
    side_elements.append(Paragraph("NATIONALITY & RELIGION", side_label))
    side_elements.append(Paragraph("Bangladeshi &nbsp;|&nbsp; Islam", side_val))
    side_elements.append(Spacer(1, 2))
    side_elements.append(Paragraph("DRIVING LICENSE", side_label))
    side_elements.append(Paragraph("<font color='#10B981'><b>Valid Government Driving License</b></font>", side_val))
    side_elements.append(Spacer(1, 2))
    side_elements.append(Paragraph("CORE STRENGTH", side_label))
    side_elements.append(Paragraph("Fast Adaptive Technology Learner", side_val))

    # ==========================================
    # 2. BUILD MAIN COLUMN CONTENT
    # ==========================================
    main_elements = []

    # Name & Headline
    main_elements.append(Paragraph("MERAJUL <font color='#FF2A3B'>ISLAM</font>", name_style))
    main_elements.append(Paragraph("WEB &amp; SOFTWARE DEVELOPER &nbsp;|&nbsp; AI AUTOMATION SPECIALIST", tagline_style))
    main_elements.append(HRFlowable(width="100%", thickness=1.5, color=c_accent_red, spaceBefore=0, spaceAfter=5))

    # Career Objective Card
    main_elements.append(Paragraph("<font color='#FF2A3B'>■</font> CAREER OBJECTIVE", main_section_h))
    obj_box_p = Paragraph(
        "A dedicated, results-oriented <b>Web &amp; Software Developer</b> and <b>AI Automation Practitioner</b>. "
        "Focused primarily on engineering high-speed, modern websites, custom software tools, and intelligent workflow automation systems. "
        "Committed to deploying artificial intelligence and clean software architecture to streamline business operations, boost organizational productivity, and deliver high-impact digital experiences.",
        body_style
    )
    obj_table = Table([[obj_box_p]], colWidths=[365])
    obj_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), c_card_bg),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('BOX', (0, 0), (-1, -1), 1, c_border_subtle),
        ('LINELEFT', (0, 0), (-1, -1), 3, c_accent_red),
    ]))
    main_elements.append(obj_table)
    main_elements.append(Spacer(1, 4))

    # Work Experience
    main_elements.append(Paragraph("<font color='#FF2A3B'>■</font> WORK EXPERIENCE &amp; PROJECTS", main_section_h))
    exp_header = Table([
        [Paragraph("<b>Freelance Web, Software &amp; AI Developer</b>", item_title),
         Paragraph("<font color='#FF2A3B'><b>2023 – Present</b></font>", ParagraphStyle('ExDate', fontName='Helvetica-Bold', fontSize=7.2, textColor=c_accent_red, alignment=TA_RIGHT))]
    ], colWidths=[265, 100])
    exp_header.setStyle(TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    main_elements.append(exp_header)
    main_elements.append(Paragraph("Independent Client &amp; Business Digital Projects", item_note))
    main_elements.append(Paragraph("• <b>Website Development (Main Focus):</b> Built and deployed lightning-fast, fully responsive business websites tailored to client requirements.", bullet_style))
    main_elements.append(Paragraph("• <b>Custom Software Systems:</b> Developed custom software solutions and management applications built for efficiency.", bullet_style))
    main_elements.append(Paragraph("• <b>Business AI Automations:</b> Implemented automated smart workflows to eliminate repetitive manual work and reduce overhead costs.", bullet_style))
    main_elements.append(Paragraph("• <b>Creative Visual Media:</b> Produced promotional AI-generated video content, brand logo designs, and marketing visual assets.", bullet_style))
    main_elements.append(Spacer(1, 4))

    # Professional Training & Courses
    main_elements.append(Paragraph("<font color='#FF2A3B'>■</font> PROFESSIONAL TRAINING &amp; CERTIFICATION", main_section_h))
    training_header = Table([
        [Paragraph("<b>AI Automation &amp; Software Development Course</b>", item_title),
         Paragraph("<font color='#10B981'><b>Certified Professional</b></font>", ParagraphStyle('TrDate', fontName='Helvetica-Bold', fontSize=7.2, textColor=c_green, alignment=TA_RIGHT))]
    ], colWidths=[265, 100])
    training_header.setStyle(TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    main_elements.append(training_header)
    main_elements.append(Paragraph("<b>As-Sunnah Skill Development Institute</b> (আস-সুন্নাহ স্কিল ডেভেলপমেন্ট ইনস্টিটিউট)", item_sub))
    main_elements.append(Paragraph("• Intensive hands-on training on architecting AI automation workflows, AI application frameworks, and practical software engineering techniques.", bullet_style))
    main_elements.append(Paragraph("• Practical implementation of artificial intelligence tools to optimize operational productivity in real-world business scenarios.", bullet_style))
    main_elements.append(Spacer(1, 4))

    # Educational Background
    main_elements.append(Paragraph("<font color='#FF2A3B'>■</font> EDUCATIONAL BACKGROUND", main_section_h))

    edu_items = [
        ("Dawra-e-Hadith (Master's Degree Equivalent)", "Jamia Arabia Imdadul Uloom Faridabad Madrasah, Dhaka", "Also studied at Jamia Islamia Darul Uloom Madania, Jatrabari, Dhaka"),
        ("Alim (Higher Secondary Certificate / HSC Equivalent)", "Tonki Sadekul Uloom Fazil Madrasah, Akhaura, Brahmanbaria", "Madrasah Education Board, Bangladesh"),
        ("Dakhil (Secondary School Certificate / SSC Equivalent)", "Tonki Sadekul Uloom Fazil Madrasah, Akhaura, Brahmanbaria", "Madrasah Education Board, Bangladesh")
    ]

    for degree, inst, note in edu_items:
        main_elements.append(Paragraph(f"<b>{degree}</b>", item_title))
        main_elements.append(Paragraph(f"{inst}", item_sub))
        main_elements.append(Paragraph(f"<font color='#94A3B8'>{note}</font>", item_note))
        main_elements.append(Spacer(1, 2))

    main_elements.append(Spacer(1, 2))

    # Declaration & Signature Block
    dec_text = "<i>I solemnly declare that all information presented in this curriculum vitae is authentic, accurate, and complete.</i>"
    sig_text = "<b>(Merajul Islam)</b><br/><font color='#94A3B8' size='6.5'>Applicant's Signature</font>"

    dec_table = Table([
        [Paragraph(dec_text, ParagraphStyle('Dec', fontName='Helvetica', fontSize=6.8, leading=8.8, textColor=c_text_dim)),
         Paragraph(sig_text, ParagraphStyle('Sig', fontName='Helvetica', fontSize=7.4, leading=9.5, textColor=c_white, alignment=TA_RIGHT))]
    ], colWidths=[265, 100])
    dec_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('LINEABOVE', (0, 0), (-1, -1), 0.5, c_border_subtle),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
    ]))
    main_elements.append(dec_table)

    # ==========================================
    # 3. COMBINE INTO 2-COLUMN TABLE
    # ==========================================
    master_table = Table(
        [[side_elements, main_elements]],
        colWidths=[SIDEBAR_WIDTH, MAIN_WIDTH]
    )

    master_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        # Sidebar padding
        ('LEFTPADDING', (0, 0), (0, 0), 16),
        ('RIGHTPADDING', (0, 0), (0, 0), 16),
        ('TOPPADDING', (0, 0), (0, 0), 20),
        ('BOTTOMPADDING', (0, 0), (0, 0), 16),
        # Main body padding
        ('LEFTPADDING', (1, 0), (1, 0), 18),
        ('RIGHTPADDING', (1, 0), (1, 0), 18),
        ('TOPPADDING', (1, 0), (1, 0), 20),
        ('BOTTOMPADDING', (1, 0), (1, 0), 16),
    ]))

    doc.build([master_table])
    print(f"Generated {pdf_filename} successfully! Size: {os.path.getsize(pdf_filename)} bytes")

if __name__ == '__main__':
    generate_photoshop_cv()
