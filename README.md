# ⚡ TikTok Account Auditor Pro | High-Performance Verification & Scraper Engine

<div align="center">
  <img src="https://img.shields.io/badge/Release-v4.5.0_Stable-blue.svg?style=for-the-badge" alt="Release">
  <img src="https://img.shields.io/badge/Speed-100k%2B_Checks%2Fhr-brightgreen.svg?style=for-the-badge" alt="Speed">
  <img src="https://img.shields.io/badge/Captcha_Solver-Direct_AI_Engine-orange.svg?style=for-the-badge" alt="Captcha">
  <img src="https://img.shields.io/badge/Status-Undetected_&_Active-success.svg?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/Architecture-Asynchronous_C%2B%2B%2FPython-purple.svg?style=for-the-badge" alt="Architecture">
</div>

<br />

<div align="center">
  <a href="https://t.me/mariabosser"><strong>👤 Contact Developer</strong></a> •
  <a href="https://t.me/Sectools1"><strong>📢 Telegram Channel</strong></a>
</div>

---

## 📌 Executive Overview

**Engineered by a senior systems architect with 20+ years of software engineering & automation experience.**

**TikTok Account Auditor Pro** is an ultra-fast, multi-threaded validation and analytics suite designed for digital asset managers, social media growth teams, and enterprise auditors. Built on an asynchronous execution model, it guarantees **100% checking accuracy without skipped tasks**, bypassing complex edge checks while preserving resource integrity.

---

## 🛠️ Core Technical Features

*   **⚡ Asynchronous Multi-Tab Core:** Utilizes lightweight worker pools capable of opening and processing multiple verification streams concurrently with minimal CPU/RAM footprint.
*   **🎯 Zero-Skip Guarantee:** Implements an atomic retry queue system. No `user:pass` line is ever dropped due to socket timeouts or network jitter.
*   **⏳ Smart Rate-Limit Auto-Isolation:** Detects rate-limited requests instantly and isolates affected `user:pass` pairs into a clean secondary output file (`rate_limited.txt`) for immediate or delayed re-auditing.
*   **🧩 Low-Latency Direct Captcha Bypass:** Proprietary AI solver engine that bypasses TikTok captcha puzzles directly on local worker threads **without routing through proxy chains**, reducing verification latency by up to 300%.
*   **🌐 Universal Proxy Engine:** Seamless native integration with SOCKS4, SOCKS5, HTTP, HTTPS, and rotating 4G/Residential proxy pools. Fully compatible with both free and premium proxy lists.
*   **🔍 Mass Scraper Engine (100k+ Capacity):** High-speed profile scraper module capable of collecting over 100,000 targeted profile IDs in minutes to populate audit pipelines.
*   **📡 Real-Time Telegram Webhooks:** Instant alerts delivered straight to your Telegram Bot/Channel containing valid hits, security flags, and account metrics.

---

## 🇬🇧 English | Feature Summary

*   **Mode:** Credentials audit (`user:pass` pair checking).
*   **Accuracy:** Zero-skip guarantee with retry mechanism.
*   **Rate-Limits:** Auto-saves rate-limited entries to separate output.
*   **Proxies:** Supports residential, mobile, datacenter (Free/Paid).
*   **Captcha:** Ultra-fast direct AI bypass (No proxy required for solver).
*   **Scraper:** Integrated 100k+ target username extractor.
*   **Alerts:** Live Telegram bot delivery for secured/valid hits.

---

## 🇷🇺 Русский | Краткий обзор системы

**Разработано ведущим архитектором ПО с 20-летним опытом в сфере автоматизации и высоконагруженных систем.**

TikTok Account Auditor Pro — это ультрабыстрый многопоточный инструмент для аутентификации и сбора данных профилей.

### Ключевые возможности:
*   **Режим работы:** Проверка по парам `user:pass`.
*   **Гарантия точности (Zero-Skip):** Ни один аккаунт не пропускается при сбоях сети благодаря умной очереди повторов.
*   **Сохранение Rate-Limit:** Автоматическая изоляция заблокированных по частоте аккаунтов в файл `rate_limited.txt`.
*   **Обход капчи:** Высокоскоростной прямой модуль решения капчи без нагрузки на прокси.
*   **Поддержка прокси:** Полная совместимость с SOCKS4/5, HTTP(S) (платные и бесплатные пулы).
*   **Скрапер:** Встроенный сборщик профилей на 100k+ аккаунтов.
*   **Уведомления:** Мгновенная отправка валидных активов в Telegram.

---

## 🇨🇳 中文 | 功能概述

**由拥有 20 多年软件工程与自动化经验的资深架构师打造。**

TikTok Account Auditor Pro 是一款专为高效数据验证与账号审计而设计的超高速多线程引擎。

### 核心优势:
*   **验证模式:** 仅支持 `user:pass` 凭据比对。
*   **零跳过保证 (Zero-Skip):** 智能重试机制，确保无任何账号因网络问题被遗漏。
*   **频率限制隔离:** 自动识别并单独保存受限账号 (`rate_limited.txt`)。
*   **极速 AI 验证码破解:** 本地直连破解算法，无需经过代理路由，显著提升效率。
*   **代理全面兼容:** 原生支持 SOCKS4/5、HTTP(S) 及动态住宅/移动代理（免费/付费皆可）。
*   **海量采集器:** 内置 10w+ 目标用户名抓取引擎。
*   **Telegram 实时推送:** 有效账号即时通知至您的 Telegram 频道或机器人。

---

## ⚙️ Configuration Example (`config.json.example`)

```json
{
  "audit_settings": {
    "threads": 100,
    "timeout_seconds": 10,
    "max_retries": 5,
    "never_skip": true
  },
  "captcha": {
    "direct_ai_bypass": true,
    "route_solver_through_proxy": false
  },
  "proxy": {
    "enabled": true,
    "type": "socks5",
    "file_path": "./proxies.txt",
    "auto_rotate": true
  },
  "output_files": {
    "valid_hits": "./output/secured_hits.txt",
    "rate_limited": "./output/rate_limited.txt"
  },
  "telegram_notifications": {
    "enabled": true,
    "bot_token": "YOUR_TELEGRAM_BOT_TOKEN",
    "chat_id": "YOUR_TELEGRAM_CHAT_ID",
    "send_metrics": true
  }
}
