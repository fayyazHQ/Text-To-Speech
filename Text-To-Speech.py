from gtts import gTTS
import os

def main():
	print("--- Text-to-Speech (TTS) ---")
	print("Supported language codes: https://gtts.readthedocs.io/en/latest/module.html#available-languages")
	lang = input("Enter the language code (e.g., 'en' for English, 'fr' for French, 'ur' for Urdu): ").strip()
	text = input("Enter the text you want it to speak: ").strip()

	if not text:
		print("No text entered. Exiting.")
		return

	try:
		tts = gTTS(text=text, lang=lang, slow=False)
		save_dir = input("Enter the directory where you want to save the audio file: ").strip()
		if not save_dir:
			save_dir = os.getcwd()
		else:
			os.makedirs(save_dir, exist_ok=True)
		filename = input("Enter the filename to save as (e.g., 'my_audio.mp3'): ").strip()
		if not filename:
			filename = "output.mp3"
		output_path = os.path.join(save_dir, filename)
		tts.save(output_path)
		print(f"Audio saved as '{output_path}' in language: {lang}")
	except Exception as e:
		print(f"Error: {e}\nPlease make sure the language code is valid and supported by gTTS.")

if __name__ == "__main__":
	main()


