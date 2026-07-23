import pyttsx3
import threading
import queue

class AudioFeedback:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 160)  # Speech speed
        self.speech_queue = queue.Queue()
        self.is_speaking = False

        # Run TTS on a separate thread to prevent blocking live video processing
        self.thread = threading.Thread(target=self._process_speech, daemon=True)
        self.thread.start()

    def speak(self, text):
        """Adds alert text to the speech queue."""
        if self.speech_queue.qsize() < 2:  # Limit queue length for low latency
            self.speech_queue.put(text)

    def _process_speech(self):
        while True:
            text = self.speech_queue.get()
            self.engine.say(text)
            self.engine.runAndWait()
            self.speech_queue.task_done()
