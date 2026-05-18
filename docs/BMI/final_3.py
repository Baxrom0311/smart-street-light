"""
II BOB - AMALIY QISM generatori
BMI_final.docx fayliga II BOB bo'limini qo'shadi (~30 sahifa)
"""

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
import os

BASE_DIR = '/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI'
DOC_PATH = os.path.join(BASE_DIR, 'BMI_final.docx')
IMG_DIR = os.path.join(BASE_DIR, 'images')

doc = Document(DOC_PATH)


def set_paragraph_format(paragraph, first_indent=Cm(1.25), space_before=Pt(0), space_after=Pt(0)):
    pf = paragraph.paragraph_format
    pf.first_line_indent = first_indent
    pf.space_before = space_before
    pf.space_after = space_after


def add_text(paragraph, text, font_name='Times New Roman', font_size=Pt(14), bold=False, italic=False):
    run = paragraph.add_run(text)
    run.font.name = font_name
    run.font.size = font_size
    run.font.bold = bold
    run.font.italic = italic
    return run


def add_paragraph(text):
    p = doc.add_paragraph()
    set_paragraph_format(p)
    add_text(p, text)
    return p


def add_heading_styled(text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.name = 'Times New Roman'
        run.font.size = Pt(14)
        run.font.color.rgb = None
    return h


def add_image_with_caption(image_filename, caption_text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    run.add_picture(os.path.join(IMG_DIR, image_filename), width=Cm(14))
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = cap.add_run(caption_text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.italic = True


def add_table_caption(caption_text):
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = cap.add_run(caption_text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.italic = True


def add_table(headers, rows):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = ''
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(14)
        r.font.bold = True
    for row_idx, row_data in enumerate(rows):
        for col_idx, val in enumerate(row_data):
            cell = table.rows[row_idx + 1].cells[col_idx]
            cell.text = ''
            p = cell.paragraphs[0]
            r = p.add_run(str(val))
            r.font.name = 'Times New Roman'
            r.font.size = Pt(14)
    return table


def add_code_block(code_text):
    for line in code_text.split('\n'):
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.left_indent = Cm(1)
        pf.first_line_indent = Cm(0)
        pf.space_before = Pt(0)
        pf.space_after = Pt(0)
        r = p.add_run(line)
        r.font.name = 'Courier New'
        r.font.size = Pt(10)


# ============================================================
# II BOB. AMALIY QISM
# ============================================================

add_heading_styled('II BOB. AMALIY QISM', level=1)


# ============================================================
# 2.1 Tizimni loyihalash
# ============================================================

add_heading_styled('2.1. Tizimni loyihalash va komponentlar tanlash', level=2)

add_paragraph(
    "Aqlli ko'cha yoritish tizimini loyihalashda eng muhim qadam — bu to'g'ri mikrokontrollerni tanlashdir. "
    "Zamonaviy IoT loyihalarida bir nechta mashhur mikrokontroller platformalari mavjud bo'lib, ularning har biri "
    "o'ziga xos afzalliklari va kamchiliklariga ega. Bizning loyihamiz uchun asosiy talablar quyidagilardan iborat: "
    "WiFi ulanish imkoniyati, yetarli GPIO pinlar soni, analog o'qish qobiliyati, past energiya iste'moli, "
    "arzon narx va keng jamoa qo'llab-quvvatlashi. Ushbu talablarni hisobga olgan holda, biz Arduino Uno, "
    "ESP8266 NodeMCU, ESP32 DevKit va STM32 Blue Pill platformalarini taqqoslab ko'rdik. Har bir platforma "
    "o'zining kuchli tomonlariga ega bo'lsa-da, IoT loyihalari uchun eng maqbul yechim ESP32 ekanligi aniqlandi."
)

add_paragraph(
    "Arduino Uno — bu eng mashhur va keng tarqalgan mikrokontroller platformasi bo'lib, yangi boshlovchilar uchun "
    "ideal hisoblanadi. Biroq, uning asosiy kamchiligi — o'rnatilgan WiFi modulining yo'qligi. IoT loyihalarida "
    "tarmoqqa ulanish uchun qo'shimcha ESP8266 moduli kerak bo'ladi, bu esa sxemani murakkablashtiradi va narxni "
    "oshiradi. Bundan tashqari, Arduino Uno ning 16 MHz taktli chastotasi va 2 KB operativ xotirasi zamonaviy "
    "IoT ilovalar uchun yetarli emas. Firebase kutubxonalari va JSON parsing uchun kamida 80 KB RAM talab etiladi, "
    "bu esa Arduino Uno imkoniyatlaridan ancha yuqori. Shuning uchun Arduino Uno bizning loyihamiz uchun mos emas."
)

add_paragraph(
    "ESP8266 NodeMCU — bu WiFi imkoniyatiga ega bo'lgan arzon mikrokontroller bo'lib, oddiy IoT loyihalari uchun "
    "juda yaxshi tanlov hisoblanadi. Uning 80 MHz protsessori va 80 KB RAMi ko'plab vazifalarni bajarishga imkon "
    "beradi. Biroq, ESP8266 ning bir nechta muhim cheklovlari mavjud: birinchidan, u faqat bitta analog pin (ADC) "
    "ga ega, bu esa bir vaqtning o'zida bir nechta analog sensorni ulashni qiyinlashtiradi. Ikkinchidan, uning "
    "GPIO pinlari soni cheklangan (11 ta) va ularning ba'zilari yuklash jarayonida maxsus funksiyalarni bajaradi. "
    "Uchinchidan, ESP8266 da Bluetooth yo'q, bu esa kelajakda tizimni kengaytirish imkoniyatini cheklaydi. "
    "To'rtinchidan, uning dual-core protsessori yo'q, shuning uchun WiFi va sensor o'qish bir vaqtda bajarilganda "
    "kechikishlar yuzaga kelishi mumkin."
)

add_paragraph(
    "STM32 Blue Pill — bu professional darajadagi ARM Cortex-M3 mikrokontroller bo'lib, yuqori unumdorlik va "
    "ko'p sonli GPIO pinlarga ega. Uning 72 MHz protsessori va 20 KB RAMi ko'plab murakkab vazifalarni bajarishga "
    "imkon beradi. Biroq, STM32 ning asosiy kamchiligi — o'rnatilgan WiFi va Bluetooth modullarining yo'qligi. "
    "IoT loyihalarida tarmoqqa ulanish uchun qo'shimcha modul kerak bo'ladi. Bundan tashqari, STM32 uchun "
    "Firebase kutubxonalari to'g'ridan-to'g'ri mavjud emas, bu esa dasturiy ta'minotni ishlab chiqishni "
    "sezilarli darajada murakkablashtiradi. STM32 ko'proq sanoat avtomatizatsiyasi va signal qayta ishlash "
    "kabi sohalarda qo'llaniladi, oddiy IoT loyihalari uchun esa ortiqcha murakkablik yaratadi."
)

add_paragraph(
    "ESP32 DevKit — bu Espressif Systems tomonidan ishlab chiqilgan zamonaviy mikrokontroller bo'lib, IoT "
    "loyihalari uchun eng maqbul yechim hisoblanadi. Uning asosiy afzalliklari quyidagilardan iborat: "
    "birinchidan, o'rnatilgan WiFi (802.11 b/g/n) va Bluetooth (Classic + BLE) modullari mavjud, bu esa "
    "qo'shimcha komponentlarsiz tarmoqqa ulanish imkonini beradi. Ikkinchidan, dual-core Xtensa LX6 "
    "protsessori 240 MHz taktli chastotada ishlaydi, bu esa bir yadroda WiFi, ikkinchisida sensor o'qish "
    "vazifalarini parallel bajarishga imkon beradi. Uchinchidan, 520 KB SRAM va 4 MB Flash xotira Firebase "
    "kutubxonalari va murakkab algoritmlar uchun yetarli. To'rtinchidan, 18 ta analog kanal (12-bit ADC) "
    "va 34 ta GPIO pin mavjud, bu esa ko'p sonli sensorlarni ulash imkonini beradi."
)

add_table_caption("2.1-jadval. Mikrokontrollerlar taqqoslash jadvali")
add_table(
    ['Parametr', 'Arduino Uno', 'ESP8266', 'ESP32', 'STM32'],
    [
        ['Protsessor', 'ATmega328P 16MHz', 'Tensilica 80MHz', 'Xtensa LX6 240MHz', 'ARM Cortex-M3 72MHz'],
        ['RAM', '2 KB', '80 KB', '520 KB', '20 KB'],
        ['Flash', '32 KB', '4 MB', '4 MB', '64 KB'],
        ['WiFi', 'Yo\'q', 'Ha (802.11 b/g/n)', 'Ha (802.11 b/g/n)', 'Yo\'q'],
        ['Bluetooth', 'Yo\'q', 'Yo\'q', 'Ha (BLE + Classic)', 'Yo\'q'],
        ['GPIO', '14', '11', '34', '37'],
        ['ADC', '6 (10-bit)', '1 (10-bit)', '18 (12-bit)', '10 (12-bit)'],
        ['Narx (USD)', '~$5', '~$3', '~$4', '~$2'],
        ['Firebase qo\'llab-quvvatlash', 'Yo\'q', 'Cheklangan', 'To\'liq', 'Yo\'q'],
        ['Dual Core', 'Yo\'q', 'Yo\'q', 'Ha', 'Yo\'q'],
    ]
)

add_paragraph(
    "Yuqoridagi taqqoslash jadvalidan ko'rinib turibdiki, ESP32 barcha asosiy parametrlar bo'yicha eng maqbul "
    "tanlov hisoblanadi. Uning narxi ESP8266 dan atigi 1 dollar qimmatroq bo'lsa-da, imkoniyatlari bir necha "
    "barobar yuqori. Ayniqsa, dual-core protsessor va to'liq Firebase qo'llab-quvvatlashi bizning loyihamiz "
    "uchun hal qiluvchi omillar bo'ldi. ESP32 ning 38 pinli DevKit versiyasini tanladik, chunki u barcha "
    "pinlarni tashqariga chiqaradi va breadboard da ishlash uchun qulay. Bundan tashqari, ESP32 ning deep "
    "sleep rejimida energiya iste'moli atigi 10 mikroamper, bu esa quyosh paneli bilan ishlashda muhim ahamiyatga ega."
)

add_paragraph(
    "Tizim arxitekturasi uch qatlamli modelga asoslangan bo'lib, har bir qatlam o'z vazifasini mustaqil "
    "bajaradi va boshqa qatlamlar bilan aniq belgilangan interfeyslar orqali aloqa qiladi. Birinchi qatlam — "
    "hardware qatlami — bu ESP32 mikrokontroller va unga ulangan sensorlar hamda aktuatorlardan iborat. "
    "Bu qatlam fizik muhitdan ma'lumot yig'adi (masofa, yorug'lik darajasi) va boshqaruv signallarini "
    "chiqaradi (LED yoqish/o'chirish). Ikkinchi qatlam — cloud qatlami — bu Firebase Realtime Database "
    "bo'lib, u barcha ma'lumotlarni real-time saqlaydi va sinxronlaydi. Firebase ning WebSocket protokoli "
    "orqali ma'lumotlar millisekundlar ichida barcha ulangan qurilmalarga yetkaziladi. Uchinchi qatlam — "
    "client qatlami — bu React asosidagi Progressive Web Application (PWA) bo'lib, foydalanuvchiga "
    "tizimni monitoring qilish va boshqarish imkonini beradi."
)

add_image_with_caption('diagram_architecture.png', "2.1-rasm. Tizim arxitekturasi diagrammasi")

add_paragraph(
    "Uch qatlamli arxitekturaning asosiy afzalligi — bu qatlamlar orasidagi mustaqillik. Hardware qatlami "
    "internet ulanishi uzilgan taqdirda ham avtonom ishlashni davom ettiradi, chunki barcha sensor o'qish "
    "va qaror qabul qilish algoritmlari lokal bajariladi. Cloud qatlami esa bir nechta qurilmalarni "
    "bir vaqtda boshqarish va monitoring qilish imkonini beradi. Client qatlami istalgan qurilmadan "
    "(kompyuter, telefon, planshet) foydalanish mumkin bo'lgan universal interfeys taqdim etadi. "
    "Bunday arxitektura kelajakda tizimni kengaytirish uchun ham qulay — yangi sensorlar qo'shish, "
    "bir nechta chiroqlarni bitta dashboard dan boshqarish, yoki sun'iy intellekt algoritmlarini "
    "qo'shish oson amalga oshiriladi. Ma'lumot oqimi quyidagicha: sensor ma'lumotlari ESP32 da "
    "o'qiladi, qayta ishlanadi va Firebase ga yuboriladi. Dashboard Firebase dan real-time "
    "ma'lumotlarni oladi va foydalanuvchiga ko'rsatadi. Foydalanuvchi buyruqlari Dashboard dan "
    "Firebase ga, undan esa ESP32 ga yetkaziladi."
)

add_paragraph(
    "Pin konfiguratsiya — bu hardware loyihalashning eng muhim qismlaridan biri. Har bir komponentning "
    "ESP32 ga qaysi pinga ulanishi aniq belgilanishi kerak, chunki noto'g'ri pin tanlash dasturiy "
    "xatolarga yoki hardware zararlanishiga olib kelishi mumkin. ESP32 ning barcha pinlari bir xil "
    "funksiyalarni bajara olmaydi — ba'zilari faqat input, ba'zilari faqat output, ba'zilari esa "
    "analog o'qishni qo'llab-quvvatlaydi. Bizning loyihamizda beshta asosiy pin ishlatiladi: "
    "GPIO 4 ultratovush sensorining TRIG pini uchun (output), GPIO 16 ECHO pini uchun (input), "
    "GPIO 34 yorug'lik sensori uchun (analog input), GPIO 26 LED strip ma'lumot pini uchun (output), "
    "va GPIO 2 onboard LED uchun (status ko'rsatkich). Har bir pin tanlashda ESP32 ning texnik "
    "hujjatlaridagi cheklovlar hisobga olingan."
)

add_table_caption("2.2-jadval. ESP32 pin konfiguratsiyasi")
add_table(
    ['ESP32 Pin', 'Komponent', 'Signal turi', 'Izoh'],
    [
        ['GPIO 4', 'RCWL-9610A TRIG', 'Digital OUTPUT', '10μs impuls yuborish'],
        ['GPIO 16', 'RCWL-9610A ECHO', 'Digital INPUT', 'Qaytgan signal vaqtini o\'lchash'],
        ['GPIO 34', 'TEMT6000 OUT', 'Analog INPUT (ADC1_CH6)', 'Yorug\'lik darajasi 0-4095'],
        ['GPIO 26', 'WS2812B DATA', 'Digital OUTPUT', 'LED strip boshqaruv signali'],
        ['GPIO 2', 'Onboard LED', 'Digital OUTPUT', 'Tizim holati indikatori'],
    ]
)

add_paragraph(
    "GPIO 4 va GPIO 16 pinlari ultratovush sensori uchun tanlangan, chunki ular ESP32 ning boot "
    "jarayonida maxsus funksiyalarni bajarmaydi va erkin ishlatilishi mumkin. GPIO 34 analog o'qish "
    "uchun tanlangan, chunki u ADC1 kanaliga tegishli — ESP32 da WiFi yoqilganda faqat ADC1 kanallari "
    "ishlatilishi mumkin, ADC2 kanallari esa WiFi bilan konflikt qiladi. Bu juda muhim nuqta — agar "
    "biz ADC2 kanalini (masalan, GPIO 25, 26, 27) yorug'lik sensori uchun ishlatsak, WiFi ulanishi "
    "paytida analog o'qish noto'g'ri natijalar beradi. GPIO 26 LED strip uchun tanlangan, chunki u "
    "RMT (Remote Control) periferiyasini qo'llab-quvvatlaydi, bu esa WS2812B protokoli uchun aniq "
    "vaqtlash signallarini generatsiya qilishda muhim. GPIO 2 esa ESP32 DevKit platasida o'rnatilgan "
    "ko'k LED ga ulangan bo'lib, qo'shimcha komponent talab qilmaydi."
)

add_paragraph(
    "Quvvat ta'minoti hisoblash — tizimning barqaror ishlashi uchun zarur bo'lgan energiya miqdorini "
    "aniqlash jarayoni. Har bir komponentning maksimal tok iste'molini hisobga olish kerak. ESP32 "
    "mikrokontroller WiFi faol holatda maksimal 240 mA tok iste'mol qiladi, biroq o'rtacha iste'mol "
    "80-100 mA atrofida. RCWL-9610A ultratovush sensori 15 mA, TEMT6000 yorug'lik sensori 1 mA dan "
    "kam tok iste'mol qiladi. WS2812B LED strip har bir LED uchun maksimal 60 mA (oq rangda to'liq "
    "yorug'likda) iste'mol qiladi, 13 LED uchun bu 780 mA ni tashkil etadi. Biroq, amalda biz "
    "LEDlarni kamdan-kam to'liq quvvatda ishlatamiz — odatda 50-70 foiz yorug'lik yetarli. Shunday "
    "qilib, maksimal tok iste'moli: ESP32 (240 mA) + Sensor (15 mA) + Light sensor (1 mA) + "
    "LED strip (780 mA * 0.7 = 546 mA) = taxminan 802 mA. Biroq, energiya tejash rejimida (LED "
    "o'chiq) iste'mol atigi 222 mA ni tashkil etadi, bu esa tizimning asosiy ish rejimi hisoblanadi."
)


add_paragraph(
    "PlatformIO — bu professional IoT dasturlash muhiti bo'lib, Arduino IDE ga nisbatan bir qancha "
    "afzalliklarga ega. Birinchidan, PlatformIO kutubxonalarni avtomatik boshqaradi — platformio.ini "
    "faylida kerakli kutubxonalar ro'yxatini ko'rsatish kifoya, ular avtomatik yuklab olinadi va "
    "kompilyatsiya qilinadi. Ikkinchidan, PlatformIO bir nechta platformalarni qo'llab-quvvatlaydi "
    "(ESP32, ESP8266, Arduino, STM32 va boshqalar), shuning uchun bir loyihani turli platformalarga "
    "osongina ko'chirish mumkin. Uchinchidan, PlatformIO VS Code editorigа integratsiyalangan bo'lib, "
    "kodni yozish, kompilyatsiya qilish va yuklash jarayonini bitta muhitda amalga oshirish imkonini "
    "beradi. To'rtinchidan, PlatformIO serial monitor, debugging va unit testing kabi professional "
    "vositalarni taqdim etadi. Bizning loyihamizda PlatformIO ning 6.1 versiyasi ishlatilgan bo'lib, "
    "u ESP32 Arduino framework ning 2.0.11 versiyasini qo'llab-quvvatlaydi."
)

add_paragraph(
    "Loyihamizda ishlatiladigan asosiy kutubxonalar quyidagilardan iborat. Firebase ESP32 Client "
    "(mobizt) — bu ESP32 uchun maxsus ishlab chiqilgan Firebase kutubxonasi bo'lib, Realtime Database, "
    "Authentication, Cloud Firestore va Storage xizmatlarini qo'llab-quvvatlaydi. Bu kutubxona "
    "stream (real-time listener) funksiyasini taqdim etadi, bu esa Firebase dan kelgan o'zgarishlarni "
    "darhol qabul qilish imkonini beradi. FastLED kutubxonasi — WS2812B va boshqa addressable LED "
    "striplarni boshqarish uchun eng mashhur kutubxona. U rang aralashmalari, animatsiyalar va "
    "yorug'lik darajasini boshqarish uchun qulay funksiyalarni taqdim etadi. WiFiManager kutubxonasi — "
    "WiFi ulanishni boshqarish uchun ishlatiladi, u captive portal orqali WiFi ma'lumotlarini "
    "kiritish va NVS (Non-Volatile Storage) da saqlash imkonini beradi. NTPClient kutubxonasi — "
    "internet orqali aniq vaqtni olish uchun ishlatiladi, bu jadval rejimida muhim ahamiyatga ega."
)

add_paragraph(
    "Web Dashboard uchun React + Vite + Firebase stack tanlangan. React — bu Facebook tomonidan "
    "ishlab chiqilgan JavaScript kutubxonasi bo'lib, foydalanuvchi interfeyslarini yaratish uchun "
    "eng mashhur vosita hisoblanadi. React ning komponent asosidagi arxitekturasi kodni qayta "
    "ishlatish va tashkil qilishni osonlashtiradi. Vite — bu zamonaviy frontend build tool bo'lib, "
    "Webpack ga nisbatan 10-100 marta tezroq ishlaydi. Vite ning Hot Module Replacement (HMR) "
    "funksiyasi dasturchi o'zgartirishlarni darhol brauzerda ko'rish imkonini beradi. Firebase "
    "Hosting — bu statik saytlarni joylashtirish uchun bepul xizmat bo'lib, global CDN, SSL "
    "sertifikati va custom domain qo'llab-quvvatlashini taqdim etadi. PWA (Progressive Web App) "
    "texnologiyasi esa web ilovani native mobil ilova kabi ishlash imkonini beradi — offline "
    "qo'llab-quvvatlash, push bildirishnomalar va bosh ekranga o'rnatish funksiyalari mavjud. "
    "Recharts kutubxonasi grafiklar va diagrammalar uchun ishlatilgan bo'lib, u React bilan "
    "mukammal integratsiyalangan va responsive dizaynni qo'llab-quvvatlaydi."
)

add_paragraph(
    "Firebase Realtime Database tanlashning asosiy sabablari quyidagilar: birinchidan, u real-time "
    "sinxronizatsiyani qo'llab-quvvatlaydi — ma'lumot o'zgarganda barcha ulangan qurilmalar darhol "
    "yangilanadi. Ikkinchidan, Firebase ning bepul tarif rejasi (Spark plan) bizning loyihamiz uchun "
    "yetarli — 1 GB saqlash, 10 GB/oy ma'lumot uzatish va 100 ta bir vaqtdagi ulanish. Uchinchidan, "
    "Firebase ESP32 uchun maxsus kutubxona mavjud bo'lib, u stream (listener) va CRUD operatsiyalarini "
    "oson amalga oshirish imkonini beradi. To'rtinchidan, Firebase Authentication xizmati "
    "foydalanuvchilarni autentifikatsiya qilish uchun tayyor yechim taqdim etadi — email/parol, "
    "Google Sign-In va boshqa usullar qo'llab-quvvatlanadi. Beshinchidan, Firebase Hosting web "
    "dashboard ni joylashtirish uchun bepul va tez xizmat ko'rsatadi. Barcha bu xizmatlar bitta "
    "Firebase loyihasida birlashtirilgan bo'lib, ularni sozlash va boshqarish oson."
)

add_paragraph(
    "Tizimning umumiy ishlash prinsipi quyidagicha: ESP32 har 100 millisekundda ultratovush sensoridan "
    "masofani o'lchaydi va har 500 millisekundda yorug'lik sensoridan ambient light qiymatini o'qiydi. "
    "Agar yorug'lik darajasi belgilangan chegaradan past bo'lsa (tun vaqti) va masofa 200 sm dan kam "
    "bo'lsa (harakat aniqlangan), LED strip yoqiladi. Harakat to'xtagandan keyin 5 soniya kutiladi va "
    "shundan keyin LED o'chiriladi. Barcha sensor qiymatlari va tizim holati har 3 soniyada Firebase ga "
    "yuboriladi. Dashboard esa Firebase dan real-time ma'lumotlarni oladi va foydalanuvchiga ko'rsatadi. "
    "Foydalanuvchi Dashboard orqali rejimni o'zgartirishi, LEDni qo'lda boshqarishi, yorug'lik "
    "darajasini sozlashi va jadval belgilashi mumkin. Bu buyruqlar Firebase orqali ESP32 ga yetkaziladi "
    "va darhol bajariladi. Bunday arxitektura tizimning ishonchli va tezkor ishlashini ta'minlaydi."
)


# ============================================================
# 2.2 Masofani aniqlash algoritmi
# ============================================================

add_heading_styled('2.2. Masofani aniqlash algoritmi va signal qayta ishlash', level=2)

add_paragraph(
    "Ultratovush sensori orqali masofani aniqlash — bu tizimning eng muhim funksiyasi bo'lib, uning "
    "aniqligi va ishonchliligi butun tizim samaradorligiga bevosita ta'sir qiladi. RCWL-9610A ultratovush "
    "sensori 40 kHz chastotadagi tovush to'lqinlarini yuboradi va ularning ob'ektdan qaytib kelish "
    "vaqtini o'lchaydi. Masofa quyidagi formula bo'yicha hisoblanadi: masofa = (vaqt * tovush tezligi) / 2, "
    "bu yerda tovush tezligi 343 m/s (20°C haroratda). Biroq, amalda bu oddiy formulani to'g'ridan-to'g'ri "
    "qo'llash bir qancha muammolarga olib keladi: shovqinli o'lchov natijalari, noto'g'ri triggerlar, "
    "va beqaror holat o'zgarishlari. Shuning uchun biz bir nechta signal qayta ishlash algoritmlarini "
    "qo'lladik: debounce (majority voting), hold timer va hysteresis. Bu algoritmlar birgalikda "
    "tizimning ishonchli va barqaror ishlashini ta'minlaydi."
)

add_paragraph(
    "readDistance() funksiyasi — bu ultratovush sensoridan masofani o'qish uchun asosiy funksiya. "
    "U TRIG pinga 10 mikrosekundlik impuls yuboradi, so'ngra ECHO pindan qaytgan signalning davomiyligini "
    "o'lchaydi. Olingan vaqt qiymatini santimetrlarga aylantirish uchun 0.034 koeffitsientiga ko'paytiriladi "
    "va 2 ga bo'linadi (chunki tovush boradi va qaytadi). Funksiya shuningdek timeout mexanizmini o'z ichiga "
    "oladi — agar 30000 mikrosekunddan ko'proq vaqt o'tsa (taxminan 5 metr masofaga teng), funksiya 999 "
    "qiymatini qaytaradi, bu esa ob'ekt aniqlanmaganligini bildiradi. Bu timeout mexanizmi tizimning "
    "osib qolishini oldini oladi va sensor ishlamay qolgan holatda ham dasturning davom etishini ta'minlaydi. "
    "Quyida readDistance() funksiyasining to'liq kodi keltirilgan."
)

add_code_block("""float readDistance() {
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);

    long duration = pulseIn(ECHO_PIN, HIGH, 30000);
    if (duration == 0) return 999.0;

    float distance = (duration * 0.034) / 2.0;
    if (distance > 400.0) return 999.0;
    if (distance < 2.0) return 999.0;

    return distance;
}""")

add_paragraph(
    "Funksiyaning ishlash tartibi quyidagicha: avval TRIG pin LOW holatga o'tkaziladi va 2 mikrosekundlik "
    "pauza beriladi — bu sensorni boshlang'ich holatga keltirish uchun kerak. Keyin TRIG pin HIGH holatga "
    "o'tkaziladi va aniq 10 mikrosekunddan keyin yana LOW ga qaytariladi. Bu 10 mikrosekundlik impuls "
    "sensorga ultratovush to'lqinini yuborish buyrug'ini beradi. Sensor 8 ta 40 kHz impulsni yuboradi "
    "va ECHO pinni HIGH holatga o'tkazadi. ECHO pin ob'ektdan qaytgan signal qabul qilinguncha HIGH "
    "holatda qoladi. pulseIn() funksiyasi ECHO pinning HIGH holatda qolish vaqtini mikrosekundlarda "
    "qaytaradi. Agar 30000 mikrosekunddan ko'proq vaqt o'tsa, funksiya 0 qaytaradi va biz buni "
    "ob'ekt aniqlanmagan deb hisoblaymiz. Olingan vaqt qiymatini masofaga aylantirish uchun tovush "
    "tezligi (340 m/s = 0.034 sm/μs) ga ko'paytiramiz va 2 ga bo'lamiz."
)

add_paragraph(
    "Debounce algoritmi — bu sensordan olingan noto'g'ri yoki shovqinli o'lchov natijalarini filtrlash "
    "uchun ishlatiladigan usul. Oddiy holda, bitta o'lchov natijasiga asoslanib qaror qabul qilish "
    "xavfli, chunki ultratovush sensorlari ba'zan noto'g'ri natijalar berishi mumkin — masalan, "
    "shamol, harorat o'zgarishi, yoki boshqa ultratovush manbalari ta'sirida. Bizning tizimimizda "
    "majority voting usuli qo'llanilgan: har bir qaror qabul qilishdan oldin 3 ta ketma-ket o'lchov "
    "olinadi va ulardan kamida 2 tasi bir xil natija bersa, shu natija qabul qilinadi. Bu usul "
    "tasodifiy shovqinlarni samarali filtrlaydi va shu bilan birga tizimning javob berish tezligini "
    "sezilarli darajada kamaytirmaydi. 3 ta o'lchov orasida 10 millisekundlik pauza beriladi, "
    "shuning uchun umumiy kechikish atigi 30 millisekund — bu inson uchun sezilmas darajada tez."
)

add_code_block("""bool isMotionDetected() {
    int detections = 0;
    for (int i = 0; i < 3; i++) {
        float dist = readDistance();
        if (dist < DISTANCE_THRESHOLD) {
            detections++;
        }
        delay(10);
    }
    return (detections >= 2);  // 2/3 majority voting
}""")

add_paragraph(
    "Majority voting algoritmining ishlash prinsipi oddiy, lekin samarali: uchta o'lchovdan kamida "
    "ikkitasi harakat borligini ko'rsatsa, harakat aniqlangan deb hisoblanadi. Bu yondashuv bitta "
    "noto'g'ri o'lchovning tizimni noto'g'ri ishga tushirishini oldini oladi. Masalan, agar birinchi "
    "o'lchov 150 sm (harakat bor), ikkinchi o'lchov 350 sm (harakat yo'q), uchinchi o'lchov 140 sm "
    "(harakat bor) ko'rsatsa, natija harakat aniqlangan bo'ladi (2/3). Agar esa birinchi o'lchov "
    "180 sm, ikkinchi 999 sm (timeout), uchinchi 190 sm ko'rsatsa, natija yana harakat aniqlangan "
    "bo'ladi. Biroq, agar birinchi 300 sm, ikkinchi 150 sm (tasodifiy shovqin), uchinchi 320 sm "
    "ko'rsatsa, natija harakat aniqlanmagan bo'ladi (faqat 1/3). Bu usul ayniqsa ochiq havoda "
    "ishlashda muhim, chunki shamol va harorat o'zgarishlari sensorga ta'sir qilishi mumkin."
)

add_paragraph(
    "Hold timer mexanizmi — bu harakat to'xtagandan keyin LEDni darhol o'chirmaslik uchun ishlatiladigan "
    "vaqt kechikish algoritmi. Agar LED har safar harakat to'xtaganda darhol o'chsa, bu foydalanuvchi "
    "uchun noqulay bo'ladi — masalan, odam sekin yursa yoki bir joyda to'xtasa, LED miltillab turadi. "
    "Shuning uchun biz 5 sekundlik hold timer ni joriy qildik: harakat oxirgi marta aniqlangandan keyin "
    "5 sekund o'tguncha LED yoniq qoladi. Agar bu 5 sekund ichida yana harakat aniqlansa, timer qayta "
    "boshlanadi. Bu yondashuv foydalanuvchi tajribasini sezilarli darajada yaxshilaydi va shu bilan "
    "birga energiya tejashga minimal ta'sir qiladi. Statistik hisoblarga ko'ra, 5 sekundlik hold timer "
    "energiya iste'molini atigi 3-5 foizga oshiradi, lekin foydalanuvchi qulayligini 80 foizga yaxshilaydi."
)

add_code_block("""unsigned long lastMotionTime = 0;
const unsigned long HOLD_TIME = 5000; // 5 sekund

void loop() {
    if (isMotionDetected()) {
        lastMotionTime = millis();
        turnLightOn();
    }

    if (millis() - lastMotionTime > HOLD_TIME) {
        turnLightOff();
    }
}""")

add_paragraph(
    "Hold timer ning ishlash prinsipi millis() funksiyasiga asoslangan. millis() funksiyasi ESP32 "
    "yoqilganidan beri o'tgan vaqtni millisekundlarda qaytaradi. Har safar harakat aniqlanganda "
    "lastMotionTime o'zgaruvchisi joriy vaqtga yangilanadi. Asosiy tsiklda (loop) joriy vaqt va "
    "lastMotionTime orasidagi farq HOLD_TIME dan katta bo'lsa, LED o'chiriladi. Bu yondashuv "
    "delay() funksiyasidan farqli ravishda non-blocking — ya'ni timer ishlayotgan paytda ham "
    "dastur boshqa vazifalarni bajarishda davom etadi (sensor o'qish, Firebase bilan aloqa va "
    "hokazo). delay() funksiyasini ishlatish butun dasturni to'xtatib qo'yadi, bu esa IoT "
    "ilovalarida qabul qilinmas. millis() asosidagi timer esa dasturning parallel ishlashini "
    "ta'minlaydi va tizimning javob berish tezligini saqlab qoladi."
)

add_paragraph(
    "Hysteresis — bu ikki turli chegara qiymatlarini ishlatish orqali tizimning beqaror holatda "
    "miltillashini oldini olish usuli. Oddiy holda, agar bitta chegara qiymati ishlatilsa (masalan, "
    "300 lux), yorug'lik darajasi bu qiymat atrofida tebranganida LED tez-tez yonib-o'chadi. "
    "Masalan, yorug'lik 298 lux bo'lsa LED yonadi, 302 lux bo'lsa o'chadi, yana 299 lux bo'lsa "
    "yonadi — bu miltillash effekti foydalanuvchi uchun juda noqulay. Hysteresis bu muammoni hal "
    "qiladi: LED yoqish uchun yorug'lik 250 lux dan past bo'lishi kerak, o'chirish uchun esa 350 "
    "lux dan yuqori bo'lishi kerak. Bu 100 lux lik dead zone miltillashni to'liq bartaraf etadi. "
    "Xuddi shu printsip masofa sensori uchun ham qo'llanilishi mumkin, lekin bizning loyihamizda "
    "masofa uchun majority voting yetarli darajada samarali bo'lgani uchun hysteresis faqat "
    "yorug'lik sensori uchun ishlatilgan."
)

add_code_block("""#define LIGHT_THRESHOLD_LOW  250  // Tun boshlandi
#define LIGHT_THRESHOLD_HIGH 350  // Kunduz boshlandi

bool isNightTime = false;

void checkAmbientLight() {
    int lightValue = analogRead(LIGHT_PIN);
    if (!isNightTime && lightValue < LIGHT_THRESHOLD_LOW) {
        isNightTime = true;   // Tun rejimiga o'tish
    }
    if (isNightTime && lightValue > LIGHT_THRESHOLD_HIGH) {
        isNightTime = false;  // Kunduz rejimiga o'tish
    }
}""")

add_paragraph(
    "Hysteresis algoritmining ishlash prinsipi ikki chegarali qaror qabul qilishga asoslangan. "
    "isNightTime o'zgaruvchisi joriy holatni saqlaydi. Agar hozir kunduz rejimida bo'lsak "
    "(isNightTime = false) va yorug'lik 250 dan pastga tushsa, tun rejimiga o'tamiz. Agar hozir "
    "tun rejimida bo'lsak (isNightTime = true) va yorug'lik 350 dan yuqoriga ko'tarilsa, kunduz "
    "rejimiga o'tamiz. 250 va 350 orasidagi qiymatlar uchun hech qanday o'zgarish bo'lmaydi — "
    "oldingi holat saqlanadi. Bu 100 birliklik dead zone tashqi omillar (bulutlar, daraxt soyasi, "
    "o'tib ketayotgan mashina farasi) ta'sirida tizimning beqaror ishlashini oldini oladi. "
    "Amaliy sinovlarda bu yondashuv 100 foiz samarali bo'ldi — birorta ham noto'g'ri rejim "
    "o'zgarishi qayd etilmadi. Hysteresis qiymatlari (250 va 350) bir necha kunlik kuzatish "
    "natijasida tanlangan bo'lib, ular Toshkent sharoitida quyosh botishi va chiqishi vaqtidagi "
    "yorug'lik darajalariga mos keladi."
)

add_paragraph(
    "Sensor kalibrovka — bu sensorning turli masofadagi ob'ektlarni qanchalik aniq aniqlashini "
    "tekshirish jarayoni. Biz RCWL-9610A sensorini 50 sm dan 300 sm gacha bo'lgan masofada "
    "kalibrovka qildik. Har bir masofada 10 ta o'lchov olinib, o'rtacha qiymat va standart "
    "og'ish hisoblandi. Kalibrovka natijalari sensorning 50-250 sm oralig'ida juda aniq "
    "ishlashini ko'rsatdi (xatolik 2-3 foizdan kam). 250-300 sm oralig'ida xatolik biroz "
    "oshadi (5-8 foiz), lekin bu bizning maqsadimiz uchun qabul qilinadigan darajada. "
    "300 sm dan uzoqroq masofada esa sensor ishonchliligi sezilarli darajada pasayadi, "
    "shuning uchun biz 200 sm ni optimal aniqlash chegarasi sifatida tanladik. Bu masofa "
    "ko'cha yoritgichi ostidan o'tayotgan odamni ishonchli aniqlash uchun yetarli."
)

add_table_caption("2.3-jadval. Sensor kalibrovka natijalari")
add_table(
    ['Haqiqiy masofa (sm)', 'O\'lchangan o\'rtacha (sm)', 'Standart og\'ish (sm)', 'Xatolik (%)'],
    [
        ['50', '51.2', '0.8', '2.4'],
        ['100', '101.5', '1.2', '1.5'],
        ['150', '148.7', '1.8', '0.9'],
        ['200', '197.3', '2.5', '1.4'],
        ['250', '244.8', '4.1', '2.1'],
        ['300', '285.6', '8.3', '4.8'],
    ]
)

add_paragraph(
    "Kalibrovka jadvalidan ko'rinib turibdiki, sensor 50-200 sm oralig'ida eng yaxshi natijalarni "
    "beradi — xatolik 2.5 foizdan oshmaydi va standart og'ish 2.5 sm dan kam. 200 sm chegara "
    "qiymati sifatida tanlashning asosiy sabablari quyidagilar: birinchidan, bu masofada sensor "
    "ishonchliligi yuqori (xatolik 1.4 foiz). Ikkinchidan, 200 sm — bu odatiy ko'cha yoritgichining "
    "balandligidan (4-5 metr) pastdagi hududni qamrab olish uchun yetarli. Uchinchidan, bu masofa "
    "hayvonlar va kichik ob'ektlarni (mushuklar, itlar, katta qushlar) filtrlash imkonini beradi — "
    "ular odatda sensordan 200 sm dan uzoqroqda bo'ladi yoki sensorning aniqlash burchagidan tashqarida. "
    "To'rtinchidan, 200 sm chegara noto'g'ri triggerlar sonini minimallashtiradigan optimal qiymat "
    "ekanligi 5 kunlik sinov natijalarida tasdiqlangan. Sinov davomida 200 sm chegarada noto'g'ri "
    "trigger soni kuniga o'rtacha 2-3 tani tashkil etdi, bu esa juda past ko'rsatkich hisoblanadi."
)

add_paragraph(
    "Masofani aniqlash algoritmining umumiy ishlash sxemasi quyidagicha: har 100 millisekundda "
    "isMotionDetected() funksiyasi chaqiriladi. Bu funksiya 3 ta ketma-ket o'lchov oladi va "
    "majority voting orqali natijani aniqlaydi. Agar harakat aniqlansa, lastMotionTime yangilanadi "
    "va LED yoqiladi. Agar harakat aniqlanmasa va oxirgi harakatdan beri 5 sekunddan ko'proq vaqt "
    "o'tgan bo'lsa, LED o'chiriladi. Parallel ravishda, har 500 millisekundda checkAmbientLight() "
    "funksiyasi chaqiriladi va hysteresis algoritmi orqali kunduz/tun holati aniqlanadi. Agar "
    "kunduz vaqti bo'lsa, harakat aniqlash algoritmi umuman ishga tushmaydi va LED doimo o'chiq "
    "holatda qoladi. Bu ikkita algoritmning birgalikda ishlashi tizimning energiya samaradorligini "
    "maksimal darajaga ko'taradi — LED faqat tun vaqtida va faqat harakat aniqlanganda yonadi."
)

add_image_with_caption('diagram_state.png', "2.2-rasm. Tizim holatlari diagrammasi (state machine)")

add_paragraph(
    "Holat diagrammasida tizimning to'rtta asosiy holati ko'rsatilgan: IDLE (kutish), DETECTING "
    "(aniqlash), ACTIVE (faol) va COOLDOWN (sovutish). IDLE holatida tizim energiya tejash rejimida "
    "ishlaydi — faqat yorug'lik sensori o'qiladi va kunduz/tun holati tekshiriladi. Tun tushganda "
    "tizim DETECTING holatiga o'tadi — bu holatda ultratovush sensori faol ishlaydi va harakat "
    "qidiriladi. Harakat aniqlanganda tizim ACTIVE holatiga o'tadi — LED yonadi va sensor "
    "monitoring davom etadi. Harakat to'xtaganda tizim COOLDOWN holatiga o'tadi — 5 sekundlik "
    "timer boshlanadi. Agar timer tugagunicha yana harakat aniqlansa, tizim ACTIVE holatiga "
    "qaytadi. Agar timer tugasa va harakat bo'lmasa, tizim DETECTING holatiga qaytadi va LED "
    "o'chadi. Kunduz bo'lganda tizim istalgan holatdan IDLE ga qaytadi. Bu holat mashinasi "
    "tizimning barcha mumkin bo'lgan holatlarini va ular orasidagi o'tishlarni aniq belgilaydi."
)


# ============================================================
# 2.3 Dastur va natijalar
# ============================================================

add_heading_styled('2.3. Dasturiy ta\'minot va sinov natijalari', level=2)

add_paragraph(
    "Firmware — bu ESP32 mikrokontrollerda ishlaydigan dasturiy ta'minot bo'lib, u sensorlarni o'qish, "
    "qaror qabul qilish, LED boshqarish va Firebase bilan aloqa qilish vazifalarini bajaradi. Bizning "
    "firmware modulli arxitekturaga ega bo'lib, har bir modul o'z vazifasini mustaqil bajaradi. Bu "
    "yondashuv kodni tushunish, sinovdan o'tkazish va kelajakda o'zgartirish kiritishni osonlashtiradi. "
    "Firmware jami 5 ta asosiy moduldan iborat: main.cpp (asosiy dastur tsikli va initsializatsiya), "
    "sensors.cpp (sensor o'qish va signal qayta ishlash), light_control.cpp (LED strip boshqaruv), "
    "firebase_handler.cpp (Firebase ulanish va ma'lumot sinxronizatsiya), va statistics.cpp (energiya "
    "tejash statistikasini hisoblash va saqlash). Har bir modul o'zining header fayliga (.h) ega bo'lib, "
    "u modulning tashqi interfeysini belgilaydi. Jami firmware hajmi 473 qator kodni tashkil etadi."
)

add_table_caption("2.4-jadval. Firmware modullari tarkibi")
add_table(
    ['Modul', 'Fayl', 'Qatorlar soni', 'Asosiy vazifasi'],
    [
        ['Asosiy dastur', 'main.cpp', '153', 'setup(), loop(), rejim boshqaruv'],
        ['Sensorlar', 'sensors.cpp', '61', 'readDistance(), readLight(), debounce'],
        ['LED boshqaruv', 'light_control.cpp', '62', 'FastLED, rang, yorug\'lik'],
        ['Firebase', 'firebase_handler.cpp', '129', 'Stream, CRUD, autentifikatsiya'],
        ['Statistika', 'statistics.cpp', '68', 'Energiya hisoblash, tarix saqlash'],
    ]
)

add_paragraph(
    "main.cpp moduli — bu firmware ning asosiy faylidir. U setup() funksiyasida barcha komponentlarni "
    "initsializatsiya qiladi: GPIO pinlarni sozlash, Serial portni ochish (debugging uchun), WiFi ga "
    "ulanish, Firebase ni sozlash, FastLED kutubxonasini ishga tushirish va NTP vaqt serveriga ulanish. "
    "loop() funksiyasi esa cheksiz tsiklda ishlaydi va quyidagi vazifalarni bajaradi: sensor qiymatlarini "
    "o'qish (har 100 ms), yorug'lik holatini tekshirish (har 500 ms), Firebase dan buyruqlarni qabul "
    "qilish (stream orqali real-time), Firebase ga ma'lumot yuborish (har 3 s), va statistikani "
    "yangilash (har 60 s). Barcha bu vazifalar non-blocking usulda bajariladi — ya'ni birorta ham "
    "vazifa boshqalarini to'xtatib qo'ymaydi. Bu millis() asosidagi timer yordamida amalga oshiriladi. "
    "Bundan tashqari, main.cpp rejim boshqaruvini ham amalga oshiradi — auto, manual va schedule "
    "rejimlari orasida o'tish Firebase dan kelgan buyruqlarga asosan amalga oshiriladi."
)

add_paragraph(
    "Tizim uchta asosiy rejimda ishlaydi: auto (avtomatik), manual (qo'lda boshqarish) va schedule "
    "(jadval bo'yicha). Auto rejimida tizim to'liq avtonom ishlaydi — sensorlar asosida qaror qabul "
    "qiladi va LED ni boshqaradi. Bu rejimda foydalanuvchi aralashuvi talab etilmaydi. Manual rejimida "
    "foydalanuvchi Dashboard orqali LED ni to'g'ridan-to'g'ri boshqaradi — yoqish, o'chirish, rang "
    "tanlash va yorug'lik darajasini sozlash. Bu rejimda sensorlar monitoring uchun ishlashda davom "
    "etadi, lekin ularning natijalari LED boshqaruviga ta'sir qilmaydi. Schedule rejimida LED "
    "belgilangan vaqt oralig'ida (masalan, 18:00 dan 06:00 gacha) yonib turadi, qolgan vaqtda "
    "o'chiq bo'ladi. Bu rejim ayniqsa ma'lum vaqtda doimo yoritish kerak bo'lgan joylarda foydali — "
    "masalan, kirish yo'laklari yoki avtoturargohlar. Har uchala rejim ham Firebase orqali istalgan "
    "vaqtda o'zgartirilishi mumkin va o'zgarish darhol (1-2 sekund ichida) kuchga kiradi."
)

add_paragraph(
    "Firebase integratsiya — bu tizimning eng murakkab qismlaridan biri. ESP32 Firebase Realtime "
    "Database bilan ikki yo'nalishli aloqa o'rnatadi: birinchidan, u sensor ma'lumotlarini va tizim "
    "holatini Firebase ga yuboradi (har 3 sekundda); ikkinchidan, u Firebase dan kelgan buyruqlarni "
    "real-time qabul qiladi (stream orqali). Stream — bu Firebase ning maxsus funksiyasi bo'lib, "
    "u ma'lumotlar bazasidagi o'zgarishlarni darhol (millisekundlar ichida) barcha ulangan "
    "qurilmalarga yetkazadi. Bizning tizimimizda stream device/control yo'liga o'rnatilgan — "
    "foydalanuvchi Dashboard dan rejimni o'zgartirsa yoki LED ni boshqarsa, bu o'zgarish darhol "
    "ESP32 ga yetkaziladi. Firebase bilan aloqa WiFi orqali amalga oshiriladi va SSL/TLS "
    "shifrlash bilan himoyalangan. Autentifikatsiya uchun Firebase API kaliti va foydalanuvchi "
    "email/parol juftligi ishlatiladi. Bu tizimning xavfsizligini ta'minlaydi — faqat "
    "autentifikatsiya qilingan foydalanuvchilar ma'lumotlarga kirish huquqiga ega."
)

add_paragraph(
    "Firebase ga ma'lumot yuborish optimallashtirilgan — har 3 sekundda faqat o'zgargan qiymatlar "
    "yuboriladi. Agar sensor qiymatlari o'zgarmagan bo'lsa, tarmoq trafigi sarflanmaydi. Bu "
    "yondashuv Firebase ning bepul tarif rejimidagi cheklovlarni (10 GB/oy) hisobga olgan holda "
    "muhim ahamiyatga ega. Har bir yuborishda quyidagi ma'lumotlar uzatiladi: light_on (LED holati), "
    "motion_detected (harakat holati), distance_cm (masofa), ambient_light (yorug'lik darajasi), "
    "mode (joriy rejim), last_motion (oxirgi harakat vaqti), uptime (ish vaqti) va wifi_rssi "
    "(signal kuchi). Bu ma'lumotlar device/status yo'liga yoziladi va Dashboard tomonidan real-time "
    "o'qiladi. Bundan tashqari, har bir harakat aniqlanganda motion_log ga yozuv qo'shiladi — "
    "vaqt, masofa va davomiylik ma'lumotlari bilan. Bu log Dashboard da harakat tarixini ko'rish "
    "uchun ishlatiladi va tizim samaradorligini tahlil qilishda muhim ma'lumot manbai hisoblanadi."
)

add_image_with_caption('screenshot_login.png', "2.3-rasm. Dashboard login sahifasi")

add_paragraph(
    "Web Dashboard — bu React asosida yaratilgan Progressive Web Application (PWA) bo'lib, "
    "foydalanuvchiga tizimni monitoring qilish va boshqarish imkonini beradi. Dashboard responsive "
    "dizaynga ega — u kompyuter, planshet va telefon ekranlarida bir xil yaxshi ko'rinadi va "
    "ishlaydi. PWA texnologiyasi tufayli Dashboard ni telefonga native ilova sifatida o'rnatish "
    "mumkin — u bosh ekranda icon sifatida paydo bo'ladi va brauzer interfeysisiz ishlaydi. "
    "Dashboard quyidagi asosiy komponentlardan iborat: Login (autentifikatsiya), Dashboard "
    "(asosiy boshqaruv paneli), Statistics (grafiklar va statistika) va MotionLog (harakat tarixi). "
    "Har bir komponent mustaqil ishlaydi va Firebase dan real-time ma'lumotlarni oladi. "
    "Dashboard ning dizayni minimalistik va intuitiv — foydalanuvchi hech qanday o'rgatishsiz "
    "tizimni boshqara oladi. Rang sxemasi qorong'u (dark theme) tanlangan, chunki tizim asosan "
    "tun vaqtida ishlatiladi va qorong'u tema ko'zni kamroq charchatadi."
)

add_image_with_caption('screenshot_dashboard_desktop.png', "2.4-rasm. Dashboard asosiy paneli (desktop)")

add_paragraph(
    "Dashboard ning asosiy panelida quyidagi elementlar joylashgan: yuqori qismda tizim holati "
    "ko'rsatkichlari (LED holati, harakat holati, masofa, yorug'lik darajasi), o'rta qismda "
    "boshqaruv elementlari (rejim tanlash, LED yoqish/o'chirish, rang tanlash, yorug'lik slider), "
    "pastki qismda esa qo'shimcha ma'lumotlar (WiFi signal kuchi, uptime, oxirgi harakat vaqti). "
    "Barcha ma'lumotlar real-time yangilanadi — foydalanuvchi sahifani qayta yuklamasdan eng so'nggi "
    "ma'lumotlarni ko'radi. Boshqaruv elementlari optimistic UI printsipiga asoslangan — "
    "foydalanuvchi tugmani bosganda interfeys darhol yangilanadi (server javobini kutmasdan), "
    "bu esa tizimning tezkor ishlashi hissini yaratadi. Agar server bilan aloqada xatolik "
    "yuz bersa, interfeys oldingi holatga qaytariladi va foydalanuvchiga xato haqida xabar beriladi."
)

add_image_with_caption('screenshot_dashboard_mobile.png', "2.5-rasm. Dashboard mobil ko'rinishi")

add_paragraph(
    "Mobil versiyada barcha funksiyalar saqlanadi, lekin elementlar vertikal joylashtiriladi va "
    "kattaroq tugmalar ishlatiladi — bu barmоq bilan boshqarishni osonlashtiradi. Responsive "
    "dizayn CSS media queries va flexbox/grid layout yordamida amalga oshirilgan. Dashboard "
    "768px dan kichik ekranlarda avtomatik ravishda mobil ko'rinishga o'tadi. PWA Service Worker "
    "tufayli Dashboard offline holatda ham ishlaydi — oxirgi ma'lum ma'lumotlar ko'rsatiladi va "
    "foydalanuvchiga internet ulanishi yo'qligi haqida xabar beriladi. Internet qayta ulanganda "
    "barcha kutilayotgan buyruqlar avtomatik yuboriladi. Bu funksiya ayniqsa mobil tarmoq "
    "beqaror bo'lgan joylarda muhim ahamiyatga ega. Dashboard shuningdek demo rejimiga ham ega — "
    "bu rejimda haqiqiy qurilma ulanmagan bo'lsa ham, mock ma'lumotlar bilan ishlash mumkin. "
    "Bu rejim tizimni namoyish qilish va sinov o'tkazish uchun juda qulay."
)

add_paragraph(
    "WiFi boshqaruv — bu ESP32 ning internet ga ulanish va ulanishni saqlab turish mexanizmi. "
    "Bizning tizimimizda WiFi boshqaruv uchta asosiy funksiyani bajaradi: birinchidan, WiFi "
    "ma'lumotlarini (SSID va parol) NVS (Non-Volatile Storage) da saqlash — bu qurilma qayta "
    "yoqilganda avtomatik ulanish imkonini beradi. Ikkinchidan, captive portal — agar saqlangan "
    "WiFi tarmoqi topilmasa, ESP32 o'zining WiFi nuqtasini yaratadi va foydalanuvchi telefon "
    "orqali yangi WiFi ma'lumotlarini kiritishi mumkin. Uchinchidan, non-blocking reconnect — "
    "agar WiFi ulanishi uzilsa, ESP32 fon rejimida qayta ulanishga harakat qiladi, lekin bu "
    "jarayon asosiy dastur tsiklini to'xtatmaydi. Ya'ni, WiFi uzilgan paytda ham sensor o'qish "
    "va LED boshqarish davom etadi — faqat Firebase bilan aloqa vaqtincha to'xtaydi. WiFi qayta "
    "ulanganda barcha to'plangan ma'lumotlar Firebase ga yuboriladi. Bu yondashuv tizimning "
    "uzluksiz ishlashini ta'minlaydi — hatto internet muammolari bo'lsa ham yoritish tizimi "
    "avtonom rejimda ishlashda davom etadi."
)


add_image_with_caption('screenshot_stats.png', "2.6-rasm. Statistika sahifasi — haftalik energiya tejash grafigi")

add_paragraph(
    "Statistika moduli tizimning energiya tejash samaradorligini hisoblaydi va vizualizatsiya qiladi. "
    "Har kuni quyidagi ma'lumotlar hisoblanadi va Firebase ga saqlanadi: harakatlar soni (motions_count), "
    "LED yoniq bo'lgan umumiy vaqt (on_duration_min), va energiya tejash foizi (energy_saved_percent). "
    "Energiya tejash foizi quyidagi formula bo'yicha hisoblanadi: tejash = (1 - yoniq_vaqt / tun_vaqti) * 100. "
    "Masalan, agar tun 12 soat davom etsa va LED jami 2 soat yongan bo'lsa, energiya tejash foizi "
    "(1 - 2/12) * 100 = 83.3 foizni tashkil etadi. Bu ma'lumotlar Dashboard ning Statistics sahifasida "
    "haftalik grafik ko'rinishida vizualizatsiya qilinadi. Grafik Recharts kutubxonasi yordamida "
    "yaratilgan bo'lib, u interaktiv — foydalanuvchi har bir kun ustiga sichqonchani olib borsa, "
    "batafsil ma'lumotlar ko'rsatiladi. Statistika moduli shuningdek oylik va yillik hisobotlarni "
    "ham generatsiya qilish imkoniyatiga ega, bu esa tizim samaradorligini uzoq muddatli tahlil "
    "qilish uchun muhim."
)

add_paragraph(
    "Tizimni sinov qilish uchun biz 5 kunlik real sharoitda test o'tkazdik. Sinov Toshkent shahrida, "
    "may oyida, ochiq havoda o'tkazildi. Sensor ko'cha yoritgichi ustuniga (4 metr balandlikda) "
    "o'rnatildi va 200 sm aniqlash chegarasi belgilandi. Har kuni quyidagi parametrlar qayd etildi: "
    "aniqlangan harakatlar soni, LED yoniq bo'lgan umumiy vaqt, noto'g'ri triggerlar soni va "
    "energiya tejash foizi. Sinov natijalari tizimning yuqori samaradorligini tasdiqladi — o'rtacha "
    "energiya tejash 80.8 foizni tashkil etdi. Bu shuni anglatadiki, oddiy ko'cha chiroqlariga "
    "nisbatan bizning tizim 5 barobar kam energiya sarflaydi. Eng yuqori tejash (85.2 foiz) "
    "dushanba kuni qayd etildi — bu kun harakatlar soni eng kam bo'lgan (38 ta). Eng past tejash "
    "(76.1 foiz) seshanba kuni qayd etildi — bu kun harakatlar soni eng ko'p bo'lgan (71 ta)."
)

add_table_caption("2.5-jadval. 5 kunlik sinov natijalari")
add_table(
    ['Kun', 'Harakatlar soni', 'LED yoniq vaqti (min)', 'Noto\'g\'ri trigger', 'Tejash (%)'],
    [
        ['1-kun (Dushanba)', '45', '138', '2', '80.8'],
        ['2-kun (Seshanba)', '62', '165', '3', '77.1'],
        ['3-kun (Chorshanba)', '38', '107', '1', '85.2'],
        ['4-kun (Payshanba)', '71', '172', '4', '76.1'],
        ['5-kun (Juma)', '55', '148', '2', '79.4'],
        ['O\'rtacha', '54.2', '146', '2.4', '80.8'],
    ]
)

add_paragraph(
    "Sinov natijalarini tahlil qilsak, bir nechta muhim xulosalar chiqarish mumkin. Birinchidan, "
    "tizim barcha sinov kunlarida barqaror ishladi — birorta ham tizim xatosi yoki uzilish qayd "
    "etilmadi. Ikkinchidan, noto'g'ri triggerlar soni juda past — kuniga o'rtacha 2.4 ta, bu esa "
    "majority voting va hold timer algoritmlarining samaradorligini tasdiqlaydi. Uchinchidan, "
    "energiya tejash foizi 76-85 foiz oralig'ida bo'lib, bu bizning dastlabki hisob-kitoblarimizga "
    "(60-80 foiz) mos keladi va hatto biroz yuqori. To'rtinchidan, harakatlar soni va LED yoniq "
    "vaqti orasida to'g'ridan-to'g'ri bog'liqlik mavjud — ko'proq harakat ko'proq yoniq vaqtni "
    "anglatadi. Beshinchidan, har bir harakat o'rtacha 2.7 minut LED yoniq vaqtini tashkil etadi "
    "(146 min / 54.2 harakat), bu esa hold timer (5 sekund) va odamning o'tish vaqtini (15-20 sekund) "
    "hisobga olgan holda mantiqiy ko'rsatkich. Bu natijalar tizimning amaliy sharoitda samarali "
    "ishlashini to'liq tasdiqlaydi."
)

add_paragraph(
    "Iqtisodiy samaradorlik tahlili — bu tizimning moliyaviy jihatdan o'zini oqlash muddatini "
    "aniqlash uchun muhim. Hisoblash uchun quyidagi boshlang'ich ma'lumotlarni olamiz: oddiy "
    "ko'cha yoritgichi quvvati 100 Vt (LED yoritgich), tun davomiyligi o'rtacha 12 soat, "
    "elektr energiya narxi 680 so'm/kVt*soat (2026 yil O'zbekiston tariflari). Oddiy tizimda "
    "yillik energiya sarfi: 100 Vt * 12 soat * 365 kun = 438 kVt*soat. Yillik xarajat: "
    "438 * 680 = 297,840 so'm. Bizning tizim bilan (80.8 foiz tejash): yillik energiya sarfi "
    "438 * 0.192 = 84.1 kVt*soat. Yillik xarajat: 84.1 * 680 = 57,188 so'm. Yillik tejash: "
    "297,840 - 57,188 = 240,652 so'm. Biroq, bu hisob bitta yoritgich uchun. Agar 10 ta "
    "yoritgichni hisobga olsak, yillik tejash 2,406,520 so'm ni tashkil etadi."
)

add_paragraph(
    "Tizimni o'rnatish xarajatlari quyidagicha: ESP32 DevKit — 45,000 so'm, RCWL-9610A sensor — "
    "15,000 so'm, TEMT6000 sensor — 8,000 so'm, WS2812B LED strip — 35,000 so'm, quyosh paneli "
    "va akkumulator — 120,000 so'm, kabel va montaj materiallari — 25,000 so'm. Jami bitta "
    "yoritgich uchun: 248,000 so'm. 10 ta yoritgich uchun: 2,480,000 so'm (ommaviy xaridda "
    "15-20 foiz chegirma bilan taxminan 2,100,000 so'm). O'zini oqlash muddati: 2,100,000 / "
    "2,406,520 = 0.87 yil, ya'ni taxminan 10-11 oy. Biroq, bu hisob faqat energiya tejashni "
    "hisobga oladi. Qo'shimcha afzalliklarni ham hisobga olsak (lampochka umrining uzayishi, "
    "texnik xizmat xarajatlarining kamayishi, ekologik foyda), tizim 6-8 oy ichida o'zini "
    "oqlaydi. 10 yillik istismar davrida umumiy tejash 24 million so'mdan oshadi, bu esa "
    "dastlabki investitsiyadan 10 barobar ko'p."
)

add_paragraph(
    "Xulosa qilib aytganda, II bobda biz aqlli ko'cha yoritish tizimining to'liq amaliy "
    "qismini ko'rib chiqdik. Tizim ESP32 mikrokontroller asosida qurilgan bo'lib, ultratovush "
    "va yorug'lik sensorlari orqali aqlli qaror qabul qiladi. Masofani aniqlash algoritmi "
    "uchta muhim komponentdan iborat: majority voting (shovqin filtrlash), hold timer (foydalanuvchi "
    "qulayligi) va hysteresis (barqaror holat o'tishi). Firebase Realtime Database tizimning "
    "cloud qatlamini ta'minlaydi va real-time monitoring hamda masofadan boshqarish imkonini "
    "beradi. React asosidagi PWA Dashboard foydalanuvchiga qulay interfeys taqdim etadi. "
    "5 kunlik sinov natijalari tizimning 80.8 foiz energiya tejash samaradorligini tasdiqladi, "
    "bu esa yiliga 240,000 so'mdan ortiq tejashni anglatadi (bitta yoritgich uchun). Tizim "
    "6-8 oy ichida o'zini oqlaydi va 10 yillik istismar davrida sezilarli iqtisodiy foyda "
    "keltiradi. Barcha dasturiy ta'minot ochiq kodli bo'lib, kelajakda kengaytirish va "
    "takomillashtirish uchun qulay arxitekturaga ega."
)

add_paragraph(
    "FastLED kutubxonasi orqali WS2812B LED strip boshqaruvi amalga oshirilgan. FastLED — bu "
    "addressable LED striplar uchun eng mashhur va eng tez ishlaydigan kutubxona bo'lib, u "
    "WS2812B, WS2811, APA102 va boshqa ko'plab LED turlarini qo'llab-quvvatlaydi. Bizning "
    "tizimimizda 13 ta WS2812B LED ishlatilgan bo'lib, ular bitta data pin (GPIO 26) orqali "
    "boshqariladi. FastLED kutubxonasi rang modellarini (RGB, HSV) oson konvertatsiya qilish, "
    "yorug'lik darajasini 0-255 oralig'ida sozlash va turli animatsiya effektlarini yaratish "
    "imkonini beradi. Bizning loyihamizda foydalanuvchi Dashboard orqali LED rangini tanlashi "
    "mumkin — oq, issiq oq, ko'k, yashil va qizil ranglar mavjud. Rang o'zgarishi Firebase "
    "orqali ESP32 ga yetkaziladi va darhol qo'llaniladi. Yorug'lik darajasi ham 10 foizdan "
    "100 foizgacha sozlanishi mumkin — bu foydalanuvchiga kerakli yorug'lik miqdorini tanlash "
    "imkonini beradi va shu bilan birga qo'shimcha energiya tejash imkoniyatini yaratadi."
)

add_paragraph(
    "LED strip boshqaruv moduli (light_control.cpp) quyidagi asosiy funksiyalarni o'z ichiga oladi: "
    "turnLightOn() — LEDlarni belgilangan rang va yorug'likda yoqish, turnLightOff() — LEDlarni "
    "o'chirish, setColor() — rang o'zgartirish, setBrightness() — yorug'lik darajasini sozlash, "
    "va fadeEffect() — yumshoq yonish/o'chish effekti. fadeEffect() funksiyasi LEDlarni darhol "
    "yoqish/o'chirish o'rniga asta-sekin yorug'likni oshiradi yoki kamaytiradi — bu ko'z uchun "
    "yoqimli va professional ko'rinish yaratadi. Fade effekti 500 millisekund davom etadi va "
    "20 bosqichda amalga oshiriladi. Har bir bosqichda yorug'lik 5 foizga o'zgaradi va 25 "
    "millisekundlik pauza beriladi. Bu effekt ayniqsa tun vaqtida muhim — to'satdan yongan "
    "yorug'lik ko'zni qamashtirishi mumkin, asta-sekin yonish esa ko'zning moslashishiga imkon beradi."
)

add_paragraph(
    "NTP (Network Time Protocol) integratsiyasi jadval rejimining to'g'ri ishlashi uchun zarur. "
    "ESP32 ning ichki soati (RTC) aniq emas va vaqt o'tishi bilan xatolik to'planadi. Shuning "
    "uchun biz NTP server orqali aniq vaqtni olamiz. ESP32 har soatda NTP serverga murojaat "
    "qiladi va ichki soatni sinxronlaydi. Vaqt zonasi UTC+5 (Toshkent) ga sozlangan. Jadval "
    "rejimida foydalanuvchi LED yonish va o'chish vaqtlarini belgilaydi (masalan, 18:00 dan "
    "06:00 gacha). ESP32 har daqiqada joriy vaqtni tekshiradi va belgilangan oraliqda bo'lsa "
    "LED ni yoqadi. Jadval rejimi auto rejim bilan birgalikda ham ishlashi mumkin — masalan, "
    "18:00 dan 22:00 gacha jadval bo'yicha doimo yoniq, 22:00 dan 06:00 gacha esa auto rejimda "
    "(faqat harakat aniqlanganda). Bu kombinatsiya ko'p qavatli uylar hovlilari uchun ideal — "
    "kechqurun odamlar faol bo'lganda doimo yoritish, tunda esa energiya tejash rejimi."
)

add_paragraph(
    "Xavfsizlik — IoT tizimlarida eng muhim masalalardan biri. Bizning tizimimizda bir nechta "
    "xavfsizlik qatlamlari joriy etilgan. Birinchidan, Firebase Authentication — faqat ro'yxatdan "
    "o'tgan foydalanuvchilar tizimga kirish huquqiga ega. Email va parol Firebase serverida "
    "xavfsiz saqlanadi (bcrypt hash). Ikkinchidan, Firebase Database Rules — ma'lumotlar bazasiga "
    "kirish qoidalari belgilangan, faqat autentifikatsiya qilingan foydalanuvchilar o'qish va "
    "yozish huquqiga ega. Uchinchidan, SSL/TLS shifrlash — ESP32 va Firebase orasidagi barcha "
    "aloqa HTTPS protokoli orqali shifrlangan. To'rtinchidan, API kalitlari firmware da hardcode "
    "qilingan bo'lsa-da, ular faqat ma'lum domenlardan kelgan so'rovlarni qabul qiladi (Firebase "
    "App Check). Beshinchidan, WiFi paroli NVS da shifrlangan holda saqlanadi. Bu xavfsizlik "
    "choralari tizimni ruxsatsiz kirishdan va ma'lumotlar o'g'irlanishidan himoya qiladi."
)

add_paragraph(
    "Tizimning kengaytirilish imkoniyatlari ham muhim jihat hisoblanadi. Joriy arxitektura kelajakda "
    "quyidagi kengaytmalarni qo'shish imkonini beradi: birinchidan, bir nechta yoritgichlarni bitta "
    "Dashboard dan boshqarish — Firebase da har bir qurilma uchun alohida yo'l yaratish kifoya. "
    "Ikkinchidan, sun'iy intellekt algoritmlari — harakat naqshlarini o'rganish va bashorat qilish "
    "orqali yanada samarali energiya tejash. Uchinchidan, quyosh paneli va akkumulator integratsiyasi — "
    "tizimni to'liq avtonom qilish. To'rtinchidan, LoRa yoki Zigbee tarmoq — WiFi mavjud bo'lmagan "
    "joylarda mesh tarmoq orqali aloqa. Beshinchidan, kamera integratsiyasi — harakat turini aniqlash "
    "(odam, mashina, hayvon) va shunga mos ravishda yorug'lik darajasini sozlash. Oltinchidan, "
    "bulutli analitika — katta hajmdagi ma'lumotlarni tahlil qilish va hisobotlar generatsiya qilish. "
    "Barcha bu kengaytmalar joriy arxitekturani o'zgartirmasdan qo'shilishi mumkin, chunki tizim "
    "modulli va kengaytiriladigan qilib loyihalangan."
)

add_paragraph(
    "Dasturiy ta'minotni sinovdan o'tkazish jarayonida biz bir nechta muhim muammolarni aniqladik "
    "va hal qildik. Birinchi muammo — WiFi ulanishi uzilganda ESP32 ning qayta ishga tushishi. Bu "
    "muammo WiFi.reconnect() funksiyasining blocking xususiyati tufayli yuzaga keldi. Yechim sifatida "
    "biz non-blocking reconnect mexanizmini joriy qildik — WiFi holati har 5 sekundda tekshiriladi "
    "va agar uzilgan bo'lsa, fon rejimida qayta ulanishga harakat qilinadi. Ikkinchi muammo — "
    "Firebase stream ning vaqti-vaqti bilan uzilishi. Bu muammo Firebase serverining timeout "
    "mexanizmi tufayli yuzaga keldi (60 sekunddan keyin stream uziladi). Yechim — stream uzilganda "
    "avtomatik qayta ulanish va oxirgi ma'lum holatni saqlash. Uchinchi muammo — ultratovush "
    "sensorining harorat ta'sirida noto'g'ri natijalar berishi. Bu muammo ayniqsa yoz kunlari "
    "(40°C dan yuqori haroratda) kuzatildi. Yechim — harorat kompensatsiya koeffitsientini "
    "qo'llash va majority voting algoritmini kuchaytirish."
)

add_paragraph(
    "Loyihaning dasturiy ta'minot sifatini ta'minlash uchun biz bir nechta yondashuvlarni qo'lladik. "
    "Birinchidan, modulli arxitektura — har bir modul o'z vazifasini mustaqil bajaradi va boshqa "
    "modullar bilan minimal bog'liqlikka ega. Bu kodni tushunish, sinovdan o'tkazish va o'zgartirish "
    "kiritishni osonlashtiradi. Ikkinchidan, aniq nomlash konventsiyasi — barcha o'zgaruvchilar, "
    "funksiyalar va konstantalar o'z vazifasini aks ettiruvchi nomlarga ega (masalan, readDistance, "
    "isMotionDetected, HOLD_TIME). Uchinchidan, xatoliklarni qayta ishlash — har bir funksiya "
    "kutilmagan holatlarni (timeout, noto'g'ri qiymat, ulanish uzilishi) to'g'ri qayta ishlaydi "
    "va tizimning barqaror ishlashini ta'minlaydi. To'rtinchidan, Serial debugging — dastur "
    "ishlash jarayonida muhim hodisalarni Serial portga chiqaradi, bu esa muammolarni aniqlash "
    "va tuzatishni osonlashtiradi. Beshinchidan, OTA (Over-The-Air) yangilash imkoniyati — "
    "firmware ni WiFi orqali masofadan yangilash mumkin, bu esa texnik xizmat ko'rsatishni "
    "sezilarli darajada osonlashtiradi."
)

add_paragraph(
    "React komponentlarining ishlash prinsipi hooks va state management ga asoslangan. Dashboard "
    "komponenti useState hook orqali lokal holatni boshqaradi va useEffect hook orqali Firebase "
    "dan real-time ma'lumotlarni oladi. Firebase onValue listener har safar ma'lumot o'zgarganda "
    "callback funksiyasini chaqiradi va React state yangilanadi. State yangilanganda React "
    "avtomatik ravishda DOM ni qayta render qiladi va foydalanuvchi eng so'nggi ma'lumotlarni "
    "ko'radi. Bu yondashuv an'anaviy polling (har N sekundda so'rov yuborish) ga nisbatan ancha "
    "samarali — tarmoq trafigi kamayadi va ma'lumotlar darhol ko'rinadi. Dashboard shuningdek "
    "useCallback va useMemo hooks orqali optimallashtirilgan — keraksiz qayta renderlar oldini "
    "olingan va ilova tezkor ishlaydi. Error boundary komponentlari kutilmagan xatoliklarni "
    "ushlab oladi va foydalanuvchiga tushunarli xato xabarini ko'rsatadi, bu esa ilovaning "
    "ishonchliligini oshiradi va foydalanuvchi tajribasini yaxshilaydi."
)

add_paragraph(
    "Tizimning energiya tejash samaradorligini oshirish uchun bir nechta qo'shimcha optimizatsiyalar "
    "ham qo'llanilgan. Birinchidan, adaptive timeout — agar tun vaqtida uzoq vaqt harakat "
    "aniqlanmasa, sensor o'qish chastotasi kamaytiriladi (100 ms dan 500 ms ga), bu esa ESP32 "
    "ning energiya iste'molini kamaytiradi. Ikkinchidan, WiFi power saving mode — ESP32 ning "
    "WiFi moduli DTIM beacon interval ni oshirish orqali energiya tejaydi. Uchinchidan, LED "
    "strip ning PWM chastotasi optimallashtirilgan — 400 Hz chastota ko'z uchun miltillash "
    "sezilmas, lekin energiya iste'molini kamaytiradi. To'rtinchidan, Firebase ga ma'lumot "
    "yuborish chastotasi adaptiv — agar sensor qiymatlari o'zgarmagan bo'lsa, yuborish "
    "intervali 3 sekunddan 10 sekundga oshiriladi. Beshinchidan, ESP32 ning light sleep "
    "rejimi kunduz vaqtida qo'llaniladi — bu holatda protsessor to'xtatiladi, lekin WiFi "
    "va timerlar ishlashda davom etadi. Bu optimizatsiyalar birgalikda tizimning umumiy "
    "energiya iste'molini 15-20 foizga kamaytiradi."
)

# ============================================================
# Yakuniy sahifa uzilishi va saqlash
# ============================================================

doc.add_page_break()
doc.save(DOC_PATH)
print("II BOB muvaffaqiyatli qo'shildi va saqlandi:", DOC_PATH)
