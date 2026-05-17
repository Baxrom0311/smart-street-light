const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const dir = './docs/BMI/images/';
  const url = 'https://smart-street-light-iot.web.app';

  // Login page
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  await page.goto(url);
  await page.waitForTimeout(2000);
  await page.screenshot({ path: dir + 'screenshot_login.png' });
  console.log('1. Login page captured');

  // Login
  await page.fill('input[type="email"]', 'device@smartlight.com');
  await page.fill('input[type="password"]', 'SmartLight2026!');
  await page.click('button[type="submit"]');
  await page.waitForTimeout(3000);

  // Dashboard desktop
  await page.screenshot({ path: dir + 'screenshot_dashboard_desktop.png' });
  console.log('2. Dashboard desktop captured');

  // Dashboard mobile
  await page.setViewportSize({ width: 375, height: 812 });
  await page.waitForTimeout(1000);
  await page.screenshot({ path: dir + 'screenshot_dashboard_mobile.png' });
  console.log('3. Dashboard mobile captured');

  // Stats tab
  await page.setViewportSize({ width: 1280, height: 800 });
  await page.click('button:has-text("Statistika")');
  await page.waitForTimeout(1000);
  await page.screenshot({ path: dir + 'screenshot_stats.png' });
  console.log('4. Statistics captured');

  // Log tab
  await page.click('button:has-text("Log")');
  await page.waitForTimeout(1000);
  await page.screenshot({ path: dir + 'screenshot_log.png' });
  console.log('5. Log captured');

  // Settings tab
  await page.click('button:has-text("Sozlama")');
  await page.waitForTimeout(1000);
  await page.screenshot({ path: dir + 'screenshot_settings.png' });
  console.log('6. Settings captured');

  // Mermaid diagrams
  const mermaidPage = await browser.newPage({ viewport: { width: 800, height: 600 } });

  const diagrams = [
    { name: 'diagram_architecture.png', code: `graph TB
      subgraph HW[Hardware]
        US[RCWL-9610A] --> ESP[ESP32]
        LS[TEMT6000] --> ESP
        ESP --> RL[Relay]
        RL --> LED[LED Chiroq]
      end
      subgraph Cloud[Firebase]
        RTDB[(Realtime DB)]
      end
      subgraph Client[Dashboard]
        PWA[React PWA]
      end
      ESP <-->|WiFi| RTDB
      RTDB <-->|WebSocket| PWA` },
    { name: 'diagram_flowchart.png', code: `flowchart TD
      A[Start] --> B{Yoruglik > 350?}
      B -->|Ha| C[LED OCHIQ]
      B -->|Yoq| D{Harakat bor?}
      D -->|Ha| E[LED YONIQ]
      D -->|Yoq| F{5s otdimi?}
      F -->|Ha| C
      F -->|Yoq| E` },
    { name: 'diagram_sequence.png', code: `sequenceDiagram
      participant S as Sensor
      participant E as ESP32
      participant F as Firebase
      participant D as Dashboard
      loop Har 300ms
        S->>E: Masofa + Yoruglik
      end
      loop Har 3s
        E->>F: Status yuborish
      end
      F-->>D: Real-time update
      D->>F: Buyruq
      F-->>E: Stream` },
    { name: 'diagram_state.png', code: `stateDiagram-v2
      [*] --> Auto
      Auto --> Manual: Dashboard
      Auto --> Schedule: Dashboard
      Manual --> Auto: Dashboard
      Schedule --> Auto: Dashboard` },
  ];

  for (const d of diagrams) {
    const encoded = encodeURIComponent(d.code);
    await mermaidPage.goto(`https://mermaid.ink/img/${Buffer.from(d.code).toString('base64')}?type=png`);
    await mermaidPage.waitForTimeout(2000);
    await mermaidPage.screenshot({ path: dir + d.name });
    console.log(`Diagram: ${d.name}`);
  }

  await browser.close();
  console.log('All screenshots done!');
})();
