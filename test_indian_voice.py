import torch
import torchaudio
import torch.nn as nn
import torch.nn.functional as F
import os

import IPython

from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio, load_voice, load_voices

clips_path= r"C:\Users\priyatosh.anand\Desktop\project\tortoise-tts\tortoise\voices\Indian_Palki_Sharma"
audio_files = os.listdir(clips_path)
reference_clips = [load_audio(os.path.join(clips_path, file), 22050) for file in audio_files]
tts = TextToSpeech()
pcm_audio = tts.tts_with_preset("Supreme court order on interim bail of Delhi chief minister Arvind kejriwal on May 10", voice_samples=reference_clips, preset='fast')