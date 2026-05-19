from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

doc = Document('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_final.docx')
IMG_DIR = '/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/images/'
total_chars = 0

def add_h1(text):
    p = doc.add_heading(text, level=1)
    for r in p.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(14)
        r.font.color.rgb = None

def add_h2(text):
    p = doc.add_heading(text, level=2)
    for r in p.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(14)
        r.font.color.rgb = None

def add_body(text):
    global total_chars
    total_chars += len(text)
    p = doc.add_paragraph(text)
    p.paragraph_format.first_line_indent = Cm(1.25)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    for r in p.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(14)

def add_image(filename, caption):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0)
    run = p.add_run()
    run.add_picture(os.path.join(IMG_DIR, filename), width=Cm(14))
    cp = doc.add_paragraph(caption)
    cp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    cp.paragraph_format.first_line_indent = Cm(0)
    for r in cp.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        r.italic = True

# ============ I BOB ============
add_h1("I BOB. SMART STREET TIZIMIDA YORITISH TIZIMLARI TIZIMLI TAHLILI VA MASALANING QO'YILISHI")

# ============ 1.1 ============
add_h2("1.1-§ Smart Street tizimlarida energiya tejamkor yoritish tizimlari va ularning ahamiyati")

add_body("Ko'cha yoritish tizimlari insoniyat tarixida muhim o'rin tutadi. Qadimgi davrlardan boshlab odamlar tungi vaqtda xavfsizlikni ta'minlash va harakatni osonlashtirish maqsadida turli yoritish usullaridan foydalanganlar. Dastlabki ko'cha yoritgichlari sifatida yog'och mash'alalar, keyin esa gaz chiroqlari ishlatilgan. XIX asrning oxirida Thomas Edison tomonidan elektr lampochkasining ixtiro qilinishi ko'cha yoritish sohasida inqilob yasadi. XX asrning boshlarida ko'plab shaharlarda elektr yoritish tizimlari joriy etildi va bu shahar infrastrukturasining ajralmas qismiga aylandi. Zamonaviy ko'cha yoritish tizimlari esa LED texnologiyasi, aqlli boshqaruv tizimlari va IoT yechimlarini o'z ichiga oladi.")

add_body("Ko'cha yoritishning rivojlanish tarixi bir necha muhim bosqichlarni o'z ichiga oladi. Birinchi bosqich XVII-XVIII asrlarda gaz lampalarining paydo bo'lishi bilan bog'liq bo'lib, London va Parij shaharlari birinchilardan bo'lib ko'cha gaz yoritgichlarini o'rnatgan. Ikkinchi bosqich XIX asr oxirida elektr lampalarning ixtiro qilinishi bilan boshlangan. Uchinchi bosqich XX asrning ikkinchi yarmida natriy va simob lampalarning keng tarqalishi bilan belgilanadi. To'rtinchi bosqich XXI asrda LED texnologiyasining paydo bo'lishi va aqlli boshqaruv tizimlarining joriy etilishi bilan boshlanadi. Har bir bosqich energiya samaradorligini oshirish va xizmat ko'rsatish xarajatlarini kamaytirish yo'nalishida sezilarli yutuqlarga erishgan.")

add_body("Hozirgi kunda dunyo bo'ylab ko'cha yoritish tizimlari jiddiy muammolarga duch kelmoqda. Birinchidan, energiya isrofi masalasi dolzarb hisoblanadi. An'anaviy ko'cha yoritgichlari tun bo'yi uzluksiz yonib turadi, holbuki ko'cha bo'sh bo'lgan vaqtlarda yoritishga ehtiyoj yo'q. Statistik ma'lumotlarga ko'ra, shahar elektr energiyasining 40 foizgacha qismi ko'cha yoritishiga sarflanadi. Ikkinchidan, ko'plab shaharlarda hali ham eskirgan natriy va simob lampalar ishlatilmoqda, ularning energiya samaradorligi past va ekologik jihatdan zararli. Uchinchidan, markazlashtirilgan boshqaruv tizimlarining yo'qligi tufayli nosoz yoritgichlarni aniqlash va ta'mirlash uzoq vaqt talab etadi.")

add_body("Energiya isrofining iqtisodiy oqibatlari ham juda katta. Dunyo bo'ylab ko'cha yoritishiga yiliga taxminan 120 milliard kVt*soat elektr energiya sarflanadi, bu esa 40 milliard dollardan ortiq xarajatni tashkil etadi. Rivojlanayotgan mamlakatlarda bu xarajatlar shahar byudjetining 20-40 foizini egallaydi. Bundan tashqari, ortiqcha energiya ishlab chiqarish atmosferaga qo'shimcha karbonat angidrid chiqarilishiga olib keladi. Birlashgan Millatlar Tashkilotining hisobotiga ko'ra, ko'cha yoritish tizimlarini optimallashtirish orqali global miqyosda yiliga 150 million tonna CO2 emissiyasini kamaytirish mumkin.")

add_body("O'zbekiston Respublikasida ko'cha yoritish tizimlarining holati alohida e'tiborga loyiq. Faqat Toshkent shahrida 150 mingdan ortiq ko'cha yoritgichlari mavjud bo'lib, ularning aksariyati oddiy taymer yordamida boshqariladi. Bu taymerlar mavsumiy o'zgarishlarni hisobga olmaydi va ko'pincha kunduz kuni ham yoritgichlar yonib turishi kuzatiladi. Mamlakatimizda energiya resurslarining cheklanganligi sharoitida bunday isrofgarchilik iqtisodiy va ekologik jihatdan katta zarar keltiradi. Hukumat tomonidan energiya tejamkorlik dasturlari qabul qilingan bo'lsa-da, ko'cha yoritish sohasida zamonaviy texnologiyalarning joriy etilishi hali boshlang'ich bosqichda.")

add_body("O'zbekiston Respublikasi Prezidentining 2019-yil 22-avgustdagi qaroriga muvofiq, energiya tejamkorlik va qayta tiklanuvchi energiya manbalarini rivojlantirish bo'yicha keng ko'lamli dastur qabul qilingan. Bu dastur doirasida ko'cha yoritish tizimlarini modernizatsiya qilish ham nazarda tutilgan. Samarqand, Buxoro va Navoiy shaharlarida pilot loyihalar amalga oshirilgan bo'lib, LED yoritgichlarga o'tish 35-45 foiz energiya tejash imkonini bergan. Biroq aqlli boshqaruv tizimlari hali keng joriy etilmagan va bu yo'nalishda ilmiy tadqiqotlar olib borish zarur.")

add_body("Smart City yoki aqlli shahar konsepsiyasi XXI asrning eng dolzarb yo'nalishlaridan biri hisoblanadi. Bu konsepsiya shahar infrastrukturasining barcha elementlarini axborot texnologiyalari yordamida birlashtirish va optimallashtirish g'oyasiga asoslanadi. Internet of Things yani IoT texnologiyalari aqlli shahar konsepsiyasining asosiy tarkibiy qismi bo'lib, turli sensorlar, aktuatorlar va boshqaruv tizimlarini yagona tarmoqqa ulash imkonini beradi. Ko'cha yoritish tizimi aqlli shaharning eng ko'p tarqalgan va samarali qo'llaniladigan yo'nalishlaridan biri hisoblanadi, chunki u nisbatan oddiy infratuzilmani talab qiladi va tezkor iqtisodiy samara beradi.")

add_body("IoT texnologiyalarining ko'cha yoritish tizimlariga qo'llanilishi bir necha muhim afzalliklarni beradi. Birinchidan, har bir yoritgichning holatini real vaqt rejimida masofadan kuzatish mumkin bo'ladi. Ikkinchidan, nosozliklarni avtomatik aniqlash va texnik xizmat ko'rsatish jarayonini optimallashtirish imkoniyati paydo bo'ladi. Uchinchidan, energiya iste'moli haqida batafsil statistik ma'lumotlar yig'iladi va tahlil qilinadi. To'rtinchidan, yoritish rejimlarini masofadan o'zgartirish va individual sozlash mumkin bo'ladi. Beshinchidan, tizim kengaytiriladigan bo'lib, yangi yoritgichlarni osongina qo'shish mumkin.")

add_body("Energiya tejash yondashuvlari ko'cha yoritish sohasida bir necha yo'nalishda rivojlanmoqda. LED texnologiyasiga o'tish birinchi va eng muhim qadam hisoblanadi, chunki LED lampalar an'anaviy lampalarga nisbatan 50-70 foiz kam energiya sarflaydi va xizmat muddati 5-10 baravar uzoq. Dimming yani yorug'lik darajasini pasaytirish texnologiyasi tun yarmida yoki kam odam yurgan vaqtlarda yoritish intensivligini kamaytirish orqali qo'shimcha 30-40 foiz energiya tejash imkonini beradi. Sensorli boshqaruv tizimlari harakat yoki transport mavjudligini aniqlash orqali faqat kerak bo'lganda to'liq quvvatda yoritish prinsipiga asoslanadi.")

add_body("Jadval bo'yicha boshqarish usuli oldindan belgilangan vaqt jadvaliga muvofiq yoritgichlarni yoqish va o'chirish yoki yorug'lik darajasini o'zgartirish imkonini beradi. Bu usul oddiy taymerlardan farqli ravishda mavsumiy o'zgarishlarni, dam olish kunlarini va maxsus tadbirlarni hisobga olishi mumkin. Adaptiv boshqaruv esa eng ilg'or yondashuv bo'lib, real vaqt rejimida turli sensorlardan olingan ma'lumotlarni tahlil qilish va sun'iy intellekt algoritmlaridan foydalanish orqali optimal yoritish rejimini tanlaydi. Bu yondashuv ob-havo sharoitlari, transport oqimi va piyodalar harakatini bir vaqtda hisobga oladi.")

add_body("Dunyo bozorida bir qancha yirik kompaniyalar aqlli ko'cha yoritish yechimlari taklif etadi. Philips CityTouch platformasi eng keng tarqalgan tijorat yechimlaridan biri bo'lib, u markazlashtirilgan bulutli boshqaruv, har bir yoritgichning individual monitoringi va energiya iste'molini real vaqtda kuzatish imkoniyatlarini taqdim etadi. Tizim GSM yoki LoRaWAN protokollari orqali ishlaydi va katta shaharlar uchun mo'ljallangan. Telensa kompaniyasining PLANet platformasi esa LoRa texnologiyasiga asoslangan bo'lib, past energiya sarfi va keng qamrov bilan ajralib turadi. U ayniqsa katta hududlarni qamrab olishda samarali.")

add_body("Tvilight kompaniyasi Gollandiyada ishlab chiqilgan bo'lib, sensorli aqlli yoritish tizimlarini taklif etadi. Ularning CitySense platformasi radar sensorlari yordamida piyodalar va transport vositalarini aniqlaydi va yoritish darajasini real vaqtda moslashtiradi. Ochiq kodli loyihalar orasida OpenStreetLight va SmartLight platformalari alohida e'tiborga loyiq. Bu loyihalar Arduino va Raspberry Pi kabi arzon mikrokontrollerlar asosida qurilgan bo'lib, kichik shaharlar va qishloqlar uchun tejamkor yechim sifatida ishlatilishi mumkin. Ular hamjamiyat tomonidan qo'llab-quvvatlanadi va doimiy ravishda yangilanib boradi.")

# Table: Mavjud yechimlarni qiyoslash
table = doc.add_table(rows=5, cols=5)
table.style = 'Table Grid'
headers = ['Yechim', 'Protokol', 'Energiya tejash', 'Narx', 'Miqyos']
for i, h in enumerate(headers):
    table.rows[0].cells[i].text = h
data = [
    ['Philips CityTouch', 'GSM/LoRaWAN', '30-40%', 'Yuqori', 'Katta shaharlar'],
    ['Telensa PLANet', 'LoRa', '35-50%', "O'rtacha", 'Katta hududlar'],
    ['Tvilight CitySense', 'Zigbee/WiFi', '40-60%', 'Yuqori', "O'rta shaharlar"],
    ['Ochiq kodli (Arduino)', 'WiFi/LoRa', '50-70%', 'Past', 'Kichik loyihalar'],
]
for row_idx, row_data in enumerate(data, 1):
    for col_idx, val in enumerate(row_data):
        table.rows[row_idx].cells[col_idx].text = val

add_body("Yuqoridagi jadvalda ko'rsatilganidek, tijorat yechimlari yuqori narxga ega bo'lib, asosan yirik shaharlar uchun mo'ljallangan. Ochiq kodli yechimlar esa arzon va moslashuvchan bo'lsa-da, professional qo'llab-quvvatlash va keng miqyosda joriy etish imkoniyatlari cheklangan. Bizning loyihamiz aynan shu bo'shliqni to'ldirish maqsadida ishlab chiqilgan bo'lib, ESP32 mikrokontrolleri va Firebase bulut platformasi asosida arzon, ishonchli va kengaytiriladigan yechim taklif etadi. Tizim ochiq kodli bo'lib, mahalliy sharoitlarga osongina moslashtirilishi mumkin.")

add_body("Xalqaro tajriba ko'rsatadiki, aqlli ko'cha yoritish tizimlari sezilarli iqtisodiy samara beradi. Barselona shahri 2012-yildan boshlab aqlli yoritish tizimini joriy etgan va yillik energiya xarajatlarini 30 foizga qisqartirgan. Los-Anjeles shahri 2009-yildan 2016-yilgacha 215 ming ko'cha yoritgichini LED texnologiyasiga almashtirgan va yillik 9 million dollar tejagan. Kopengagen shahri velosiped yo'laklari bo'ylab sensorli yoritish tizimini o'rnatgan bo'lib, velosipedchi yaqinlashganda yoritish kuchayadi va uzoqlashganda pasayadi. Bu yondashuv 65 foiz energiya tejash imkonini bergan.")

add_body("Hindiston hukumati UJALA dasturi doirasida millionlab LED lampalarni tarqatgan va ko'cha yoritish tizimlarini modernizatsiya qilgan. Bu dastur yiliga 40 milliard kVt*soat elektr energiyasini tejash imkonini bergan. Janubiy Koreya, Yaponiya va Xitoy kabi mamlakatlar ham aqlli shahar loyihalarida ko'cha yoritish tizimlarini birinchi navbatda modernizatsiya qilmoqda. Bu tajribalar shuni ko'rsatadiki, dastlabki investitsiya 2-3 yil ichida o'zini oqlaydi va uzoq muddatda sezilarli iqtisodiy samara beradi. O'zbekiston uchun ham bu yo'nalish istiqbolli hisoblanadi.")

add_body("Singapur shahri aqlli yoritish sohasida eng ilg'or tajribaga ega mamlakatlardan biri hisoblanadi. Ularning Smart Nation dasturi doirasida barcha ko'cha yoritgichlari sensorlar bilan jihozlangan va markazlashtirilgan boshqaruv tizimiga ulangan. Tizim nafaqat energiya tejash, balki xavfsizlik kameralari, atrof-muhit sensorlari va WiFi hotspot funksiyalarini ham bajaradi. Dubai shahri esa 2030-yilga qadar barcha ko'cha yoritgichlarini aqlli tizimlarga almashtirish rejasini e'lon qilgan. Bu loyiha yiliga 200 million dirham tejash imkonini berishi kutilmoqda.")

add_body("IoT protokollari tanlovi aqlli yoritish tizimining samaradorligiga bevosita ta'sir qiladi. WiFi protokoli eng keng tarqalgan simsiz aloqa standarti bo'lib, yuqori ma'lumot uzatish tezligi va mavjud infratuzilmadan foydalanish imkoniyati bilan ajralib turadi. Biroq WiFi ning energiya sarfi nisbatan yuqori va qamrov masofasi cheklangan bo'lib, 50-100 metrni tashkil etadi. LoRa yani Long Range protokoli past energiya sarfi va 10-15 kilometrgacha qamrov masofasi bilan ko'cha yoritish tizimlari uchun juda mos keladi, lekin ma'lumot uzatish tezligi past va maxsus gateway qurilmalari talab etiladi.")

add_body("Zigbee protokoli mesh tarmoq arxitekturasiga asoslangan bo'lib, har bir qurilma signal retranslyatori vazifasini bajarishi mumkin. Bu xususiyat katta hududlarda tarmoq qamrovini kengaytirish imkonini beradi. Biroq Zigbee ning ma'lumot uzatish tezligi past va maxsus koordinator qurilmasi talab etiladi. Bizning loyihamizda WiFi protokoli tanlangan, chunki ESP32 mikrokontrollerida WiFi moduli o'rnatilgan, Firebase bulut platformasi bilan integratsiya oson va real vaqt rejimida ikki tomonlama ma'lumot almashish imkoniyati mavjud. Bundan tashqari, loyiha maket darajasida bo'lgani uchun WiFi ning qamrov cheklovi muhim emas.")

add_body("MQTT protokoli IoT tizimlarida keng qo'llaniladigan yengil vaznli xabar almashish protokoli hisoblanadi. U publish-subscribe modeliga asoslanadi va past tarmoqli kengligi sharoitlarida samarali ishlaydi. CoAP protokoli esa HTTP ga o'xshash, lekin IoT qurilmalari uchun optimallashtirilgan protokol bo'lib, UDP transport qatlami ustida ishlaydi. Bizning loyihamizda Firebase Realtime Database WebSocket protokoli orqali real vaqt sinxronizatsiyani ta'minlaydi, bu MQTT va CoAP ga muqobil yechim sifatida ishlatiladi va qo'shimcha broker server talab etmaydi.")

add_body("Energiya tejamkor yoritish tizimlarining iqtisodiy samaradorligini baholashda bir necha ko'rsatkichlar hisobga olinadi. Birinchisi, dastlabki investitsiya qiymati bo'lib, u sensorlar, kontrollerlar, LED yoritgichlar va o'rnatish xarajatlarini o'z ichiga oladi. Ikkinchisi, operatsion xarajatlarning kamayishi bo'lib, u energiya tejash va texnik xizmat ko'rsatish xarajatlarining qisqarishi hisobiga shakllanadi. Uchinchisi, investitsiyaning qaytish muddati bo'lib, u odatda 2-5 yilni tashkil etadi. To'rtinchisi, tizimning xizmat muddati bo'lib, LED yoritgichlar 50-100 ming soat ishlash qobiliyatiga ega.")

add_body("Zamonaviy aqlli yoritish tizimlari nafaqat energiya tejash, balki qo'shimcha funksiyalarni ham bajarishi mumkin. Masalan, atrof-muhit monitoringi sensorlari yordamida havo sifati, shovqin darajasi va haroratni o'lchash mumkin. Transport oqimini kuzatish va statistik ma'lumotlarni yig'ish shahar transportini rejalashtirish uchun foydali. Favqulodda vaziyatlarda yoritish rejimini o'zgartirish xavfsizlik xizmatlariga yordam beradi. Shuningdek, aqlli yoritgichlar WiFi hotspot, elektr transport zaryadlash stantsiyasi yoki reklama paneli sifatida ham ishlatilishi mumkin.")

add_body("Xulosa qilib aytganda, aqlli ko'cha yoritish tizimlari zamonaviy shahar infrastrukturasining ajralmas qismiga aylanmoqda. Ular energiya tejash, xavfsizlikni oshirish va shahar muhitini yaxshilash kabi bir necha muhim vazifalarni bir vaqtda hal etadi. O'zbekiston uchun bu texnologiyalarni joriy etish nafaqat iqtisodiy, balki ekologik jihatdan ham muhim ahamiyatga ega. Bizning loyihamiz aynan shu yo'nalishda amaliy yechim taklif etadi va mahalliy sharoitlarga moslashtirilgan arzon, ishonchli va kengaytiriladigan tizim yaratishni maqsad qiladi.")

add_body("Smart Street yoritish tizimlarining rivojlanish tendensiyalari sun'iy intellekt va mashinaviy o'rganish texnologiyalarining qo'llanilishi tomon yo'nalgan. Kelajakda yoritish tizimlari nafaqat sensorlar ma'lumotlariga, balki tarixiy statistikaga asoslangan prognozlash algoritmlariga ham tayanadi. Masalan, tizim ma'lum bir ko'chada qaysi soatlarda odamlar ko'p bo'lishini oldindan bashorat qilishi va yoritish rejimini muvofiq ravishda sozlashi mumkin. Bundan tashqari, bir nechta yoritgichlarning birgalikda ishlashi va o'zaro muvofiqlashtirilishi energiya tejashni yanada oshiradi.")

add_body("Bulut texnologiyalari aqlli yoritish tizimlarining markazlashtirilgan boshqaruvini ta'minlashda muhim rol o'ynaydi. Firebase, AWS IoT, Azure IoT Hub kabi platformalar minglab qurilmalarni bir vaqtda boshqarish, ma'lumotlarni saqlash va tahlil qilish imkoniyatini beradi. Real vaqt ma'lumotlar bazalari yordamida operator istalgan vaqtda har bir yoritgichning holatini ko'rishi, sozlamalarni o'zgartirishi va nosozliklarni aniqlashi mumkin. Bizning loyihamizda Firebase Realtime Database tanlangan, chunki u bepul rejimda yetarli imkoniyatlar taqdim etadi va ESP32 bilan integratsiyasi oson.")

add_body("Edge computing yani chekka hisoblash texnologiyasi IoT tizimlarida tobora muhim rol o'ynamoqda. Bu yondashuvda ma'lumotlarni qayta ishlash bulut serverida emas, balki to'g'ridan-to'g'ri qurilmaning o'zida amalga oshiriladi. Ko'cha yoritish tizimlarida bu yondashuv internet uzilgan holatlarda ham tizimning mustaqil ishlashini ta'minlaydi. Bizning loyihamizda ESP32 mikrokontrolleri edge computing vazifasini bajaradi, ya'ni sensor ma'lumotlarini qayta ishlash va qaror qabul qilish lokal ravishda amalga oshiriladi, bulut esa faqat monitoring va masofadan boshqarish uchun ishlatiladi.")

add_body("Kiberxavfsizlik masalasi IoT asosidagi yoritish tizimlarida alohida e'tiborga loyiq. Internetga ulangan har qanday qurilma potentsial hujum nishoniga aylanishi mumkin. Shuning uchun tizimda autentifikatsiya, ma'lumotlarni shifrlash va kirish huquqlarini boshqarish mexanizmlari joriy etilishi kerak. Bizning loyihamizda Firebase Authentication xizmati foydalanuvchilarni tekshirish uchun, Firebase Security Rules esa ma'lumotlar bazasiga kirishni cheklash uchun ishlatiladi. ESP32 va Firebase orasidagi aloqa SSL/TLS protokoli orqali shifrlangan holda amalga oshiriladi.")

add_body("Tizimning kengaytirilishi va miqyoslashtirilishi ham muhim loyihalash mezoni hisoblanadi. Bitta ESP32 kontrolleri bir nechta yoritgichni boshqarishi mumkin va bir nechta kontrollerlar bitta Firebase loyihasiga ulangan holda ishlashi mumkin. Bu arxitektura kichik ko'chadan to butun shahar miqyosigacha kengaytirilishi mumkin. Firebase Realtime Database bir vaqtda 200 mingtagacha ulanishni qo'llab-quvvatlaydi, bu esa minglab yoritgichlarni boshqarish uchun yetarli. Bundan tashqari, tizim modular tuzilishga ega bo'lib, yangi sensorlar va funksiyalar osongina qo'shilishi mumkin.")

add_body("Energiya manbai masalasi ko'cha yoritish tizimlarida muhim o'rin tutadi. An'anaviy tizimlar elektr tarmog'iga to'liq bog'liq bo'lib, elektr uzilishlarida ishlamay qoladi. Zamonaviy yondashuvlar quyosh panellari va akkumulyatorlar yordamida avtonom energiya ta'minotini ta'minlaydi. Bizning loyihamizda maket darajasida kichik quyosh paneli ishlatilgan bo'lib, u tizimning avtonom ishlash imkoniyatini namoyish etadi. Kelajakda real tizimda 50-100 vattli quyosh paneli va 12 voltli akkumulyator yordamida to'liq avtonom ishlash ta'minlanishi mumkin.")

add_body("PWM yani impulsli kenglik modulyatsiyasi LED yoritgichlarning yorug'lik darajasini boshqarish uchun ishlatiladigan asosiy usul hisoblanadi. ESP32 da 16 ta PWM kanali mavjud bo'lib, har birining chastotasi va aniqligini mustaqil sozlash mumkin. WS2812B LED strip uchun esa maxsus protokol ishlatiladi, bunda har bir LED ning rangi va yorug'ligi individual boshqariladi. FastLED kutubxonasi bu murakkab protokolni sodda dasturiy interfeys orqali boshqarish imkonini beradi. Bizning tizimimizda 13 ta LED individual boshqariladi va turli ranglar hamda yorug'lik darajalari sozlanishi mumkin.")

add_image("diagram_architecture.png", "1.1-rasm. Smart Street Light tizimining umumiy arxitekturasi")

# ============ 1.2 ============
add_h2("1.2-§ Ultratovush sensorlarning ishlash prinsipi va texnik xususiyatlari")

add_body("Ultratovush to'lqinlari inson qulog'i eshita olmaydigan, chastotasi 20 kHz dan yuqori bo'lgan tovush to'lqinlaridir. Ular mexanik to'lqinlar turkumiga kiradi va tarqalishi uchun moddiy muhit talab etiladi. Havoda ultratovush to'lqinlarining tezligi haroratga bog'liq bo'lib, v=331.3+0.606*T formulasi bilan aniqlanadi, bu yerda v metr/sekundda tezlik va T Selsiy darajasida haroratdir. Xona haroratida yani 20 daraja Selsiyda ultratovush tezligi taxminan 343.5 metr/sekundni tashkil etadi. Bu xususiyat masofa o'lchash sensorlarida keng qo'llaniladi.")

add_body("Ultratovush to'lqinlarining fizik xususiyatlari ularning qo'llanilish sohalarini belgilaydi. Chastota oshgan sari to'lqin uzunligi qisqaradi va yo'nalganlik yaxshilanadi, lekin so'nilish ham ortadi. 40 kHz chastotadagi ultratovush to'lqinining to'lqin uzunligi havoda taxminan 8.6 millimetrni tashkil etadi. Bu shuni anglatadiki, sensor 8.6 millimetrdan katta ob'ektlarni ishonchli aniqlashi mumkin. Ultratovush to'lqinlari havoda tarqalganda energiyasini yo'qotadi, bu hodisa absorpsiya deb ataladi. Absorpsiya koeffitsienti chastotaning kvadratiga proporsional bo'lib, yuqori chastotali to'lqinlar tezroq so'niladi.")

add_body("Ultratovush sensorlari piezoelektrik effektga asoslanadi. Piezoelektrik kristall elektr signal ta'sirida mexanik tebranishga keladi va ultratovush to'lqinlarini hosil qiladi. Xuddi shu kristall qaytgan to'lqinni qabul qilganda mexanik tebranishni elektr signalga aylantiradi. Sensorning ishlash prinsipi quyidagicha: transmitter ultratovush impulsini yuboradi, bu impuls ob'ektdan qaytadi va receiver tomonidan qabul qilinadi. Yuborish va qabul qilish orasidagi vaqt farqi asosida ob'ektgacha bo'lgan masofa hisoblanadi. Bu usul Time of Flight yani parvoz vaqti prinsipi deb ataladi.")

add_body("Piezoelektrik materiallar orasida qo'rg'oshin zirkonat titanat yani PZT eng keng tarqalgan hisoblanadi. Bu material yuqori piezoelektrik koeffitsientga ega bo'lib, kichik elektr signalni kuchli mexanik tebranishga aylantiradi. Sensorning transmitter qismi PZT diskdan iborat bo'lib, unga 40 kHz chastotali elektr impuls berilganda u ultratovush to'lqinlarini hosil qiladi. Receiver qismi ham xuddi shunday PZT diskdan iborat bo'lib, qaytgan to'lqinlarni elektr signalga aylantiradi. Ba'zi sensorlarda transmitter va receiver bitta elementda birlashtirilgan bo'lib, bu sensorning o'lchamlarini kichraytiradi.")

add_body("Time of Flight prinsipi bo'yicha masofa hisoblash formulasi d=(t*v)/2 ko'rinishida ifodalanadi, bu yerda d ob'ektgacha bo'lgan masofa metrda, t impulsning borib qaytish vaqti sekundda va v tovush tezligi metr/sekundda. Ikki ga bo'lish sababi shundaki, to'lqin ob'ektgacha borib va qaytib keladi, ya'ni ikki marta masofani bosib o'tadi. Amaliy misol sifatida, agar impulsning borib qaytish vaqti 1000 mikrosekund bo'lsa va harorat 25 daraja Selsiy bo'lsa, masofa d=(0.001*346.5)/2=0.173 metr yani 17.3 santimetr bo'ladi. Bu formulaning aniqligi harorat kompensatsiyasiga bog'liq.")

add_body("Amaliy qo'llanishda masofa hisoblash bir necha omillarni hisobga olishni talab qiladi. Birinchidan, harorat kompensatsiyasi muhim, chunki 10 daraja harorat o'zgarishi tovush tezligini 6 metr/sekund ga o'zgartiradi va bu 1 metr masofada 1.7 foiz xatolikka olib keladi. Ikkinchidan, namlik ham tovush tezligiga ta'sir qiladi, lekin bu ta'sir haroratga nisbatan kichik. Uchinchidan, sensor va ob'ekt orasidagi burchak o'lchash natijasiga ta'sir qiladi, chunki to'lqin ob'ektdan burchak ostida qaytganda sensor uni qabul qilmasligi mumkin. Bu omillarni hisobga olish tizimning aniqligini oshiradi.")

add_body("Ultratovush sensorlarining qo'llanilish sohalari juda keng. Sanoatda suyuqlik sathini o'lchash, robotikada to'siqlarni aniqlash, avtomobil sanoatida park sensori sifatida, tibbiyotda ultrasonografiya va ko'plab boshqa sohalarda ishlatiladi. Ko'cha yoritish tizimlarida ultratovush sensorlari piyodalar va transport vositalarini aniqlash uchun qo'llaniladi. Infraqizil sensorlarga nisbatan ultratovush sensorlarining afzalligi shundaki, ular ob'ektning rangi, shakli va haroratidan qat'i nazar ishlaydi. Shuningdek, ular yorug'lik sharoitlariga bog'liq emas va tunda ham kunduz kuni ham bir xil aniqlikda ishlaydi.")

add_body("Ultratovush to'lqinlarining tarqalish xususiyatlari bir necha omillarga bog'liq. Birinchidan, to'lqin chastotasi oshgan sari yo'nalganlik yaxshilanadi, lekin so'nilish ham ortadi. Ikkinchidan, havo harorati va namligi tovush tezligiga ta'sir qiladi. Uchinchidan, shamol tezligi va yo'nalishi o'lchash natijalariga xatolik kiritishi mumkin. To'rtinchidan, ob'ektning sirt xususiyatlari qaytish koeffitsientiga ta'sir qiladi. Yumshoq va g'ovak sirtlar tovushni yutadi, qattiq va silliq sirtlar esa yaxshi aks ettiradi. Bu omillarni hisobga olish sensor tizimini loyihalashda muhim ahamiyatga ega.")

add_image("diagram_sequence.png", "1.2-rasm. Ultratovush sensori ishlash jarayonining ketma-ketlik diagrammasi")

add_body("RCWL-9610A ultratovush sensori bizning loyihamiz uchun tanlangan asosiy harakat aniqlash qurilmasi hisoblanadi. Bu sensor 3.3 volt kuchlanishda ishlaydi va atigi 2 milliamper tok sarflaydi, bu uni energiya tejamkor tizimlar uchun ideal qiladi. Sensorning maksimal o'lchash masofasi 450 santimetrni tashkil etadi va diagramma bo'yicha nurlanish burchagi 30 darajani tashkil etadi. Sensor TRIG va ECHO pinlariga ega bo'lib, TRIG pinga 10 mikrosekund davomiylikdagi impuls yuborilganda sensor 8 ta ultratovush impulsi chiqaradi va ECHO pin orqali qaytish vaqtini bildiradi.")

add_body("RCWL-9610A sensorining muhim afzalliklaridan biri uning 3.3 volt kuchlanishda ishlashi hisoblanadi. Ko'pgina ultratovush sensorlari 5 volt talab qiladi va ESP32 kabi 3.3 voltli mikrokontrollerlar bilan ishlash uchun qo'shimcha kuchlanish darajasi o'zgartiruvchi sxema kerak bo'ladi. RCWL-9610A esa to'g'ridan-to'g'ri ESP32 ga ulanishi mumkin, bu sxemani soddalashtiradi va ishonchlilikni oshiradi. Sensorning ish harorati diapazoni minus 20 dan plus 70 daraja Selsiyga qadar bo'lib, ko'cha sharoitlarida yil bo'yi ishlatish imkonini beradi.")

add_body("Sensorning elektr xususiyatlari ham muhim ahamiyatga ega. RCWL-9610A ning ish kuchlanishi 2.7 dan 5.5 voltgacha bo'lib, bu uni turli mikrokontrollerlar bilan mos kelishini ta'minlaydi. Kutish rejimida tok sarfi 1.5 milliamper, o'lchash rejimida esa 2 milliamper atrofida bo'ladi. Sensorning javob berish vaqti 100 mikrosekunddan kam bo'lib, tezkor o'lchashlarni amalga oshirish imkonini beradi. Chiqish signali TTL darajasida bo'lib, 3.3 voltli mantiqiy darajaga mos keladi. Bu xususiyatlar sensorni ESP32 bilan bevosita ulash imkonini beradi.")

add_body("HC-SR04 sensori bilan qiyoslaganda RCWL-9610A bir necha muhim afzalliklarga ega. HC-SR04 5 volt kuchlanish talab qiladi va 15 milliamper tok sarflaydi, bu RCWL-9610A ning 2 milliamperiga nisbatan 7.5 baravar ko'p. HC-SR04 ning maksimal o'lchash masofasi 400 santimetr bo'lib, RCWL-9610A ning 450 santimetriga nisbatan kamroq. Biroq HC-SR04 ning narxi pastroq va bozorda kengroq tarqalgan. Bizning loyihamizda RCWL-9610A tanlangan, chunki u ESP32 bilan to'g'ridan-to'g'ri mos keladi, kam energiya sarflaydi va ko'cha sharoitlarida ishonchli ishlaydi.")

add_body("HC-SR04 sensorining yana bir kamchiligi shundaki, uning ECHO pini 5 volt darajasida signal beradi va bu ESP32 ning 3.3 voltli GPIO pinlariga zarar yetkazishi mumkin. Bu muammoni hal qilish uchun kuchlanish bo'luvchi rezistorlar yoki mantiqiy daraja o'zgartiruvchi sxema kerak bo'ladi. RCWL-9610A da bunday muammo yo'q, chunki u to'liq 3.3 volt darajasida ishlaydi. Bundan tashqari, RCWL-9610A ning o'lchash burchagi 30 daraja bo'lib, HC-SR04 ning 15 darajasiga nisbatan kengroq hududni qamrab oladi, bu ko'cha yoritish tizimlarida muhim afzallik hisoblanadi.")

add_image("esp32_devkit.png", "1.3-rasm. ESP32 DevKit mikrokontroller platasi va uning asosiy komponentlari")

add_body("TEMT6000 yorug'lik sensori fototransistor asosida ishlaydigan analog sensor bo'lib, atrof muhitdagi yorug'lik darajasini o'lchash uchun ishlatiladi. Sensor chiqish kuchlanishi yorug'lik intensivligiga proporsional ravishda o'zgaradi. ESP32 ning 12-bitli analog-raqamli o'zgartiruvchisi yordamida sensor qiymati 0 dan 4095 gacha bo'lgan raqamli qiymatga aylantiriladi. Qorong'u sharoitda qiymat 0 ga yaqin, to'liq yorug'likda esa 4095 ga yaqin bo'ladi. Bizning tizimimizda 300 qiymati kunduz va tun chegarasi sifatida belgilangan.")

add_body("TEMT6000 sensorining spektral sezgirligi inson ko'zining sezgirligiga yaqin bo'lib, 570 nanometr to'lqin uzunligida maksimal sezgirlikka ega. Bu xususiyat uni ko'cha yoritish tizimlarida qo'llash uchun ideal qiladi, chunki sensor inson ko'zi ko'radigan yorug'likni to'g'ri baholaydi. Sensorning javob berish tezligi juda yuqori bo'lib, mikrosekundlar darajasida o'zgarishlarni aniqlaydi. Ish harorati diapazoni minus 40 dan plus 85 daraja Selsiyga qadar bo'lib, ekstremal ob-havo sharoitlarida ham ishonchli ishlaydi. Sensor oddiy ikki pinli ulanishga ega va qo'shimcha sxema talab etmaydi.")

add_body("Fototransistorning ishlash prinsipi quyidagicha: yorug'lik fotonlari bazaga tushganda elektron-kovak juftliklari hosil bo'ladi va transistor ochiladi. Yorug'lik intensivligi oshgan sari transistor orqali o'tadigan tok ham ortadi. TEMT6000 da yuklama rezistori orqali oqayotgan tok kuchlanish tushishini hosil qiladi va bu kuchlanish ESP32 ning ADC kanaliga beriladi. Sensorning chiziqli ishlash diapazoni 1 dan 1000 lyuksgacha bo'lib, ko'cha yoritish tizimlarida uchraydigan barcha yorug'lik sharoitlarini qamrab oladi.")

add_body("ESP32 mikrokontrolleri Espressif Systems kompaniyasi tomonidan ishlab chiqilgan yuqori samarali mikrokontroller bo'lib, ikki yadroli Xtensa LX6 protsessoriga ega. Protsessor chastotasi 240 MHz gacha bo'lib, murakkab hisoblashlarni tezkor bajarish imkonini beradi. Mikrokontrollerda 520 KB SRAM operativ xotira va 4 MB flesh xotira mavjud. Eng muhimi, ESP32 da WiFi va Bluetooth modullari o'rnatilgan bo'lib, qo'shimcha simsiz aloqa moduli talab etilmaydi. Bu xususiyat IoT loyihalar uchun uni eng mashhur tanlovga aylantirgan.")

add_body("ESP32 ning analog-raqamli o'zgartiruvchisi 12-bit aniqlikka ega bo'lib, 0 dan 3.3 voltgacha bo'lgan kuchlanishni 4096 ta diskret qiymatga aylantiradi. Bu TEMT6000 yorug'lik sensorining qiymatlarini yuqori aniqlikda o'qish imkonini beradi. ESP32 da 18 ta ADC kanali mavjud bo'lib, bir nechta analog sensorlarni bir vaqtda ulash mumkin. Biroq WiFi ishlatilganda ADC2 kanallari ishlamaydi, shuning uchun bizning loyihamizda TEMT6000 sensori ADC1 kanaliga yani GPIO 34 pinga ulangan. Bu cheklovni hisobga olish loyiha ishlab chiqish bosqichida muhim.")

add_body("ESP32 ning WiFi moduli IEEE 802.11 b/g/n standartlarini qo'llab-quvvatlaydi va 2.4 GHz chastotada ishlaydi. Maksimal uzatish quvvati 20 dBm bo'lib, ochiq maydonda 100 metrgacha qamrov masofasini ta'minlaydi. Mikrokontroller Station va Access Point rejimlarida ishlashi mumkin, ya'ni u mavjud WiFi tarmoqqa ulanishi yoki o'zi tarmoq yaratishi mumkin. Bizning loyihamizda ESP32 Station rejimida ishlaydi va mavjud WiFi routerga ulanib Firebase serveriga ma'lumot yuboradi. Deep sleep rejimida energiya sarfi 10 mikroamperga tushadi.")

add_body("Debounce algoritmi sensor signallarini filtrlash uchun qo'llaniladigan muhim dasturiy usul hisoblanadi. Ultratovush sensori ba'zan noto'g'ri qiymatlar berishi mumkin, masalan, shamol ta'sirida yoki bir nechta ob'ektlardan qaytgan signallar aralashganda. Debounce algoritmi ketma-ket bir nechta o'lchash natijalarini taqqoslaydi va faqat barqaror natijani haqiqiy deb qabul qiladi. Bizning tizimimizda 3 ta ketma-ket o'lchash bir xil natija berganida harakat aniqlangan deb hisoblanadi. Bu yondashuv soxta signallarni filtrlaydi va tizimning ishonchliligini sezilarli darajada oshiradi.")

add_body("Debounce algoritmining dasturiy amalga oshirilishi quyidagicha ishlaydi: har bir o'lchash natijasi oldingi natijalar bilan taqqoslanadi. Agar yangi natija oldingi natijadan sezilarli farq qilsa, hisoblagich nolga qaytariladi. Agar natijalar bir xil bo'lsa, hisoblagich oshiriladi. Hisoblagich belgilangan chegaraga yetganda natija haqiqiy deb qabul qilinadi. Bu usul tizimning javob berish vaqtini biroz oshiradi, lekin soxta ishga tushishlarni deyarli to'liq bartaraf etadi. Bizning tizimimizda o'lchash oralig'i 100 millisekund bo'lgani uchun debounce kechikishi 300 millisekund atrofida bo'ladi.")

add_body("Hold timer mexanizmi harakat aniqlangandan keyin yoritgichning ma'lum vaqt davomida yonib turishini ta'minlaydi. Agar hold timer ishlatilmasa, odam sensor zonasidan chiqishi bilanoq yoritgich o'chadi va bu foydalanuvchi uchun noqulay bo'ladi. Bizning tizimimizda hold timer 5 sekund qilib belgilangan, ya'ni oxirgi harakat aniqlangandan keyin yoritgich yana 5 sekund yonib turadi. Agar bu vaqt ichida yangi harakat aniqlansa, taymer qayta boshlanadi. Bu mexanizm uzluksiz yoritishni ta'minlaydi va energiya tejash bilan foydalanuvchi qulayligi o'rtasida muvozanat yaratadi.")

add_body("Hold timer qiymatini tanlash muhim muhandislik qarori hisoblanadi. Juda qisqa vaqt belgilansa, odam hali ko'chada bo'lganida yoritgich o'chib qolishi mumkin. Juda uzun vaqt belgilansa, energiya tejash samaradorligi pasayadi. Bizning tizimimizda bu qiymat Firebase orqali masofadan o'zgartirilishi mumkin, bu esa turli sharoitlarga moslashish imkonini beradi. Masalan, gavjum ko'chalarda hold timer 10-15 sekund, kam odam yurgan ko'chalarda esa 3-5 sekund qilib belgilanishi mumkin. Bu moslashuvchanlik tizimning universal qo'llanilishini ta'minlaydi.")

add_body("Hysteresis yoki gisterezis prinsipi sensorli tizimlarda tebranishlarni oldini olish uchun qo'llaniladi. Agar yoritgich yoqish va o'chirish uchun bir xil chegara qiymati ishlatilsa, sensor qiymati chegara atrofida tebranganda yoritgich tez-tez yonib-o'chib turadi. Hysteresis bu muammoni hal qilish uchun ikki xil chegara qiymatini belgilaydi. Bizning tizimimizda yorug'lik sensori uchun yoqish chegarasi 250 va o'chirish chegarasi 350 qilib belgilangan. Ya'ni yoritgich faqat yorug'lik 250 dan pastga tushganda yonadi va faqat 350 dan oshganda o'chadi. Bu oraliq tebranishlarni bartaraf etadi.")

add_body("Hysteresis prinsipi nafaqat yorug'lik sensori, balki ultratovush sensori uchun ham qo'llaniladi. Harakat aniqlash chegarasi 200 santimetr qilib belgilangan, lekin harakatni to'xtatish chegarasi 220 santimetr qilib belgilangan. Ya'ni ob'ekt 200 santimetrdan yaqinlashganda harakat aniqlangan deb hisoblanadi, lekin faqat 220 santimetrdan uzoqlashganda harakat to'xtagan deb hisoblanadi. Bu 20 santimetrlik oraliq ob'ekt chegara atrofida harakatlanganda tizimning barqaror ishlashini ta'minlaydi va keraksiz yonib-o'chishlarni oldini oladi.")

add_body("Ultratovush sensorlarining cheklovlari ham mavjud va ularni loyihalash bosqichida hisobga olish kerak. Birinchidan, sensor nurlanish burchagi 30 daraja bo'lgani uchun keng ko'chalarni to'liq qamrab olish uchun bir nechta sensor kerak bo'lishi mumkin. Ikkinchidan, juda kichik ob'ektlar yoki yumshoq kiyimdagi odamlar signalni yaxshi aks ettirmasligi mumkin. Uchinchidan, kuchli shamol yoki yomg'ir sensorning aniqligiga ta'sir qilishi mumkin. Bu cheklovlarni bartaraf etish uchun bir nechta sensorni birgalikda ishlatish yoki ultratovush sensorini boshqa turdagi sensorlar bilan kombinatsiya qilish mumkin.")

add_body("Sensor ma'lumotlarini qayta ishlash algoritmi bir necha bosqichdan iborat. Birinchi bosqichda xom ma'lumotlar o'qiladi va fizik qiymatlarga aylantiriladi. Ikkinchi bosqichda filtrlash amalga oshiriladi, bunda o'rtacha qiymat yoki median filtr qo'llaniladi. Uchinchi bosqichda debounce algoritmi yordamida barqaror natija aniqlanadi. To'rtinchi bosqichda hysteresis prinsipi qo'llaniladi va qaror qabul qilinadi. Beshinchi bosqichda hold timer boshqariladi. Bu bosqichlar har 100 millisekund takrorlanadi va tizimning real vaqt rejimida ishlashini ta'minlaydi.")

add_body("Sensorlar orasidagi sinxronizatsiya ham muhim masala hisoblanadi. Ultratovush sensori va yorug'lik sensori turli tezlikda ma'lumot beradi va ularning natijalarini birlashtirish uchun maxsus algoritm kerak. Bizning tizimimizda yorug'lik sensori har 1 sekund, ultratovush sensori esa har 100 millisekund o'qiladi. Qaror qabul qilish algoritmi avval yorug'lik sensorini tekshiradi va agar tun bo'lsa, ultratovush sensori natijasini baholaydi. Agar kunduz bo'lsa, ultratovush sensori natijalari e'tiborga olinmaydi va yoritgich o'chirilgan holda qoladi. Bu iyerarxik yondashuv energiya tejashni maksimal darajada ta'minlaydi.")

add_body("Median filtr signalni filtrlash uchun samarali usul bo'lib, u impulsli shovqinlarni bartaraf etishda ayniqsa yaxshi natija beradi. Filtr oxirgi N ta o'lchash natijasini kattaliklariga ko'ra tartiblaydi va o'rtadagi qiymatni natija sifatida qaytaradi. Bizning tizimimizda N=5 qilib belgilangan, ya'ni oxirgi 5 ta o'lchash natijasidan mediannasi olinadi. Bu usul o'rtacha qiymat filtriga nisbatan afzal, chunki u bitta keskin og'ish natijasiga ta'sirlanmaydi. Masalan, agar 5 ta o'lchash natijasi 150, 155, 800, 148, 152 bo'lsa, median 152 bo'ladi, o'rtacha esa 281 bo'ladi.")

add_body("WS2812B LED strip zamonaviy yoritish tizimlarida keng qo'llaniladigan adreslangan LED tasma hisoblanadi. Har bir LED o'z ichida WS2812B drayver chipini saqlaydi va individual boshqarilishi mumkin. Ma'lumot uzatish bitta signal liniyasi orqali amalga oshiriladi, bunda har bir LED o'ziga tegishli ma'lumotni oladi va qolganini keyingi LED ga uzatadi. Har bir LED uchun 24 bit ma'lumot kerak bo'lib, 8 bit qizil, 8 bit yashil va 8 bit ko'k rang uchun ajratilgan. Bu 16 milliondan ortiq rang kombinatsiyasini hosil qilish imkonini beradi va ko'cha yoritishida turli rejimlarni amalga oshirish uchun yetarli.")

add_body("Real vaqt operatsion tizimi yani RTOS ESP32 da bir nechta vazifalarni parallel bajarish imkonini beradi. FreeRTOS ESP32 ning standart operatsion tizimi bo'lib, u vazifalarni prioritet asosida boshqaradi. Bizning tizimimizda sensor o'qish, LED boshqarish va Firebase sinxronizatsiya alohida vazifalar sifatida ishlaydi. Bu yondashuv tizimning javob berish tezligini oshiradi va bitta vazifaning kechikishi boshqa vazifalarni bloklamasligini ta'minlaydi. Masalan, Firebase bilan aloqa vaqtinchalik uzilgan bo'lsa ham, sensor o'qish va LED boshqarish to'xtovsiz davom etadi.")

add_image("diagram_flowchart.png", "1.4-rasm. Tizimning ishlash algoritmi oqim diagrammasi")

# ============ 1.3 ============
add_h2("1.3-§ Masalaning qo'yilishi")

add_body("Yuqorida keltirilgan tahlil asosida quyidagi muammo aniq ko'rinadi: hozirgi ko'cha yoritish tizimlari energiya resurslaridan samarasiz foydalanadi, markazlashtirilgan monitoring va boshqaruv imkoniyatiga ega emas, hamda mahalliy sharoitlarga moslashtirilgan arzon yechimlar mavjud emas. O'zbekiston sharoitida bu muammo ayniqsa dolzarb, chunki energiya resurslari cheklangan va ko'cha yoritish infratuzilmasi modernizatsiyaga muhtoj. Shu sababli, ultratovush sensori orqali harakatni aniqlash va energiya tejamkorligini ta'minlovchi aqlli yoritish tizimini ishlab chiqish zarur.")

add_body("Ishlab chiqiladigan tizimga quyidagi talablar qo'yiladi: tizim ultratovush sensori yordamida 200 santimetr masofada harakatni ishonchli aniqlashi, yorug'lik sensori yordamida kunduz va tunni avtomatik farqlashi, WiFi orqali bulut platformasiga ulanishi va real vaqt rejimida ma'lumot almashishi, web-interfeys orqali masofadan boshqarilishi, avtomatik, qo'lda va jadval rejimlarida ishlashi kerak. Tizimning energiya tejash samaradorligi E=((T_tun-T_yonish)/T_tun)*100% formulasi bilan hisoblanadi, bu yerda T_tun tunning umumiy davomiyligi va T_yonish yoritgichning yonib turgan vaqti hisoblanadi.")

add_body("Tizimning muvaffaqiyat mezonlari quyidagilardan iborat: energiya tejash darajasi kamida 60 foizni tashkil etishi, sensorning harakat aniqlash aniqligi 95 foizdan yuqori bo'lishi, tizimning uzluksiz ishlash vaqti kamida 720 soat bo'lishi, web-interfeys orqali boshqarish kechikishi 2 sekunddan oshmasligi va tizimning umumiy narxi tijorat analoglariga nisbatan kamida 5 baravar arzon bo'lishi kerak. Bu mezonlar loyihaning muvaffaqiyatini baholash uchun asosiy ko'rsatkichlar sifatida ishlatiladi va sinov bosqichida tekshiriladi.")

# Page break at end
doc.add_page_break()

# Save
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_final.docx')
print(f"I BOB yozildi. Jami belgilar soni: {total_chars}")
