import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, Image as RLImage, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

def build_pinterest_style_cv():
    pdf_filename = "Merajul_Islam_CV.pdf"

    PAGE_WIDTH, PAGE_HEIGHT = A4
    SIDEBAR_WIDTH = 208
    MAIN_WIDTH = PAGE_WIDTH - SIDEBAR_WIDTH
    HEADER_HEIGHT = 135

    doc = BaseDocTemplate(
        pdf_filename,
        pagesize=A4,
        leftMargin=0,
        rightMargin=0,
        topMargin=0,
        bottomMargin=0
    )

    # Exact Palette from Pinterest Pin:
    c_dark_bg = colors.HexColor("#262626")      # Dark Charcoal #262626
    c_main_bg = colors.HexColor("#FFFFFF")      # Clean White #FFFFFF
    c_accent_orange = colors.HexColor("#E46C0A")# Warm Vibrant Amber Orange #E46C0A
    c_white = colors.HexColor("#FFFFFF")        # Pure White
    c_side_text = colors.HexColor("#E5E7EB")    # Off-white for sidebar
    c_side_muted = colors.HexColor("#9CA3AF")   # Muted slate for sidebar
    c_main_dark = colors.HexColor("#1F2937")    # Charcoal body text on white
    c_main_heading = colors.HexColor("#E46C0A") # Orange headings
    c_main_muted = colors.HexColor("#4B5563")   # Muted body text on white
    c_track_bg = colors.HexColor("#3F3F46")     # Dark progress track
    c_border_gray = colors.HexColor("#E5E7EB")  # Subtle divider on white

    # Background canvas callback
    def draw_exact_pin_background(canvas, doc):
        canvas.saveState()
        # 1. Full Left Sidebar (Dark #262626)
        canvas.setFillColor(c_dark_bg)
        canvas.rect(0, 0, SIDEBAR_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

        # 2. Top Header Right (Dark #262626)
        canvas.setFillColor(c_dark_bg)
        canvas.rect(SIDEBAR_WIDTH, PAGE_HEIGHT - HEADER_HEIGHT, MAIN_WIDTH, HEADER_HEIGHT, fill=1, stroke=0)

        # 3. Main Body Canvas (White #FFFFFF)
        canvas.setFillColor(c_main_bg)
        canvas.rect(SIDEBAR_WIDTH, 0, MAIN_WIDTH, PAGE_HEIGHT - HEADER_HEIGHT, fill=1, stroke=0)

        # 4. Orange Accent Strip under Top Header
        canvas.setFillColor(c_accent_orange)
        canvas.rect(SIDEBAR_WIDTH, PAGE_HEIGHT - HEADER_HEIGHT - 3.5, MAIN_WIDTH, 3.5, fill=1, stroke=0)

        canvas.restoreState()

    main_frame = Frame(0, 0, PAGE_WIDTH, PAGE_HEIGHT, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id='FullPage')
    template = PageTemplate(id='PinterestCV', frames=main_frame, onPage=draw_exact_pin_background)
    doc.addPageTemplates([template])

    styles = getSampleStyleSheet()

    # ==========================================
    # TYPOGRAPHY STYLES
    # ==========================================
    # Sidebar Styles (Dark Background)
    side_section_h = ParagraphStyle(
        'SideSecH',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=c_accent_orange,
        textTransform='uppercase',
        spaceBefore=7,
        spaceAfter=3
    )

    side_label = ParagraphStyle(
        'SideLbl',
        fontName='Helvetica-Bold',
        fontSize=6.8,
        leading=8.5,
        textColor=c_side_muted,
        textTransform='uppercase'
    )

    side_val = ParagraphStyle(
        'SideVal',
        fontName='Helvetica-Bold',
        fontSize=7.2,
        leading=9.5,
        textColor=c_white
    )

    side_skill_label = ParagraphStyle(
        'SideSkillLbl',
        fontName='Helvetica-Bold',
        fontSize=7.2,
        leading=9,
        textColor=c_side_text
    )

    # Main Header Styles (Dark Background)
    name_style = ParagraphStyle(
        'MainName',
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=26,
        textColor=c_white,
        spaceAfter=3
    )

    tagline_style = ParagraphStyle(
        'MainTagline',
        fontName='Helvetica-Bold',
        fontSize=9.2,
        leading=12,
        textColor=c_accent_orange,
        spaceAfter=6
    )

    header_summary_style = ParagraphStyle(
        'HeadSum',
        fontName='Helvetica',
        fontSize=7.5,
        leading=10.5,
        textColor=c_side_text
    )

    # Main Body Styles (White Background)
    main_section_h = ParagraphStyle(
        'MainSecH',
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12.5,
        textColor=c_main_heading,
        textTransform='uppercase',
        spaceBefore=6,
        spaceAfter=3
    )

    body_style = ParagraphStyle(
        'MainBody',
        fontName='Helvetica',
        fontSize=7.4,
        leading=10.5,
        textColor=c_main_dark,
        alignment=TA_JUSTIFY
    )

    item_title = ParagraphStyle(
        'ItemTitle',
        fontName='Helvetica-Bold',
        fontSize=8.0,
        leading=10.5,
        textColor=c_main_dark
    )

    item_sub = ParagraphStyle(
        'ItemSub',
        fontName='Helvetica-Bold',
        fontSize=7.4,
        leading=9.8,
        textColor=c_accent_orange
    )

    item_note = ParagraphStyle(
        'ItemNote',
        fontName='Helvetica',
        fontSize=6.8,
        leading=9.0,
        textColor=c_main_muted
    )

    bullet_style = ParagraphStyle(
        'MainBullet',
        fontName='Helvetica',
        fontSize=7.2,
        leading=9.8,
        textColor=c_main_dark,
        leftIndent=8
    )

    # Progress bar helper
    def make_progress_bar(percent_val, width=170, height=3.5):
        fill_w = (width * percent_val) / 100
        unfill_w = width - fill_w
        data = [['', '']]
        t = Table(data, colWidths=[fill_w, unfill_w], rowHeights=[height])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, 0), c_accent_orange),
            ('BACKGROUND', (1, 0), (1, 0), c_track_bg),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ]))
        return t

    # ==========================================
    # 1. BUILD SIDEBAR CONTENT (Left Column)
    # ==========================================
    side_elements = []

    # Circular Portrait Photo (with orange ring matching pin)
    avatar_path = "images/cv_avatar_orange_ring.png"
    if not os.path.exists(avatar_path):
        avatar_path = "images/cv_avatar_circular.png"
    
    if os.path.exists(avatar_path):
        avatar_img = RLImage(avatar_path, width=86, height=86)
        avatar_table = Table([[avatar_img]], colWidths=[176])
        avatar_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ]))
        side_elements.append(avatar_table)

    side_elements.append(Spacer(1, 4))

    # CONTACT INFO
    side_elements.append(Paragraph("CONTACT INFO", side_section_h))
    side_elements.append(HRFlowable(width="100%", thickness=1, color=c_accent_orange, spaceBefore=0, spaceAfter=4))

    contacts = [
        ("PHONE / WHATSAPP", '<a href="https://wa.me/8801339564967"><font color="#FFFFFF">+880 1339-564967</font></a>'),
        ("EMAIL", '<a href="mailto:mdmirazahmed3690@gmail.com"><font color="#FFFFFF">mdmirazahmed3690@gmail.com</font></a>'),
        ("CURRENT LOCATION", "Dhaka, Bangladesh"),
        ("PERMANENT ADDRESS", "Ashuganj, Brahmanbaria"),
        ("GITHUB PROFILE", '<a href="https://github.com/MdMiraz-dev"><font color="#E46C0A"><u>github.com/MdMiraz-dev</u></font></a>'),
        ("PORTFOLIO", '<a href="https://further-across-munich-hon.trycloudflare.com"><font color="#E46C0A"><u>Online Portfolio</u></font></a>')
    ]
    for lbl, val in contacts:
        side_elements.append(Paragraph(lbl, side_label))
        side_elements.append(Paragraph(val, side_val))
        side_elements.append(Spacer(1, 2))

    side_elements.append(Spacer(1, 2))

    # TECHNICAL SKILLS (Visual Orange Progress Bars)
    side_elements.append(Paragraph("TECHNICAL SKILLS", side_section_h))
    side_elements.append(HRFlowable(width="100%", thickness=1, color=c_accent_orange, spaceBefore=0, spaceAfter=4))

    skills = [
        ("Website Development (Main)", 95),
        ("Custom Software Development", 92),
        ("AI & Workflow Automation", 90),
        ("AI Video Creation", 88),
        ("Brand Logo & Graphic Design", 85)
    ]
    for s_name, s_pct in skills:
        side_elements.append(Paragraph(f"{s_name} &nbsp;<font color='#E46C0A'><b>{s_pct}%</b></font>", side_skill_label))
        side_elements.append(Spacer(1, 1.5))
        side_elements.append(make_progress_bar(s_pct, width=172, height=3.5))
        side_elements.append(Spacer(1, 3))

    side_elements.append(Spacer(1, 2))

    # LANGUAGES
    side_elements.append(Paragraph("LANGUAGES", side_section_h))
    side_elements.append(HRFlowable(width="100%", thickness=1, color=c_accent_orange, spaceBefore=0, spaceAfter=4))
    side_elements.append(Paragraph("<b>Bengali:</b> Native (মাতৃভাষা)", side_val))
    side_elements.append(Spacer(1, 1.5))
    side_elements.append(Paragraph("<b>Arabic:</b> Proficient (পড়া ও বোঝায় পারদর্শী)", side_val))
    side_elements.append(Spacer(1, 1.5))
    side_elements.append(Paragraph("<b>English:</b> Professional Working Knowledge", side_val))

    side_elements.append(Spacer(1, 3))

    # PERSONAL DETAILS & LICENSE
    side_elements.append(Paragraph("PERSONAL DETAILS", side_section_h))
    side_elements.append(HRFlowable(width="100%", thickness=1, color=c_accent_orange, spaceBefore=0, spaceAfter=4))
    side_elements.append(Paragraph("FATHER'S NAME", side_label))
    side_elements.append(Paragraph("Abdul Kadir (আব্দুল কাদির)", side_val))
    side_elements.append(Spacer(1, 2))
    side_elements.append(Paragraph("NATIONALITY & RELIGION", side_label))
    side_elements.append(Paragraph("Bangladeshi &nbsp;|&nbsp; Islam", side_val))
    side_elements.append(Spacer(1, 2))
    side_elements.append(Paragraph("DRIVING LICENSE", side_label))
    side_elements.append(Paragraph("<font color='#10B981'><b>Valid Government Driving License</b></font>", side_val))

    # ==========================================
    # 2. BUILD MAIN COLUMN CONTENT (Right Column)
    # ==========================================
    main_elements = []

    # Header Box (Dark background matching Pin)
    main_elements.append(Paragraph("MERAJUL <font color='#E46C0A'>ISLAM</font>", name_style))
    main_elements.append(Paragraph("WEB &amp; SOFTWARE DEVELOPER &nbsp;|&nbsp; AI AUTOMATION SPECIALIST", tagline_style))
    header_intro = (
        "Enthusiastic Web &amp; Software Developer specializing in building modern websites, custom software tools, "
        "and automated intelligent workflows to drive business productivity and digital excellence."
    )
    main_elements.append(Paragraph(header_intro, header_summary_style))
    main_elements.append(Spacer(1, 14)) # Spacing past the top header into the white canvas

    # CAREER OBJECTIVE
    main_elements.append(Paragraph("<font color='#E46C0A'>■</font> CAREER OBJECTIVE", main_section_h))
    main_elements.append(HRFlowable(width="100%", thickness=1, color=c_border_gray, spaceBefore=0, spaceAfter=3))
    obj_text = (
        "An energetic Web &amp; Software Developer and AI Automation Practitioner dedicated to creating high-speed, "
        "responsive websites, scalable software architectures, and automated business workflows. "
        "Focused on leveraging modern AI technologies and clean software engineering to optimize business efficiency and achieve organizational goals."
    )
    main_elements.append(Paragraph(obj_text, body_style))
    main_elements.append(Spacer(1, 4))

    # WORK EXPERIENCE & PROJECTS (Short & concise, as instructed)
    main_elements.append(Paragraph("<font color='#E46C0A'>■</font> WORK EXPERIENCE &amp; PROJECTS", main_section_h))
    main_elements.append(HRFlowable(width="100%", thickness=1, color=c_border_gray, spaceBefore=0, spaceAfter=3))

    exp_hdr = Table([
        [Paragraph("<b>Freelance Web, Software &amp; AI Developer</b>", item_title),
         Paragraph("<font color='#E46C0A'><b>2023 – Present</b></font>", ParagraphStyle('ExDt', fontName='Helvetica-Bold', fontSize=7.2, textColor=c_accent_orange, alignment=TA_RIGHT))]
    ], colWidths=[265, 95])
    exp_hdr.setStyle(TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    main_elements.append(exp_hdr)
    main_elements.append(Paragraph("Independent Business &amp; Client Projects", item_note))
    main_elements.append(Paragraph("• <b>Website Development (Main Focus):</b> Built and deployed modern, fast, responsive business websites.", bullet_style))
    main_elements.append(Paragraph("• <b>Custom Software Development:</b> Developed tailored software applications for business workflow management.", bullet_style))
    main_elements.append(Paragraph("• <b>AI Automation Workflows:</b> Configured end-to-end automation systems to reduce repetitive tasks and save costs.", bullet_style))
    main_elements.append(Paragraph("• <b>Digital Media &amp; Design:</b> Created promotional AI video content and custom brand logo designs.", bullet_style))
    main_elements.append(Spacer(1, 4))

    # TRAINING & COURSES
    main_elements.append(Paragraph("<font color='#E46C0A'>■</font> PROFESSIONAL TRAINING &amp; COURSES", main_section_h))
    main_elements.append(HRFlowable(width="100%", thickness=1, color=c_border_gray, spaceBefore=0, spaceAfter=3))
    
    tr_hdr = Table([
        [Paragraph("<b>AI Automation &amp; Software Development Course</b>", item_title),
         Paragraph("<font color='#10B981'><b>Certified Professional</b></font>", ParagraphStyle('TrDt', fontName='Helvetica-Bold', fontSize=7.2, textColor=colors.HexColor("#10B981"), alignment=TA_RIGHT))]
    ], colWidths=[265, 95])
    tr_hdr.setStyle(TableStyle([
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    main_elements.append(tr_hdr)
    main_elements.append(Paragraph("<b>As-Sunnah Skill Development Institute</b> (আস-সুন্নাহ স্কিল ডেভেলপমেন্ট ইনস্টিটিউট)", item_sub))
    main_elements.append(Paragraph("• Hands-on practical training on creating AI automation systems and software engineering techniques.", bullet_style))
    main_elements.append(Paragraph("• Applied practical artificial intelligence tools to optimize operational productivity in business tasks.", bullet_style))
    main_elements.append(Spacer(1, 4))

    # EDUCATIONAL BACKGROUND (NO graduation years, exactly as requested)
    main_elements.append(Paragraph("<font color='#E46C0A'>■</font> EDUCATIONAL BACKGROUND", main_section_h))
    main_elements.append(HRFlowable(width="100%", thickness=1, color=c_border_gray, spaceBefore=0, spaceAfter=3))

    edu_items = [
        ("Dawra-e-Hadith (Master's Degree Equivalent)", "Jamia Arabia Imdadul Uloom Faridabad Madrasah, Dhaka", "Also studied at Jamia Islamia Darul Uloom Madania, Jatrabari, Dhaka"),
        ("Alim (Higher Secondary Certificate / HSC Equivalent)", "Tonki Sadekul Uloom Fazil Madrasah, Akhaura, Brahmanbaria", "Madrasah Education Board, Bangladesh"),
        ("Dakhil (Secondary School Certificate / SSC Equivalent)", "Tonki Sadekul Uloom Fazil Madrasah, Akhaura, Brahmanbaria", "Madrasah Education Board, Bangladesh")
    ]

    for degree, inst, note in edu_items:
        main_elements.append(Paragraph(f"<b>{degree}</b>", item_title))
        main_elements.append(Paragraph(f"{inst}", item_sub))
        main_elements.append(Paragraph(f"<font color='#6B7280'>{note}</font>", item_note))
        main_elements.append(Spacer(1, 2))

    main_elements.append(Spacer(1, 3))

    # DECLARATION & SIGNATURE
    dec_text = "<i>I solemnly declare that all particulars stated in this curriculum vitae are authentic and true.</i>"
    sig_text = "<b>(Merajul Islam)</b><br/><font color='#6B7280' size='6.5'>Applicant's Signature</font>"

    dec_table = Table([
        [Paragraph(dec_text, ParagraphStyle('Dec', fontName='Helvetica', fontSize=6.8, leading=8.8, textColor=c_main_muted)),
         Paragraph(sig_text, ParagraphStyle('Sig', fontName='Helvetica', fontSize=7.4, leading=9.5, textColor=c_main_dark, alignment=TA_RIGHT))]
    ], colWidths=[265, 95])
    dec_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('LINEABOVE', (0, 0), (-1, -1), 0.5, c_border_gray),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
    ]))
    main_elements.append(dec_table)

    # ==========================================
    # 3. MASTER 2-COLUMN TABLE
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
    print(f"Generated Pinterest Replica CV: {pdf_filename} (Size: {os.path.getsize(pdf_filename)} bytes)")

if __name__ == '__main__':
    build_pinterest_style_cv()
