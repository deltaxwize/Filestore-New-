import asyncio
import json
from bot import Bot, web_app
from pyrogram import compose

# Static default fallback message templates
default_messages = {
    'START': '<blockquote expandable>__Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit sed.\nVivamus luctus urna sed urna.\nCurabitur blandit tempus porttitor.\nNullam quis risus eget urna.__</blockquote>',
    'FSUB': '',
    'ABOUT': 'ABOUT MSG',
    'REPLY': 'reply_text',
    'START_PHOTO': '',
    'FSUB_PHOTO': ''
}

async def main():
    apps = []

    # Load setup.json
    with open("setup.json", "r", encoding="utf-8") as f:
        setups = json.load(f)

    # Loop through each bot setup config
    for config in setups:
        apps.append(
            Bot(
                session=config["session"],
                workers=config["workers"],
                db=config["db"],
                fsubs=config["fsubs"],
                token=config["token"],
                admins=config["admins"],
                messages=config.get("messages", default_messages),
                auto_del=config["auto_del"],
                db_uri=config["db_uri"],
                db_name=config["db_name"],
                api_id=int(config["api_id"]),       # ✅ ensure int
                api_hash=config["api_hash"],        # ✅ ensure non-empty
                protect=config["protect"],
                disable_btn=config["disable_btn"]
            )
        )

    # Start all bots
    await compose(apps)


async def runner():
    await asyncio.gather(
        main(),
        web_app()
    )

if __name__ == "__main__":
    asyncio.run(runner())
