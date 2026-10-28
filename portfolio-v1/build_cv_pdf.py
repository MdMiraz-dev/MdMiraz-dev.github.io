import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

def generate_pdf():
    pdf_filename = "Merajul_Islam_CV.pdf"
    
    # 12mm margins
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=A4,
        leftMargin=14 * mm,
        rightMargin=14 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm
    )

    styles = getSampleStyleSheet()

    # Custom Palette
    c_primary = colors.HexColor("#0F172A")    # Deep slate
    c_accent = colors.HexColor("#E11D48")     # Crimson red accent
    c_subtext = colors.HexColor("#475569")    # Slate text
    c_body = colors.HexColor("#1E293B")       # Dark charcoal
    c_bg_light = colors.HexColor("#F8FAFC")   # Light slate
    c_border = colors.HexColor("#CBD5E1")     # Subtle border

    # Styles
    title_style = ParagraphStyle(
        'CVTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=c_primary,
        spaceAfter=2
    )

    subtitle_style = ParagraphStyle(
        'CVSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=c_accent,
        spaceAfter=6
    )

    contact_style = ParagraphStyle(
        'CVContact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=c_subtext
    )

    section_heading_style = ParagraphStyle(
        'CVSectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=c_primary,
        spaceBefore=7,
        spaceAfter=4,
        textTransform='uppercase'
    )

    body_style = ParagraphStyle(
        'CVBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.8,
        leading=13,
        textColor=c_body,
        alignment=TA_JUSTIFY
    )

    bold_body_style = ParagraphStyle(
        'CVBoldBody',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=13,
        textColor=c_primary
    )

    bullet_style = ParagraphStyle(
        'CVBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.6,
        leading=12.5,
        textColor=c_body,
        leftIndent=10
    )

    elements = []

    # ==========================================
    # 1. HEADER (Photo on right, Info on left)
    # ==========================================
    photo_path = os.path.join("images", "merajul_formal_photo.png")
    photo_img = None
    if os.path.exists(photo_path):
        # 26mm x 32mm photo
        photo_img = RLImage(photo_path, width=28 * mm, height=34 * mm)

    contact_info_html = """
    <b>Phone / WhatsApp:</b> +880 1339-564967 &nbsp;|&nbsp; <b>Email:</b> mdmirazahmed3690@gmail.com<br/>
    <b>Location:</b> Dhaka, Bangladesh (Permanent: Ashuganj, Brahmanbaria)<br/>
    <b>GitHub:</b> github.com/MdMiraz-dev &nbsp;|&nbsp; <b>Portfolio:</b> Available Online
    """

    header_text_cells = [
        Paragraph("MERAJUL <font color='#E11D48'>ISLAM</font>", title_style),
        Paragraph("Web &amp; Software Developer &nbsp;|&nbsp; AI Automation Specialist", subtitle_style),
        Paragraph(contact_info_html, contact_style)
    ]

    header_data = [
        [header_text_cells, photo_img if photo_img else ""]
    ]

    header_table = Table(header_data, colWidths=[146 * mm, 36 * mm])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    elements.append(header_table)
    elements.append(Spacer(1, 4 * mm))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=c_accent, spaceBefore=0, spaceAfter=5))

    # ==========================================
    # 2. CAREER OBJECTIVE
    # ==========================================
    elements.append(Paragraph("<font color='#E11D48'>■</font> CAREER OBJECTIVE", section_heading_style))
    obj_text = (
        "An enthusiastic Web &amp; Software Developer and AI Automation Practitioner seeking to build a progressive "
        "career by leveraging practical expertise in Artificial Intelligence (AI), automated workflows, and custom "
        "software engineering. Committed to driving organizational productivity, modernizing digital processes, and "
        "delivering high-quality, impactful digital solutions."
    )
    elements.append(Paragraph(obj_text, body_style))
    elements.append(Spacer(1, 3.5 * mm))

    # ==========================================
    # 3. CORE COMPETENCIES & TECHNICAL SKILLS
    # ==========================================
    elements.append(Paragraph("<font color='#E11D48'>■</font> CORE COMPETENCIES &amp; SKILLS", section_heading_style))

    skill_col1 = [
        Paragraph("<b>💻 Web &amp; Software Development:</b>", bold_body_style),
        Paragraph("• <b>Modern Websites (Main Focus):</b> Fast, responsive &amp; business-centric websites.", bullet_style),
        Paragraph("• <b>Custom Software:</b> Tailor-made management tools and desktop solutions.", bullet_style),
        Paragraph("• Clean full-stack code architecture, API integrations, and maintenance.", bullet_style),
        Spacer(1, 2 * mm),
        Paragraph("<b>🎨 Digital Content &amp; Graphic Design:</b>", bold_body_style),
        Paragraph("• <b>AI Video Creation:</b> Promotional reels &amp; visual storytelling using AI.", bullet_style),
        Paragraph("• <b>Brand Logo &amp; Graphics:</b> Logo design and social media visual assets.", bullet_style),
    ]

    skill_col2 = [
        Paragraph("<b>🤖 AI &amp; Workflow Automation:</b>", bold_body_style),
        Paragraph("• <b>Business Process Automation:</b> End-to-end automated smart workflows.", bullet_style),
        Paragraph("• <b>AI Tools Implementation:</b> Amplifying operational speed and productivity.", bullet_style),
        Paragraph("• Automated data processing, task routing, and system integrations.", bullet_style),
        Spacer(1, 2 * mm),
        Paragraph("<b>⚡ Professional Attributes:</b>", bold_body_style),
        Paragraph("• <b>Driving License:</b> Valid Government Driving License Holder.", bullet_style),
        Paragraph("• <b>Rapid Learner:</b> Quick adoption of new technologies and AI frameworks.", bullet_style),
    ]

    skills_table = Table([[skill_col1, skill_col2]], colWidths=[91 * mm, 91 * mm])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    elements.append(skills_table)
    elements.append(Spacer(1, 3.5 * mm))

    # ==========================================
    # 4. PROFESSIONAL TRAINING & CERTIFICATION
    # ==========================================
    elements.append(Paragraph("<font color='#E11D48'>■</font> PROFESSIONAL TRAINING &amp; COURSES", section_heading_style))
    training_html = (
        "<b>AI Automation &amp; Software Development Course</b> &nbsp;|&nbsp; "
        "<font color='#475569'>As-Sunnah Skill Development Institute</font><br/>"
        "<font color='#334155'>• Comprehensive practical training on constructing AI automation systems, applying artificial intelligence tools in business workflows, and practical software development methodologies.</font>"
    )
    elements.append(Paragraph(training_html, body_style))
    elements.append(Spacer(1, 3.5 * mm))

    # ==========================================
    # 5. WORK EXPERIENCE & PROJECTS
    # ==========================================
    elements.append(Paragraph("<font color='#E11D48'>■</font> WORK EXPERIENCE &amp; PROJECTS", section_heading_style))
    exp_header = "<b>Freelance Developer &amp; AI Automation Specialist</b> &nbsp;|&nbsp; <font color='#E11D48'>2023 – Present</font>"
    elements.append(Paragraph(exp_header, bold_body_style))
    elements.append(Paragraph("• Developed customized, high-speed websites and software applications tailored to client requirements.", bullet_style))
    elements.append(Paragraph("• Set up intelligent AI automation workflows for businesses to minimize manual repetitive labor and operational costs.", bullet_style))
    elements.append(Paragraph("• Created promotional AI video content and custom brand logos for diverse clients and personal brands.", bullet_style))
    elements.append(Spacer(1, 3.5 * mm))

    # ==========================================
    # 6. EDUCATION & PERSONAL DETAILS (2-Column)
    # ==========================================
    edu_content = [
        Paragraph("<font color='#E11D48'>■</font> <b>EDUCATIONAL BACKGROUND</b>", section_heading_style),
        Paragraph("<b>Dawra-e-Hadith (Master's Equivalent)</b>", bold_body_style),
        Paragraph("Jamia Arabia Imdadul Uloom Faridabad Madrasah, Dhaka<br/><font color='#64748B' size='7.5'>(Also studied at Jamia Islamia Darul Uloom Madania, Jatrabari)</font>", body_style),
        Spacer(1, 1.5 * mm),
        Paragraph("<b>Alim (Higher Secondary / HSC Equivalent)</b>", bold_body_style),
        Paragraph("Tonki Sadekul Uloom Fazil Madrasah, Akhaura, Brahmanbaria", body_style),
        Spacer(1, 1.5 * mm),
        Paragraph("<b>Dakhil (Secondary / SSC Equivalent)</b>", bold_body_style),
        Paragraph("Tonki Sadekul Uloom Fazil Madrasah, Akhaura, Brahmanbaria", body_style),
    ]

    personal_content = [
        Paragraph("<font color='#E11D48'>■</font> <b>PERSONAL DETAILS</b>", section_heading_style),
        Paragraph("<b>Father's Name:</b> Abdul Kadir (আব্দুল কাদির)", body_style),
        Paragraph("<b>Permanent Address:</b> Ashuganj, Brahmanbaria", body_style),
        Paragraph("<b>Current Address:</b> Dhaka, Bangladesh", body_style),
        Paragraph("<b>Nationality:</b> Bangladeshi &nbsp;|&nbsp; <b>Religion:</b> Islam", body_style),
        Paragraph("<b>Driving License:</b> Valid Driving License Holder", body_style),
        Paragraph("<b>Languages:</b> Bengali (Native), Arabic (Proficient), English (Working)", body_style),
    ]

    bottom_table = Table([[edu_content, personal_content]], colWidths=[96 * mm, 86 * mm])
    bottom_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    elements.append(bottom_table)
    elements.append(Spacer(1, 4 * mm))

    # ==========================================
    # 7. DECLARATION & SIGNATURE
    # ==========================================
    dec_text = "<i>I hereby certify that the information presented above is accurate and true to the best of my knowledge.</i>"
    sig_text = "<b>(Merajul Islam)</b><br/><font color='#64748B' size='7.5'>Signature &amp; Date</font>"
    
    dec_table = Table([[Paragraph(dec_text, contact_style), Paragraph(sig_text, ParagraphStyle('Sig', parent=styles['Normal'], alignment=TA_RIGHT, fontSize=8.5, leading=11))]], colWidths=[130 * mm, 52 * mm])
    dec_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('LINEABOVE', (0, 0), (-1, -1), 0.5, c_border),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
    ]))
    elements.append(dec_table)

    doc.build(elements)
    print(f"Generated {pdf_filename} successfully! Size: {os.path.getsize(pdf_filename)} bytes")

if __name__ == '__main__':
    generate_pdf()
