from transformers import AutoProcessor, WhisperForConditionalGeneration
import librosa

audio_file = 'assets/sample_audio.wav'
model_name = 'hojin/whispertalk'


processor = AutoProcessor.from_pretrained(model_name)
model = WhisperForConditionalGeneration.from_pretrained(model_name)

arr,sr = librosa.load(audio_file,sr=None)

prompt = ""
inputs = processor(arr, return_tensors="pt")
decoder_ids = processor.tokenizer.encode(prompt, return_tensors="pt",add_special_tokens=False)

input_features = inputs.input_features

generated_ids = model.generate(inputs=input_features,decoder_input_ids = decoder_ids, num_beams=3)
output = processor.batch_decode(generated_ids)[0]
print(output)