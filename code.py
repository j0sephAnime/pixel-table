from aiogram import *
from config import *
from table import *

bot = Bot(token = token)
dp = Dispatcher(bot)

@dp.message_handler(content_types = ["text"])
async def text(message):
	if len(message.text) >= 12 or len(message.text) <= 14:
		message = message.text.replace("=", "").replace(" ", "").replace(",", " ").replace("x", "").replace("y", "").split()
		if len(message) <= 2 or len(message) >= 4:
			if int(message[0]) < 1920 / 24:
				if int(message[1]) < 1080 / 24:
					pixelTable(int(message[0]), int(message[1]))

if __name__ == "__main__":
	executor.start_polling(dp)