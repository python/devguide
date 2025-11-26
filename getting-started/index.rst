#!/usr/bin/env python3
# bot.py — простой Telegram FAQ-бот с ссылкой на материалы курса
# Требуется: python 3.10+ и python-telegram-bot v20+
# Установка:
#   pip install python-telegram-bot==20.6

import os
import logging
from typing import Dict, List
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# Настройка логов
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# --------------------------
# Настройки — поменяй здесь
# --------------------------
BOT_TOKEN = os.getenv("BOT_TOKEN")  # рекомендую задать в окружении
if not BOT_TOKEN:
    # Можно временно вставить токен прямо сюда (не рекомендуется публиковать)
    BOT_TOKEN = "ВАШ_TELEGRAM_BOT_TOKEN_ЗДЕСЬ"

# Ссылка на материалы курса (Google Drive, LMS и т.д.)
COURSE_MATERIALS_LINK = "https://drive.google.com/your-course-materials-link"

# Админ (необязательно) — Telegram user_id, который может расширять функционал в будущем
ADMIN_USER_ID = None

# --------------------------
# Часто задаваемые вопросы
# --------------------------
# Пример: список словарей с 'id','question','answer'
FAQS: List[Dict[str, str]] = [
    {
        "id": "schedule",
        "question": "Расписание занятий",
        "answer": "Занятия проходят по расписанию: Понедельник и Среда 14:00–16:00, Аудитория 204. Полное расписание — в календаре курса."
    },
    {
        "id": "contacts",
        "question": "Контакты кафедры",
        "answer": "Кафедра: +7 (727) 123-45-67, email: kafedra@example.edu. Ответственный: Иванов И.И."
    },
    {
        "id": "papers_rules",
        "question": "Правила оформления работ",
        "answer": "Формат: A4, шрифт Times New Roman 12, межстрочный интервал 1.5. Список литературы — в конце. Строго по шаблону (см. файл 'Template.docx' в материалах)."
    },
    {
        "id": "deadlines",
        "question": "Сроки сдачи работ",
        "answer": "Промежуточные отчёты: 1 октября и 1 ноября. Итоговая работа — до 15 декабря (точные даты уточняйте в LMS)."
    },
    {
        "id": "useful_links",
        "question": "Полезные ресурсы",
        "answer": "1) Электронная библиотека — https://elib.example.edu\n2) Руководства по цитированию — https://citation.example.edu\n3) Лекции и презентации — в разделе 'Материалы курса'."
    },
    {
        "id": "materials",
        "question": "Материалы курса (Google Drive / LMS)",
        "answer": f"Все материалы курса доступны по ссылке: {COURSE_MATERIALS_LINK}"
    },
    # При желании добавь ещё 3–4 вопроса аналогично
]

# Вспомогательная функция: строит клавиатуру из FAQS
def build_faq_keyboard() -> InlineKeyboardMarkup:
    buttons = []
    for item in FAQS:
        buttons.append([InlineKeyboardButton(text=item["question"], callback_data=f"faq:{item['id']}")])
    # Добавим отдельную кнопку "Материалы курса" (если хочется)
    buttons.append([InlineKeyboardButton(text="Материалы курса", callback_data="materials")])
    return InlineKeyboardMarkup(buttons)

# --------------------------
# Обработчики команд/кнопок
# --------------------------
async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = (
        f"Привет, {user.first_name if user else 'студент'}!\n\n"
        "Я — помощник по курсу. Могу ответить на часто задаваемые вопросы и дать ссылку на материалы.\n\n"
        "Выбери вопрос в меню или введи /faq для списка вопросов."
    )
    keyboard = build_faq_keyboard()
    await update.message.reply_text(text, reply_markup=keyboard)


async def faq_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Отправляем список вопросов (текст + кнопки)
    keyboard = build_faq_keyboard()
    await update.message.reply_text("Выберите вопрос:", reply_markup=keyboard)


async def materials_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Материалы курса: {COURSE_MATERIALS_LINK}\n\n"
        "Если ссылка не открывается, сообщите преподавателю или напишите в поддержку LMS."
    )


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Доступные команды:\n"
        "/start — приветствие и меню\n"
        "/faq — часто задаваемые вопросы\n"
        "/materials — ссылка на материалы курса\n"
        "/help — помощь"
    )


async def callback_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # убирает 'нажатие'
    data = query.data or ""

    if data.startswith("faq:"):
        faq_id = data.split(":", 1)[1]
        faq_item = next((f for f in FAQS if f["id"] == faq_id), None)
        if faq_item:
            await query.edit_message_text(text=f"*{faq_item['question']}*\n\n{faq_item['answer']}", parse_mode="Markdown")
        else:
            await query.edit_message_text(text="Извините, этот вопрос не найден.")
    elif data == "materials":
        await query.edit_message_text(text=f"Материалы курса: {COURSE_MATERIALS_LINK}")
    else:
        await query.edit_message_text(text="Неизвестная команда. Попробуйте /faq или /help.")


# --------------------------
# Запуск приложения
# --------------------------
def main() -> None:
    if BOT_TOKEN is None or BOT_TOKEN.strip() == "" or "8428197715: AAHLL0wShvvMw0jgpsttYn4PbRF
o-FzUmLQ" in BOT_TOKEN:
        logger.error("Токен бота не задан. Укажи BOT_TOKEN в переменных окружения или прямо в коде.")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Команды
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("faq", faq_command_handler))
    app.add_handler(CommandHandler("materials", materials_command_handler))
    app.add_handler(CommandHandler("help", help_handler))

    # Кнопки
    app.add_handler(CallbackQueryHandler(callback_query_handler))

    # Запуск (long polling)
    logger.info("Бот запущен (polling). Нажми Ctrl+C для остановки.")
    app.run_polling()

if __name__ == "__main__":
    main()
