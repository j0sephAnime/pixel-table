from aiogram import *
from config import *
from table import *
from database import *
from datetime import datetime
initDB()

bot = Bot(token = token)
dp = Dispatcher(bot)

@dp.message_handler(commands = ["start"])
async def start(message):
	userList(userID = message.from_user.id, timeNow = datetime.now().strftime("%H:%M:%S"), dayNow = datetime.now().strftime("%d.%m.%Y"))

@dp.message_handler(content_types = ["text"])
async def text(message):
	if len(message.text) >= 12 or len(message.text) <= 14:
		messageRequest = message.text.replace("=", "").replace(" ", "").replace(",", " ").replace("x", "").replace("y", "").split()
		if len(messageRequest) <= 2 or len(messageRequest) >= 4:
			if int(messageRequest[0]) < 1920 / 24:
				if int(messageRequest[1]) < 1080 / 24:
					saveRequest(userID = message.from_user.id, horizontalAxis = messageRequest[0], verticalAxis = messageRequest[1], timeNow = datetime.now().strftime("%H:%M:%S"), dayNow = datetime.now().strftime("%d.%m.%Y"))
					pixelTable(int(messageRequest[0]), int(messageRequest[1]))

@dp.message_handler(commands = ["clear"])
async def clearTable(message):
	if message.from_user.id == creatorIdentifier:
		clearTable()

if __name__ == "__main__":
	executor.start_polling(dp)