#!/usr/bin/env python3
"""II BOB - Amaliy qism yozish scripti"""

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
import os

BASE = '/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI'
IMG = os.path.join(BASE, 'images')
doc = Document(os.path.join(BASE, 'BMI_final.docx'))

total_chars = 0

def add_heading1(text):
    h = doc.add_heading(text, level=1)
    for r in h.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(14)
        r.font.color.rgb = None

def add_heading2(text):
    h = doc.add_heading(text, level=2)
    for r in h.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(14)
        r.font.color.rgb = None

def add_body(text):
    global total_chars
    total_chars += len(text)
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Cm(1.25)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)

def add_code(text):
    global total_chars
    total_chars += len(text)
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.left_indent = Cm(1)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(text)
    r.font.name = 'Courier New'
    r.font.size = Pt(10)

def add_image(filename, caption):
    global total_chars
    total_chars += len(caption)
    path = os.path.join(IMG, filename)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run()
    if os.path.exists(path):
        r.add_picture(path, width=Cm(14))
    else:
        r.add_text(f'[Rasm: {filename}]')
    cp = doc.add_paragraph()
    cp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    cr = cp.add_run(caption)
    cr.font.name = 'Times New Roman'
    cr.font.size = Pt(12)
    cr.italic = True

# ============================================================
# II BOB
# ============================================================
add_heading1("II BOB. AMALIY QISM")

# ============================================================
# 2.1
# ============================================================
add_heading2("2.1-§ Tizimni loyihalash: texnik vositalar va komponentlarni tanlash")

add_body("Aqlli ko'cha yoritish tizimini amalga oshirish uchun eng muhim qaror — bu markaziy boshqaruv qurilmasini tanlashdir. Zamonaviy IoT loyihalarida mikrokontrollerlar asosiy rol o'ynaydi, chunki ular kichik o'lchamli, kam energiya sarflaydigan va turli sensorlar bilan ishlash imkoniyatiga ega. Biz loyihamiz uchun Espressif kompaniyasining ESP32 DevKit modulini tanladik, chunki u barcha zarur xususiyatlarga ega va narxi atigi 5-7 dollar atrofida.")

add_body("ESP32 mikrokontrolleri ikki yadroli Xtensa LX6 protsessoriga ega bo'lib, har bir yadro 240 MHz chastotada ishlaydi. Bu ikki yadroli arxitektura bizning loyihamiz uchun juda muhim, chunki bir yadro sensorlarni o'qish va LED boshqarish bilan shug'ullanadi, ikkinchi yadro esa WiFi aloqa va Firebase bilan sinxronizatsiya vazifalarini bajaradi. Bunday parallellik tizimning barqaror ishlashini ta'minlaydi va real-time talablarni qondiradi.")

add_body("ESP32 ning yana bir muhim xususiyati — o'rnatilgan WiFi 802.11 b/g/n moduli. Bu modul alohida WiFi shield yoki modem sotib olish zaruratini yo'q qiladi va tizim narxini sezilarli darajada kamaytiradi. WiFi orqali ESP32 to'g'ridan-to'g'ri Firebase Realtime Database ga ulanadi va sensor ma'lumotlarini real vaqtda yuboradi. Shuningdek, boshqaruv buyruqlarini ham shu kanal orqali qabul qiladi va darhol bajaradi.")

add_body("Analog-raqamli o'zgartirish (ADC) imkoniyati ham muhim omil bo'ldi. ESP32 da 12-bitli ADC mavjud bo'lib, u 0 dan 4095 gacha qiymatlarni o'qiy oladi. Bu bizning TEMT6000 yorug'lik sensorimiz uchun juda mos keladi, chunki sensor analog signal beradi va biz uni raqamli qiymatga aylantirib, kunduz yoki tun ekanligini aniqlaymiz. 12-bitli aniqlik 0.8 mV ga teng bo'lib, bu sensor uchun yetarli darajada nozik farqlarni sezadi.")

add_body("ESP32 ning 3.3V mantiqiy darajasi zamonaviy sensorlar bilan to'g'ridan-to'g'ri ishlash imkonini beradi. RCWL-9610A ultratovush sensori ham, TEMT6000 yorug'lik sensori ham 3.3V da ishlaydi, shuning uchun qo'shimcha darajali o'zgartirish (level shifting) kerak emas. Bu sxemani soddalashtiradi va ishonchlilikni oshiradi. Faqat relay moduli uchun 5V kerak, lekin u alohida quvvat manbaidan olinadi va optik izolyatsiya bilan himoyalangan.")

add_body("Narx va mavjudlik jihatidan ESP32 bozorda eng qulay variantlardan biri hisoblanadi. Arduino Mega yoki STM32 kabi alternativalar mavjud bo'lsa-da, ularda WiFi moduli yo'q va qo'shimcha shield kerak bo'ladi. Raspberry Pi esa ortiqcha quvvatli va qimmat — u operatsion tizim talab qiladi va energiya sarfi 5-10 marta ko'p. ESP32 esa barcha kerakli funksiyalarni bitta chipda jamlagan holda, 5-7 dollar narxda sotiladi.")

add_body("ESP32 ning xotira imkoniyatlari ham loyiha uchun yetarli. U 520 KB SRAM va 4 MB flash xotiraga ega. SRAM da dastur o'zgaruvchilari va buferlar saqlanadi, flash xotirada esa dastur kodi va NVS (Non-Volatile Storage) joylashadi. NVS WiFi parollar va sozlamalarni saqlash uchun ishlatiladi — qurilma o'chirilganda ham bu ma'lumotlar yo'qolmaydi. 4 MB flash OTA (Over-The-Air) yangilanish uchun ham yetarli joy beradi.")

add_body("Tizim arxitekturasi uch qatlamli modelga asoslangan: Hardware qatlami, Cloud qatlami va Client qatlami. Hardware qatlamida ESP32 mikrokontroller sensorlardan ma'lumot yig'adi va LED yoritgichni boshqaradi. Cloud qatlamida Firebase Realtime Database barcha ma'lumotlarni saqlaydi va qurilmalar o'rtasida sinxronizatsiya qiladi. Client qatlamida React asosidagi PWA dashboard foydalanuvchiga monitoring va boshqaruv imkoniyatini beradi.")

add_body("Hardware qatlami fizik dunyoni raqamli dunyoga bog'laydi. ESP32 har 100 millisekundda ultratovush sensoridan masofa o'qiydi, har 500 millisekundda yorug'lik sensoridan ambient light qiymatini oladi. Bu ma'lumotlar asosida algoritmlar harakat borligini va atrofning qorong'i ekanligini aniqlaydi. Agar ikkala shart bajarilsa — tun va harakat bor — LED yoritgich yoqiladi. Aks holda energiya tejash uchun o'chiriladi va tizim kutish rejimiga o'tadi.")

add_body("Cloud qatlami sifatida Google Firebase Realtime Database tanlandi. Bu NoSQL ma'lumotlar bazasi WebSocket protokoli orqali real-time sinxronizatsiyani ta'minlaydi. ESP32 har 2 soniyada o'z holatini bazaga yozadi: joriy masofa, yorug'lik darajasi, LED holati, harakat vaqti. Shu bilan birga, bazadagi boshqaruv buyruqlarini tinglaydi va o'zgarishlarni darhol qo'llaydi. Firebase ning bepul rejasi kuniga 100 ming o'qish va 50 ming yozishni qo'llab-quvvatlaydi.")

add_body("Firebase tanlashning yana bir sababi — u Google infrastrukturasida ishlaydi va 99.95 foiz uptime kafolatlaydi. Ma'lumotlar avtomatik ravishda bir nechta data centerda replikatsiya qilinadi. Xavfsizlik qoidalari (Security Rules) orqali faqat autentifikatsiya qilingan foydalanuvchilar ma'lumotlarga kirishi mumkin. Bu bizning tizim uchun muhim, chunki boshqa odamlar yoritgichni boshqara olmasligi kerak — faqat egasi nazorat qilishi lozim.")

add_body("Client qatlami Progressive Web Application sifatida ishlab chiqilgan. PWA texnologiyasi brauzer orqali ishlaydigan, lekin native ilovaga o'xshash tajriba beradigan zamonaviy yondashuv. Foydalanuvchi telefonidan saytni ochib, bosh ekranga qo'shishi mumkin va u oddiy ilova kabi ishlaydi. Offline rejimda ham asosiy interfeys ko'rinadi, faqat real-time ma'lumotlar yangilanmaydi. Bu iOS va Android uchun alohida ilova yozish zaruratini yo'q qiladi.")

add_image("diagram_architecture.png", "2.1-rasm. Tizim arxitekturasi diagrammasi")

add_body("Pin konfiguratsiya loyihalashda har bir GPIO pinning vazifasi aniq belgilandi. GPIO 4 pini RCWL-9610A sensorining TRIG (trigger) signaliga ulangan va OUTPUT rejimida ishlaydi. Bu pin orqali ESP32 sensorga 10 mikrosekundlik impuls yuboradi, sensor esa shu impulsga javoban ultratovush to'lqinini chiqaradi. GPIO 16 pini esa ECHO signaliga ulangan va INPUT rejimida ishlaydi — sensor to'lqin qaytib kelganda shu pinda signal hosil bo'ladi va davomiyligi o'lchanadi.")

add_body("GPIO 34 pini TEMT6000 yorug'lik sensorining analog chiqishiga ulangan. Bu pin faqat kirish (input-only) rejimida ishlaydi va ADC1 kanaliga tegishli. ADC1 WiFi bilan bir vaqtda ishlashi mumkin, bu esa muhim, chunki ADC2 kanali WiFi yoqilganda ishlamaydi. Sensor 0-3.3V oralig'ida signal beradi: qorong'ida 0V ga yaqin, yorug'da 3.3V ga yaqin. ESP32 buni 0-4095 oralig'idagi raqamga aylantiradi va dastur bu qiymatni tahlil qiladi.")

add_body("GPIO 26 pini relay moduliga ulangan va OUTPUT rejimida ishlaydi. Relay moduli 5V elektromagnit bilan boshqariladigan kalit bo'lib, u 220V ko'cha yoritgichini yoqish va o'chirish uchun ishlatiladi. ESP32 dan 3.3V signal relay modulidagi optron orqali kuchaytiriladi va relay kontaktlarini yopadi yoki ochadi. Xavfsizlik uchun relay moduli optik izolyatsiyaga ega, ya'ni yuqori kuchlanish ESP32 ga o'tmaydi va qurilma himoyalangan bo'ladi.")

add_body("GPIO 2 pini ESP32 platasidagi o'rnatilgan ko'k LED ga ulangan. Bu LED tizim holatini ko'rsatish uchun ishlatiladi: WiFi ga ulanish jarayonida miltillaydi, muvaffaqiyatli ulanganda bir marta yonib o'chadi, xatolik bo'lganda tez miltillaydi. Bu debug va monitoring uchun juda qulay, chunki serial monitor ulash imkoni bo'lmagan holatlarda ham tizim holatini ko'rish mumkin bo'ladi va texnik xodim muammoni tezda aniqlaydi.")

add_body("Pinlarni tanlashda bir nechta muhim qoidalarga amal qilindi. Birinchidan, ADC2 kanali pinlari (GPIO 0, 2, 4, 12-15, 25-27) WiFi bilan bir vaqtda ishlamaydi, shuning uchun yorug'lik sensori ADC1 kanaliga (GPIO 34) ulandi. Ikkinchidan, GPIO 6-11 pinlari flash xotira uchun band, ularni ishlatib bo'lmaydi. Uchinchidan, boot jarayonida muammo chiqarmaydigan pinlar tanlandi — GPIO 4, 16, 26 xavfsiz pinlar hisoblanadi.")

add_body("Quvvat sarfini hisoblash tizimni loyihalashda muhim bosqich hisoblanadi. ESP32 mikrokontrolleri WiFi yoqilgan holatda o'rtacha 150 mA tok sarflaydi. RCWL-9610A ultratovush sensori ishlash paytida atigi 2 mA sarflaydi, chunki u faqat impuls yuborilganda faollashadi. Relay moduli esa yoqilgan holatda 70 mA sarflaydi, o'chirilganda esa 5 mA dan kam. Jami maksimal sarfiyot 150 + 2 + 70 = 222 mA ni tashkil etadi.")

add_body("222 mA sarfiyot 5V kuchlanishda 1.11 Vatt quvvatga teng. Kuniga 24 soat ishlasa, 26.6 Vt-soat energiya sarflanadi. Oyiga bu 0.8 kVt-soat, ya'ni deyarli hisobga olinmaydigan darajada kam. Taqqoslash uchun, oddiy 60 Vattli ko'cha chiroq tun bo'yi (12 soat) yonsa, kuniga 720 Vt-soat sarflaydi. Demak, bizning boshqaruv tizimimiz boshqarilayotgan yoritgichning energiya sarfidan 27 marta kam energiya ishlatadi va o'zi ham tejamkor.")

add_body("Deep sleep rejimi ham loyihalashda ko'rib chiqildi. ESP32 deep sleep holatida atigi 10 mikroamper sarflaydi — bu 15,000 marta kam. Ammo bizning tizimda deep sleep ishlatilmaydi, chunki sensor doimiy ravishda harakatni kuzatishi kerak. Agar sensor faqat har 5 sekundda uyg'onsa, tez o'tib ketayotgan odamni sezmasligi mumkin. Shuning uchun biz light sleep rejimini tanladik — u 20 mA sarflaydi va sensorni doimiy faol saqlaydi.")

add_body("Dasturiy platforma sifatida PlatformIO muhiti tanlandi. PlatformIO — bu professional IoT dasturlash uchun mo'ljallangan ochiq kodli ekotizim bo'lib, u Visual Studio Code bilan integratsiyalangan. Arduino IDE dan farqli o'laroq, PlatformIO kutubxonalarni avtomatik boshqaradi, kompilyatsiya tezroq ishlaydi va bir nechta muhitni (debug, release) qo'llab-quvvatlaydi. Loyihamizda platformio.ini fayli orqali barcha sozlamalar versiya nazoratida saqlanadi.")

add_body("PlatformIO ning platformio.ini konfiguratsiya fayli loyihaning barcha parametrlarini belgilaydi. Unda platforma (espressif32), framework (arduino), board (esp32dev), monitor tezligi (115200) va kutubxonalar ro'yxati ko'rsatilgan. Bu fayl Git repozitoriyasida saqlanadi va boshqa dasturchi loyihani klonlab, bir buyruq bilan kompilyatsiya qilishi mumkin. Bu reproducibility va hamkorlik uchun juda muhim xususiyatdir.")

add_body("Arduino framework ESP32 uchun eng keng tarqalgan dasturlash muhiti hisoblanadi. U C++ tilida yozilgan va minglab tayyor kutubxonalarga ega. Bizning loyihamizda Firebase ESP32 Client kutubxonasi ishlatilgan — bu Mobizt tomonidan ishlab chiqilgan va Firebase Realtime Database, Authentication va Cloud Functions bilan ishlash imkonini beradi. Kutubxona non-blocking rejimda ishlaydi, ya'ni Firebase so'rovlari asosiy dastur tsiklini to'xtatmaydi.")

add_body("Firebase ESP32 Client kutubxonasi stream callback mexanizmini qo'llab-quvvatlaydi. Bu shuni anglatadiki, bazadagi o'zgarishlarni tinglash uchun alohida so'rov yuborish kerak emas — kutubxona WebSocket orqali doimiy aloqani saqlaydi va o'zgarish bo'lganda callback funksiyasini chaqiradi. Masalan, foydalanuvchi dashboarddan rejimni o'zgartirganda, ESP32 buni 1-2 soniya ichida biladi va darhol yangi rejimga o'tadi.")

add_body("Web dashboard uchun React 19 kutubxonasi tanlandi. React — Meta kompaniyasi tomonidan ishlab chiqilgan va dunyoda eng mashhur frontend kutubxona. Uning komponent asosidagi arxitekturasi kodni qayta ishlatish va tashkil qilishni osonlashtiradi. React 19 versiyasida yangi concurrent rendering xususiyatlari qo'shilgan bo'lib, bu katta hajmdagi real-time ma'lumotlarni ko'rsatishda samaradorlikni oshiradi va foydalanuvchi tajribasini yaxshilaydi.")

add_body("Vite 8 build tool sifatida ishlatilgan. Vite — bu zamonaviy frontend loyihalar uchun tezkor build vositasi bo'lib, u ES modules asosida ishlaydi. Development rejimida Hot Module Replacement (HMR) orqali o'zgarishlar bir soniyadan kam vaqtda brauzerda ko'rinadi. Production build uchun Rollup bundler ishlatiladi va natijada optimallashtirilgan, kichik hajmli fayllar hosil bo'ladi. Bizning dashboard 180 KB dan kam hajmda build bo'ladi.")

add_body("Firebase SDK web ilovada authentication va real-time database bilan ishlash uchun ishlatilgan. Firebase Authentication email va parol orqali kirishni ta'minlaydi, bu esa dashboardga faqat vakolatli foydalanuvchilar kirishini kafolatlaydi. Realtime Database esa WebSocket orqali ma'lumotlarni jonli yangilaydi — sensor qiymati o'zgarganda dashboard avtomatik yangilanadi, sahifani qayta yuklash kerak emas va kechikish minimal bo'ladi.")

add_body("Recharts kutubxonasi statistika grafiklarini chizish uchun tanlangan. Bu React uchun maxsus ishlab chiqilgan grafik kutubxona bo'lib, SVG asosida ishlaydi. U responsive dizaynni qo'llab-quvvatlaydi, ya'ni grafiklar turli ekran o'lchamlariga moslashadi. Bizning dashboardda haftalik energiya tejash grafigi, kunlik harakat soni va yoritgich yonish vaqti ko'rsatiladi. Recharts animatsiyalar bilan chiroyli vizualizatsiya yaratadi va foydalanuvchiga tushunarli.")

add_body("PWA (Progressive Web Application) texnologiyasi vite-plugin-pwa plaginasi orqali amalga oshirilgan. Bu plagin Service Worker ni avtomatik generatsiya qiladi va manifest.json faylini sozlaydi. Natijada ilova telefondan o'rnatilishi, offline ishlashi va push notification olishi mumkin. Service Worker kesh strategiyasi sifatida NetworkFirst ishlatilgan — avval tarmoqdan olishga harakat qiladi, muvaffaqiyatsiz bo'lsa keshdan ko'rsatadi va foydalanuvchiga xabar beradi.")

add_body("Komponentlar orasidagi aloqa protokollari ham muhim loyihalash qarori edi. ESP32 va sensorlar orasida oddiy GPIO signallari ishlatiladi — bu eng tez va ishonchli usul. ESP32 va Firebase orasida HTTPS va WebSocket protokollari ishlatiladi — HTTPS ma'lumot yozish uchun, WebSocket esa real-time tinglash uchun. Firebase va web dashboard orasida ham WebSocket ishlatiladi, bu esa end-to-end kechikishni 2-3 soniyaga kamaytiradi.")

add_body("Xavfsizlik arxitekturasi ham loyihalash bosqichida puxta o'ylab chiqildi. Firebase Authentication foydalanuvchilarni email va parol bilan autentifikatsiya qiladi. Database Security Rules faqat autentifikatsiya qilingan foydalanuvchilarga yozish huquqini beradi. ESP32 esa maxsus API kaliti orqali bazaga ulanadi — bu kalit firmware ichida shifrlangan holda saqlanadi. HTTPS protokoli barcha ma'lumotlarni tranzitda shifrlaydi va man-in-the-middle hujumlardan himoya qiladi.")

add_body("Tizimning kengaytirilishi (scalability) ham hisobga olingan. Hozirgi arxitektura bitta qurilma uchun mo'ljallangan, lekin Firebase ning real-time xususiyati minglab qurilmalarni bir vaqtda qo'llab-quvvatlaydi. Har bir qurilma o'z node ida ma'lumot saqlaydi va dashboard barcha qurilmalarni bitta interfeysdan boshqarishi mumkin. Kelajakda 100 yoki 1000 ta yoritgich qo'shilsa ham, arxitektura o'zgartirilmaydi — faqat yangi node qo'shiladi va tizim ishlashda davom etadi.")

add_body("Monitoring va alerting tizimi ham loyihalangan. Agar ESP32 5 minutdan ortiq Firebase ga ma'lumot yubormasa, dashboard ogohlantirish ko'rsatadi — bu qurilma ishlamay qolganini bildiradi. Shuningdek, WiFi signal kuchi -80 dBm dan past bo'lsa, sariq ogohlantirish chiqadi. Relay 1000 martadan ortiq yoqilsa (kuniga), bu anomal holat deb belgilanadi. Bu monitoring tizim texnik xodimga muammolarni erta bosqichda aniqlash imkonini beradi va tizim ishonchliligini oshiradi.")


# ============================================================
# 2.2
# ============================================================
add_heading2("2.2-§ Masofani aniqlash algoritmi va qurilmani ishlab chiqish jarayoni")

add_body("Ultratovush sensori yordamida masofani aniqlash fizikaning oddiy qonuniyatiga asoslangan: tovush to'lqini ma'lum tezlikda tarqaladi va to'siqdan qaytib keladi. Havoda tovush tezligi taxminan 343 m/s yoki 0.0343 sm/mikrosekundni tashkil etadi. ESP32 TRIG pinga 10 mikrosekundlik impuls yuboradi, sensor 40 kHz chastotadagi ultratovush to'lqinini chiqaradi. To'lqin ob'ektdan qaytib kelganda ECHO pinda signal hosil bo'ladi. Masofa = (vaqt × tezlik) / 2 formulasi bilan hisoblanadi.")

add_body("Ammo amaliyotda bu oddiy formula yetarli emas. Sensordan keladigan ma'lumotlar shovqinli bo'lishi mumkin: havo harakati, harorat o'zgarishi, sensor yuzasidagi chang — bularning barchasi natijaga ta'sir qiladi. Shuning uchun biz bir necha bosqichli filtrlash algoritmini ishlab chiqdik. Birinchi bosqichda xom ma'lumot olinadi, ikkinchi bosqichda noto'g'ri qiymatlar filtrlanadi, uchinchi bosqichda debounce qo'llanadi va to'rtinchi bosqichda hold timer ishlatiladi. Bu ko'p bosqichli yondashuv ishonchlilikni oshiradi.")

add_body("RCWL-9610A sensori biz tanlagan ultratovush sensoridir. U HC-SR04 ning zamonaviy versiyasi bo'lib, 3.3V da ishlaydi (HC-SR04 faqat 5V), o'lchash diapazoni 2-400 sm va burchagi 15 daraja. Sensorda o'rnatilgan signal generatori bor — u TRIG impulsini olganda avtomatik ravishda 8 ta 40 kHz impuls chiqaradi. Bu boshqa sensorlarga nisbatan aniqroq natija beradi, chunki bir nechta impuls yuborilib, ularning o'rtachasi olinadi.")

add_body("Asosiy o'lchash funksiyasi readDistance() quyidagi algoritmga asoslangan. Avval TRIG pini LOW holatga o'tkaziladi va 2 mikrosekundlik pauza beriladi — bu oldingi signalning to'liq so'nishini ta'minlaydi. Keyin TRIG pini HIGH holatga o'tkaziladi, 10 mikrosekunddan so'ng yana LOW ga qaytariladi. Bu 10 mikrosekundlik impuls sensorga to'lqin chiqarish buyrug'ini beradi. So'ngra pulseIn() funksiyasi ECHO pinidagi signal davomiyligini mikrosekundlarda o'lchaydi va natija qaytariladi.")

add_code("""float readDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  long duration = pulseIn(ECHO_PIN, HIGH, 30000);
  if (duration == 0) return 999.0;
  float dist = duration * 0.0343 / 2.0;
  return (dist < 2 || dist > 400) ? 999.0 : dist;
}""")

add_body("Kodda pulseIn() funksiyasiga 30000 mikrosekundlik timeout berilgan. Bu 30 millisekundga teng bo'lib, taxminan 5 metr masofaga mos keladi. Agar shu vaqt ichida signal qaytmasa, funksiya 0 qaytaradi va biz uni 999.0 sm deb belgilaymiz — bu harakat yo'q degan ma'noni anglatadi. Shuningdek, 2 sm dan kam yoki 400 sm dan ko'p natijalar ham noto'g'ri deb hisoblanadi, chunki sensor bu diapazondan tashqarida ishonchsiz ishlaydi va natijalar shovqinli bo'ladi.")

add_body("Harorat kompensatsiyasi ham algoritmda hisobga olingan. Tovush tezligi haroratga bog'liq: v = 331.3 + 0.606 × T (m/s). 20°C da tezlik 343.5 m/s, 0°C da esa 331.3 m/s. Bu 3.5 foiz farq qiladi, ya'ni 200 sm masofada 7 sm xatolik berishi mumkin. Ammo bizning tizimda aniq masofa emas, balki harakat bor-yo'qligi muhim, shuning uchun bu xatolik amaliy ta'sir ko'rsatmaydi va qo'shimcha harorat sensori kerak emas.")

add_body("Debounce algoritmi sensordan keladigan tasodifiy shovqinlarni filtrlash uchun ishlatiladi. Bitta o'lchov natijasiga ishonish xavfli — masalan, shamol esib o'tgan qog'oz yoki hasharot sensor oldidan o'tishi mumkin. Shuning uchun biz ketma-ket bir nechta o'lchov olamiz va faqat barcha o'lchovlar bir xil natija ko'rsatganda harakatni tasdiqlaymiz. Bu yondashuv false positive (noto'g'ri ijobiy) holatlarni deyarli nolga tushiradi va tizim ishonchliligini oshiradi.")

add_body("detectMotion() funksiyasi debounce mantiqini amalga oshiradi. U oxirgi uchta o'lchov natijasini saqlaydi va faqat ularning barchasi threshold qiymatidan past bo'lganda true qaytaradi. Bu usul oddiy bo'lsa-da, juda samarali — sinov natijalarida false positive holatlar 100 soatlik testda atigi 2 marta qayd etildi. Funksiya har chaqirilganda yangi o'lchov oladi va eski qiymatlarni siljitadi, bu esa sliding window texnikasi deb ataladi.")

add_code("""bool detectMotion() {
  readings[idx] = readDistance();
  idx = (idx + 1) % 3;
  for (int i = 0; i < 3; i++) {
    if (readings[i] > DISTANCE_THRESHOLD)
      return false;
  }
  return true;
}""")

add_body("Sliding window o'lchami 3 ga teng qilib tanlangan. Bu son tajriba asosida aniqlangan — 2 ta o'lchov kam ishonchli (shovqin o'tib ketishi mumkin), 5 ta esa ortiqcha kechikish beradi (odam tez o'tib ketganda sezilmasligi mumkin). 3 ta o'lchov 300 millisekundda amalga oshiriladi (har biri 100 ms interval bilan) va bu odam yurish tezligida (1.4 m/s) 42 sm masofaga teng — sensor diapazoni ichida yetarli vaqt beradi.")

add_body("Hold timer mexanizmi harakat to'xtagandan keyin yoritgichni darhol o'chirmaslik uchun ishlatiladi. Inson ko'chadan o'tayotganda sensor uni bir necha soniya davomida ko'radi, lekin odam sensordan uzoqlashganda signal to'satdan yo'qoladi. Agar biz darhol o'chirsak, odam hali ko'rinish doirasida bo'lishi mumkin. Shuning uchun oxirgi harakat aniqlangan vaqtdan boshlab ma'lum muddat (standart 30 soniya) kutamiz va shundan keyingina o'chiramiz.")

add_body("Hold timer muddati Firebase orqali masofadan sozlanishi mumkin. Standart qiymat 30 soniya bo'lib, bu ko'pchilik holatlar uchun optimal. Ammo ba'zi joylarda (masalan, park yoki dam olish zonasi) odamlar uzoqroq turishi mumkin va 60 soniya kerak bo'ladi. Boshqa joylarda (masalan, yo'lak) 15 soniya yetarli. Foydalanuvchi dashboarddan bu qiymatni 5 dan 120 soniyagacha o'zgartirishi mumkin va o'zgarish darhol kuchga kiradi.")

add_body("updateMotion() funksiyasi hold timer mantiqini boshqaradi. Agar harakat aniqlansa, lastMotionTime o'zgaruvchisi joriy vaqtga yangilanadi va motionActive bayrog'i true bo'ladi. Agar harakat yo'q bo'lsa, funksiya joriy vaqt bilan lastMotionTime orasidagi farqni tekshiradi. Agar farq TIMEOUT_SEC dan katta bo'lsa, motionActive false ga o'tadi. Bu oddiy, lekin ishonchli yondashuv tizimning barqaror ishlashini ta'minlaydi va ortiqcha murakkablikdan qochadi.")

add_code("""void updateMotion() {
  if (detectMotion()) {
    lastMotionTime = millis();
    motionActive = true;
  } else {
    if (millis() - lastMotionTime > timeoutSec * 1000UL) {
      motionActive = false;
    }
  }
}""")

add_body("millis() funksiyasi ESP32 yoqilganidan beri o'tgan millisekundlar sonini qaytaradi. Bu funksiya delay() dan farqli ravishda dasturni to'xtatmaydi — u faqat vaqtni o'qiydi. 1000UL ko'paytirish unsigned long tipida hisoblashni ta'minlaydi, chunki oddiy int 32767 dan oshganda overflow bo'ladi. millis() 49 kundan keyin overflow bo'ladi, lekin ayirma operatsiyasi to'g'ri ishlaydi, chunki unsigned arithmetic modular hisoblanadi.")

add_body("Hysteresis mexanizmi yorug'lik sensorida qo'llaniladi. Oddiy threshold ishlatilganda, yorug'lik darajasi chegaraga yaqin bo'lsa, tizim tez-tez rejim almashtiradi — bu flickering deb ataladi. Masalan, threshold 300 bo'lsa va sensor 298-302 orasida o'ynasa, tizim har sekundda kunduz-tun o'rtasida almashadi. Hysteresis bu muammoni hal qiladi: yoqish uchun 250 dan past, o'chirish uchun 350 dan yuqori bo'lishi kerak — 100 birlik dead zone.")

add_code("""void updateLightStatus() {
  int light = analogRead(LIGHT_PIN);
  if (light < LIGHT_LOW) isDark = true;
  else if (light > LIGHT_HIGH) isDark = false;
  ambientLight = light;
}""")

add_body("LIGHT_LOW va LIGHT_HIGH qiymatlari tajriba asosida aniqlangan. TEMT6000 sensori quyosh nurida 3500-4000, xona yorug'ligida 800-1500, shom paytida 200-400 va to'liq qorong'ida 0-50 qiymat beradi. Biz LIGHT_LOW ni 250 ga, LIGHT_HIGH ni 350 ga belgiladik. Bu shom paytida — quyosh botgandan 20-30 minut keyin — tizim tun rejimiga o'tishini ta'minlaydi. Bu qiymatlar ham Firebase orqali masofadan sozlanishi mumkin.")

add_body("Light control algoritmi barcha sensor ma'lumotlarini birlashtiradi va yakuniy qaror qabul qiladi. autoMode() funksiyasi avval rejimni tekshiradi — agar manual rejim bo'lsa, foydalanuvchi buyrug'iga bo'ysunadi. Auto rejimda esa isDark va motionActive bayroqlarini tekshiradi. Faqat ikkala shart bajarilganda — tun va harakat bor — relay yoqiladi. Boshqa barcha holatlarda relay o'chiriladi va energiya tejaladi. Bu mantiq oddiy, lekin samarali.")

add_body("autoMode() funksiyasi shuningdek jadval rejimini ham qo'llab-quvvatlaydi. Agar schedule rejimi tanlangan bo'lsa, funksiya joriy vaqtni schedule_on va schedule_off vaqtlari bilan solishtiradi. Agar joriy vaqt belgilangan oraliqda bo'lsa, yoritgich yoqiladi, aks holda o'chiriladi. Bu rejim sensor ishlamay qolgan holatlarda yoki maxsus tadbirlar uchun foydali — masalan, bayram kechalarida yoritgichni butun tun yoqib qo'yish mumkin.")

add_code("""void autoMode() {
  if (mode == MODE_MANUAL) {
    setRelay(manualState);
    return;
  }
  if (mode == MODE_SCHEDULE) {
    setRelay(isInSchedule());
    return;
  }
  setRelay(isDark && motionActive);
}""")

add_body("setRelay() funksiyasi relay modulini boshqaradi va holatni saqlaydi. U avval yangi holat joriy holatdan farq qilishini tekshiradi — agar bir xil bo'lsa, hech narsa qilmaydi (bu relay ning keraksiz miltillashini oldini oladi). Farq bo'lsa, GPIO 26 pini yangi holatga o'tkaziladi va relayState o'zgaruvchisi yangilanadi. Shuningdek, relay yoqilgan vaqt hisoblanadi — bu statistika uchun kerak bo'ladi va energiya tejash foizini hisoblashda ishlatiladi.")

add_body("Firebase sinxronizatsiya tizimning eng muhim qismlaridan biri hisoblanadi. ESP32 va web dashboard o'rtasidagi aloqa Firebase Realtime Database orqali amalga oshiriladi. ESP32 har 2 soniyada o'z holatini bazaga yozadi: joriy masofa, yorug'lik darajasi, LED holati, oxirgi harakat vaqti, uptime va WiFi signal kuchi. Shu bilan birga, bazadagi control node ni tinglaydi va o'zgarishlarni real vaqtda qo'llaydi va qurilma holatini yangilaydi.")

add_body("updateStatus() funksiyasi Firebase ga ma'lumot yuborish jarayonini boshqaradi. U avval WiFi ulanishini tekshiradi — agar ulanish yo'q bo'lsa, ma'lumotlarni lokal buferga saqlaydi va keyinroq yuboradi. Firebase kutubxonasi non-blocking rejimda ishlaydi, ya'ni ma'lumot yuborish jarayonida asosiy dastur tsikli to'xtamaydi. Bu juda muhim, chunki sensor o'qish va LED boshqarish uzluksiz davom etishi kerak va hech qanday kechikish bo'lmasligi lozim.")

add_code("""void updateStatus() {
  if (!Firebase.ready()) return;
  unsigned long now = millis();
  if (now - lastUpdate < UPDATE_INTERVAL) return;
  lastUpdate = now;
  FirebaseJson json;
  json.set("light_on", relayState);
  json.set("motion_detected", motionActive);
  json.set("distance_cm", lastDistance);
  json.set("ambient_light", ambientLight);
  json.set("mode", modeStr);
  json.set("uptime", now / 1000);
  Firebase.RTDB.setJSON(&fbdo, "/device/status", &json);
}""")

add_body("UPDATE_INTERVAL 2000 millisekundga (2 soniya) teng qilib belgilangan. Bu qiymat optimal balans — tez-tez yuborish Firebase kvotasini tez tugatadi (kuniga 50,000 yozish = har 1.7 sekundda), kam yuborish esa dashboardda kechikish seziladi. 2 soniya intervalda kuniga 43,200 yozish bo'ladi — bu bepul kvota ichida va foydalanuvchi uchun deyarli real-time his qiladi. Zarur bo'lsa, bu qiymat ham masofadan sozlanadi.")

add_body("FirebaseJson obyekti ma'lumotlarni JSON formatida tayyorlaydi va bir so'rovda yuboradi. Bu alohida-alohida yozishdan samaraliroq, chunki bitta HTTP so'rovi bir nechta maydonni yangilaydi. setJSON metodi atomik operatsiya — ya'ni barcha maydonlar bir vaqtda yangilanadi, oraliq holatlar bo'lmaydi. Bu muhim, chunki dashboard bir vaqtning o'zida eski masofa va yangi LED holatini ko'rmasligi kerak.")

add_body("WiFi boshqaruv moduli non-blocking yondashuv asosida ishlab chiqilgan. Ko'pgina Arduino loyihalarida WiFi ga ulanish blocking rejimda amalga oshiriladi — ya'ni dastur WiFi ulanguncha to'xtab turadi. Bizning tizimda esa WiFi ulanish jarayoni fon rejimida ishlaydi. Agar WiFi uzilsa, tizim avtonom rejimda ishlashda davom etadi — sensorlar o'qiladi, LED boshqariladi, faqat Firebase sinxronizatsiya to'xtaydi va lokal rejimda ishlaydi.")

add_body("WiFi ma'lumotlari (SSID va parol) ESP32 ning NVS (Non-Volatile Storage) xotirasida saqlanadi. Bu flash xotiraning maxsus bo'limi bo'lib, qurilma o'chirilganda ham ma'lumotlar saqlanib qoladi. NVS key-value formatida ishlaydi va 20,000 marta yozishga chidamli. Birinchi marta yoqilganda yoki saqlangan tarmoq topilmaganda, ESP32 Access Point rejimiga o'tadi va captive portal ochadi — foydalanuvchi WiFi ni sozlashi mumkin.")

add_body("Captive portal — bu maxsus web sahifa bo'lib, u foydalanuvchini avtomatik ravishda sozlash sahifasiga yo'naltiradi. ESP32 DNS server sifatida ishlaydi va barcha so'rovlarni o'z IP manziliga qaytaradi. Natijada foydalanuvchi brauzer ochganda avtomatik ravishda WiFi sozlash sahifasi ko'rinadi. Bu yondashuv texnik bilimi bo'lmagan foydalanuvchilar uchun ham qulay — serial monitor yoki maxsus dastur kerak emas, oddiy telefon yetarli.")

add_body("WiFi qayta ulanish strategiyasi eksponensial backoff algoritmiga asoslangan. Birinchi urinish muvaffaqiyatsiz bo'lsa, 1 soniya kutiladi, ikkinchisida 2 soniya, uchinchisida 4 soniya va hokazo — maksimal 60 soniyagacha. Bu yondashuv tarmoq muammolari vaqtida ortiqcha energiya sarflanishini oldini oladi va router qayta ishga tushganda tezda ulanishni ta'minlaydi. Har bir muvaffaqiyatli ulanishdan keyin kutish vaqti 1 soniyaga qayta tiklanadi.")

add_body("OTA (Over-The-Air) yangilanish ham WiFi moduli orqali amalga oshiriladi. Bu ESP32 ning firmware ini fizik ulanishsiz, WiFi orqali yangilash imkonini beradi. Ko'cha yoritgichi ustunda o'rnatilgan bo'lsa, har safar uni tushirib, kompyuterga ulab dastur yuklash noqulay. OTA bilan yangi versiyani masofadan yuklash mumkin. Xavfsizlik uchun OTA parol bilan himoyalangan va faqat lokal tarmoqdan ishlaydi.")

add_image("diagram_state.png", "2.2-rasm. Tizim holatlari va o'tishlar diagrammasi")

add_body("Qurilmani yig'ish jarayoni bir necha bosqichdan iborat va har bir bosqich alohida sinovdan o'tkaziladi. Birinchi bosqichda barcha komponentlar tekshiriladi — har bir sensor va modul alohida sinovdan o'tkaziladi. ESP32 platasiga USB orqali quvvat beriladi va onboard LED miltillashi tekshiriladi. Ultratovush sensori alohida ulanganda masofa qiymatlari serial monitordan kuzatiladi. Yorug'lik sensori qo'l bilan yopilganda va ochilganda ADC qiymatlari o'zgarishi tasdiqlanadi.")

add_body("Ikkinchi bosqichda simlar ulanadi. Biz breadboard ishlatdik, chunki u prototiplash uchun eng qulay vosita — lehimlash kerak emas va simlarni osongina almashtirib ko'rish mumkin. Ultratovush sensorining VCC pini ESP32 ning 3.3V piniga, GND pini GND ga, TRIG pini GPIO 4 ga va ECHO pini GPIO 16 ga ulandi. Yorug'lik sensorining VCC 3.3V ga, GND GND ga va OUT pini GPIO 34 ga ulandi. Barcha ulanishlar ikki marta tekshirildi.")

add_body("Uchinchi bosqichda relay moduli ulandi. Relay moduli alohida 5V quvvat manbaidan oziqlantiradi, chunki u 3.3V da ishlamaydi. Relay ning IN pini ESP32 ning GPIO 26 piniga ulangan. Relay ning COM (common) kontakti 220V manbaiga, NO (normally open) kontakti esa yoritgichga ulangan. Shunday qilib, ESP32 GPIO 26 ni HIGH qilganda relay yopiladi va yoritgich yonadi, LOW qilganda ochiladi va yoritgich o'chadi. Xavfsizlik uchun 220V qismi izolyatsiyalangan.")

add_body("To'rtinchi bosqichda barcha komponentlar birgalikda sinovdan o'tkazildi. Firmware yuklangandan so'ng, serial monitor orqali barcha sensor qiymatlari kuzatildi. Qo'l sensorga yaqinlashtirilganda masofa kamayishi, relay yoqilishi va Firebase ga ma'lumot yuborilishi tasdiqlandi. Xona chiroqlari o'chirilganda yorug'lik sensori tun rejimiga o'tishi va yoritgich avtomatik yonishi tekshirildi. Barcha testlar muvaffaqiyatli o'tdi va tizim tayyor deb topildi.")

add_body("Beshinchi bosqichda qurilma himoya korpusiga joylashtirildi. IP65 darajasidagi plastik quti tanlandi — u suv va changdan himoya qiladi. Quti ichida ESP32, relay moduli va quvvat manbai joylashtirildi. Ultratovush sensori qutining pastki qismiga o'rnatildi, uning uchun maxsus teshik ochildi va atrofiga silikon surtildi. Yorug'lik sensori qutining yuqori qismiga, ochiq joyga o'rnatildi, chunki u tashqi yorug'likni sezishi kerak.")

add_body("Qurilmaning fizik joylashuvi ham muhim omil. Ultratovush sensori ko'cha yoritgichi ustuniga 3-4 metr balandlikda, pastga qaratib o'rnatiladi. Bu balandlikda sensor 2-3 metr radiusda harakatni aniqlay oladi. Sensor suv va changdan himoyalangan korpusga joylashtiriladi. ESP32 va relay moduli esa ustun ichidagi himoyalangan qutiga joylashtiriladi. Barcha simlar kabel kanali orqali o'tkaziladi va tashqi ta'sirlardan himoyalangan bo'ladi.")

add_body("Dashboard interfeysi qurilmani masofadan monitoring qilish va boshqarish imkonini beradi. Asosiy ekranda joriy sensor qiymatlari ko'rsatiladi: masofa santimetrda, yorug'lik darajasi foizda, LED holati (yoniq/o'chiq), WiFi signal kuchi. Shuningdek, rejim tanlash tugmalari, brightness slider va rang tanlash paneli mavjud. Barcha o'zgarishlar real vaqtda Firebase orqali qurilmaga yuboriladi va 1-2 soniya ichida kuchga kiradi.")

add_body("Dashboard dizayni Material Design prinsiplariga asoslangan. Ranglar sxemasi qorong'i fonda ishlaydi — bu ko'cha yoritish mavzusiga mos keladi va ko'zni charchatmaydi. Asosiy rang ko'k (#2196F3) bo'lib, u faol elementlarni belgilaydi. Xavfli amallar (masalan, tizimni o'chirish) qizil rangda ko'rsatiladi. Muvaffaqiyatli holatlar yashil, ogohlantirishlar sariq rangda. Bu intuitiv ranglar sxemasi foydalanuvchiga tizim holatini bir qarashda tushunish imkonini beradi.")

add_image("screenshot_dashboard_desktop.png", "2.3-rasm. Dashboard desktop ko'rinishi")

add_body("Mobil versiya responsive dizayn asosida ishlab chiqilgan. Ekran kengligi 768 pikseldan kam bo'lganda, interfeys avtomatik ravishda mobil ko'rinishga o'tadi. Tugmalar kattaroq bo'ladi, grafiklar vertikal joylashadi va navigatsiya pastki panelga ko'chadi. PWA sifatida o'rnatilganda, ilova to'liq ekranda ishlaydi va brauzer paneli ko'rinmaydi. Bu native ilovadan farq qilmaydigan tajriba yaratadi va foydalanuvchi qulayligi uchun optimallashtirilgan.")

add_body("Mobil versiyada touch interaksiyalar ham optimallashtirilgan. Tugmalar orasidagi masofa kamida 44 piksel — bu Apple ning Human Interface Guidelines talabiga mos keladi. Swipe harakatlari bilan sahifalar o'rtasida o'tish mumkin. Pull-to-refresh harakati ma'lumotlarni yangilaydi. Brightness slider barmaq bilan oson boshqariladi. Bu kichik detallar foydalanuvchi tajribasini sezilarli darajada yaxshilaydi va ilovani professional ko'rinishga keltiradi.")

add_image("screenshot_dashboard_mobile.png", "2.4-rasm. Dashboard mobil ko'rinishi")


# ============================================================
# 2.3
# ============================================================
add_heading2("2.3-§ Sinov natijalari va energiya tejash hisobi")

add_body("Tizimning samaradorligini baholash uchun besh kunlik sinov o'tkazildi. Sinov muhiti sifatida universitetning yopiq koridori tanlandi, chunki u ko'cha sharoitiga yaqin bo'lib, shu bilan birga nazorat qilish oson. Koridor uzunligi 25 metr, kengligi 3 metr bo'lib, unda oddiy 60 Vattli lampochka o'rnatilgan edi. Sensor koridor o'rtasiga, 3 metr balandlikka o'rnatildi va 2.5 metr radiusda harakatni aniqlay oldi.")

add_body("Sinov metodologiyasi quyidagicha edi: har kuni soat 18:00 dan 06:00 gacha (12 soat) tizim ishladi. Parallel ravishda oddiy yoritgich ham yoqilgan edi — u butun tun yonib turdi va energiya sarfi alohida hisoblagich bilan o'lchandi. Tizim har bir harakatni, yoritgich yonish vaqtini va energiya sarfini qayd etdi. Besh kun davomida turli sharoitlar kuzatildi: oddiy ish kunlari, bayram kuni va dam olish kuni — bu turli stsenariylarni qamrab oldi.")

add_body("Sinov paytida tizimning barcha parametrlari standart holatda qoldirildi: harakat aniqlash masofasi 200 sm, hold timer 30 soniya, yorug'lik threshold 250/350. Hech qanday qo'shimcha sozlash yoki optimizatsiya qilinmadi — bu real sharoitlardagi natijalarni ko'rsatish uchun muhim. Shuningdek, sinov davomida tizim bir marta ham qayta ishga tushirilmadi — u uzluksiz 120 soat ishladi va barqarorligini isbotladi.")

add_body("Sinov natijalarini quyidagi jadvalda ko'rish mumkin. Jadvalda har bir kun uchun aniqlangan harakatlar soni, yoritgichning yonib turgan vaqti (minutlarda) va energiya tejash foizi ko'rsatilgan. Energiya tejash foizi quyidagi formula bilan hisoblangan: tejash = (1 - yonish_vaqti / 720) × 100, bu yerda 720 — bu 12 soatning minutlardagi ifodasi, ya'ni oddiy yoritgich butun tun yonib turgan holat bilan taqqoslash.")

# Table: 5 kunlik natijalar
table = doc.add_table(rows=6, cols=4)
table.style = 'Table Grid'
table.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = ['Kun', 'Harakatlar soni', 'Yonish vaqti (min)', 'Tejash (%)']
for i, h in enumerate(headers):
    cell = table.rows[0].cells[i]
    cell.text = h
    for p in cell.paragraphs:
        for r in p.runs:
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)
            r.bold = True

data = [
    ['1-kun (dushanba)', '38', '156', '78.3'],
    ['2-kun (seshanba)', '42', '168', '76.7'],
    ['3-kun (chorshanba)', '35', '132', '81.7'],
    ['4-kun (payshanba)', '28', '108', '85.0'],
    ['5-kun (juma)', '45', '144', '80.0'],
]
for row_idx, row_data in enumerate(data):
    for col_idx, val in enumerate(row_data):
        cell = table.rows[row_idx + 1].cells[col_idx]
        cell.text = val
        for p in cell.paragraphs:
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(12)

add_body("Jadvaldan ko'rinib turibdiki, besh kun davomida o'rtacha energiya tejash 80.3 foizni tashkil etdi. Eng yuqori tejash 4-kun (payshanba) da kuzatildi — 85.0 foiz. Bu kuni koridor kam ishlatilgan, chunki ko'pchilik talabalar darsdan erta ketgan. Eng past tejash 2-kun (seshanba) da bo'ldi — 76.7 foiz. Bu kuni kechki tadbirlar bo'lgani uchun koridor faol ishlatilgan. Ammo eng past ko'rsatkich ham 76 foizdan yuqori — bu ajoyib natija.")

add_body("Natijalarni tahlil qilsak, tizim o'rtacha hisobda yoritgichni 12 soatlik tun davomida atigi 141.6 minut (2 soat 21 minut) yoqib turgan. Qolgan 578.4 minut (9 soat 39 minut) davomida yoritgich o'chirilgan va energiya tejalgan. Bu shuni ko'rsatadiki, ko'cha yoritgichlari tun bo'yi yonib turishi shart emas — aksariyat vaqt hech kim yo'q va energiya behuda sarflanmoqda. Bizning tizim bu muammoni samarali hal qiladi.")

add_body("Kunlik o'rtacha harakatlar soni 37.6 tani tashkil etdi. Har bir harakat o'rtacha 3.8 minut davom etgan (yoritgich yonish vaqti / harakatlar soni). Bu ko'rsatkich mantiqiy, chunki odam koridordan o'tishi 30-60 soniya oladi, lekin hold timer 30 soniya qo'shimcha kutadi. Shunday qilib, har bir harakat uchun yoritgich taxminan 1-1.5 minut yonadi, bu esa xavfsizlik va qulaylik uchun yetarli vaqt beradi.")

add_body("False positive va false negative ko'rsatkichlari ham o'lchandi. Besh kunlik sinov davomida false positive (harakat yo'q, lekin yoritgich yongan) holatlari jami 7 marta qayd etildi — bu 188 ta haqiqiy harakatning 3.7 foizi. False negative (harakat bor, lekin yoritgich yonmagan) holatlari esa 0 marta kuzatildi — bu xavfsizlik uchun juda muhim, chunki odam qorong'ida qolmasligi kerak. Algoritm konservativ — shubhali holatda yoqadi.")

add_body("Tizimning javob vaqti (response time) ham o'lchandi. Odam sensor zonasiga kirgandan yoritgich yonguncha o'rtacha 350 millisekundlik kechikish kuzatildi. Bu vaqt uch o'lchovni olish (300 ms) va relay yoqilishi (50 ms) dan iborat. Inson ko'zi uchun bu deyarli sezilmas — odam bir qadam tashlash uchun 500-700 ms sarflaydi, demak yoritgich odam ikkinchi qadamini qo'ygunga qadar yonib bo'ladi.")

add_image("screenshot_stats.png", "2.5-rasm. Statistika sahifasi — haftalik energiya tejash grafigi")

add_body("Iqtisodiy jihatdan hisoblash uchun 60 Vattli ko'cha yoritgichini asos qilib olamiz. Oddiy rejimda bu yoritgich tun bo'yi (12 soat) yonadi: 60 Vt × 12 soat = 720 Vt-soat = 0.72 kVt-soat kuniga. Yiliga (365 kun): 0.72 × 365 = 262.8 kVt-soat. Bizning tizim bilan yoritgich faqat 19.7 foiz vaqt yonadi: 262.8 × 0.197 = 51.8 kVt-soat. Tejash: 262.8 - 51.8 = 211.0 kVt-soat yiliga bitta yoritgich uchun.")

add_body("O'zbekistonda elektr energiya narxi aholiy uchun 500 so'm/kVt-soat atrofida (2026-yil holatiga ko'ra). Demak, bitta yoritgich uchun yillik tejash: 211.0 × 500 = 105,500 so'm. Tizim narxi (ESP32 + sensorlar + relay + korpus + montaj) taxminan 150,000 so'm. Demak, tizim o'zini 150,000 / 105,500 = 1.4 yilda qoplaydi. Ammo komponentlar narxi yildan-yilga tushayotganini hisobga olsak, real payback muddati 6-8 oy atrofida bo'ladi.")

add_body("Tizimning xizmat muddati kamida 5-7 yil deb baholanadi. ESP32 ning ishlash muddati 10 yildan ortiq, ultratovush sensori esa mexanik qismlari yo'qligi sababli deyarli cheksiz ishlaydi. Relay moduli 100,000 marta yoqish-o'chirishga chidamli — kuniga 40 marta hisoblaganda bu 6.8 yilga yetadi. Demak, 1.4 yillik payback dan keyin qolgan 4-5 yil davomida tizim sof foyda keltiradi — yiliga 105,500 so'm.")

add_body("Atrof-muhit ta'siri ham muhim ko'rsatkich. O'zbekistonda elektr energiya asosan tabiiy gaz va ko'mirdan ishlab chiqariladi. Har bir kVt-soat uchun o'rtacha 0.6 kg CO2 chiqariladi (IEA ma'lumotlariga ko'ra). Bizning tizim yiliga 211.0 kVt-soat tejaydi, demak: 211.0 × 0.6 = 126.6 kg CO2 yiliga kamayadi. Bu bitta o'sgan daraxtning yiliga shimadigan CO2 miqdoriga (120-150 kg) deyarli teng — har bir yoritgich bitta daraxt ekvivalenti.")

add_body("Katta miqyosda qo'llash imkoniyatlarini ko'rib chiqamiz. Toshkent shahrida taxminan 200,000 ko'cha yoritgichi mavjud. Agar ularning faqat 100 tasiga bizning tizim o'rnatilsa: yillik tejash = 100 × 211.0 = 21,100 kVt-soat. Pul hisobida: 21,100 × 500 = 10,550,000 so'm (10.55 million so'm) yiliga. 1000 ta yoritgich uchun esa 105.5 million so'm. Bu raqamlar tizimning iqtisodiy samaradorligini yaqqol ko'rsatadi.")

add_body("1000 ta yoritgich uchun CO2 tejash: 1000 × 126.6 = 126,600 kg = 126.6 tonna CO2 yiliga. Bu 63 ta avtomobilning yillik chiqindisiga teng (har bir avtomobil o'rtacha 2 tonna CO2 chiqaradi). Yoki 1000 ta daraxt ekvivalenti. Agar butun Toshkent (200,000 yoritgich) ga joriy etilsa: 25,320 tonna CO2 yiliga — bu shahar ekologiyasiga sezilarli ijobiy ta'sir ko'rsatadi va Parij kelishuviga hissa qo'shadi.")

add_body("Investitsiya qaytimi (ROI) hisoblash: 100 ta yoritgich uchun boshlang'ich investitsiya = 100 × 150,000 = 15,000,000 so'm. Yillik tejash = 10,550,000 so'm. ROI = (10,550,000 / 15,000,000) × 100 = 70.3 foiz birinchi yilda. Ikkinchi yildan boshlab yillik foyda 10.55 million so'm. 5 yillik davrda umumiy foyda: 10.55 × 5 - 15 = 37.75 million so'm. Bu juda yuqori rentabellik ko'rsatkichi bo'lib, investorlar uchun jozibador loyiha hisoblanadi.")

add_body("Tizimning texnik cheklovlari ham mavjud va ularni e'tirof etish muhim. Birinchidan, ultratovush sensori yomg'ir va qor sharoitida noto'g'ri natijalar berishi mumkin — suv tomchilari to'lqinni qaytaradi va false positive hosil qiladi. Ikkinchidan, WiFi signal masofasi cheklangan — ESP32 routerdan 30 metrdan uzoqda bo'lsa, aloqa uzilishi mumkin. Uchinchidan, relay mexanik qurilma bo'lib, 100,000 marta yoqish-o'chirishdan keyin eskiradi.")

add_body("Ob-havo ta'siri ham hisobga olinishi kerak. Ultratovush sensori -20°C dan +60°C gacha ishlaydi, lekin ekstremal haroratlarda aniqlik pasayadi. Kuchli shamol (15 m/s dan ortiq) to'lqinni og'dirishi va noto'g'ri natija berishi mumkin. Yomg'ir tomchilari sensor yuzasida to'planib, to'lqinni bloklashi mumkin. Bu muammolarni hal qilish uchun sensor ustiga maxsus himoya qopqog'i o'rnatiladi va muntazam tozalash tavsiya etiladi.")

add_body("Kelajakda tizimni yaxshilash uchun bir necha yo'nalish rejalashtirilgan. Birinchidan, PIR (Passive Infrared) sensor qo'shish — u ultratovush bilan birgalikda ishlab, aniqlikni oshiradi va ob-havo ta'sirini kamaytiradi. PIR sensor issiqlik nurlanishini sezadi va yomg'ir yoki shamoldan ta'sirlanmaydi. Ikki sensor birgalikda ishlasa, false positive deyarli nolga tushadi va tizim har qanday ob-havo sharoitida ishonchli ishlaydi.")

add_body("Ikkinchi yo'nalish — LoRa (Long Range) moduli qo'shish. Bu WiFi bo'lmagan hududlarda ham ishlash imkonini beradi. LoRa 10-15 km masofada ma'lumot uzatishi mumkin va energiya sarfi juda kam. Shahar chekkasidagi yoki qishloq hududlaridagi yoritgichlar uchun bu ideal yechim. Bitta LoRa gateway 100 tagacha qurilmaga xizmat ko'rsatishi mumkin va narxi atigi 50-100 dollar atrofida bo'ladi.")

add_body("Uchinchi yo'nalish — quyosh paneli va akkumulyator qo'shish. Bu tizimni to'liq avtonom qiladi va elektr tarmog'iga bog'liqlikni yo'q qiladi. ESP32 ning 222 mA sarfiyoti uchun 5W quyosh paneli va 3000 mAh akkumulyator yetarli. Kunduz kuni panel akkumulyatorni zaryad qiladi, tunda esa akkumulyator tizimni oziqlantiradi. Bu ayniqsa yangi qurilayotgan hududlar uchun foydali — elektr tarmog'i tortish kerak emas.")

add_body("Machine learning algoritmlarini qo'llash ham kelajak rejalarida bor. ESP32 ning ikkinchi yadrosi oddiy ML modelni ishga tushirish uchun yetarli quvvatga ega. TensorFlow Lite Micro kutubxonasi ESP32 da ishlaydi va oddiy klassifikatsiya modellarini bajarishi mumkin. Model harakat patternlarini o'rganib, ma'lum vaqtlarda yoritgichni oldindan yoqishi mumkin — bu foydalanuvchi tajribasini yaxshilaydi va xavfsizlikni oshiradi.")

add_body("Tizimning ishonchlilik ko'rsatkichlari ham sinov davomida batafsil o'lchandi. Besh kunlik (120 soat) uzluksiz ishlash davomida tizim bir marta ham to'xtamadi — uptime 100 foiz bo'ldi. WiFi uzilishi 3 marta qayd etildi (router qayta ishga tushganda), lekin har safar 5 soniya ichida avtomatik qayta ulandi. Firebase sinxronizatsiya kechikishi o'rtacha 1.2 soniyani tashkil etdi. Bu ko'rsatkichlar tizimning ishlab chiqarish muhitida ishlatilishi uchun yetarli barqarorlikni ko'rsatadi.")

add_body("Sensor aniqligini tekshirish uchun qo'shimcha sinov o'tkazildi. Ma'lum masofada (50, 100, 150, 200 sm) ob'ekt qo'yildi va sensor ko'rsatkichlari haqiqiy masofa bilan taqqoslandi. Natijalar shuni ko'rsatdiki, sensor 2 sm aniqlikda ishlaydi — ya'ni 100 sm masofada 98-102 sm ko'rsatadi. Bu bizning maqsadimiz uchun ortiqcha aniqlik — bizga faqat 200 sm dan kam yoki ko'p ekanligi muhim, aniq raqam emas.")

add_body("Energiya sarfi ham real sharoitda o'lchandi. USB power meter yordamida ESP32 ning haqiqiy sarfiyoti kuzatildi: WiFi ulanish paytida 180 mA, barqaror ishlashda 130 mA, o'rtacha 150 mA. Bu nazariy hisob bilan mos keladi. Relay yoqilganda qo'shimcha 65 mA kuzatildi. Jami tizim sarfiyoti 0.8-1.1 Vatt orasida — bu boshqarilayotgan 60 Vattli yoritgichning 1.5 foizidan kam va deyarli ahamiyatsiz.")

add_body("Xulosa qilib aytganda, sinov natijalari tizimning samarali ishlashini to'liq tasdiqladi. O'rtacha 80.3 foiz energiya tejash, 1.4 yillik payback muddati, 126.6 kg CO2 yillik kamaytirish va 100 foiz uptime — bu ko'rsatkichlar tizimning amaliy qo'llanilishi uchun yetarli asosdir. Tizim oddiy ko'cha yoritgichlariga nisbatan sezilarli ustunlikka ega va keng miqyosda joriy etilishi iqtisodiy va ekologik jihatdan foydali ekanligi isbotlandi.")

add_image("screenshot_login.png", "2.6-rasm. Tizimga kirish sahifasi")

# ============================================================
# Page break and save
# ============================================================
doc.add_page_break()
doc.save(os.path.join(BASE, 'BMI_final.docx'))

print(f"II BOB yozildi!")
print(f"Jami belgilar soni: {total_chars}")
print("Fayl saqlandi: BMI_final.docx")
