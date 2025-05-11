# meta developer: @ethdrugs

from .. import loader, utils
from telethon.tl.custom import Button

@loader.tds
class SponsorModule(loader.Module):
    """Модуль для отображения ссылки на спонсорство"""
    strings = {"name": "Sponsor"}

    async def sponsor_urlcmd(self, message):
        """Устанавливает URL спонсорства"""
        args = utils.get_args_raw(message)
        if args:
            self.set("sponsor_url", args)
            await message.edit(f"✅ URL установлен:\n{args}")
        else:
            # Отправляем кнопочную панель
            await message.client.send_message(
                message.chat_id,
                "Введите ссылку для спонсорства:",
                buttons=[
                    [Button.inline("📝 Ввести ссылку", data=b"enter_url")]
                ]
            )
            await message.delete()

    async def sponsorcmd(self, message):
        """Показывает кнопку 'Buy: <URL>'"""
        url = self.get("sponsor_url", None)
        if url:
            await message.edit(f"Buy: {url}")
        else:
            await message.edit("⚠️ Ссылка не установлена. Используйте .sponsor_url")

    async def _cb_handler(self, call):
        if call.data == b"enter_url":
            await call.answer()
            await call.edit("Введите новую ссылку через `.sponsor_url <ссылка>`")
