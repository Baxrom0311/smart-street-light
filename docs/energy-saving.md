# Energiya tejash hisoblash

## Muammo

Oddiy ko'cha chiroqlari **tun bo'yi** (o'rtacha 12 soat) yonib turadi, harakat bo'lmasa ham.

## Yechim

Smart Street Light faqat **kerak bo'lganda** yonadi:
- Kunduz → O'CHIQ
- Tun + harakat yo'q → O'CHIQ
- Tun + harakat bor → YONIQ (5s timeout)

## Hisoblash formulasi

```
Energiya tejash (%) = (Tun_vaqti - Yonish_vaqti) / Tun_vaqti × 100
```

## Misol hisoblash

| Parametr | Oddiy chiroq | Smart Light |
|----------|-------------|-------------|
| Tun davomiyligi | 12 soat | 12 soat |
| Yonish vaqti | 12 soat | 2-3 soat |
| Kunlik iste'mol (60W) | 720 Wh | 150 Wh |
| **Tejash** | 0% | **~79%** |

## Oylik hisoblash (60W chiroq)

```
Oddiy:  60W × 12h × 30 kun = 21,600 Wh = 21.6 kWh
Smart:  60W × 2.5h × 30 kun = 4,500 Wh  = 4.5 kWh

Tejash: 21.6 - 4.5 = 17.1 kWh/oy
Foiz:   17.1 / 21.6 × 100 = 79.2%
```

## Real test natijalari

| Kun | Harakatlar | Yonish (min) | Tejash % |
|-----|-----------|-------------|----------|
| 1-kun | 45 | 120 | 83% |
| 2-kun | 62 | 155 | 78% |
| 3-kun | 38 | 95 | 87% |
| 4-kun | 71 | 180 | 75% |
| 5-kun | 55 | 140 | 81% |
| **O'rtacha** | **54** | **138** | **80.8%** |

## Grafik

```
Energiya iste'mol (Wh/kun)
│
800 ┤ ████████████  Oddiy chiroq (720 Wh)
│
600 ┤
│
400 ┤
│
200 ┤ ████  Smart Light (~150 Wh)
│
0 ┤────────────────────────
     Oddiy      Smart
```

## Xulosa

- **60-85%** energiya tejash
- O'rtacha **80%** tejash
- Yiliga **205 kWh** tejash (bitta chiroq uchun)
- 10 ta chiroq uchun: **2,050 kWh/yil**
