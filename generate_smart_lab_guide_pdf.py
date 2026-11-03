import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register fonts
pdfmetrics.registerFont(TTFont('Nirmala', r'C:\Windows\Fonts\Nirmala.ttc', subfontIndex=0))
pdfmetrics.registerFont(TTFont('Nirmala-Bold', r'C:\Windows\Fonts\Nirmala.ttc', subfontIndex=1))

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Nirmala-Bold", 8)
        self.setFillColor(colors.HexColor("#64748b"))

        # Header (Pages > 1)
        if self._pageNumber > 1:
            self.drawString(40, 808, "SMART LAB COMMAND CENTER — প্রাতিষ্ঠানিক ব্যবহার ও ডেমো নির্দেশিকা")
            self.setFont("Nirmala", 8)
            self.drawRightString(555, 808, "MERAJUL ISLAM | PRODUCTION GUIDE")
            self.setStrokeColor(colors.HexColor("#e2e8f0"))
            self.setLineWidth(0.75)
            self.line(40, 801, 555, 801)

        # Footer (All pages)
        self.setStrokeColor(colors.HexColor("#e2e8f0"))
        self.setLineWidth(0.75)
        self.line(40, 40, 555, 40)

        self.setFont("Nirmala", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(40, 28, "Smart Lab Command Center • Designed & Developed by Merajul Islam (mdmiraz.com)")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(555, 28, page_str)
        self.restoreState()


def create_callout(title, text, bg_color="#f8fafc", border_color="#3b82f6", title_color="#1d4ed8"):
    t_style = ParagraphStyle(
        'CalloutTitle',
        fontName='Nirmala-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor(title_color)
    )
    b_style = ParagraphStyle(
        'CalloutBody',
        fontName='Nirmala',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#334155')
    )
    content = [
        Paragraph(title, t_style),
        Spacer(1, 2),
        Paragraph(text, b_style)
    ]
    t = Table([[content]], colWidths=[515])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(bg_color)),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor(border_color)),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    return t


def build_guide_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=48,
        bottomMargin=48
    )

    styles = getSampleStyleSheet()

    # Typography styles
    title_style = ParagraphStyle(
        'DocTitle',
        fontName='Nirmala-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=2
    )
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        fontName='Nirmala',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#475569'),
        spaceAfter=8
    )
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        fontName='Nirmala-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#0f172a'),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        fontName='Nirmala-Bold',
        fontSize=10,
        leading=13.5,
        textColor=colors.HexColor('#1e293b'),
        spaceBefore=5,
        spaceAfter=2,
        keepWithNext=True
    )
    body_style = ParagraphStyle(
        'Body_Custom',
        fontName='Nirmala',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#334155'),
        spaceAfter=4
    )
    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        fontName='Nirmala',
        fontSize=8.8,
        leading=12.5,
        textColor=colors.HexColor('#334155'),
        leftIndent=12,
        spaceAfter=2
    )

    story = []

    # ==================== PAGE 1 ====================
    # Title & Header
    story.append(Paragraph("SMART LAB COMMAND CENTER", title_style))
    story.append(Paragraph("সম্পূর্ণ ব্যবহার, সেটআপ এবং ক্লায়েন্ট ডেমোনস্ট্রেশন গাইডলাইন (Official Manual)", subtitle_style))

    # Meta Info Table
    meta_data = [
        [
            Paragraph("<b>সফটওয়্যার:</b> Smart Lab Command Center v2.4", body_style),
            Paragraph("<b>ডেভেলপার:</b> মেরাজুল ইসলাম (Merajul Islam)", body_style)
        ],
        [
            Paragraph("<b>পোর্টফোলিও:</b> mdmiraz.com | GitHub: MdMiraz-dev", body_style),
            Paragraph("<b>উদ্দেশ্য:</b> প্রাতিষ্ঠানিক কম্পিউটার ল্যাব সেন্ট্রাল মনিটরিং", body_style)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[255, 260])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f1f5f9')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 6))

    # Section 1: Overview
    story.append(Paragraph("১. সিস্টেম পরিচিতি — এটি কেন তৈরি করা হয়েছে?", h1_style))
    story.append(Paragraph(
        "সাধারণ কম্পিউটার ল্যাবে শিক্ষককে প্রতিটি ছাত্রের পেছনে ঘুরে ঘুরে দেখতে হয় ছাত্ররা কী করছে। এতে সময় নষ্ট হয় এবং ছাত্ররা শিক্ষক কাছে এলেই দ্রুত ট্যাব বদলে পড়ার ভান করে। <b>Smart Lab Command Center</b> এই সমস্যার একটি ডিজিটাল প্রাতিষ্ঠানিক সমাধান। শিক্ষক তার চেয়ারে বসেই এক স্ক্রিনে পুরো ল্যাবের সমস্ত কম্পিউটার রিয়েল-টাইমে দেখতে পারেন এবং নিয়ন্ত্রণ করতে পারেন।",
        body_style
    ))

    # Core Features 3-Column Table
    features_data = [
        [
            Paragraph("<b>১. সেন্ট্রাল লাইভ ড্যাশবোর্ড</b><br/>এক স্ক্রিন থেকেই প্রতিটি ছাত্রের লাইভ ডিসপ্লে, প্রসেসর (CPU) ও মেমরি (RAM) সেকেন্ডে সেকেন্ডে আপডেট হয়।", body_style),
            Paragraph("<b>২. ডিস্ট্রাকশন ওয়াচডগ</b><br/>ছাত্ররা ক্লাসের সময় ইউটিউব, ফেসবুক বা গেমস চালালেই শিক্ষকের স্ক্রিনে লাল সতর্কতা আসে এবং প্রমাণস্বরূপ স্ক্রিনশট জমা হয়।", body_style),
            Paragraph("<b>৩. অটোলক ও কার্ফিউ</b><br/>রাত ৯টা বাজলেই পুরো ল্যাব স্বয়ংক্রিয়ভাবে লক হয়ে বিদ্যুৎ বাঁচায়। এছাড়া শিক্ষক চাইলে এক ক্লিকেই যেকোনো পিসি লক করতে পারেন।", body_style),
        ]
    ]
    feat_table = Table(features_data, colWidths=[171, 172, 172])
    feat_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(feat_table)
    story.append(Spacer(1, 6))

    # Section 2: Step-by-Step Setup
    story.append(Paragraph("২. ল্যাবে সেটআপ ও চালু করার ৩টি সহজ ধাপ", h1_style))

    # Step 1
    story.append(Paragraph("ধাপ ১: শিক্ষক কম্পিউটারে সার্ভার চালু করা", h2_style))
    story.append(Paragraph(
        "• শিক্ষক পিসির ফোল্ডারে থাকা <b>Start-Teacher-Server.bat</b> ফাইলে ডাবল ক্লিক করুন।<br/>"
        "• কালো উইন্ডোতে শিক্ষক পিসির নিজস্ব লোকাল আইপি (যেমন: <b>10.13.108.16</b> বা <b>192.168.x.x</b>) স্পষ্টভাবে দেখা যাবে।<br/>"
        "• শিক্ষক পিসির ব্রাউজারে <b>http://localhost:8500</b> লিংকে ঢুকলেই সেন্ট্রাল কন্ট্রোল ড্যাশবোর্ড চালু হয়ে যাবে।",
        bullet_style
    ))

    # Step 2
    story.append(Paragraph("ধাপ ২: পেনড্রাইভ ছাড়া ছাত্র কম্পিউটারে ফাইল নেওয়া (Direct LAN Download)", h2_style))
    story.append(Paragraph(
        "• ছাত্র কম্পিউটারের গুগল ক্রোম বা এজ ব্রাউজারের অ্যাড্রেস বারে সরাসরি লিখুন:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>http://&lt;শিক্ষক-কম্পিউটারের-আইপি&gt;:8500/download-agent</b> "
        "(যেমন: <b>http://10.13.108.16:8500/download-agent</b>)<br/>"
        "• ব্রাউজার সাথে সাথে সার্ভার থেকে <b>SmartLab-Student-Agent.zip</b> (সাইজ মাত্র ৯ কিলোবাইট) ডাউনলোড করে দেবে। কোনো পেনড্রাইভ লাগবে না!<br/>"
        "• ডাউনলোড করা জিপ ফাইলটির ওপর রাইট ক্লিক করে <b>Extract All...</b> দিয়ে আনজিপ করুন।",
        bullet_style
    ))

    # Step 3
    story.append(Paragraph("ধাপ ৩: ছাত্র কম্পিউটারে এজেন্ট চালু করা", h2_style))
    story.append(Paragraph(
        "• আনজিপ করা ফোল্ডারে থাকা <b>Start-Student-Workstation.bat</b> ফাইলে ডাবল ক্লিক করুন।<br/>"
        "• কালো উইন্ডোতে শিক্ষক পিসির আইপি অ্যাড্রেস চাইবে: সেখানে শিক্ষক পিসির আইপি (যেমন: <b>10.13.108.16</b>) লিখে Enter চাপুন।<br/>"
        "• এরপর কম্পিউটারের আইডি (যেমন: <b>LAB-PC-01</b>) এবং ছাত্রের নাম লিখে Enter চাপুন।<br/>"
        "• টার্মিনালে <b>[INFO] Connected successfully as LAB-PC-01</b> লেখা আসলেই কাজ শেষ! এই উইন্ডোটি মিনিমাইজ করে রাখুন।",
        bullet_style
    ))
    story.append(Spacer(1, 4))

    # Callout Box: Success Check
    story.append(create_callout(
        "✓ ফলাফল যাচাই:",
        "এবার শিক্ষক কম্পিউটারের ড্যাশবোর্ডে তাকালেই দেখবেন ছাত্র কম্পিউটারের কার্ডটি সবুজ বাতি জ্বালিয়ে একটিভ হয়ে গেছে এবং ছাত্র তার স্ক্রিনে যা করছে, শিক্ষক সাথে সাথে রিয়েল-টাইমে তা দেখতে পাচ্ছেন!",
        bg_color="#f0fdf4", border_color="#22c55e", title_color="#15803d"
    ))

    story.append(PageBreak())

    # ==================== PAGE 2 ====================
    # Section 3: Droste Effect & Demonstration Guide
    story.append(Paragraph("৩. স্ক্রিনের ভেতর স্ক্রিনের সুরঙ্গ (Droste Effect) কেন হয় এবং সমাধানের নিয়ম", h1_style))
    story.append(Paragraph(
        "একই কম্পিউটারে শিক্ষক ও ছাত্র উভয় অংশ টেস্ট করার সময় আপনি নিশ্চয়ই লক্ষ্য করেছেন যে স্ক্রিনে একটার ভেতর আরেকটা ছবির সুরঙ্গ বা আয়নার মতো তৈরি হয়। এটি কেন হয় এবং অন্যকে কীভাবে পরিষ্কার করে বুঝিয়ে বলবেন:",
        body_style
    ))

    droste_info = [
        [
            Paragraph("<b>সমস্যার মূল কারণ:</b>", body_style),
            Paragraph("যখন আপনি একই মনিটরে শিক্ষক ড্যাশবোর্ডও খুলে রাখেন এবং ছাত্র এজেন্টও চালু করেন, তখন ছাত্র সফটওয়্যার প্রতি সেকেন্ডে পুরো মনিটরের ছবি তোলে। মনিটরে যেহেতু শিক্ষকের ড্যাশবোর্ডও খোলা থাকে, তাই ড্যাশবোর্ডের ছবি আবার ড্যাশবোর্ডে গিয়ে পড়ে। আয়নার সামনে আয়না ধরলে যেমন অনন্ত সুরঙ্গ তৈরি হয়, ঠিক তেমনই ঘটে।", body_style)
        ],
        [
            Paragraph("<b>আসল ল্যাব টেস্ট (০% সমস্যা):</b>", body_style),
            Paragraph("ল্যাবের ছাত্র কম্পিউটারে তো আর শিক্ষক ড্যাশবোর্ড খোলা থাকবে না! ছাত্রের স্ক্রিনে থাকবে শুধু তার পড়া, ইউটিউব কিংবা কোডিং। ফলে শিক্ষকের স্ক্রিনে ছাত্রের স্ক্রিন ১০০% নিখুঁত, পরিষ্কার এবং ফুল কোয়ালিটিতে ভেসে উঠবে—কোনো সুরঙ্গ বা মিরর ইফেক্ট তৈরি হবে না।", body_style)
        ],
        [
            Paragraph("<b>একই পিসিতে টেস্ট করার কৌশল:</b>", body_style),
            Paragraph("যদি আপনি ১টি কম্পিউটারেই অন্য কাউকে বা ক্লায়েন্টকে ডেমো দেখাতে চান, তবে ড্যাশবোর্ডটি কম্পিউটারে মিনিমাইজ করে রাখুন এবং আপনার স্মার্টফোনের ব্রাউজার দিয়ে <b>http://&lt;শিক্ষক-আইপি&gt;:8500</b> লিংকে ঢুকুন। তখন ফোনে শিক্ষক ড্যাশবোর্ড একদম আয়নার ইফেক্ট ছাড়া ক্রিস্টাল ক্লিয়ার দেখাবে।", body_style)
        ]
    ]
    t_droste = Table(droste_info, colWidths=[130, 385])
    t_droste.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_droste)
    story.append(Spacer(1, 8))

    # Section 4: Live Demonstration to Clients/Principals
    story.append(Paragraph("৪. শিক্ষক, অধ্যক্ষ কিংবা ক্লায়েন্টকে ডেমো দেখানোর ধাপসমূহ", h1_style))
    story.append(Paragraph(
        "আপনি যখন কোনো মাদরাসা, স্কুল বা কম্পিউটার ল্যাবের কর্তৃপক্ষের সামনে এই সফটওয়্যারটি উপস্থাপন করবেন, তখন নিচের ক্রমানুসারে ডেমো দেখালে তারা সবচেয়ে বেশি মুগ্ধ হবে:",
        body_style
    ))

    demo_steps = [
        ("১. লাইভ স্ক্রিন স্ট্রিমিং", "শিক্ষক ড্যাশবোর্ড প্রজেক্টরে বা শিক্ষক পিসিতে ওপেন রাখুন। ছাত্র পিসিতে কোনো ব্রাউজার খুলুন বা কোড লিখুন। দেখান যে শিক্ষক কোনো ক্লিক না করেই সাথে সাথে ছাত্রের স্ক্রিন আপডেট দেখতে পাচ্ছেন।"),
        ("২. ইউটিউব / ফেসবুক ধরার ম্যাজিক", "ছাত্র কম্পিউটারে ইউটিউব ওপেন করুন বা কোনো বিনোদনমূলক ভিডিও প্লে করুন। শিক্ষক স্ক্রিনে দেখান—সাথে সাথে ছাত্রের কার্ডে লাল রঙের 'ENTERTAINMENT DETECTED' সতর্কতা চলে এসেছে এবং ড্যাশবোর্ডে অ্যালার্ম বেজে উঠেছে।"),
        ("৩. অকাট্য প্রমাণের স্ক্রিনশট (Daily Audit Report)", "ছাত্র যদি বলে 'আমি তো ইউটিউব দেখিনি!', তখন শিক্ষক ড্যাশবোর্ডে থাকা 'Daily Audit Report' বাটনে চাপ দিন। সেখানে ছাত্র কোন সময় থেকে কোন সময় ইউটিউব দেখেছে তা গুগল শিটের মতো নিখুঁত টেবিল আকারে চলে আসবে এবং সাথে তারিখ, সময়, আইপি ও ম্যাক অ্যাড্রেস ওয়াটারমার্কযুক্ত ফুল স্ক্রিনশট দেখা যাবে।"),
        ("৪. রিমোট পিসি লক (Remote Lockdown)", "শিক্ষক ড্যাশবোর্ড থেকে 'Lock PC' বাটনে ক্লিক করুন। সাথে সাথে ছাত্রের কম্পিউটারের স্ক্রিন বন্ধ হয়ে গিয়ে বড় করে 'CLASS IN SESSION - SCREEN LOCKED' ভেসে উঠবে। ছাত্রের মাউস বা কিবোর্ড কাজ করবে না।"),
        ("৫. স্বয়ংক্রিয় রাত ৯টা কার্ফিউ (Curfew Auto-Lock)", "ল্যাব ছুটির সময় বা রাত ৯টা বাজলে কাউকে গিয়ে একটি একটি করে পিসি বন্ধ করতে হয় না। সফটওয়্যার নিজে থেকেই পুরো ল্যাবের সব পিসি একযোগে অফ করে প্রতিষ্ঠানের বিদ্যুৎ সাশ্রয় নিশ্চিত করে।"),
        ("৬. মোবাইল টেলিগ্রাম বট (Anywhere Supervision)", "শিক্ষক বা প্রধান শিক্ষক ল্যাবের বাইরে থাকলেও মোবাইল ফোনের টেলিগ্রাম বট দিয়ে /status দিলে পুরো ল্যাবের অবস্থা জানতে পারেন এবং /lock দিলে ফোন থেকেই ল্যাব লক করতে পারেন।")
    ]

    demo_table_data = []
    for title, desc in demo_steps:
        demo_table_data.append([
            Paragraph(f"<b>{title}</b>", ParagraphStyle('DTitle', fontName='Nirmala-Bold', fontSize=9.5, leading=13, textColor=colors.HexColor('#0f172a'))),
            Paragraph(desc, ParagraphStyle('DDesc', fontName='Nirmala', fontSize=8.8, leading=12.5, textColor=colors.HexColor('#334155')))
        ])

    t_demo = Table(demo_table_data, colWidths=[155, 360])
    t_demo.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#ffffff')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_demo)

    story.append(PageBreak())

    # ==================== PAGE 3 ====================
    # Section 5: FAQs
    story.append(Paragraph("৫. বহুল জিজ্ঞাসিত প্রশ্ন ও উত্তর (FAQs)", h1_style))

    faq_data = [
        [
            Paragraph("<b>প্রশ্ন: ল্যাবে কি ইন্টারনেট কানেকশন বাধ্যতামূলক?</b>", body_style),
            Paragraph("<b>উত্তর:</b> না! এই সফটওয়্যারটি ১০০% লোকাল নেটওয়ার্কে (Local Offline LAN / Wi-Fi Router) কাজ করে। ব্রডব্যান্ড ইন্টারনেট বন্ধ থাকলেও ল্যাব মনিটরিং, স্ক্রিনশট এবং পিসি লক পুরোদমে সচল থাকে।", body_style)
        ],
        [
            Paragraph("<b>প্রশ্ন: ছাত্ররা কি সফটওয়্যারটি বন্ধ করে দিতে পারবে?</b>", body_style),
            Paragraph("<b>উত্তর:</b> না। ছাত্র এজেন্ট ব্যাকগ্রাউন্ড সার্ভিস হিসেবে চলে। কোনো ছাত্র যদি টাস্ক ম্যানেজার থেকে বন্ধ করার চেষ্টা করে, সাথে সাথে শিক্ষকের ড্যাশবোর্ডে 'OFFLINE DISCONNECT ALERT' লাল বাতি জ্বলে ওঠে।", body_style)
        ],
        [
            Paragraph("<b>প্রশ্ন: কম্পিউটার কি স্লো হয়ে যাবে?</b>", body_style),
            Paragraph("<b>উত্তর:</b> একদমই না। ছাত্র সফটওয়্যারটি অতি হালকা পাইথন স্ক্রিপ্ট হিসেবে তৈরি। এটি মাত্র ১৫ থেকে ২৫ মেগাবাইট র‍্যাম এবং ০.৫% এরও কম সিপিইউ ব্যবহার করে, ফলে সাধারণ মানের কম্পিউটারেও কোনো ল্যাগ হয় না।", body_style)
        ],
        [
            Paragraph("<b>প্রশ্ন: শিক্ষক ল্যাবের বাইরে থাকলে মনিটর করবেন কীভাবে?</b>", body_style),
            Paragraph("<b>উত্তর:</b> স্মার্ট ল্যাব টেলিগ্রাম বটের মাধ্যমে যুক্ত। শিক্ষক ল্যাব থেকে দূরে নিজের বাসায় বা অফিসে বসেও মোবাইল ফোনে টেলিগ্রামের মাধ্যমে ল্যাবের নোটিফিকেশন পান এবং কমান্ড পাঠাতে পারেন।", body_style)
        ],
        [
            Paragraph("<b>প্রশ্ন: দৈনিক অডিট রিপোর্ট কি প্রিন্ট বা এক্সেল করা যায়?</b>", body_style),
            Paragraph("<b>উত্তর:</b> হ্যাঁ। ড্যাশবোর্ডের 'Daily Audit Report' থেকে এক ক্লিকেই গুগল শিট বা এক্সেল ফরম্যাটে (.CSV) সমস্ত তথ্য ডাউনলোড ও প্রিন্ট করা যায়।", body_style)
        ]
    ]

    t_faq = Table(faq_data, colWidths=[175, 340])
    t_faq.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_faq)
    story.append(Spacer(1, 10))

    # Section 6: Institutional Value Pitch
    story.append(Paragraph("৬. প্রাতিষ্ঠানিক সুবিধা ও ক্লায়েন্ট কনভিন্স করার মূল পয়েন্ট", h1_style))
    story.append(Paragraph(
        "যেকোনো শিক্ষা প্রতিষ্ঠান বা মাদরাসার প্রিন্সিপালকে সফটওয়্যারটির প্রাতিষ্ঠানিক মূল্য বোঝানোর জন্য এই ৩টি বিষয় তুলে ধরবেন:",
        body_style
    ))

    pitch_data = [
        [
            Paragraph("<b>১. শিক্ষার মান ও মনোযোগ নিশ্চিতকরণ</b><br/>ছাত্ররা ক্লাসের সময় গেম বা ইউটিউবে না গিয়ে ১০০% ক্লাসের বিষয়ে মনোযোগী থাকে। অভিভাবকরাও আশ্বস্ত হন যে তাদের সন্তান ল্যাবে অপচয় করছে না।", body_style),
            Paragraph("<b>২. বিদ্যুৎ ও হার্ডওয়্যার সুরক্ষা</b><br/>রাত ৯টায় স্বয়ংক্রিয় শাটডাউন ল্যাবের বিদ্যুৎ বিল সাশ্রয় করে এবং সারারাত পিসি অন থাকার কারণে যন্ত্রাংশ গরম হওয়া ও নষ্ট হওয়া থেকে রক্ষা করে।", body_style),
            Paragraph("<b>৩. সম্পূর্ণ নিজস্ব ও নিরাপদ ডেটা</b><br/>কোনো থার্ড-পার্টি ক্লাউড সার্ভারে ছাত্রদের ডেটা যায় না। সব কিছু প্রতিষ্ঠানের নিজস্ব রাউটার ও শিক্ষক কম্পিউটারের লোকাল স্টোরেজে সংরক্ষিত থাকে।", body_style),
        ]
    ]
    t_pitch = Table(pitch_data, colWidths=[171, 172, 172])
    t_pitch.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f1f5f9')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#94a3b8')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_pitch)
    story.append(Spacer(1, 10))

    # Developer Signoff
    signoff_content = [
        Paragraph("<b>অফিসিয়াল সিস্টেম সাপোর্ট ও যোগাযোগ:</b>", ParagraphStyle('SignTitle', fontName='Nirmala-Bold', fontSize=10, leading=14, textColor=colors.HexColor('#0f172a'))),
        Spacer(1, 3),
        Paragraph(
            "সফটওয়্যারটি তৈরি ও পরিচালনা করছেন <b>মেরাজুল ইসলাম (Merajul Islam)</b>। ল্যাবে কাস্টম ইন্সটলেশন, একাধিক ব্রাঞ্চ নেটওয়ার্কিং কিংবা টেলিগ্রাম বট কনফিগারেশনের জন্য যেকোনো সময় পোর্টফোলিও বা সরাসরি যোগাযোগ করা যাবে।<br/>"
            "🌐 <b>ওয়েবসাইট পোর্টফোলিও:</b> https://mdmiraz.com &nbsp;&nbsp;|&nbsp;&nbsp; 💻 <b>GitHub:</b> https://github.com/MdMiraz-dev<br/>"
            "📍 <b>ঠিকানা:</b> আশুগঞ্জ, ব্রাহ্মণবাড়িয়া, বাংলাদেশ © ২০২৬",
            ParagraphStyle('SignBody', fontName='Nirmala', fontSize=8.8, leading=13.5, textColor=colors.HexColor('#475569'))
        )
    ]
    t_sign = Table([[signoff_content]], colWidths=[515])
    t_sign.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 9),
        ('RIGHTPADDING', (0,0), (-1,-1), 9),
    ]))
    story.append(t_sign)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"SUCCESS: Generated {output_path}")

if __name__ == '__main__':
    out_pdf = 'Smart_Lab_Complete_User_Guide.pdf'
    build_guide_pdf(out_pdf)
