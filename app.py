import streamlit as st
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
import io
import librosa

from resampler import resample_audio
from analysis import calculate_distortion


# Page configuration
st.set_page_config(
    page_title="Multi-Rate Audio Resampler",
    page_icon="🎵",
    layout="wide"
)

# Application title
st.title("🎵 Multi-Rate Audio Resampling")
st.write("Upload an audio file and convert it to different sampling rates.")


# Upload audio file
uploaded_file = st.file_uploader(
    "Upload an audio file",
    type=["wav", "mp3"]
)


if uploaded_file is not None:

    try:
        # Read audio while preserving original sampling rate
        audio, original_rate = librosa.load(
            uploaded_file,
            sr=None,
            mono=False
        )

        # Convert mono audio to 2D format
        if audio.ndim == 1:
            audio = audio.reshape(-1, 1)
        else:
            audio = audio.T

        st.success("Audio uploaded successfully!")

        # Display original audio information
        st.subheader("Original Audio Information")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Sampling Rate", f"{original_rate} Hz")

        with col2:
            st.metric("Duration", f"{len(audio) / original_rate:.2f} seconds")

        # Play original audio
        st.subheader("Original Audio")
        original_buffer = io.BytesIO()

        sf.write(
            original_buffer,
            audio,
            original_rate,
            format="WAV"
        )

        st.audio(original_buffer.getvalue(), format="audio/wav")

        # Select target sampling rate
        st.subheader("Resampling Settings")

        target_rate = st.selectbox(
            "Select target sampling rate",
            [8000, 16000, 22050, 44100, 48000],
            index=1
        )

        # Resampling
        if st.button("Resample Audio"):

            if target_rate == original_rate:
                st.info("The selected sampling rate is the same as the original.")
            
            else:
                converted = resample_audio(
                    audio,
                    original_rate,
                    target_rate
                )

                st.success("Audio resampled successfully!")

                # Display converted audio information
                st.subheader("Converted Audio")

                st.write(
                    "New sampling rate:",
                    target_rate,
                    "Hz"
                )

                st.write(
                    "New duration:",
                    f"{len(converted) / target_rate:.2f} seconds"
                )

                # Save converted audio
                output = io.BytesIO()

                sf.write(
                    output,
                    converted,
                    target_rate,
                    format="WAV"
                )

                audio_bytes = output.getvalue()

                # Play converted audio
                st.audio(
                    audio_bytes,
                    format="audio/wav"
                )

                # Download converted audio
                st.download_button(
                    label="Download Converted Audio",
                    data=audio_bytes,
                    file_name="resampled_audio.wav",
                    mime="audio/wav"
                )

                # Distortion analysis
                mse, snr, reconstructed = calculate_distortion(
                    audio,
                    converted,
                    original_rate,
                    target_rate
                )

                st.subheader("Distortion Analysis")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("MSE", f"{mse:.8f}")

                with col2:
                    st.metric("SNR", f"{snr:.2f} dB")

                # Original waveform
                st.subheader("Original Waveform")

                fig, ax = plt.subplots(figsize=(10, 4))

                time = np.arange(len(audio)) / original_rate

                ax.plot(time, audio[:, 0])
                ax.set_xlabel("Time (seconds)")
                ax.set_ylabel("Amplitude")
                ax.set_title("Original Audio Waveform")
                ax.grid(True)

                st.pyplot(fig)
                plt.close(fig)

                # Resampled waveform
                st.subheader("Resampled Waveform")

                fig2, ax2 = plt.subplots(figsize=(10, 4))

                new_time = np.arange(len(converted)) / target_rate

                ax2.plot(new_time, converted[:, 0])
                ax2.set_xlabel("Time (seconds)")
                ax2.set_ylabel("Amplitude")
                ax2.set_title("Resampled Audio Waveform")
                ax2.grid(True)

                st.pyplot(fig2)
                plt.close(fig2)

    except Exception as e:
        st.error(f"An error occurred: {e}")

else:
    st.info("Please upload a WAV or MP3 audio file to get started.")
