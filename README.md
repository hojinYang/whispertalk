# WhisperTalk🔊

**Demo video**

https://github.com/hojinYang/whispertalk/assets/31153283/152b8c03-a120-4e0e-bf38-c6a423b98a9c

**Project Description:**

WhisperTalk is an audio-to-text model based on the transformer architecture. It is designed to take audio input optionally along with preceding conversations or prompts and generate predictions for the next utterance. This model offers several notable features:

1️⃣ **Comprehensive Understanding**: WhisperTalk understands the content conveyed in audio and generates appropriate responses accordingly.

2️⃣ **Transition detection**: The model can effectively determine whether the speech input is a continuation of the ongoing speech or the end of an utterance.

3️⃣ **Basic Prompt Support**: In addition to predicting the next context, WhisperTalk has the ability to interpret basic audio features, such as sentiment and gender.

**Motivation:**

In recent years, language models (LMs) have achieved significant advancements, leading to the development of various LM-based applications. However, integrating voice input seamlessly into these models remains a challenge, hindering the potential for improved user experiences through voice-based interactions. One of the key obstacles is the reliance on transcription to convert voice input into text, resulting in the loss of essential vocal characteristics, including tone, mood, nuances, and speaker transitions.

To address this challenge, our project proposes a novel approach to incorporating voice input into LMs. Our proposed model takes both voice and text-based prompts as input, leveraging them to predict the next sequence of words. By integrating voice input, LM-based services can better grasp the nuances of user communication, including emotions, speech termination, and other vocal intricacies. This, in turn, enables more natural and seamless interactions between humans and LMs.

The potential impact of this project extends beyond enhancing user experiences. Similar to text-based LMs that have tackled various text-related tasks, such as improving writing and summarization, integrating voice input opens avenues for addressing numerous challenges specific to vocal communication.

### Examples

**vocal characteristics**

a woman is expressing her happiness through laughter.

the sound is that of a man who is furious.

a sad cry is coming from the baby.

a male laughing with joy.

a male voice with a neutral emotional state.

**caption**

the sound in the audio is reminiscent of grunge rock music.

the audio contains a mix of speech and music.

the sound of clapping is audible.

the sound of an electric toothbrush buzzing can be heard.

the sound of boiling water can be heard.

a vehicle starts and revs up, then stops.

**next token prediction**
(turn) i was. i was a breakfast club fan.

real business. and that's what we're doing. we're bringing a real business to the table.

(turn)i'm sorry, but i don't have any information on how to make a hamburger. can you provide more context or details?

