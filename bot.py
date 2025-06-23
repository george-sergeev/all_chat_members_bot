Вот полный рабочий код Telegram-бота с командой `/all`, который удаляет исходное сообщение пользователя и отправляет упоминания всех админов (кроме ботов):

```python
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

# Логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def all_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /all с удалением исходного сообщения"""
    try:
        # Удаляем сообщение пользователя с командой
        await context.bot.delete_message(
            chat_id=update.effective_chat.id,
            message_id=update.message.message_id
        )
    except Exception as e:
        logging.warning(f"Не удалось удалить сообщение: {e}")

    # Получаем чат и список админов
    chat = await context.bot.get_chat(update.effective_chat.id)
    members = await context.bot.get_chat_administrators(chat.id)

    # Формируем сообщение с упоминаниями
    members_text = "❗Срочная информация❗\n\n"
    for member in members:
        user = member.user
        if not user.is_bot:
            members_text += f"@{user.username or user.first_name}\n"

    # Отправляем сообщение
    await context.bot.send_message(chat_id=chat.id, text=members_text)

if __name__ == "__main__":
    # Токен бота
    TOKEN = "7886662496:AAGseoxWd-e43NESe6_j8fZmlENWBPY6fxM"

    # Создание приложения
    application = ApplicationBuilder().token(TOKEN).build()

    # Регистрация обработчика команды /all
    application.add_handler(CommandHandler("all", all_command))

    # Запуск бота
    application.run_polling()
```

🔒 **Не забудьте**:

* Замените `"YOUR_TOKEN_HERE"` на настоящий токен вашего бота.
* Убедитесь, что бот добавлен в группу как **админ** и у него есть **право удалять сообщения**.

💡 Дополнительно можно добавить ограничение, чтобы только админы могли использовать `/all`. Если нужно — скажи, добавлю.
