@dp.callback_query(F.data.in_(
    ['text', 'audio', 'video', 'document', 'photo', 'voice']
))
async def process_button_press(callback: CallbackQuery):
    markup = get_markup(2, 'text')
    if callback.message.text == LEXICON['text_1']:
        text = LEXICON['text_2']
    else:
        text = LEXICON['text_1']
    await callback.message.edit_text(
        text=text,
        reply_markup=markup
    )