from aiogram import Bot, Dispatcher, types, executor

from asyncio import sleep



bot = Bot('1525901166:AAFPhqABtSxjW066C4gIpaOFDuKIdjqYfFA')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def on_message(message : types.Message):
	await bot.send_message(message.from_user.id,"Да начнётся игра")
	await sleep(1)

	bot_data = await bot.send_dice(message.from_user.id)
	bot_data = bot_data['dice']['value']
	await sleep(5)

	await bot.send_message(message.from_user.id, "Теперь твоя очередь")
	
	user_data = await bot.send_dice(message.from_user.id)
	user_data = user_data['dice']['value']


	await sleep(5)
	if bot_data > user_data :
		await bot.send_message(message.from_user.id , "Лохъ")
	elif bot_data < user_data :
		await bot.send_message(message.from_user.id , "Ну-ну,а ты хорош")
	else :
		await bot.send_message(message.from_user.id , "Меня это не устраивает")

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True )


		

