**WhisperTalk**

**Project Description:**

🔊 WhisperTalk is an audio-to-text model based on the transformer architecture. It is designed to take audio input optionally along with preceding conversations or prompts and generate predictions for the next utterance. This model offers several notable features:

1️⃣ **Comprehensive Understanding**: WhisperTalk understands the content conveyed in audio and generates appropriate responses accordingly.

2️⃣ **Transition detection**: The model can effectively determine whether the speech input is a continuation of the ongoing speech or the end of an utterance.

3️⃣ **Basic Prompt Support**: In addition to predicting the next context, WhisperTalk has the ability to interpret basic audio features, such as sentiment and gender.

**Motivation:**

In recent years, language models (LMs) have achieved significant advancements, leading to the development of various LM-based applications. However, integrating voice input seamlessly into these models remains a challenge, hindering the potential for improved user experiences through voice-based interactions. One of the key obstacles is the reliance on transcription to convert voice input into text, resulting in the loss of essential vocal characteristics, including tone, mood, nuances, and speaker transitions.

To address this challenge, our project proposes a novel approach to incorporating voice input into LMs. Our proposed model takes both voice and text-based prompts as input, leveraging them to predict the next sequence of words. By integrating voice input, LM-based services can better grasp the nuances of user communication, including emotions, speech termination, and other vocal intricacies. This, in turn, enables more natural and seamless interactions between humans and LMs.

The potential impact of this project extends beyond enhancing user experiences. Similar to text-based LMs that have tackled various text-related tasks, such as improving writing and summarization, integrating voice input opens avenues for addressing numerous challenges specific to vocal communication.

By leveraging the WhisperTalk model, we aim to improve the way voice input is incorporated into language models, enabling richer and more immersive interactions while preserving the unique characteristics of human speech.


https://github.com/hojinYang/whispertalk/assets/31153283/2389c5ae-2b18-4602-ab93-3d2c4dded480



https://github.com/hojinYang/whispertalk/assets/31153283/feea4067-19bc-4477-a4a3-d33728720a2b



**Examples**
| Audio | Continuation |
|-------|-------------|
| https://github.com/hojinYang/whispertalk/assets/31153283/e0934c68-ba2a-40e1-a3d7-3d6148dcd59d | Introduction to the topic |
| <audio controls><source src="src/audio5.wav" type="audio/wav"></audio> | Introduction to the topic |
