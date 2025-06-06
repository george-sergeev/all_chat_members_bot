from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

# Логирование
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

async def all_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды @all"""
    chat = await context.bot.get_chat(update.effective_chat.id)
    members = await context.bot.get_chat_administrators(chat.id)
    members_text = "❗Срочная информация❗\n\n"
    
    for member in members:
        user = member.user
        if not user.is_bot:
            members_text += f"@{user.username or user.first_name}\n"

    await update.message.reply_text(members_text)

if __name__ == "__main__":
    # Токен бота
    TOKEN = "7886662496:AAHGpgSRAHGEkYxKOWugROcs7sGq43emBxs"
    

    # Создаем приложение
    application = ApplicationBuilder().token(TOKEN).build()

    # Регистрируем обработчики
    application.add_handler(CommandHandler("all", all_command))

    # Запускаем бота
    application.run_polling()
