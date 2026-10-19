BOT_TOKEN = "8643606998:AAF1_wBgKosfxf07hZeEyFS2BCc4OmlXwfM"
ADMIN_ID = 8194746903
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
async def start(u,c):
 k=[[InlineKeyboardButton("🇺🇸 امريكي",callback_data="usa")],[InlineKeyboardButton("🇬🇧 بريطاني",callback_data="uk")]]
 await u.message.reply_text("اختر نوع الرقم:",reply_markup=InlineKeyboardMarkup(k))
async def btn(u,c):
 q=u.callback_query;await q.answer();await q.edit_message_text("✅ تم ارسال طلبك، انتظر الرقم")
 await c.bot.send_message(ADMIN_ID,f"📩 طلب جديد\nID:{q.from_user.id}\nالنوع:{q.data}")
async def send(u,c):
 if u.effective_user.id!=ADMIN_ID:return
 try:
  await c.bot.send_message(int(c.args[0]),f"✅ رقمك:\n{c.args[1]}");await u.message.reply_text("✅ تم الارسال")
 except Exception as e: await u.message.reply_text(f"خطأ: {e}")
app=Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start",start));app.add_handler(CommandHandler("send",send));app.add_handler(CallbackQueryHandler(btn))
app.run_polling()
