import gtts


def transform_string_to_audio(text="Вы не ввели текст", language="ru", file_name="test.mp3"):
    gtts.gTTS(text, slow=False, lang=language).save(fr"audio_files\{file_name}")


if __name__ == "__main__":
    transform_string_to_audio("Привет, мир", "ru")
