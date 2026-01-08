from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat
from fluent.runtime import FluentLocalization

from bot.config_reader import config


async def set_bot_info(bot: Bot, l10n: FluentLocalization):
    try:
        usercommands = [
            BotCommand(command="help", description=l10n.format_value("command-help")),
        ]
        await bot.set_my_commands(usercommands, scope=BotCommandScopeDefault())

        admin_commands = [
            BotCommand(command="who", description=l10n.format_value("command-who")),
            BotCommand(command="ban", description=l10n.format_value("command-ban")),
            BotCommand(command="shadowban", description=l10n.format_value("command-shadowban")),
            BotCommand(command="unban", description=l10n.format_value("command-unban")),
            BotCommand(command="list_banned", description=l10n.format_value("command-list-banned")),
        ]
        await bot.set_my_commands(
            admin_commands,
            scope=BotCommandScopeChat(chat_id=config.admin_chat_id)
        )

        await bot.set_my_description(description = l10n.format_value("intro"))
        await bot.set_my_short_description(short_description = l10n.format_value("intro"))
    except Exception as e:
        print(f"An error occurred while setting bot info: {e}")
