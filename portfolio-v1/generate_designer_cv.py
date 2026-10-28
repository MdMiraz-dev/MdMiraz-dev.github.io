import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

def build_designer_cv():
    pdf_filename = "Merajul_Islam_CV.pdf"
    
    # Exact A4 dimensions: 595.28 x 841.89 points
    # Zero margins for full-bleed background layout
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=A4,
        leftMargin=0,
        rightMargin=0,
        topMargin=0,
        bottomMargin=0
    )

    styles = getSampleStyleSheet()

    # Premium Photoshop Color Palette
    c_sidebar_bg = colors.HexColor("#080A0F")    # Deep Obsidian Black
    c_main_bg = colors.HexColor("#0F1420")       # Dark Titanium Slate
    c_accent_red = colors.HexColor("#FF2A3B")    # Signature Neon Crimson Red
    c_white = colors.HexColor("#FFFFFF")         # Pure White
    c_text_bright = colors.HexColor("#F1F5F9")   # 95% White
    c_text_muted = colors.HexColor("#94A3B8")    # Soft Slate
    c_text_dim = colors.HexColor("#64748B")      # Dim Slate
    c_card_bg = colors.HexColor("#161D2E")       # Elevated Card Fill
    c_border_subtle = colors.HexColor("#1E293B") # Card Border
    c_red_border = colors.HexColor("#7F1D1D")    # Dark red border

    # ==========================================
    # TYPOGRAPHY STYLES
    # ==========================================
    # Sidebar Styles
    side_heading = ParagraphStyle(
        'SideHeading',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=c_accent_red,
        textTransform='uppercase',
        spaceBefore=8,
        spaceAfter=4
    )

    side_label = ParagraphStyle(
        'SideLabel',
        fontName='Helvetica-Bold',
        fontSize=7.2,
        leading=9.5,
        textColor=c_white
    )

    side_val = ParagraphStyle(
        'SideVal',
        fontName='Helvetica',
        fontSize=6.8,
        leading=9,
        textColor=c_text_muted
    )

    side_skill_name = ParagraphStyle(
        'SideSkillName',
        fontName='Helvetica-Bold',
        fontSize=7.0,
        leading=9,
        textColor=c_text_bright
    )

    # Main Column Styles
    name_style = ParagraphStyle(
        'MainName',
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=22,
        textColor=c_white,
        spaceAfter=2
    )

    tagline_style = ParagraphStyle(
        'MainTagline',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=c_accent_red,
        spaceAfter=6
    )

    main_heading = ParagraphStyle(
        'MainHeading',
        fontName='Helvetica-Bold',
        fontSize=9.2,
        leading=12,
        textColor=c_white,
        textTransform='uppercase',
        spaceBefore=5,
        spaceAfter=3
    )

    body_style = ParagraphStyle(
        'MainBody',
        fontName='Helvetica',
        fontSize=7.2,
        leading=10.2,
        textColor=c_text_bright,
        alignment=TA_JUSTIFY
    )

    item_title = ParagraphStyle(
        'ItemTitle',
        fontName='Helvetica-Bold',
        fontSize=7.6,
        leading=10,
        textColor=c_white
    )

    item_sub = ParagraphStyle(
        'ItemSub',
        fontName='Helvetica-Bold',
        fontSize=7.0,
        leading=9.5,
        textColor=c_accent_red
    )

    item_desc = ParagraphStyle(
        'ItemDesc',
        fontName='Helvetica',
        fontSize=6.8,
        leading=9.2,
        textColor=c_text_muted
    )

    bullet_style = ParagraphStyle(
        'MainBullet',
        fontName='Helvetica',
        fontSize=6.8,
        leading=9.2,
        textColor=c_text_bright,
        leftIndent=8
    )

    # ==========================================
    # HELPER: PROGRESS BAR FLOWABLE
    # ==========================================
    def make_progress_bar(percent_val, width=155, height=3.5):
        fill_w = (width * percent_val) / 100
        unfill_w = width - fill_w
        data = [['', '']]
        t = Table(data, colWidths=[fill_w, unfill_w], rowHeights=[height])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, 0), c_accent_red),
            ('BACKGROUND', (1, 0), (1, 0), colors.HexColor("#1E2536")),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ]))
        return t

    # ==========================================
    # 1. SIDEBAR ELEMENTS (Left Column - 195 pt)
    # ==========================================
    side_elements = []

    # Avatar Image
    avatar_path = "images/cv_avatar_circular.png"
    if os.path.exists(avatar_path):
        avatar_img = RLImage(avatar_path, width=76, height=76)
        avatar_table = Table([[avatar_img]], colWidths=[175])
        avatar_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ]))
        side_elements.append(avatar_table)

    # Candidate Mini Badge
    badge_p = Paragraph("<font color='#FF2A3B'>●</font> AVAILABLE FOR HIRE", ParagraphStyle('Bdg', fontName='Helvetica-Bold', fontSize=6.5, leading=8, textColor=colors.HexColor("#10B981"), alignment=TA_CENTER))
    side_elements.append(badge_p)
    side_elements.append(Spacer(1, 4))

    # Contact Details
    side_elements.append(Paragraph("CONTACT INFO", side_heading))
    side_elements.append(HRFlowable(width="100%", thickness=1, color=c_accent_red, spaceBefore=0, spaceAfter=4))
    
    contacts = [
        ("PHONE / WHATSAPP", "+880 1339-564967"),
        ("EMAIL", "mdmirazahmed3690@gmail.com"),
        ("LOCATION", "Dhaka, Bangladesh"),
        ("PERMANENT", "Ashuganj, Brahmanbaria"),
        ("GITHUB", "github.com/MdMiraz-dev"),
        ("PORTFOLIO", "Live & Accessible Online")
    ]
    for lbl, val in contacts:
        side_elements.append(Paragraph(lbl, side_label))
        side_elements.append(Paragraph(val, side_val))
        side_elements.append(Spacer(1, 1.5))

    side_elements.append(Spacer(1, 3))

    # Core Skills & Visual Progress Bars
    side_elements.append(Paragraph("TECHNICAL PROFICIENCY", side_heading))
    side_elements.append(HRFlowable(width="100%", thickness=1, color=c_accent_red, spaceBefore=0, spaceAfter=4))

    skills_data = [
        ("Website Development (Main)", 95),
        ("Custom Software Engineering", 90),
        ("AI & Workflow Automation", 90),
        ("AI Video Creation", 85),
        ("Brand Logo & Graphic Design", 82),
        ("Full-Stack Web Tech", 88)
    ]
    for s_name, s_pct in skills_data:
        side_elements.append(Paragraph(f"<b>{s_name}</b> <font color='#FF2A3B'><b>{s_pct}%</b></font>", side_skill_name))
        side_elements.append(Spacer(1, 1))
        side_elements.append(make_progress_bar(s_pct, width=165, height=3.2))
        side_elements.append(Spacer(1, 3))

    side_elements.append(Spacer(1, 2))

    # Languages
    side_elements.append(Paragraph("LANGUAGES", side_heading))
    side_elements.append(HRFlowable(width="100%", thickness=1, color=c_accent_red, spaceBefore=0, spaceAfter=4))
    side_elements.append(Paragraph("<b>Bengali:</b> Native (মাতৃভাষা)", side_val))
    side_elements.append(Paragraph("<b>Arabic:</b> Proficient Reading & Comprehension", side_val))
    side_elements.append(Paragraph("<b>English:</b> Professional Working Knowledge", side_val))

    side_elements.append(Spacer(1, 3))

    # Personal Profile & License
    side_elements.append(Paragraph("PERSONAL PROFILE", side_heading))
    side_elements.append(HRFlowable(width="100%", thickness=1, color=c_accent_red, spaceBefore=0, spaceAfter=4))
    side_elements.append(Paragraph("<b>Father's Name:</b> Abdul Kadir (আব্দুল কাদির)", side_val))
    side_elements.append(Paragraph("<b>Nationality:</b> Bangladeshi", side_val))
    side_elements.append(Paragraph("<b>Religion:</b> Islam", side_val))
    side_elements.append(Paragraph("<b>Driving License:</b> <font color='#10B981'><b>Valid License Holder</b></font>", side_val))
    side_elements.append(Paragraph("<b>Learning Speed:</b> Fast Adaptive Learner", side_val))

    # ==========================================
    # 2. MAIN COLUMN ELEMENTS (Right Column - 400 pt)
    # ==========================================
    main_elements = []

    # Name & Headline Banner
    main_elements.append(Paragraph("MERAJUL <font color='#FF2A3B'>ISLAM</font>", name_style))
    main_elements.append(Paragraph("WEB &amp; SOFTWARE DEVELOPER &nbsp;|&nbsp; AI AUTOMATION SPECIALIST", tagline_style))
    main_elements.append(HRFlowable(width="100%", thickness=1.5, color=c_accent_red, spaceBefore=0, spaceAfter=5))

    # Executive Objective
    main_elements.append(Paragraph("<font color='#FF2A3B'>■</font> CAREER OBJECTIVE", main_heading))
    obj_box_p = Paragraph(
        "Dedicated and innovative <b>Web &amp; Software Developer</b> and <b>AI Automation Practitioner</b>. "
        "Passionate about building fast, modern websites, custom software architectures, and automated intelligent workflows. "
        "Committed to deploying artificial intelligence and clean software solutions to maximize business productivity, eliminate operational friction, and deliver measurable results.",
        body_style
    )
    obj_table = Table([[obj_box_p]], colWidths=[372])
    obj_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), c_card_bg),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('BOX', (0, 0), (-1, -1), 0.75, c_border_subtle),
        ('LINELEFT', (0, 0), (-1, -1), 2.5, c_accent_red),
    ]))
    main_elements.append(obj_table)
    main_elements.append(Spacer(1, 4))

    # Work Experience
    main_elements.append(Paragraph("<font color='#FF2A3B'>■</font> WORK EXPERIENCE &amp; PROJECTS", main_heading))
    
    exp_header = Table([
        [Paragraph("<b>Freelance Web, Software &amp; AI Developer</b>", item_title), Paragraph("<font color='#FF2A3B'><b>2023 – Present</b></font>", ParagraphStyle('ExDate', fontName='Helvetica-Bold', fontSize=7, textColor=c_accent_red, alignment=TA_RIGHT))]
    ], colWidths=[270, 102])
    exp_header.setStyle(TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    main_elements.append(exp_header)
    main_elements.append(Paragraph("Custom Client Projects &amp; Digital Solutions", item_desc))
    main_elements.append(Paragraph("• <b>Website Architecture:</b> Engineered modern, high-speed, and responsive business websites.", bullet_style))
    main_elements.append(Paragraph("• <b>Custom Software Development:</b> Built functional management tools &amp; scalable web applications.", bullet_style))
    main_elements.append(Paragraph("• <b>AI Automation Systems:</b> Designed smart workflows automating tasks, saving business time &amp; costs.", bullet_style))
    main_elements.append(Paragraph("• <b>Digital Content:</b> Created high-impact AI promotional video reels and brand identity logo designs.", bullet_style))
    main_elements.append(Spacer(1, 4))

    # Professional Training & Courses
    main_elements.append(Paragraph("<font color='#FF2A3B'>■</font> PROFESSIONAL TRAINING &amp; COURSES", main_heading))
    training_header = Table([
        [Paragraph("<b>AI Automation &amp; Software Development Course</b>", item_title), Paragraph("<font color='#10B981'><b>Certified</b></font>", ParagraphStyle('TrDate', fontName='Helvetica-Bold', fontSize=7, textColor=colors.HexColor("#10B981"), alignment=TA_RIGHT))]
    ], colWidths=[290, 82])
    training_header.setStyle(TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    main_elements.append(training_header)
    main_elements.append(Paragraph("<b>As-Sunnah Skill Development Institute</b> (আস-সুন্নাহ স্কিল ডেভেলপমেন্ট ইনস্টিটিউট)", item_sub))
    main_elements.append(Paragraph("• Hands-on expertise in creating AI automation workflows and practical software implementation.", bullet_style))
    main_elements.append(Paragraph("• Applying modern AI technologies to streamline operational productivity and real-world business tasks.", bullet_style))
    main_elements.append(Spacer(1, 4))

    # Educational Background
    main_elements.append(Paragraph("<font color='#FF2A3B'>■</font> EDUCATIONAL BACKGROUND", main_heading))

    edu_list = [
        ("Dawra-e-Hadith (Master's Degree Equivalent)", "Jamia Arabia Imdadul Uloom Faridabad Madrasah, Dhaka", "Also studied at Jamia Islamia Darul Uloom Madania, Jatrabari, Dhaka"),
        ("Alim (Higher Secondary Certificate / HSC Equivalent)", "Tonki Sadekul Uloom Fazil Madrasah, Akhaura, Brahmanbaria", "Madrasah Education Board, Bangladesh"),
        ("Dakhil (Secondary School Certificate / SSC Equivalent)", "Tonki Sadekul Uloom Fazil Madrasah, Akhaura, Brahmanbaria", "Madrasah Education Board, Bangladesh")
    ]

    for degree, inst, note in edu_list:
        main_elements.append(Paragraph(f"<b>{degree}</b>", item_title))
        main_elements.append(Paragraph(f"{inst}", item_desc))
        main_elements.append(Paragraph(f"<font color='#64748B'>{note}</font>", item_desc))
        main_elements.append(Spacer(1, 2))

    main_elements.append(Spacer(1, 2))

    # Declaration & Signature Block
    dec_text = "<i>I solemnly declare that all particulars stated in this curriculum vitae are authentic and complete to the best of my knowledge.</i>"
    sig_text = "<b>(Merajul Islam)</b><br/><font color='#64748B' size='6.5'>Applicant's Signature</font>"

    dec_table = Table([
        [Paragraph(dec_text, ParagraphStyle('Dec', fontName='Helvetica', fontSize=6.5, leading=8.5, textColor=c_text_dim)),
         Paragraph(sig_text, ParagraphStyle('Sig', fontName='Helvetica', fontSize=7.2, leading=9.5, textColor=c_white, alignment=TA_RIGHT))]
    ], colWidths=[270, 102])
    dec_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('LINEABOVE', (0, 0), (-1, -1), 0.5, c_border_subtle),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
    ]))
    main_elements.append(dec_table)

    # ==========================================
    # 3. COMBINE INTO 2-COLUMN FULL-BLEED TABLE
    # ==========================================
    # Total width: 195 + 400.28 = 595.28 pt (Exact A4 width)
    # Height: 841.89 pt (Exact A4 height)
    master_table = Table(
        [[side_elements, main_elements]],
        colWidths=[195, 400.28],
        rowHeights=[841.89]
    )

    master_table.setStyle(TableStyle([
        # Backgrounds
        ('BACKGROUND', (0, 0), (0, 0), c_sidebar_bg),
        ('BACKGROUND', (1, 0), (1, 0), c_main_bg),
        # Vertical alignment
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        # Padding
        ('LEFTPADDING', (0, 0), (0, 0), 15),
        ('RIGHTPADDING', (0, 0), (0, 0), 15),
        ('TOPPADDING', (0, 0), (0, 0), 18),
        ('BOTTOMPADDING', (0, 0), (0, 0), 15),

        ('LEFTPADDING', (1, 0), (1, 0), 18),
        ('RIGHTPADDING', (1, 0), (1, 0), 18),
        ('TOPPADDING', (1, 0), (1, 0), 18),
        ('BOTTOMPADDING', (1, 0), (1, 0), 15),

        # Divider between sidebar and main
        ('LINEAFTER', (0, 0), (0, 0), 1, c_border_subtle),
    ]))

    doc.build([master_table])
    print(f"Generated {pdf_filename} successfully! Size: {os.path.getsize(pdf_filename)} bytes")

if __name__ == '__main__':
    build_designer_cv()
