# Audio Resampler
This a web application which convert a high frequency audio in to a low frequency audio


# Multi-Rate Audio Resampling

A Python-based audio resampling application built using Digital Signal Processing (DSP).

## Project Overview

This application allows users to upload audio files and convert them between different sampling rates, such as 48 kHz, 44.1 kHz, 22.05 kHz, 16 kHz, and 8 kHz.

It also provides basic distortion analysis to evaluate the difference between the original and resampled audio.

## Features

- Upload WAV and MP3 audio files
- Convert audio to different sampling rates
- Play original and converted audio
- Download resampled audio in WAV format
- Calculate Mean Squared Error (MSE)
- Calculate Signal-to-Noise Ratio (SNR)
- Visualize original and resampled waveforms

## Technologies Used

- Python
- NumPy
- SciPy
- Librosa
- SoundFile
- Matplotlib
- Streamlit

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

## Project Structure

```text
Multi-Rate-Audio-Resampling/
├── app.py
├── resampler.py
├── analysis.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Future Improvements

- Frequency-domain analysis using FFT
- Spectrogram visualization
- Improved audio quality evaluation
- More resampling options
- Deployment as a web application

## Author

Suman Kumbhakar
