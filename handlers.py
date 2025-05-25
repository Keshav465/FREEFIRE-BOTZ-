import os
from telegram import Update, ParseMode
from telegram.ext import CommandHandler, ContextTypes
from datetime import datetime
import requests
from bot.database import has_liked_today, save_like

AUTHORIZED_GROUPS = os.getenv("AUTHORIZED_GROUPS", "-1002269649979").split(",")

async def like_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = str(update.effective_chat.id)
    message = update.message
    args = context.args

    if chat_id not in AUTHORIZED_GROUPS:
        await message.reply_text("⚠️ This group is not authorized.\nMessage @Keshavraj_77 to get access.")
        return

    if len(args) != 2:
        await message.reply_text("❌ Usage: /like REGION UID")
        return

    region = args[0].upper()
    uid = args[1]
    today = datetime.utcnow().strftime("%Y-%m-%d")

    if has_liked_today(uid, today):
        await message.reply_text(f"❌ UID {uid} already received likes today.")
        return

    loading_msg = await message.reply_text("⏳ Processing...")

    try:
        res = requests.get(f"https://narayan-api.vercel.app/like?uid={uid}&server_name={region}")
        data = res.json()
    except Exception as e:
        await loading_msg.edit_text("❌ API error. Try again later.")
        return

    if data.get("LikesGivenByAPI", 0) == 0:
        await loading_msg.edit_text(
            f"UID <b>{uid}</b> in region <b>{region}</b> has already received max likes today.",
            parse_mode=ParseMode.HTML
        )
        return

    save_like(uid, region, today, data.get("LikesGivenByAPI", 0))

    result_msg = (
        "✨ <b>LIKE SENDED SUCCESS</b> ✨\n\n"
        f"✨ <b>NAME:</b> {data.get('PlayerNickname', 'N/A')}\n"
        f"✨ <b>REGION:</b> {region} 🇮🇳\n"
        f"✨ <b>LIKES SENDED:</b> {data['LikesGivenByAPI']}\n"
        f"✨ <b>LIKE BEFORE:</b> {data['LikesbeforeCommand']}\n"
        f"✨ <b>LIKE AFTER:</b> {data['LikesafterCommand']}\n\n"
        "✨ <b>BOT BY:</b> @Keshavraj_77"
    )

    await loading_msg.edit_text(result_msg, parse_mode=ParseMode.HTML)

like_handler = CommandHandler("like", like_command)
