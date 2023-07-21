from deep_translator import GoogleTranslator

translated = GoogleTranslator(source="auto", target="de").translate("Hello world in German(de)")
print(translated)
print()

texts = ["halllo welt", "guten morgen", "apa kabar"]
translate_batch = GoogleTranslator('auto','zh-CN').translate_batch(texts)
print(translate_batch)